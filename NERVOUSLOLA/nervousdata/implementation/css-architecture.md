# 🎨 CSS Architecture - ITCSS Implementation

## 📋 Обзор

CSS архитектура проекта "Нервная Лола" построена на методологии ITCSS (Inverted Triangle CSS) с использованием BEM naming convention и CSS Custom Properties.

## 🏗️ ITCSS Layers

### Структура папок
```
assets/css/
├── main.css              # Entry point
├── variables.css         # CSS Custom Properties
├── animations.css        # Animation definitions
├── breakpoints.css       # Media queries
├── critical.css          # Critical CSS (above fold)
├── force-fixes.css       # Hotfixes and overrides
│
├── itcss/
│   ├── main.css         # ITCSS entry
│   ├── 1-settings.css   # Variables
│   ├── 2-tools.css      # Mixins (via PostCSS)
│   ├── 3-generic.css    # Normalize, reset
│   ├── 4-elements.css   # Base HTML elements
│   ├── 5-objects.css    # Layout patterns
│   ├── 6-components.css # UI components
│   └── 7-utilities.css  # Utility classes
│
└── components/
    ├── header.css
    ├── nav.css
    ├── hero.css
    ├── carousel.css
    ├── menu.css
    ├── footer.css
    └── ...
```

## 📊 ITCSS Specificity Graph

```
Settings     [Specificity: 0]
Tools        [Specificity: 0]
Generic      [Specificity: 0.001]
Elements     [Specificity: 0.001]
Objects      [Specificity: 0.01]
Components   [Specificity: 0.01-0.1]
Utilities    [Specificity: 0.1-1]
```

Принцип: **Специфичность увеличивается вниз по треугольнику**

## 🎯 Layer 1: Settings

### CSS Custom Properties
```css
:root {
  /* Colors */
  --color-primary: #FF7A00;
  --color-primary-dark: #E56F00;
  --color-secondary: #1A1A1A;
  --color-accent-gold: #FFD700;
  --color-text: #2C2C2C;
  --color-text-light: #666666;
  --color-background: #FFFFFF;
  --color-background-alt: #F8F9FA;
  
  /* Typography */
  --font-primary: 'Montserrat', sans-serif;
  --font-secondary: 'Playfair Display', serif;
  --font-size-base: 16px;
  --font-size-h1: 3rem;
  --font-size-h2: 2.5rem;
  --font-weight-regular: 400;
  --font-weight-bold: 700;
  
  /* Spacing */
  --spacing-xs: 0.5rem;
  --spacing-sm: 1rem;
  --spacing-md: 2rem;
  --spacing-lg: 3rem;
  --spacing-xl: 4rem;
  
  /* Layout */
  --container-max-width: 1200px;
  --section-padding: 4rem 2rem;
  --grid-gap: 2rem;
  
  /* Effects */
  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 4px 8px rgba(0, 0, 0, 0.15);
  --shadow-lg: 0 8px 16px rgba(0, 0, 0, 0.2);
  --border-radius: 8px;
  --transition-speed: 0.3s;
}
```

### Dark mode support (future)
```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-background: #1A1A1A;
    --color-text: #FFFFFF;
    /* ... */
  }
}
```

## 🛠️ Layer 2: Tools

Используется PostCSS для "миксинов":
```css
/* Via PostCSS custom media */
@custom-media --mobile (max-width: 767px);
@custom-media --tablet (min-width: 768px) and (max-width: 1023px);
@custom-media --desktop (min-width: 1024px);
```

## 🔧 Layer 3: Generic

### Normalize & Reset
```css
/* Modern normalize */
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  min-height: 100vh;
  text-rendering: optimizeSpeed;
}
```

## 📐 Layer 4: Elements

### Base HTML Styling
```css
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-secondary);
  font-weight: var(--font-weight-bold);
  line-height: 1.2;
  margin-bottom: var(--spacing-sm);
}

p {
  margin-bottom: var(--spacing-sm);
  font-family: var(--font-primary);
}

a {
  color: var(--color-primary);
  text-decoration: none;
  transition: color var(--transition-speed);
}

a:hover {
  color: var(--color-primary-dark);
}
```

## 🔲 Layer 5: Objects

### Layout Patterns
```css
/* Container */
.o-container {
  max-width: var(--container-max-width);
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--spacing-md);
  padding-right: var(--spacing-md);
}

/* Grid */
.o-grid {
  display: grid;
  gap: var(--grid-gap);
}

/* Flex */
.o-flex {
  display: flex;
  gap: var(--spacing-sm);
}

/* Section */
.o-section {
  padding: var(--section-padding);
}
```

## 🧩 Layer 6: Components

