---
name: presentation-slides
description: Create interactive full-screen HTML presentations with scroll-snap, keyboard nav, animated reveals, and multiple style presets. Uses /frontend-design process and UI component catalogues. For talks, workshops, pitches, or any screen presentation.
---

# Presentation Slides Skill

Create interactive full-screen HTML presentations as a single self-contained file. Zero dependencies. Keyboard/touch navigation. Scroll-snap. Animated reveals. Multiple style presets powered by the UI component catalogues.

**This is NOT for social carousels** (use `/linkedin-carousel`, `/ig-carousel`, `/tiktok-slides` for those). This is for **screen presentations** — talks, workshops, pitches, demos, lectures.

**IMPORTANT:** Always invoke `/frontend-design` before building. Use it for design thinking, layout decisions, and illustration choices. Never produce generic slides.

## How to Use

The user provides a topic, outline, or content via `$ARGUMENTS`. Generate a complete HTML file.

Save output to: `content/presentation-{topic-slug}.html`

After generating, tell the user: **Open in browser. Navigate with arrow keys, Space, or swipe. Press F for fullscreen.**

---

## Architecture — Non-Negotiable

Every presentation is a single HTML file with all CSS and JS inline. Zero external dependencies except Google Fonts / Fontshare.

```
presentation.html    # Self-contained
assets/              # Images only, if any
```

### Viewport-Locked Slides

Every slide = one full viewport. No scrolling within a slide.

```css
html {
  scroll-snap-type: y mandatory;
  overflow-y: scroll;
  scroll-behavior: smooth;
}

.slide {
  width: 100vw;
  height: 100vh;
  height: 100dvh; /* Mobile dynamic viewport */
  overflow: hidden;
  scroll-snap-align: start;
  position: relative;
}
```

### Fluid Responsive Scaling

ALL typography and spacing use `clamp()`. No media queries for sizing.

```css
:root {
  /* Typography — MUST use clamp() */
  --title-size: clamp(2rem, 6vw, 5rem);
  --subtitle-size: clamp(1rem, 2.5vw, 1.5rem);
  --body-size: clamp(0.875rem, 1.5vw, 1.25rem);
  --label-size: clamp(0.625rem, 1vw, 0.875rem);

  /* Spacing — MUST use clamp() */
  --slide-padding: clamp(1.5rem, 5vw, 5rem);
  --content-gap: clamp(1rem, 2.5vw, 2.5rem);

  /* Animation */
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --duration-normal: 0.6s;
  --duration-slow: 1s;
}
```

Only use media queries for hiding non-essential elements on very short viewports:

```css
@media (max-height: 600px) { .slide-footer, .nav-dots { display: none; } }
@media (max-height: 500px) { .slide-subtitle { display: none; } }
```

---

## Required JavaScript Controller

Every presentation MUST include this controller class. Adapt the interaction patterns from the UI component catalogues (see "Motion & Interaction Patterns" section).

```javascript
class SlidePresentation {
  constructor() {
    this.slides = document.querySelectorAll('.slide');
    this.currentSlide = 0;
    this.isTransitioning = false;

    this.setupIntersectionObserver();
    this.setupKeyboardNav();
    this.setupTouchNav();
    this.setupWheelNav();
    this.setupProgressBar();
    this.setupNavDots();
    this.setupFullscreen();
  }

  // Intersection Observer — triggers .visible class for CSS animations
  setupIntersectionObserver() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          this.currentSlide = [...this.slides].indexOf(entry.target);
          this.updateProgressBar();
          this.updateNavDots();
        }
      });
    }, { threshold: 0.5 });
    this.slides.forEach(slide => observer.observe(slide));
  }

  // Keyboard: arrows, space, page up/down
  setupKeyboardNav() {
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
        e.preventDefault();
        this.goToSlide(this.currentSlide + 1);
      } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft' || e.key === 'PageUp') {
        e.preventDefault();
        this.goToSlide(this.currentSlide - 1);
      } else if (e.key === 'Home') {
        e.preventDefault();
        this.goToSlide(0);
      } else if (e.key === 'End') {
        e.preventDefault();
        this.goToSlide(this.slides.length - 1);
      } else if (e.key === 'f' || e.key === 'F') {
        this.toggleFullscreen();
      }
    });
  }

  // Touch/swipe support
  setupTouchNav() {
    let startY = 0;
    document.addEventListener('touchstart', (e) => { startY = e.touches[0].clientY; });
    document.addEventListener('touchend', (e) => {
      const diff = startY - e.changedTouches[0].clientY;
      if (Math.abs(diff) > 50) {
        this.goToSlide(this.currentSlide + (diff > 0 ? 1 : -1));
      }
    });
  }

  // Mouse wheel with debounce
  setupWheelNav() {
    let lastWheel = 0;
    document.addEventListener('wheel', (e) => {
      const now = Date.now();
      if (now - lastWheel < 800) return;
      lastWheel = now;
      if (e.deltaY > 0) this.goToSlide(this.currentSlide + 1);
      else if (e.deltaY < 0) this.goToSlide(this.currentSlide - 1);
    }, { passive: true });
  }

  // Progress bar
  setupProgressBar() {
    const bar = document.querySelector('.progress-bar');
    if (bar) this.progressBar = bar;
  }

  updateProgressBar() {
    if (this.progressBar) {
      const pct = ((this.currentSlide + 1) / this.slides.length) * 100;
      this.progressBar.style.width = pct + '%';
    }
  }

  // Navigation dots
  setupNavDots() {
    const nav = document.querySelector('.nav-dots');
    if (!nav) return;
    this.slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.className = 'nav-dot' + (i === 0 ? ' active' : '');
      dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
      dot.addEventListener('click', () => this.goToSlide(i));
      nav.appendChild(dot);
    });
    this.navDots = nav.querySelectorAll('.nav-dot');
  }

  updateNavDots() {
    if (!this.navDots) return;
    this.navDots.forEach((dot, i) => {
      dot.classList.toggle('active', i === this.currentSlide);
    });
  }

  // Fullscreen toggle (F key)
  setupFullscreen() { /* bound in keydown */ }
  toggleFullscreen() {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen();
    else document.exitFullscreen();
  }

  goToSlide(index) {
    if (index < 0 || index >= this.slides.length) return;
    this.slides[index].scrollIntoView({ behavior: 'smooth' });
  }
}

document.addEventListener('DOMContentLoaded', () => new SlidePresentation());
```

---

## Entrance Animations

Elements with `.reveal` start hidden and animate in when their slide gets `.visible`.

