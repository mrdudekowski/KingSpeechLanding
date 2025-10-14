# 🔧 JavaScript Modules - Модульная архитектура

## 📋 Обзор

JavaScript архитектура проекта "Нервная Лола" построена на нативных ES6 модулях с функциональным подходом и событийно-ориентированной моделью.

## 🏗️ Структура модулей

```
assets/js/
├── main.js              # Entry point
├── fallback.js          # Fallbacks для старых браузеров
│
├── modules/
│   ├── carousel.js      # Карусель отзывов
│   ├── languageSwitcher.js  # Многоязычность
│   ├── mobileMenu.js    # Мобильное меню
│   ├── smoothScroll.js  # Плавный скролл
│   ├── animations.js    # GSAP анимации
│   ├── videoBackground.js   # Видео фоны
│   └── contactForm.js   # Форма обратной связи
│
└── utils/
    ├── dom.js           # DOM utilities
    ├── events.js        # Event helpers
    └── storage.js       # localStorage wrapper
```

## 📦 Module Pattern

### ES6 Module Template
```javascript
// modules/example.js

/**
 * Example Module
 * @description Brief description of what this module does
 */

// Private variables
let privateState = null;

// Private functions
function privateHelper() {
  // Implementation
}

// Public API
export function init(options = {}) {
  // Initialization logic
}

export function destroy() {
  // Cleanup logic
}

// Default export (if needed)
export default {
  init,
  destroy
};
```

## 🔧 Core Modules

### 1. Main.js - Entry Point
```javascript
// main.js
import { init as initCarousel } from './modules/carousel.js';
import { init as initLanguageSwitcher } from './modules/languageSwitcher.js';
import { init as initMobileMenu } from './modules/mobileMenu.js';
import { init as initSmoothScroll } from './modules/smoothScroll.js';
import { init as initAnimations } from './modules/animations.js';

// Initialize all modules on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
  // Check for required features
  if (!supportsModernFeatures()) {
    loadFallbacks();
    return;
  }
  
  // Initialize modules
  initCarousel();
  initLanguageSwitcher();
  initMobileMenu();
  initSmoothScroll();
  initAnimations();
  
  // Mark as loaded
  document.body.classList.add('js-loaded');
});

function supportsModernFeatures() {
  return 'fetch' in window && 
         'Promise' in window && 
         'IntersectionObserver' in window;
}
```

### 2. Carousel Module
```javascript
// modules/carousel.js
import { gsap } from 'gsap';

let currentIndex = 0;
let autoplayInterval = null;
let slides = [];
let track = null;

export function init() {
  track = document.querySelector('.testimonials__track');
  slides = Array.from(document.querySelectorAll('.testimonial-card'));
  
  if (!track || slides.length === 0) return;
  
  setupControls();
  startAutoplay();
  setupTouchEvents();
  setupKeyboardNavigation();
}

function goToSlide(index) {
  // Boundary check
  if (index < 0) index = slides.length - 1;
  if (index >= slides.length) index = 0;
  
  currentIndex = index;
  
  // Animate
  gsap.to(track, {
    x: -slides[0].offsetWidth * currentIndex,
    duration: 0.6,
    ease: 'power2.inOut'
  });
  
  updateDots();
}

function startAutoplay() {
  stopAutoplay();
  autoplayInterval = setInterval(() => {
    goToSlide(currentIndex + 1);
  }, 5000);
}

function stopAutoplay() {
  if (autoplayInterval) {
    clearInterval(autoplayInterval);
    autoplayInterval = null;
  }
}

export function destroy() {
  stopAutoplay();
  // Remove event listeners
  // Cleanup GSAP animations
}
```