### BEM Naming Convention
```css
/* Block */
.nav {
  background: var(--color-background);
}

/* Element */
.nav__list {
  display: flex;
  list-style: none;
}

.nav__item {
  padding: var(--spacing-sm);
}

.nav__link {
  color: var(--color-text);
}

/* Modifier */
.nav--transparent {
  background: transparent;
}

.nav__link--active {
  color: var(--color-primary);
  font-weight: var(--font-weight-bold);
}
```

### Component Example: Carousel
```css
.testimonials {
  position: relative;
  overflow: hidden;
}

.testimonials__container {
  position: relative;
  width: 100%;
}

.testimonials__track {
  display: flex;
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform;
}

.testimonial-card {
  flex: 0 0 100%;
  padding: var(--spacing-md);
}

.testimonials__controls {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: var(--spacing-md);
  margin-top: var(--spacing-lg);
}
```

## ⚡ Layer 7: Utilities

### Utility Classes
```css
/* Display */
.u-hidden { display: none !important; }
.u-block { display: block !important; }
.u-flex { display: flex !important; }

/* Spacing */
.u-mt-sm { margin-top: var(--spacing-sm) !important; }
.u-mb-md { margin-bottom: var(--spacing-md) !important; }
.u-p-lg { padding: var(--spacing-lg) !important; }

/* Text */
.u-text-center { text-align: center !important; }
.u-text-bold { font-weight: var(--font-weight-bold) !important; }

/* Colors */
.u-color-primary { color: var(--color-primary) !important; }
.u-bg-gold { background-color: var(--color-accent-gold) !important; }
```

## 📱 Responsive Design

### Mobile-First Approach
```css
/* Mobile (default) */
.grid {
  grid-template-columns: 1fr;
}

/* Tablet */
@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

### Breakpoints System
```css
/* breakpoints.css */
:root {
  --bp-mobile: 767px;
  --bp-tablet: 768px;
  --bp-desktop: 1024px;
  --bp-wide: 1440px;
}
```

## 🎬 Animations

### Performance-First Animations
```css
/* Используем только transform и opacity для 60fps */
.fade-in {
  animation: fadeIn 0.6s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* GPU acceleration */
.animated-element {
  will-change: transform;
  transform: translateZ(0);
}
```

## 📊 CSS Metrics

- **Total Lines**: ~5000
- **Files**: 25+ файлов
- **Components**: 15+ компонентов
- **Utilities**: 30+ утилит
- **Variables**: 50+ CSS Custom Properties
- **File Size**: ~45KB (uncompressed), ~12KB (минифицировано)

## 🔧 Build Process

### PostCSS Pipeline
```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer'),
    require('postcss-custom-media'),
    require('cssnano')({
      preset: 'default'
    })
  ]
};
```

### Webpack Integration
```javascript
// webpack.config.js
module: {
  rules: [{
    test: /\.css$/,
    use: [
      MiniCssExtractPlugin.loader,
      'css-loader',
      'postcss-loader'
    ]
  }]
}
```

## 🎯 Code Quality

### Stylelint Rules
- **color-no-hex**: Только CSS Custom Properties
- **selector-max-id**: ID селекторы запрещены
- **declaration-no-important**: !important только в utilities
- **selector-class-pattern**: BEM naming
- **selector-max-compound-selectors**: Максимум 3 уровня

## 🐛 Known Issues

### Issue 1: Specificity Wars
**Problem**: Некоторые компоненты имеют повышенную специфичность  
**Solution**: Рефакторинг к BEM и уменьшение вложенности  
**Status**: ⚠️ Частично решено

### Issue 2: Critical CSS
**Problem**: Размер critical CSS > 14KB  
**Solution**: Оптимизация и удаление неиспользуемых стилей  
**Status**: ✅ Решено

## 📚 Извлеченные универсальные паттерны

Для Landing Memory Bank:
1. **ARCHITECTURE/css/ITCSS.md** - ITCSS методология
2. **ARCHITECTURE/css/BEM.md** - BEM naming
3. **ARCHITECTURE/css/CSS_CUSTOM_PROPERTIES.md** - CSS переменные
4. **ARCHITECTURE/css/RESPONSIVE_DESIGN.md** - Responsive подход

## 🎯 Lessons Learned

### Что сработало хорошо
- ✅ ITCSS обеспечивает предсказуемую специфичность
- ✅ BEM делает код самодокументируемым
- ✅ CSS Custom Properties упрощают темизацию
- ✅ Mobile-first подход ускоряет разработку

### Что можно улучшить
- ⚠️ Уменьшить глубину вложенности селекторов
- ⚠️ Добавить автоматическую генерацию критического CSS
- ⚠️ Внедрить CSS-in-JS для динамических стилей
- ⚠️ Улучшить организацию utilities

---

**Complexity**: High  
**Methodology**: ITCSS + BEM  
**Lines of Code**: ~5000  
**Status**: ✅ Production-ready  
**Maintainability**: ⭐⭐⭐⭐⭐