```css
/* === Base reveal — fade + slide up === */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity var(--duration-normal) var(--ease-out-expo),
              transform var(--duration-normal) var(--ease-out-expo);
}
.slide.visible .reveal {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger children */
.reveal:nth-child(1) { transition-delay: 0.1s; }
.reveal:nth-child(2) { transition-delay: 0.2s; }
.reveal:nth-child(3) { transition-delay: 0.3s; }
.reveal:nth-child(4) { transition-delay: 0.4s; }
.reveal:nth-child(5) { transition-delay: 0.5s; }
.reveal:nth-child(6) { transition-delay: 0.6s; }

/* === Scale In (from TripleD scroll-reveal) === */
.reveal-scale {
  opacity: 0;
  transform: scale(0.9);
  transition: opacity var(--duration-normal), transform var(--duration-normal) var(--ease-spring);
}
.slide.visible .reveal-scale { opacity: 1; transform: scale(1); }

/* === Slide from Left (from UseLayouts feature-carousel) === */
.reveal-left {
  opacity: 0;
  transform: translateX(-50px);
  transition: opacity var(--duration-normal), transform var(--duration-normal) var(--ease-out-expo);
}
.slide.visible .reveal-left { opacity: 1; transform: translateX(0); }

/* === Slide from Right === */
.reveal-right {
  opacity: 0;
  transform: translateX(50px);
  transition: opacity var(--duration-normal), transform var(--duration-normal) var(--ease-out-expo);
}
.slide.visible .reveal-right { opacity: 1; transform: translateX(0); }

/* === Blur In (cinematic, from TripleD staggered-hero) === */
.reveal-blur {
  opacity: 0;
  filter: blur(10px);
  transition: opacity var(--duration-slow), filter var(--duration-slow) var(--ease-out-expo);
}
.slide.visible .reveal-blur { opacity: 1; filter: blur(0); }

/* === Per-word stagger (from TripleD auto-revealing-heading) === */
.reveal-word span {
  display: inline-block;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.4s var(--ease-out-expo), transform 0.4s var(--ease-out-expo);
}
.slide.visible .reveal-word span { opacity: 1; transform: translateY(0); }
/* JS splits headline into <span> per word, sets transition-delay: i * 60ms */
```

---

## Motion & Interaction Patterns from UI Libraries

These are the specific patterns to draw from. **Adapt to vanilla HTML/CSS/JS** (presentations are zero-dependency).

### From UseLayouts (27 micro-interactions)

| Pattern | Source Component | Use In Presentations |
|---|---|---|
| **Spring pill indicator** | `discrete-tabs`, `bento-card` | Tab/section indicators that slide between items with spring easing |
| **Staggered list entry** | `stacked-list` | Bullet points / feature lists entering one-by-one |
| **3D tilt on hover** | `3d-book` | Interactive cards that respond to cursor. `perspective: 1000px` + `rotateY/X` mapped to mouse position |
| **Auto-play progress** | `vertical-tabs` | Auto-advancing slides with visible countdown bar |
| **Morphing input/search** | `morphing-input` | Per-character `rotateX` flip for text swaps (stat reveals, word cycling) |
| **Status button states** | `status-button` | Loading → success micro-animations for demo slides |
| **Expandable gallery** | `expandable-gallery` | Collapsed image stack → expanded grid on click. FLIP animation technique |
| **Magnetic effect** | TripleD `magnetic` | Cursor-following magnetic pull on key elements (CTAs, featured items) |
| **Feature carousel stack** | `feature-carousel` | Image card stack with active/prev/next offset + rotation |
| **Direction-aware transitions** | `vertical-tabs` | Content slides up/down based on navigation direction |

### From TripleD (137 page blocks)

| Pattern | Source Component | Use In Presentations |
|---|---|---|
| **Staggered hero** | `staggered-hero`, `hero-section` | Title slide with per-word cascade reveal |
| **Counter animation** | `stats-section`, `counter-up` | Animated numbers for data/stats slides |
| **Dynamic spotlight** | `dynamic-spotlight-cta` | Cursor-following radial gradient that reveals text. `background-clip: text` |
| **Floating gradient blobs** | `floating-gradient` | Atmospheric animated background. Multiple `radial-gradient` layers with `@keyframes` |
| **Typewriter effect** | `typewriter` | Code demos, quote reveals. JS `setInterval` adding characters + CSS blinking cursor |
| **Flip text** | `flip-text` | 3D word rotation for cycling through concepts. `rotateX(90deg)` + `blur` |
| **Interactive timeline** | `interactive-timeline` | Scroll-triggered milestone reveals for roadmap slides |
| **Glassmorphism cards** | `feature-cards-block` | `backdrop-filter: blur(12px)` cards over gradient backgrounds |
| **Glowing waves** | `glowy-waves-hero` | Hero slide atmospheric effect |
| **Holographic wall** | `holographic-wall` | SVG pattern + radial gradient mask following cursor for specialty slides |

### From Neobrutal (21 components)

| Pattern | Source Component | Use In Presentations |
|---|---|---|
| **Hard shadow cards** | `Card` | `border: 2px solid black; box-shadow: 4px 4px 0 0 black` for bold layouts |
| **Press-in hover** | `Button` | `translate(1px,1px)` + shadow disappears on interaction |
| **Progress bar** | `Progress` | Bold bordered progress indicator |
| **Accordion** | `Accordion` | Expandable content sections within a slide |
| **Bold badges** | `Badge` | Section labels, tags. Black border + flat accent colour |
| **Toast notifications** | `Toast` | Slide-in callouts or annotations |

---

## Style Presets

Choose ONE preset per presentation. Each maps to a primary UI library and defines the complete visual system.

### Preset 1: Editorial Gravity

**Vibe:** Confident, warm, editorial. Like a premium magazine presentation.
**Primary library:** TripleD (page blocks) + UseLayouts (micro-interactions)
**Best for:** Keynotes, thought leadership, workshop intros

```css
:root {
  --bg-primary: #faf8f5;
  --bg-accent: #1a1612;
  --text-primary: #1a1612;
  --text-secondary: #6b5e52;
  --accent: #c4450a;
  --accent-soft: rgba(196, 69, 10, 0.08);
  --surface: #ffffff;
  --rule: #e2ddd6;
  --font-display: 'Fraunces', serif;
  --font-body: 'Work Sans', sans-serif;
}
```

**Signature elements:**
- Oversized serif headlines with per-word stagger reveal (from `staggered-hero`)
- Thin horizontal rules as section dividers
- Accent colour used sparingly (one element per slide)
- Floating gradient blob as atmosphere on title/closing slides (from `floating-gradient`)
- Counter animations for stat slides (from `counter-up`)

**Title slide:** Dark `--bg-accent` background, oversized `Fraunces` headline fading in word-by-word, subtle floating gradient blob in accent colour
**Content slides:** Light `--bg-primary`, left-aligned content, generous whitespace, one accent detail per slide
**Closing slide:** Matches title slide. CTA with magnetic hover effect (from `magnetic`)

---

### Preset 2: Neon Studio

**Vibe:** Technical, high-energy, future-forward. For dev talks and product demos.
**Primary library:** TripleD (glassmorphism blocks) + UseLayouts (carousels, tabs)
**Best for:** Tech talks, product demos, developer audiences

```css
:root {
  --bg-primary: #0a0f1c;
  --bg-secondary: #111827;
  --text-primary: #f0f0f0;
  --text-secondary: #9ca3af;
  --accent: #00ffcc;
  --accent-glow: rgba(0, 255, 204, 0.2);
  --accent-secondary: #ff6b9d;
  --surface: rgba(255, 255, 255, 0.05);
  --rule: rgba(255, 255, 255, 0.08);
  --font-display: 'Clash Display', sans-serif;
  --font-body: 'Satoshi', sans-serif;
}
```

