"""Wiki linter for Obsidian-based skill_md repository.

Checks:
1. Broken wikilinks — links pointing to files that don't exist
2. Orphaned files — .md files not linked from any other file
3. Missing/invalid frontmatter — files without YAML frontmatter or required fields
4. Broken source references — sources in frontmatter pointing to non-existent files
5. Duplicate entries in index.md — same target linked more than once
6. Empty files — .md files with no meaningful content
7. Filename inconsistencies — spaces, special chars, casing
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent

# Folders to skip
SKIP_DIRS = {'.git', '.claude', '.obsidian', 'node_modules', '__pycache__'}

# All .md files in the repo (relative paths as posix strings)
all_md_files: set[str] = set()
# Map of normalized path -> actual path for fuzzy matching
file_index: dict[str, Path] = {}

def collect_files():
    for p in ROOT.rglob('*.md'):
        rel = p.relative_to(ROOT)
        if any(part.startswith('.') for part in rel.parts):
            continue
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        posix = rel.as_posix()
        all_md_files.add(posix)
        # Normalize for fuzzy matching: lowercase, strip extension
        stem = rel.stem.lower().replace(' ', '-').replace('—', '-').replace('--', '-')
        file_index[stem] = rel

def parse_frontmatter(text: str) -> tuple[dict | None, int]:
    """Return (frontmatter_dict, end_line). None if no frontmatter."""
    if not text.startswith('---'):
        return None, 0
    end = text.find('---', 3)
    if end == -1:
        return None, 0
    block = text[3:end].strip()
    # Simple YAML parser for our needs
    fm = {}
    current_key = None
    current_list = None
    for line in block.split('\n'):
        line_stripped = line.strip()
        if line_stripped.startswith('- ') and current_key:
            if current_list is None:
                current_list = []
            current_list.append(line_stripped[2:].strip().strip('"').strip("'"))
            fm[current_key] = current_list
        elif ':' in line_stripped:
            if current_key and current_list:
                fm[current_key] = current_list
            current_list = None
            key, _, val = line_stripped.partition(':')
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val:
                fm[key] = val
            else:
                current_key = key
                fm[key] = None
    if current_key and current_list:
        fm[current_key] = current_list
    return fm, end + 3

WIKILINK_RE = re.compile(r'\[\[([^\]|#]+?)(?:[|#][^\]]*?)?\]\]')
MD_LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+\.md)\)')

def extract_links(text: str) -> list[str]:
    """Extract all internal .md link targets from wikilinks and markdown links."""
    links = []
    for m in WIKILINK_RE.finditer(text):
        target = m.group(1).strip()
        if not target.startswith('http'):
            links.append(target)
    for m in MD_LINK_RE.finditer(text):
        target = m.group(2).strip()
        if not target.startswith('http'):
            links.append(target)
    return links

def normalize_link(link: str) -> str:
    """Normalize a wikilink target for matching against file paths."""
    # Remove leading slash
    link = link.lstrip('/')
    # Add .md if not present
    if not link.endswith('.md'):
        link += '.md'
    return link

def resolve_link(link: str, source_file: str) -> str | None:
    """Try to resolve a link to an actual file. Return path or None."""
    norm = normalize_link(link)
    # Direct match
    if norm in all_md_files:
        return norm
    # Try relative to source directory
    source_dir = str(Path(source_file).parent)
    if source_dir == '.':
        candidate = norm
    else:
        candidate = source_dir + '/' + norm
    if candidate in all_md_files:
        return candidate
    # Try just the filename (for flat wikilinks)
    basename = Path(norm).name
    matches = [f for f in all_md_files if f.endswith('/' + basename) or f == basename]
    if len(matches) == 1:
        return matches[0]
    # Ambiguous or not found
    return None

# ── Checks ──────────────────────────────────────────────────────────────

def check_broken_wikilinks() -> list[str]:
    issues = []
    for fpath in sorted(all_md_files):
        full = ROOT / fpath
        text = full.read_text(encoding='utf-8', errors='replace')
        links = extract_links(text)
        for link in links:
            resolved = resolve_link(link, fpath)
            if resolved is None:
                issues.append(f"  BROKEN_LINK  {fpath}: [[{link}]]")
    return issues

def check_orphaned_files() -> list[str]:
    # Collect all link targets
    linked_targets: set[str] = set()
    for fpath in all_md_files:
        full = ROOT / fpath
        text = full.read_text(encoding='utf-8', errors='replace')
        links = extract_links(text)
        for link in links:
            resolved = resolve_link(link, fpath)
            if resolved:
                linked_targets.add(resolved)
    # index.md is always considered linked
    if 'index.md' in all_md_files:
        linked_targets.add('index.md')
    orphans = []
    repo_meta = {'AGENTS.md', 'README.md', 'log.md', 'CLAUDE.md'}
    for fpath in sorted(all_md_files):
        if fpath not in linked_targets:
            # Skip raw/ sources — they're inputs, not navigated to
            if fpath.startswith('raw/'):
                continue
            # Skip repo meta-files (agent instructions, readme, activity log)
            if fpath in repo_meta:
                continue
            orphans.append(f"  ORPHAN       {fpath}")
    return orphans

def check_frontmatter() -> list[str]:
    issues = []
    required_fields = {'type', 'created', 'status'}
    for fpath in sorted(all_md_files):
        full = ROOT / fpath
        text = full.read_text(encoding='utf-8', errors='replace')
        fm, _ = parse_frontmatter(text)
        if fm is None:
            # raw/ files often lack frontmatter — only flag non-raw
            if not fpath.startswith('raw/'):
                issues.append(f"  NO_FRONTMATTER {fpath}")
            continue
        for field in required_fields:
            if field not in fm or fm[field] is None:
                issues.append(f"  MISSING_FIELD  {fpath}: missing '{field}'")
    return issues

def check_broken_sources() -> list[str]:
    issues = []
    for fpath in sorted(all_md_files):
        if fpath.startswith('raw/'):
            continue
        full = ROOT / fpath
        text = full.read_text(encoding='utf-8', errors='replace')
        fm, _ = parse_frontmatter(text)
        if not fm or 'sources' not in fm or not fm['sources']:
            continue
        sources = fm['sources']
        if not isinstance(sources, list):
            continue
        for src in sources:
            src_clean = src.strip().strip('"').strip("'")
            if src_clean.startswith('http'):
                continue
            if src_clean not in all_md_files:
                issues.append(f"  BROKEN_SOURCE {fpath}: source '{src_clean}' not found")
    return issues

def check_index_duplicates() -> list[str]:
    issues = []
    index_path = ROOT / 'index.md'
    if not index_path.exists():
        return ['  NO_INDEX    index.md not found']
    text = index_path.read_text(encoding='utf-8', errors='replace')
    # Extract wikilink targets
    targets = []
    for m in WIKILINK_RE.finditer(text):
        target = m.group(1).strip()
        targets.append(target)
    seen = defaultdict(int)
    for t in targets:
        seen[t] += 1
    for t, count in sorted(seen.items()):
        if count > 1:
            issues.append(f"  DUP_ENTRY    index.md: [[{t}]] appears {count} times")
    return issues

def check_empty_files() -> list[str]:
    issues = []
    for fpath in sorted(all_md_files):
        if fpath.startswith('raw/'):
            continue
        full = ROOT / fpath
        text = full.read_text(encoding='utf-8', errors='replace')
        # Strip frontmatter and check remaining content
        _, end = parse_frontmatter(text)
        body = text[end:].strip()
        # Remove markdown headers and whitespace
        body_content = re.sub(r'^#+\s*$', '', body, flags=re.MULTILINE).strip()
        if len(body_content) < 10:
            issues.append(f"  EMPTY_FILE   {fpath}")
    return issues

def check_filename_issues() -> list[str]:
    issues = []
    for fpath in sorted(all_md_files):
        name = Path(fpath).name
        # Double spaces
        if '  ' in name:
            issues.append(f"  DBL_SPACE    {fpath}")
        # Trailing space before extension
        if name.endswith(' .md'):
            issues.append(f"  TRAIL_SPACE  {fpath}")
    return issues

def check_index_completeness() -> list[str]:
    """Check if concept and source files are listed in index.md."""
    issues = []
    index_path = ROOT / 'index.md'
    if not index_path.exists():
        return []
    index_text = index_path.read_text(encoding='utf-8', errors='replace')
    # Check concepts
    for fpath in sorted(all_md_files):
        if fpath.startswith('concepts/') and fpath.endswith('.md'):
            stem = Path(fpath).stem
            # Check if the concept name appears in index
            if stem not in index_text:
                issues.append(f"  NOT_IN_INDEX {fpath}")
        elif fpath.startswith('sources/') and fpath.endswith('.md'):
            stem = Path(fpath).stem
            if stem not in index_text:
                issues.append(f"  NOT_IN_INDEX {fpath}")
    return issues

# ── Main ────────────────────────────────────────────────────────────────

def main():
    collect_files()
    print(f"Scanned {len(all_md_files)} markdown files\n")

    all_issues = []
    checks = [
        ("Broken wikilinks", check_broken_wikilinks),
        ("Broken source references", check_broken_sources),
        ("Index duplicates", check_index_duplicates),
        ("Missing frontmatter", check_frontmatter),
        ("Empty files", check_empty_files),
        ("Filename issues", check_filename_issues),
        ("Index completeness", check_index_completeness),
        ("Orphaned files", check_orphaned_files),
    ]

    total = 0
    for label, check_fn in checks:
        issues = check_fn()
        if issues:
            print(f"── {label} ({len(issues)}) ──")
            for i in issues:
                print(i)
            print()
            total += len(issues)
        else:
            print(f"── {label}: ✓ clean ──\n")

    print(f"{'='*50}")
    print(f"Total issues: {total}")
    return 1 if total > 0 else 0

if __name__ == '__main__':
    sys.exit(main())