### 3. Language Switcher Module
```javascript
// modules/languageSwitcher.js

let currentLanguage = 'ru';
let translations = {};

export async function init() {
  currentLanguage = getStoredLanguage() || 'ru';
  
  await loadTranslations(currentLanguage);
  applyTranslations();
  setupSwitcher();
}

async function loadTranslations(lang) {
  try {
    const response = await fetch(`assets/data/translations/${lang}.json`);
    translations = await response.json();
  } catch (error) {
    console.error('Failed to load translations:', error);
    if (lang !== 'ru') {
      await loadTranslations('ru'); // Fallback
    }
  }
}

function applyTranslations() {
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    const translation = getNestedValue(translations, key);
    
    if (translation) {
      element.textContent = translation;
    }
  });
  
  // Update lang attribute
  document.documentElement.lang = currentLanguage;
}

function setupSwitcher() {
  const buttons = document.querySelectorAll('[data-lang]');
  
  buttons.forEach(button => {
    button.addEventListener('click', async () => {
      const lang = button.getAttribute('data-lang');
      await switchLanguage(lang);
    });
  });
}

async function switchLanguage(lang) {
  currentLanguage = lang;
  localStorage.setItem('preferred-language', lang);
  
  await loadTranslations(lang);
  applyTranslations();
  updateActiveSwitcher();
  
  // Dispatch event for other modules
  dispatchLanguageChange(lang);
}

function dispatchLanguageChange(lang) {
  window.dispatchEvent(new CustomEvent('languageChanged', {
    detail: { language: lang }
  }));
}

export { switchLanguage };
```

### 4. Animations Module
```javascript
// modules/animations.js
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

export function init() {
  // Fade in on scroll
  gsap.utils.toArray('.fade-in').forEach(element => {
    gsap.from(element, {
      opacity: 0,
      y: 50,
      duration: 1,
      scrollTrigger: {
        trigger: element,
        start: 'top 80%',
        end: 'top 20%',
        toggleActions: 'play none none reverse'
      }
    });
  });
  
  // Parallax effect
  gsap.utils.toArray('[data-parallax]').forEach(element => {
    const speed = element.getAttribute('data-parallax') || 0.5;
    
    gsap.to(element, {
      y: () => window.innerHeight * speed,
      ease: 'none',
      scrollTrigger: {
        trigger: element,
        start: 'top bottom',
        end: 'bottom top',
        scrub: true
      }
    });
  });
}
```

## 🛠️ Utility Modules

### DOM Utilities
```javascript
// utils/dom.js

export function $(selector, context = document) {
  return context.querySelector(selector);
}

export function $$(selector, context = document) {
  return Array.from(context.querySelectorAll(selector));
}

export function createElement(tag, attributes = {}, children = []) {
  const element = document.createElement(tag);
  
  Object.entries(attributes).forEach(([key, value]) => {
    if (key === 'className') {
      element.className = value;
    } else if (key.startsWith('data-')) {
      element.setAttribute(key, value);
    } else {
      element[key] = value;
    }
  });
  
  children.forEach(child => {
    if (typeof child === 'string') {
      element.appendChild(document.createTextNode(child));
    } else {
      element.appendChild(child);
    }
  });
  
  return element;
}

export function removeElement(element) {
  if (element && element.parentNode) {
    element.parentNode.removeChild(element);
  }
}
```

### Event Utilities
```javascript
// utils/events.js

export function delegate(eventType, selector, handler) {
  document.addEventListener(eventType, (event) => {
    const target = event.target.closest(selector);
    if (target) {
      handler.call(target, event);
    }
  });
}

export function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

export function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}
```

### Storage Utilities
```javascript
// utils/storage.js

export function setItem(key, value) {
  try {
    const serialized = JSON.stringify(value);
    localStorage.setItem(key, serialized);
    return true;
  } catch (error) {
    console.error('Storage error:', error);
    return false;
  }
}

export function getItem(key, defaultValue = null) {
  try {
    const serialized = localStorage.getItem(key);
    return serialized ? JSON.parse(serialized) : defaultValue;
  } catch (error) {
    console.error('Storage error:', error);
    return defaultValue;
  }
}

export function removeItem(key) {
  try {
    localStorage.removeItem(key);
    return true;
  } catch (error) {
    console.error('Storage error:', error);
    return false;
  }
}
```