**Font source:** Fontshare (free) — `https://api.fontshare.com/v2/css?f[]=clash-display@700&f[]=satoshi@400;500;700&display=swap`

**Signature elements:**
- Dynamic spotlight following cursor on title slide (from `dynamic-spotlight-cta`)
- Glassmorphism cards with `backdrop-filter: blur(12px)` (from `feature-cards-block`)
- Neon glow on accent elements: `box-shadow: 0 0 20px var(--accent-glow)`
- Grid pattern background: thin white lines at 3% opacity
- Code blocks with typewriter reveal (from `typewriter`)
- Flip text for cycling feature names (from `flip-text`)

**Title slide:** Deep dark with subtle grid, headline with dynamic spotlight cursor effect, neon accent glow
**Content slides:** Dark with glassmorphism cards, code in monospace with typewriter entry
**Closing slide:** Full neon glow CTA with magnetic hover

---

### Preset 3: Warm Signal

**Vibe:** Clean, confident, approachable. Professional without being corporate.
**Primary library:** UseLayouts (spring physics) + TripleD (page sections)
**Best for:** Client pitches, team presentations, workshops

```css
:root {
  --bg-primary: #ffffff;
  --bg-warm: #faf6f1;
  --text-primary: #1a1a1a;
  --text-secondary: #555555;
  --accent: #e8642c;
  --accent-soft: rgba(232, 100, 44, 0.08);
  --surface: #f5f5f5;
  --rule: #e5e5e5;
  --font-display: 'DM Serif Display', serif;
  --font-body: 'Inter', sans-serif;
}
```

**Signature elements:**
- Clean split layouts (text left, visual right) with direction-aware transitions (from `vertical-tabs`)
- Spring pill indicator for section navigation (from `discrete-tabs`)
- Feature carousel card stack for multi-item slides (from `feature-carousel`)
- Staggered list entry for bullet points (from `stacked-list`)
- Numbered section markers with counter animation

**Title slide:** White background, large serif headline, warm accent rule below, fade-in with subtle scale
**Content slides:** Alternating white/warm-white, split layouts, spring-animated tabs
**Closing slide:** Warm background with accent CTA, expandable contact details

---

### Preset 4: Brutalist Bold

**Vibe:** Loud, playful, unapologetic. Stands out in a sea of boring decks.
**Primary library:** Neobrutal (complete design system)
**Best for:** Workshop content, creative talks, developer audiences, internal presentations

```css
:root {
  --bg-primary: #f0eefc;
  --bg-white: #ffffff;
  --text-primary: #000000;
  --accent: #B6ACE4;
  --accent-alt: #97ee88;
  --black: #000000;
  --shadow-brutal: 4px 4px 0px 0px var(--black);
  --shadow-brutal-lg: 8px 8px 0px 0px var(--black);
  --font-display: 'Space Grotesk', sans-serif;
  --font-body: 'Space Grotesk', sans-serif;
}
```

**Signature elements:**
- Hard shadow cards: `border: 2px solid black; box-shadow: 8px 8px 0 0 black` (from Neobrutal `Card`)
- Press-in hover on interactive elements (from Neobrutal `Button`)
- Bold bordered badges for slide labels (from Neobrutal `Badge`)
- Flat, saturated accent colours. Zero gradients.
- Visible structure: borders, shadows, no subtlety
- Progress bar with neobrutal styling (from Neobrutal `Progress`)
- Accent colour rotation between slides (lavender, mint, peach, sky, lemon)

**Title slide:** White card with `--shadow-brutal-lg` centered on accent background, headline in heavy weight
**Content slides:** Hard shadow cards on coloured backgrounds, rotating accent per section
**Closing slide:** Bold black background, white text, accent CTA with press-in effect

**Theme variants** (swap per section for energy):
- Lavender: `#B6ACE4` / `#f0eefc`
- Mint: `#97ee88` / `#eefbec`
- Peach: `#f5a8a8` / `#fef0f0`
- Sky: `#88c8ee` / `#ecf5fb`
- Lemon: `#f5e888` / `#fefaec`

---

### Preset 5: Dark Botanical

**Vibe:** Elegant, sophisticated, premium. High-end keynote energy.
**Primary library:** TripleD (glassmorphism, atmospheric effects)
**Best for:** Keynotes, premium product reveals, executive presentations

```css
:root {
  --bg-primary: #0f0f0f;
  --bg-deep: #080808;
  --text-primary: #e8e4df;
  --text-secondary: #9a9590;
  --accent-warm: #d4a574;
  --accent-pink: #e8b4b8;
  --accent-gold: #c9b896;
  --surface: rgba(255, 255, 255, 0.04);
  --rule: rgba(255, 255, 255, 0.06);
  --font-display: 'Cormorant', serif;
  --font-body: 'IBM Plex Sans', sans-serif;
}
```

**Signature elements:**
- Abstract soft gradient circles (blurred CSS radial-gradients, 2-3 overlapping)
- Thin vertical accent lines (1px gold or pink, partial height)
- Slow cinematic reveals: `duration: 1s`, scale from `0.95` with blur fade (from `staggered-hero` slowed down)
- Counter-up for stat reveals with gold numerals (from `counter-up`)
- Italic signature typography for pull quotes
- Glowing waves on title slide (from `glowy-waves-hero`)
- **No illustrations. Only abstract CSS shapes.**

---

### Preset 6: Swiss Grid

**Vibe:** Minimal, precise, Bauhaus-inspired. Maximum clarity.
**Primary library:** UseLayouts (precise micro-interactions)
**Best for:** Data presentations, design talks, structured content

```css
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f5f5f5;
  --text-primary: #000000;
  --text-secondary: #666666;
  --accent: #ff3300;
  --surface: #f0f0f0;
  --rule: #000000;
  --font-display: 'Archivo', sans-serif;
  --font-body: 'Nunito', sans-serif;
}
```

**Signature elements:**
- Visible grid: thin black lines at 5% opacity creating structure
- Asymmetric layouts: content deliberately off-centre
- Red accent used only for ONE element per slide
- Strong typographic hierarchy: massive display vs. small body
- Geometric shapes: circles, lines, rectangles as structural decoration
- Direction-aware slide transitions (from `vertical-tabs`)
- Minimal motion: fast, precise, no spring physics. `ease-out` only, 300ms max.

---

## Content Density Rules

Hard limits per slide type. Do not exceed.

| Slide Type | Max Content |
|---|---|
| **Title** | 1 headline + 1 subtitle (+ optional tagline) |
| **Section divider** | 1 section number + 1 section name |
| **Content** | 1 headline + 4-6 bullet points OR 1 headline + 2 short paragraphs |
| **Feature grid** | 1 headline + max 6 cards (3x2) |
| **Stats** | 1 headline + max 4 stat numbers |
| **Quote** | 1 quote (max 3 lines) + attribution |
| **Image** | 1 headline + 1 image (max 60vh height) |
| **Code** | 1 headline + max 15 lines of code |
| **Comparison** | 1 headline + 2 columns |
| **Closing/CTA** | 1 headline + 1 action line + contact details |

**If content doesn't fit, add a slide. Never shrink text to fit.**

---

## Slide Type Templates

### Section Divider Slide

**CRITICAL: The section number and section name must NEVER overlap.** The layout below enforces clear separation — use it for every section divider.

```html
<section class="slide section-divider">
  <div class="slide-bg"><!-- Preset-specific atmosphere --></div>
  <div class="section-divider-content">
    <div class="section-number-row">
      <span class="reveal section-number">01</span>
      <span class="reveal section-rule"></span>
    </div>
    <h2 class="reveal section-title">The Evolution</h2>
    <p class="reveal section-subtitle">Three paradigms. Three ways of telling computers what to do.</p>
  </div>
</section>
```

**Required CSS for section dividers — this MUST be included:**

```css
.section-divider-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  padding: var(--slide-padding);
  gap: var(--content-gap);
}
.section-number-row {
  display: flex;
  align-items: center;
  gap: clamp(0.75rem, 2vw, 1.5rem);
}
.section-number {
  font-size: clamp(4rem, 12vw, 10rem);
  font-weight: 900;
  line-height: 1;
  color: var(--accent);
  font-family: var(--font-display);
}
.section-rule {
  flex: 1;
  max-width: clamp(3rem, 10vw, 8rem);
  height: 2px;
  background: var(--rule);
}
.section-divider .section-title {
  font-size: clamp(2rem, 5vw, 4rem);
  font-weight: 700;
  font-family: var(--font-display);
  margin: 0;
  line-height: 1.1;
}
.section-divider .section-subtitle {
  font-size: var(--subtitle-size);
  color: var(--text-secondary);
  margin: 0;
  max-width: 30ch;
}
```

**Layout rule:** The section number, horizontal rule, title, and subtitle are stacked vertically in a flex column with consistent `gap: var(--content-gap)` spacing. This guarantees the number and title never overlap regardless of viewport size.

### Title Slide

```html
<section class="slide title-slide">
  <div class="slide-bg"><!-- Preset-specific atmosphere: gradient blobs, grid, shapes --></div>
  <div class="slide-content">
    <p class="reveal label">PRESENTATION LABEL</p>
    <h1 class="reveal reveal-word">The Main Headline Here</h1>
    <p class="reveal subtitle">Supporting line — one sentence max</p>
    <div class="reveal author">
      <span class="author-name">Speaker Name</span>
      <span class="author-detail">Role / Date</span>
    </div>
  </div>
</section>
```

### Content Slide

```html
<section class="slide">
  <div class="slide-content">
    <p class="reveal label">SECTION NAME</p>
    <h2 class="reveal">Slide Headline</h2>
    <div class="reveal body-content">
      <p>Content here. One idea per slide.</p>
    </div>
  </div>
  <div class="slide-footer">
    <span class="slide-number">03 / 12</span>
  </div>
</section>
```

### Stats Slide

```html
<section class="slide stats-slide">
  <div class="slide-content">
    <h2 class="reveal">The Numbers</h2>
    <div class="stats-grid reveal">
      <div class="stat">
        <span class="stat-number" data-target="85">0</span>
        <span class="stat-unit">%</span>
        <span class="stat-label">Conversion rate</span>
      </div>
      <!-- Use counter-up animation from TripleD counter-up component -->
    </div>
  </div>
</section>
```

### Code Slide

```html
<section class="slide code-slide">
  <div class="slide-content">
    <h2 class="reveal">Code Example</h2>
    <pre class="reveal code-block"><code><!-- Use typewriter reveal from TripleD typewriter --></code></pre>
  </div>
</section>
```

### Quote Slide

```html
<section class="slide quote-slide">
  <div class="slide-content">
    <blockquote class="reveal-blur">
      <p>"The quote text here, max three lines."</p>
      <cite>Attribution</cite>
    </blockquote>
  </div>
</section>
```

---

## Progress Bar & Navigation Dots

```css
/* Progress bar — fixed top */
.progress-bar-track {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: var(--rule);
  z-index: 1000;
}
.progress-bar {
  height: 100%;
  background: var(--accent);
  width: 0%;
  transition: width 0.3s ease;
}

/* Navigation dots — fixed right */
.nav-dots {
  position: fixed;
  right: clamp(0.75rem, 2vw, 2rem);
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  gap: 8px;
  z-index: 1000;
}
.nav-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  border: none;
  background: var(--text-secondary);
  opacity: 0.3;
  cursor: pointer;
  transition: opacity 0.3s, transform 0.3s;
  padding: 0;
}
.nav-dot.active {
  opacity: 1;
  transform: scale(1.4);
  background: var(--accent);
}
```

---

## Background Effects

Use preset-appropriate atmospheric effects. Never mix styles.

```css
/* Gradient mesh (Editorial Gravity, Dark Botanical) */
.bg-gradient-mesh {
  background:
    radial-gradient(ellipse at 20% 80%, rgba(var(--accent-rgb), 0.15) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 20%, rgba(var(--accent-rgb), 0.08) 0%, transparent 50%),
    var(--bg-primary);
}

/* Grid pattern (Neon Studio, Swiss Grid) */
.bg-grid {
  background-image:
    linear-gradient(rgba(var(--grid-rgb), 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(var(--grid-rgb), 0.05) 1px, transparent 1px);
  background-size: 60px 60px;
}

/* Floating gradient blobs — animated (Dark Botanical, Editorial Gravity) */
.bg-blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  animation: float 8s ease-in-out infinite alternate;
}
@keyframes float {
  0% { transform: translate(0, 0) scale(1); }
  100% { transform: translate(30px, -20px) scale(1.1); }
}
```

---

## Counter Animation (for Stats Slides)

Adapted from TripleD `counter-up` component:

```javascript
function animateCounters() {
  document.querySelectorAll('.stat-number[data-target]').forEach(el => {
    const observer = new IntersectionObserver(entries => {
      if (entries[0].isIntersecting) {
        const target = parseInt(el.dataset.target);
        const duration = 1500;
        const start = performance.now();
        function tick(now) {
          const elapsed = now - start;
          const progress = Math.min(elapsed / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
          el.textContent = Math.round(target * eased);
          if (progress < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
        observer.disconnect();
      }
    }, { threshold: 0.5 });
    observer.observe(el);
  });
}
```

---

## Word Split Animation (for Headlines)

Adapted from TripleD `auto-revealing-heading`:

```javascript
function splitWords() {
  document.querySelectorAll('.reveal-word').forEach(el => {
    const words = el.textContent.trim().split(/\s+/);
    el.innerHTML = words.map((word, i) =>
      `<span style="transition-delay: ${i * 60}ms">${word}</span>`
    ).join(' ');
  });
}
```

---

## DO NOT USE (Anti-AI-Slop)