## 🎯 Design Patterns

### 1. Module Pattern
- Инкапсуляция через ES6 модули
- Private/public API separation
- Singleton modules где необходимо

### 2. Event-Driven Architecture
```javascript
// Publisher
function notifyChange(data) {
  window.dispatchEvent(new CustomEvent('dataChanged', {
    detail: data
  }));
}

// Subscriber
window.addEventListener('dataChanged', (event) => {
  console.log('Data changed:', event.detail);
});
```

### 3. Factory Pattern
```javascript
// Factory for creating similar elements
function createCard(data) {
  return {
    element: createElement('div', { className: 'card' }),
    update: (newData) => { /* update logic */ },
    destroy: () => { /* cleanup */ }
  };
}
```

## 📊 JavaScript Metrics

- **Total Lines**: ~2000
- **Modules**: 12 модулей
- **Utilities**: 3 utility файла
- **Dependencies**: GSAP 3.13 (единственная внешняя зависимость)
- **Bundle Size**: ~25KB (минифицировано, без GSAP)
- **GSAP Size**: ~35KB (минифицировано)

## 🔧 Build & Optimization

### Webpack Configuration
```javascript
// webpack.config.js
module.exports = {
  entry: './assets/js/main.js',
  output: {
    filename: 'bundle.[contenthash].js',
    path: path.resolve(__dirname, 'dist')
  },
  module: {
    rules: [{
      test: /\.js$/,
      exclude: /node_modules/,
      use: {
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env']
        }
      }
    }]
  },
  optimization: {
    minimize: true,
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: 10
        }
      }
    }
  }
};
```

### Babel Configuration
```javascript
// .babelrc
{
  "presets": [
    ["@babel/preset-env", {
      "targets": {
        "browsers": [">0.25%", "not dead"]
      },
      "useBuiltIns": "usage",
      "corejs": 3
    }]
  ]
}
```

## 🎯 Code Quality

### ESLint Rules
- **no-var**: Только let/const
- **prefer-const**: Prefer const где возможно
- **arrow-body-style**: Consistent arrow functions
- **no-unused-vars**: No unused variables
- **eqeqeq**: Always use ===

## 🐛 Known Issues

### Issue 1: GSAP Bundle Size
**Problem**: GSAP adds ~35KB to bundle  
**Solution**: Tree-shaking неиспользуемых GSAP features  
**Status**: ⚠️ In progress

### Issue 2: Module Loading Order
**Problem**: Некоторые модули зависят от порядка инициализации  
**Solution**: Explicit dependency management  
**Status**: ✅ Resolved

## 📚 Извлеченные универсальные паттерны

Для Landing Memory Bank:
1. **ARCHITECTURE/javascript/MODULE_SYSTEM.md** - Модульная система
2. **ARCHITECTURE/javascript/ES6_PATTERNS.md** - ES6+ паттерны
3. **PATTERNS/js-patterns/EVENT_HANDLING.md** - Event-driven architecture
4. **PATTERNS/js-patterns/MODULE_PATTERNS.md** - Module patterns

## 🎯 Lessons Learned

### Что сработало хорошо
- ✅ ES6 модули обеспечивают чистую структуру
- ✅ Event-driven подход обеспечивает расширяемость
- ✅ Utility модули переиспользуемы
- ✅ Functional approach упрощает тестирование

### Что можно улучшить
- ⚠️ Добавить TypeScript для type safety
- ⚠️ Реализовать lazy loading модулей
- ⚠️ Добавить unit тесты
- ⚠️ Улучшить error handling

---

**Complexity**: Medium-High  
**Paradigm**: Functional + Event-driven  
**Lines of Code**: ~2000  
**Dependencies**: GSAP 3.13  
**Status**: ✅ Production-ready  
**Maintainability**: ⭐⭐⭐⭐☆