**Emojis:** NEVER use emojis as icons in slides. They scream "AI generated." Use typographic markers instead: bold letters (R, W, X, F), numbers (01, 02, 03), symbols (>, //, +, *), or styled CSS squares/circles with text inside. Neobrutal squares with single letters > emojis every time.

**Fonts:** Inter, Roboto, Arial as display/headline fonts. (Inter is fine as body.)
**Colours:** `#6366f1` (generic indigo), purple-on-white, purple gradients.
**Layouts:** Everything centred on every slide, identical card grids, generic SaaS hero patterns.
**Decorations:** Realistic illustrations, gratuitous glassmorphism without purpose, unnecessary gradients.
**Motion:** Bounce animations, excessive parallax, ornamental-only effects.

---

## Choosing a Preset

If the user doesn't specify, choose based on context:

| Context | Recommended Preset |
|---|---|
| Workshop, teaching | **Brutalist Bold** or **Warm Signal** |
| Keynote, thought leadership | **Editorial Gravity** or **Dark Botanical** |
| Tech talk, dev audience | **Neon Studio** or **Brutalist Bold** |
| Client pitch, professional | **Warm Signal** or **Editorial Gravity** |
| Data presentation | **Swiss Grid** |
| Product launch, premium | **Dark Botanical** |
| Creative / design talk | **Brutalist Bold** or **Swiss Grid** |

---

## Quality Checks Before Shipping

1. **Navigate with arrows, space, swipe, and wheel.** All must work.
2. **F key toggles fullscreen.** Must work.
3. **Every slide has at least one animated reveal.** No static slides.
4. **Content density within limits.** No slide violates the density table.
5. **Section divider: number and title do not overlap.** Number, rule, title, and subtitle are stacked vertically with `gap: var(--content-gap)`.
6. **Text readable at any viewport.** Resize browser — `clamp()` must handle it.
6. **Brand test:** If you swap out the fonts and colours, would the animations and layout still feel distinctive? If everything depends on the colour palette, the design is too weak.
7. **One idea per slide.** If a slide has two ideas, split it.
8. **Motion serves hierarchy.** Every animation makes something clearer. Remove ornamental-only motion.
9. **No AI-slop patterns.** Check against the DO NOT USE list.
10. **Progress bar and nav dots work.** Both update correctly on navigation.

---

## Accessibility

- Semantic HTML: `<section>`, `<nav>`, `<h1>`-`<h3>`, `<blockquote>`
- All navigation keyboard-accessible
- `aria-label` on nav dots
- `prefers-reduced-motion` support:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

## Print Export (Optional)

For PDF handouts, add a print stylesheet:

```css
@media print {
  html { scroll-snap-type: none; }
  .slide {
    height: auto;
    min-height: 100vh;
    page-break-after: always;
    page-break-inside: avoid;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .progress-bar-track, .nav-dots { display: none; }
  .reveal, .reveal-scale, .reveal-left, .reveal-right, .reveal-blur {
    opacity: 1 !important;
    transform: none !important;
    filter: none !important;
  }
  .reveal-word span { opacity: 1 !important; transform: none !important; }
}
```

---

## Presenter Mode (Speaker View)

Press **S** on any deck to open a separate presenter window. The audience view stays in the original window — the two stay synchronized via `BroadcastChannel`.

### Architecture

```
┌─────────────────────┬──────────────────┐
│ 🔵 CURRENT          │ 🟣 NEXT           │
│ (iframe preview)    │ (iframe preview)  │
├─────────────────────┼──────────────────┤
│ 🟠 SPEAKER SCRIPT   │                   │
│ (scrollable notes)  │                   │
├─────────────────────┴──────────────────┤
│ 🟢 TIMER  ⏱ 12:34   3 / 8              │
│ [← Prev][Next →]                       │
└────────────────────────────────────────┘
```

Four draggable, resizable cards:

| Card | Purpose |
|---|---|
| **CURRENT** (🔵) | Pixel-perfect iframe preview of the current slide. What the audience sees right now. |
| **NEXT** (🟣) | Preview of the next slide. Prepares transition sentences before flipping. |
| **SPEAKER SCRIPT** (🟠) | Large-font speaker notes (`<aside class="notes">` content). Scrollable, high contrast. |
| **TIMER** (🟢) | Elapsed time, slide counter, Prev/Next/Reset buttons. |

### How It Works

1. **Iframe previews** — Each preview card loads the same deck HTML with `?preview=N` query parameter. The runtime detects this and renders only slide N with no chrome (no progress bar, no nav dots, no keyboard handlers). Iframes are 1920×1080, scaled via `transform: scale()` to fit the card body.

2. **Smooth navigation** — After initial load, the presenter sends `postMessage({type:'preview-goto', idx:N})` to each iframe. The iframe just toggles `.is-active` between slides — no reload, no flicker.

3. **BroadcastChannel sync** — Both windows communicate over `BroadcastChannel('html-ppt-presenter-' + location.pathname)`. Navigation and theme changes flow both ways.

4. **Draggable cards** — Drag by the card header (colored dot + title bar). Resize by dragging the bottom-right corner. Position and size are saved to `localStorage` and restored on next open.

5. **Layout reset** — Bottom bar has a "Reset Layout" button that clears `localStorage` and restores the default two-column layout.

### Required HTML Structure

Speaker notes go inside `<aside class="notes">` within each slide section:

```html
<section class="slide" data-title="Agenda">
  <h2>Today's Agenda</h2>
  <p>Content visible to audience...</p>
  <aside class="notes">
    <p>Hello everyone — today I want to talk about <strong>a problem many people overlook</strong>...</p>
    <p>First, a bold claim: <em>making slides and delivering slides are two different things</em>.</p>
    <p>Next, I'll prove this with 3 concrete examples...</p>
  </aside>
</section>
```

The `<aside class="notes">` is `display: none` in the audience view via CSS — only visible in the presenter window's speaker script card.

### Speaker Script Authoring Rules

**Every slide's `<aside class="notes">` should contain 150–300 words.** Three golden rules:

1. **Prompt signals, not lines to read** — Bold key points, separate transition sentences into their own paragraphs, list data and names clearly. The goal is "glance and continue," not "read verbatim."
2. **150–300 words per slide** — Less than 150 and you'll run out of prompts; more than 300 and you won't have time to scan them all. Pace: ~2–3 minutes per slide.
3. **Write it like you speak** — Use conversational language. "Therefore" becomes "so"; "this approach" not "the aforementioned methodology." Read it aloud — if it sounds like written prose, rewrite it.

Supported inline formatting in notes:
- `<strong>` — Highlighted (orange in presenter view)
- `<em>` — Italic emphasis (blue in presenter view)
- `<code>` — Monospace font
- `<p>` — Paragraph breaks (each paragraph should cover ~30-60 seconds of speaking)

### Keyboard Shortcuts

| Key | Audience View | Presenter View |
|---|---|---|
| `S` | Open presenter window | — |
| `←` `→` / `Space` / `PgUp` `PgDn` | Navigate slides | Navigate slides |
| `F` | Toggle fullscreen | — |
| `O` | Slide overview grid | — |
| `N` | Notes overlay (bottom drawer) | — |
| `T` | Cycle themes | Cycle themes (syncs) |
| `R` | — | Reset timer |
| `Esc` | Close overlays | Close presenter window |
| `A` | Cycle animation on current slide | — |

### Implementation: JavaScript

Add this to the `SlidePresentation` constructor and class:

```javascript
class SlidePresentation {
  constructor() {
    // ... existing setup ...
    this.presenterWin = null;
    this.channelName = 'html-ppt-presenter-' + location.pathname;
    this.setupBroadcastChannel();
    this.setupPresenterMode();
  }

  // ========== BroadcastChannel for presenter sync ==========
  setupBroadcastChannel() {
    try {
      this.bc = new BroadcastChannel(this.channelName);
      this.bc.onmessage = (e) => {
        if (!e.data) return;
        if (e.data.type === 'go' && typeof e.data.idx === 'number') {
          this.goToSlide(e.data.idx, true);
        } else if (e.data.type === 'theme' && e.data.name) {
          this.applyTheme(e.data.name);
        }
      };
    } catch(e) { this.bc = null; }
  }

  // ========== Presenter Mode — Magnetic-card popup ==========
  setupPresenterMode() {
    document.addEventListener('keydown', (e) => {
      if (e.key === 's' || e.key === 'S') {
        e.preventDefault();
        this.openPresenterWindow();
      }
    });
  }

  openPresenterWindow() {
    if (this.presenterWin && !this.presenterWin.closed) {
      this.presenterWin.focus();
      return;
    }

    const deckUrl = location.protocol + '//' + location.host + location.pathname;
    const slideMeta = this.slides.map((s, i) => {
      const note = s.querySelector('.notes, aside.notes, .speaker-notes');
      return {
        title: s.getAttribute('data-title') ||
          (s.querySelector('h1,h2,h3')||{}).textContent || ('Slide '+(i+1)),
        notes: note ? note.innerHTML : ''
      };
    });

    const html = this.buildPresenterHTML(deckUrl, slideMeta, this.slides.length, this.currentSlide, this.channelName);
    this.presenterWin = window.open('', 'html-ppt-presenter', 'width=1280,height=820,menubar=no,toolbar=no');
    if (!this.presenterWin) {
      alert('Please allow popups to use presenter view');
      return;
    }
    this.presenterWin.document.open();
    this.presenterWin.document.write(html);
    this.presenterWin.document.close();
  }

  buildPresenterHTML(deckUrl, slideMeta, total, startIdx, channelName) {
    const metaJSON = JSON.stringify(slideMeta);
    const storageKey = 'html-ppt-presenter:' + location.pathname;
    return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>Presenter View</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body {
    width: 100%; height: 100%; overflow: hidden;
    background: #1a1d24;
    background-image:
      radial-gradient(circle at 20% 30%, rgba(88,166,255,.04), transparent 50%),
      radial-gradient(circle at 80% 70%, rgba(188,140,255,.04), transparent 50%);
    color: #e6edf3;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", sans-serif;
  }
  #stage { position: absolute; inset: 0; overflow: hidden; }
  .pcard {
    position: absolute; background: #0d1117;
    border: 1px solid rgba(255,255,255,.1); border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0,0,0,.45), 0 0 0 1px rgba(255,255,255,.02);
    display: flex; flex-direction: column; overflow: hidden;
    min-width: 180px; min-height: 100px;
    transition: box-shadow .2s, border-color .2s;
  }
  .pcard.dragging { box-shadow: 0 16px 48px rgba(0,0,0,.6), 0 0 0 2px rgba(88,166,255,.5); border-color: #58a6ff; transition: none; z-index: 9999; }
  .pcard.resizing { box-shadow: 0 16px 48px rgba(0,0,0,.6), 0 0 0 2px rgba(63,185,80,.5); border-color: #3fb950; transition: none; z-index: 9999; }
  .pcard:hover { border-color: rgba(88,166,255,.3); }
  .pcard-head {
    display: flex; align-items: center; gap: 10px; padding: 8px 12px;
    background: rgba(255,255,255,.04); border-bottom: 1px solid rgba(255,255,255,.06);
    cursor: move; user-select: none; flex-shrink: 0;
  }
  .pcard-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--dot-color, #58a6ff); flex-shrink: 0; }
  .pcard-title { font-size: 11px; letter-spacing: .15em; text-transform: uppercase; font-weight: 700; color: #8b949e; flex: 1; }
  .pcard-meta { font-size: 11px; color: #6e7681; }
  .pcard-body { flex: 1; position: relative; overflow: hidden; min-height: 0; }
  .pcard-preview .pcard-body { background: #000; }
  .pcard-preview iframe {
    position: absolute; top: 0; left: 0; width: 1920px; height: 1080px;
    border: none; transform-origin: top left; pointer-events: none; background: transparent;
  }
  .pcard-notes .pcard-body {
    padding: 14px 18px; overflow-y: auto; font-size: 18px; line-height: 1.75;
    color: #d0d7de; font-family: "Noto Sans SC", -apple-system, sans-serif;
  }
  .pcard-notes .pcard-body p { margin: 0 0 .7em 0; }
  .pcard-notes .pcard-body strong { color: #f0883e; }
  .pcard-notes .pcard-body em { color: #58a6ff; font-style: normal; }
  .pcard-notes .pcard-body code {
    font-family: "SF Mono", monospace; font-size: .9em;
    background: rgba(255,255,255,.08); padding: 1px 6px; border-radius: 4px;
  }
  .pcard-notes .empty { color: #484f58; font-style: italic; }
  .pcard-timer .pcard-body {
    display: flex; flex-direction: column; gap: 14px;
    padding: 18px 20px; justify-content: center;
  }
  .timer-display {
    font-family: "SF Mono", "JetBrains Mono", monospace;
    font-size: 42px; font-weight: 700; color: #3fb950; letter-spacing: .04em; line-height: 1;
  }
  .timer-row { display: flex; align-items: center; gap: 12px; font-size: 14px; color: #8b949e; }
  .timer-row .label { font-size: 10px; letter-spacing: .15em; text-transform: uppercase; color: #6e7681; }
  .timer-row .val { color: #e6edf3; font-weight: 600; font-family: "SF Mono", monospace; }
  .timer-controls { display: flex; gap: 8px; flex-wrap: wrap; }
  .timer-btn {
    background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.1);
    color: #e6edf3; padding: 6px 12px; border-radius: 6px; font-size: 12px;
    cursor: pointer; font-family: inherit;
  }
  .timer-btn:hover { background: rgba(88,166,255,.15); border-color: #58a6ff; }
  .pcard-resize {
    position: absolute; right: 0; bottom: 0; width: 18px; height: 18px;
    cursor: nwse-resize;
    background: linear-gradient(135deg, transparent 50%, rgba(255,255,255,.25) 50%, rgba(255,255,255,.25) 60%, transparent 60%, transparent 70%, rgba(255,255,255,.25) 70%, rgba(255,255,255,.25) 80%, transparent 80%);
    z-index: 5;
  }
  .hint-bar {
    position: fixed; bottom: 0; left: 0; right: 0;
    background: rgba(0,0,0,.6); backdrop-filter: blur(10px);
    border-top: 1px solid rgba(255,255,255,.08);
    padding: 6px 16px; font-size: 11px; color: #8b949e;
    display: flex; gap: 18px; align-items: center; z-index: 1000;
  }
  .hint-bar kbd {
    background: rgba(255,255,255,.08); padding: 1px 6px; border-radius: 3px;
    font-family: "SF Mono", monospace; font-size: 10px;
    border: 1px solid rgba(255,255,255,.1); color: #e6edf3;
  }
  .hint-bar .reset-layout {
    margin-left: auto; background: transparent; border: 1px solid rgba(255,255,255,.15);
    color: #8b949e; padding: 3px 10px; border-radius: 4px; font-size: 11px; cursor: pointer;
  }
  .hint-bar .reset-layout:hover { background: rgba(248,81,73,.15); border-color: #f85149; color: #f85149; }
  body.is-dragging-card * { user-select: none !important; }
  body.is-dragging-card iframe { pointer-events: none !important; }
</style>
</head>
<body>
<div id="stage">
  <div class="pcard pcard-preview" id="card-cur" style="--dot-color:#58a6ff">
    <div class="pcard-head" data-drag><span class="pcard-dot"></span><span class="pcard-title">CURRENT</span><span class="pcard-meta" id="cur-meta">—</span></div>
    <div class="pcard-body"><iframe id="iframe-cur"></iframe></div>
    <div class="pcard-resize" data-resize></div>
  </div>
  <div class="pcard pcard-preview" id="card-nxt" style="--dot-color:#bc8cff">
    <div class="pcard-head" data-drag><span class="pcard-dot"></span><span class="pcard-title">NEXT</span><span class="pcard-meta" id="nxt-meta">—</span></div>
    <div class="pcard-body"><iframe id="iframe-nxt"></iframe></div>
    <div class="pcard-resize" data-resize></div>
  </div>
  <div class="pcard pcard-notes" id="card-notes" style="--dot-color:#f0883e">
    <div class="pcard-head" data-drag><span class="pcard-dot"></span><span class="pcard-title">SPEAKER SCRIPT</span></div>
    <div class="pcard-body" id="notes-body"></div>
    <div class="pcard-resize" data-resize></div>
  </div>
  <div class="pcard pcard-timer" id="card-timer" style="--dot-color:#3fb950">
    <div class="pcard-head" data-drag><span class="pcard-dot"></span><span class="pcard-title">TIMER</span></div>
    <div class="pcard-body">
      <div class="timer-display" id="timer-display">00:00</div>
      <div class="timer-row"><span class="label">Slide</span><span class="val" id="timer-count">1 / ${total}</span></div>
      <div class="timer-controls">
        <button class="timer-btn" id="btn-prev">← Prev</button>
        <button class="timer-btn" id="btn-next">Next →</button>
        <button class="timer-btn" id="btn-reset">Reset</button>
      </div>
    </div>
    <div class="pcard-resize" data-resize></div>
  </div>
</div>
<div class="hint-bar">
  <span><kbd>← →</kbd> Navigate</span>
  <span><kbd>R</kbd> Reset timer</span>
  <span><kbd>Esc</kbd> Close</span>
  <span style="color:#6e7681">Drag header to move · Drag corner to resize</span>
  <button class="reset-layout" id="reset-layout">Reset Layout</button>
</div>
<script>
(function(){
  var slideMeta = ${metaJSON};
  var total = ${total};
  var idx = ${startIdx};
  var deckUrl = ${JSON.stringify(deckUrl)};
  var STORAGE_KEY = ${JSON.stringify(storageKey)};
  var bc;
  try { bc = new BroadcastChannel(${JSON.stringify(channelName)}); } catch(e) {}

  var iframeCur = document.getElementById('iframe-cur');
  var iframeNxt = document.getElementById('iframe-nxt');
  var notesBody = document.getElementById('notes-body');
  var curMeta = document.getElementById('cur-meta');
  var nxtMeta = document.getElementById('nxt-meta');
  var timerDisplay = document.getElementById('timer-display');
  var timerCount = document.getElementById('timer-count');

  function defaultLayout() {
    var w = window.innerWidth, h = window.innerHeight - 36;
    return {
      'card-cur':   { x: 16, y: 16, w: Math.round(w*0.55)-24, h: Math.round(h*0.62)-16 },
      'card-nxt':   { x: Math.round(w*0.55)+8, y: 16, w: w-Math.round(w*0.55)-24, h: Math.round(h*0.42)-16 },
      'card-notes': { x: Math.round(w*0.55)+8, y: Math.round(h*0.42)+8, w: w-Math.round(w*0.55)-24, h: h-Math.round(h*0.42)-16 },
      'card-timer': { x: 16, y: Math.round(h*0.62)+8, w: Math.round(w*0.55)-24, h: h-Math.round(h*0.62)-16 }
    };
  }
  function applyLayout(l) {
    Object.keys(l).forEach(function(id){
      var el = document.getElementById(id), p = l[id];
      if (el && p) { el.style.left=p.x+'px'; el.style.top=p.y+'px'; el.style.width=p.w+'px'; el.style.height=p.h+'px'; }
    });
    rescaleAll();
  }
  function readLayout() { try { var s=localStorage.getItem(STORAGE_KEY); if(s) return JSON.parse(s); } catch(e){} return defaultLayout(); }
  function saveLayout() {
    var l={};
    ['card-cur','card-nxt','card-notes','card-timer'].forEach(function(id){
      var el=document.getElementById(id);
      if(el) l[id]={x:parseInt(el.style.left)||0,y:parseInt(el.style.top)||0,w:parseInt(el.style.width)||300,h:parseInt(el.style.height)||200};
    });
    try{localStorage.setItem(STORAGE_KEY,JSON.stringify(l))}catch(e){}
  }
  function rescaleIframe(iframe) {
    if(!iframe||iframe.style.display==='none') return;
    var body=iframe.parentElement, cw=body.clientWidth, ch=body.clientHeight;
    if(!cw||!ch) return;
    var s=Math.min(cw/1920, ch/1080);
    iframe.style.transform='scale('+s+')';
    var sw=1920*s, sh=1080*s;
    iframe.style.left=Math.max(0,(cw-sw)/2)+'px';
    iframe.style.top=Math.max(0,(ch-sh)/2)+'px';
  }
  function rescaleAll(){ rescaleIframe(iframeCur); rescaleIframe(iframeNxt); }
  window.addEventListener('resize', rescaleAll);

  // Drag
  document.querySelectorAll('[data-drag]').forEach(function(handle){
    handle.addEventListener('mousedown',function(e){
      if(e.button!==0) return;
      var card=handle.closest('.pcard'); if(!card) return;
      e.preventDefault(); card.classList.add('dragging'); document.body.classList.add('is-dragging-card');
      var sx=e.clientX, sy=e.clientY, sl=parseInt(card.style.left)||0, st=parseInt(card.style.top)||0;
      function mv(ev){ card.style.left=Math.max(0,Math.min(window.innerWidth-100,sl+ev.clientX-sx))+'px'; card.style.top=Math.max(0,Math.min(window.innerHeight-50,st+ev.clientY-sy))+'px'; }
      function up(){ card.classList.remove('dragging'); document.body.classList.remove('is-dragging-card'); document.removeEventListener('mousemove',mv); document.removeEventListener('mouseup',up); saveLayout(); }
      document.addEventListener('mousemove',mv); document.addEventListener('mouseup',up);
    });
  });
  // Resize
  document.querySelectorAll('[data-resize]').forEach(function(handle){
    handle.addEventListener('mousedown',function(e){
      if(e.button!==0) return;
      var card=handle.closest('.pcard'); if(!card) return;
      e.preventDefault(); e.stopPropagation(); card.classList.add('resizing'); document.body.classList.add('is-dragging-card');
      var sx=e.clientX, sy=e.clientY, sw=parseInt(card.style.width)||card.offsetWidth, sh=parseInt(card.style.height)||card.offsetHeight;
      function mv(ev){ card.style.width=Math.max(180,sw+ev.clientX-sx)+'px'; card.style.height=Math.max(100,sh+ev.clientY-sy)+'px'; if(card.querySelector('iframe')) rescaleIframe(card.querySelector('iframe')); }
      function up(){ card.classList.remove('resizing'); document.body.classList.remove('is-dragging-card'); document.removeEventListener('mousemove',mv); document.removeEventListener('mouseup',up); rescaleAll(); saveLayout(); }
      document.addEventListener('mousemove',mv); document.addEventListener('mouseup',up);
    });
  });

  // Preview iframe ready
  var iframeReady={cur:false,nxt:false};
  window.addEventListener('message',function(e){
    if(!e.data||e.data.type!=='preview-ready') return;
    var iframe=null;
    if(e.source===iframeCur.contentWindow){ iframeReady.cur=true; iframe=iframeCur; postGoto(iframeCur,idx); }
    else if(e.source===iframeNxt.contentWindow){ iframeReady.nxt=true; iframe=iframeNxt; postGoto(iframeNxt,idx+1<total?idx+1:idx); }
    if(iframe) rescaleIframe(iframe);
  });
  function postGoto(iframe,n){ try{iframe.contentWindow.postMessage({type:'preview-goto',idx:n},'*')}catch(e){} }

  function update(n) {
    n=Math.max(0,Math.min(total-1,n)); idx=n;
    if(iframeReady.cur) postGoto(iframeCur,n);
    curMeta.textContent=(n+1)+'/'+total;
    if(n+1<total){
      iframeNxt.style.display='';
      var end=document.querySelector('#card-nxt .preview-end'); if(end) end.remove();
      if(iframeReady.nxt) postGoto(iframeNxt,n+1);
      nxtMeta.textContent=(n+2)+'/'+total;
    } else {
      iframeNxt.style.display='none';
      var body=document.querySelector('#card-nxt .pcard-body');
      if(body&&!body.querySelector('.preview-end')){ var e=document.createElement('div'); e.className='preview-end'; e.textContent='— END —'; body.appendChild(e); }
      nxtMeta.textContent='END';
    }
    notesBody.innerHTML=slideMeta[n].notes||'<span class="empty">(No notes for this slide)</span>';
    timerCount.textContent=(n+1)+' / '+total;
  }

  // Timer
  var tStart=Date.now();
  setInterval(function(){ var s=Math.floor((Date.now()-tStart)/1000); timerDisplay.textContent=String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0'); },1000);
  function resetTimer(){ tStart=Date.now(); timerDisplay.textContent='00:00'; }

  // BroadcastChannel
  if(bc){
    bc.onmessage=function(e){ if(!e.data) return; if(e.data.type==='go') update(e.data.idx); };
  }
  function go(n){ update(n); if(bc) bc.postMessage({type:'go',idx:idx}); }

  // Buttons
  document.getElementById('btn-prev').addEventListener('click',function(){ go(idx-1); });
  document.getElementById('btn-next').addEventListener('click',function(){ go(idx+1); });
  document.getElementById('btn-reset').addEventListener('click', resetTimer);
  document.getElementById('reset-layout').addEventListener('click',function(){
    if(confirm('Reset card layout?')){ try{localStorage.removeItem(STORAGE_KEY)}catch(e){} applyLayout(defaultLayout()); }
  });

  // Keyboard
  document.addEventListener('keydown',function(e){
    if(e.metaKey||e.ctrlKey||e.altKey) return;
    switch(e.key){
      case'ArrowRight':case' ':case'PageDown': go(idx+1); e.preventDefault(); break;
      case'ArrowLeft':case'PageUp': go(idx-1); e.preventDefault(); break;
      case'Home': go(0); break;
      case'End': go(total-1); break;
      case'r':case'R': resetTimer(); break;
      case'Escape': window.close(); break;
    }
  });

  iframeCur.addEventListener('load',function(){ rescaleIframe(iframeCur); });
  iframeNxt.addEventListener('load',function(){ rescaleIframe(iframeNxt); });

  // Init
  applyLayout(readLayout());
  iframeCur.src = deckUrl + '?preview=' + (idx+1);
  if(idx+1 < total) iframeNxt.src = deckUrl + '?preview=' + (idx+2);
  notesBody.innerHTML = slideMeta[idx].notes || '<span class="empty">(No notes for this slide)</span>';
  curMeta.textContent = (idx+1)+'/'+total;
  nxtMeta.textContent = (idx+2)+'/'+total;
  timerCount.textContent = (idx+1)+' / '+total;
})();
<\/script>
</body></html>`;
  }
}
```

### Preview-Only Mode (iframe handler)

The deck must also detect `?preview=N` in the URL and enter single-slide locked mode. Add this at the top of the `SlidePresentation` constructor, before any other setup:

```javascript
constructor() {
  // Preview-only mode: when loaded as iframe with ?preview=N
  const previewMatch = /[?&]preview=(\d+)/.exec(location.search || '');
  if (previewMatch) {
    const previewIdx = parseInt(previewMatch[1], 10) - 1;
    this.slides = document.querySelectorAll('.slide');
    // Show only the preview slide, hide chrome
    this.slides.forEach((s, i) => {
      const active = (i === previewIdx);
      s.classList.toggle('is-active', active);
      s.style.display = active ? '' : 'none';
      if (active) { s.style.opacity = '1'; s.style.transform = 'none'; s.style.pointerEvents = 'auto'; }
    });
    document.querySelectorAll('.progress-bar-track, .nav-dots, .slide-footer').forEach(el => { el.style.display = 'none'; });
    // Listen for postMessage from presenter parent
    window.addEventListener('message', (e) => {
      if (!e.data) return;
      if (e.data.type === 'preview-goto') {
        const n = parseInt(e.data.idx, 10);
        if (n >= 0 && n < this.slides.length) {
          this.slides.forEach((s, i) => {
            s.classList.toggle('is-active', i === n);
            s.style.display = i === n ? '' : 'none';
          });
        }
      }
    });
    try { window.parent.postMessage({ type: 'preview-ready' }, '*'); } catch(e) {}
    return; // Skip normal presentation setup
  }

  // ... normal constructor code follows ...
}
```

### Dual-Screen Workflow

When presenting with a projector or external display:

1. Open the deck HTML in the browser
2. Press **S** — the presenter window pops up
3. Drag the **audience window** to the projector/external screen, press **F** for fullscreen
4. Keep the **presenter window** on your own screen
5. Navigate with arrows — both windows stay synchronized

### Quality Checks for Presenter Mode

1. **Press S — presenter window opens.** Four cards visible with correct layout.
2. **Navigate with arrows in presenter window.** Both CURRENT and NEXT previews update without flicker.
3. **Speaker notes display correctly.** Bold text is orange, italic is blue, code is monospace.
4. **Timer runs and resets with R.**
5. **Drag cards and resize.** Layout persists after closing and reopening.
6. **Reset Layout button works.** Restores default two-column arrangement.
7. **Notes are invisible in audience view.** `<aside class="notes>` must be `display: none` in the base CSS.
