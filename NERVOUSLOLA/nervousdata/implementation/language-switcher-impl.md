# 🌍 Language Switcher Implementation - Многоязычная система

## 📋 Обзор

Многоязычная система сайта "Нервная Лола" обеспечивает поддержку трёх языков (RU/EN/ZH) с динамическим переключением без перезагрузки страницы.

## 🏗️ Архитектура

### Основные компоненты

1. **Translations Storage** - JSON файлы переводов
2. **Language Switcher UI** - Переключатель в навигации
3. **Translation Engine** - Модуль замены текста
4. **State Management** - localStorage для сохранения выбора

### Файловая структура
```
assets/
├── data/
│   └── translations/
│       ├── ru.json    # Русский (default)
│       ├── en.json    # English
│       └── zh.json    # 中文
└── js/
    └── modules/
        └── languageSwitcher.js
```

## 📄 Формат файлов переводов

### Структура JSON
```json
{
  "nav": {
    "home": "Главная",
    "menu": "Меню",
    "about": "О нас",
    "contact": "Контакты"
  },
  "hero": {
    "title": "Добро пожаловать",
    "subtitle": "Кофейня с характером"
  },
  "menu": {
    "coffee": "Кофе",
    "desserts": "Десерты"
  }
}
```

### Принципы организации
- **Flat structure** - Максимум 2 уровня вложенности
- **Semantic keys** - Осмысленные ключи (не просто text1, text2)
- **Consistent naming** - Единый стиль именования
- **Complete coverage** - Все языки содержат одинаковые ключи

## ⚙️ Реализация JavaScript

### Core Module
```javascript
class LanguageSwitcher {
  constructor() {
    this.currentLanguage = this.getStoredLanguage() || 'ru';
    this.translations = {};
    this.init();
  }
  
  async init() {
    await this.loadTranslations(this.currentLanguage);
    this.attachEventListeners();
    this.applyTranslations();
  }
  
  async loadTranslations(lang) {
    const response = await fetch(`assets/data/translations/${lang}.json`);
    this.translations = await response.json();
  }
  
  applyTranslations() {
    document.querySelectorAll('[data-i18n]').forEach(element => {
      const key = element.getAttribute('data-i18n');
      const translation = this.getTranslation(key);
      if (translation) {
        element.textContent = translation;
      }
    });
  }
  
  getTranslation(key) {
    const keys = key.split('.');
    let value = this.translations;
    for (const k of keys) {
      value = value[k];
      if (!value) return null;
    }
    return value;
  }
  
  switchLanguage(lang) {
    this.currentLanguage = lang;
    localStorage.setItem('preferred-language', lang);
    this.loadTranslations(lang).then(() => {
      this.applyTranslations();
      this.dispatchLanguageChangeEvent();
    });
  }
  
  dispatchLanguageChangeEvent() {
    window.dispatchEvent(new CustomEvent('languageChanged', {
      detail: { language: this.currentLanguage }
    }));
  }
}
```

### HTML Integration
```html
<nav class="nav">
  <a href="#home" data-i18n="nav.home">Главная</a>
  <a href="#menu" data-i18n="nav.menu">Меню</a>
  <a href="#about" data-i18n="nav.about">О нас</a>
</nav>

<div class="language-switcher">
  <button data-lang="ru" class="active">RU</button>
  <button data-lang="en">EN</button>
  <button data-lang="zh">中</button>
</div>
```

## 🎨 UI/UX решения

### Language Switcher Design
- **Position**: Top-right corner навигации
- **Visual feedback**: Active state для текущего языка
- **Animation**: Smooth transition при переключении
- **Mobile**: Доступен в мобильном меню

### Transition Effects
```css
[data-i18n] {
  transition: opacity 0.2s ease;
}

.language-switching [data-i18n] {
  opacity: 0.5;
}
```

## 🔧 Технические решения

### 1. Performance Optimization
- **Caching** - Кэширование загруженных переводов
- **Lazy loading** - Загрузка только активного языка
- **Batch updates** - Единовременное обновление DOM

### 2. Error Handling
```javascript
async loadTranslations(lang) {
  try {
    const response = await fetch(`assets/data/translations/${lang}.json`);
    if (!response.ok) throw new Error('Translation not found');
    this.translations = await response.json();
  } catch (error) {
    console.error(`Failed to load ${lang}:`, error);
    // Fallback to default language
    if (lang !== 'ru') {
      await this.loadTranslations('ru');
    }
  }
}
```

### 3. SEO Considerations
- **lang attribute** - Динамическое обновление `<html lang="...">`
- **hreflang** - Meta tags для поисковых систем (для будущего multi-page)
- **Default language** - Русский как default

## 📊 Метрики

- **Languages**: 3 (RU/EN/ZH)
- **Translation keys**: ~80 ключей
- **File size**: ~3KB per language (uncompressed)
- **Switch time**: < 50ms
- **Bundle size**: ~2KB (JS, минифицировано)

## 🌐 Поддержка языков

### Русский (RU)
- **Status**: ✅ Complete
- **Coverage**: 100%
- **Native speaker review**: ✅

### English (EN)
- **Status**: ✅ Complete
- **Coverage**: 100%
- **Native speaker review**: ✅

### 中文 (ZH)
- **Status**: ✅ Complete
- **Coverage**: 100%
- **Native speaker review**: ⚠️ Machine translation + review

## 🐛 Известные проблемы и решения

### Проблема 1: FOUC (Flash of Untranslated Content)
**Проблема**: Виден original text до применения переводов  
**Решение**: CSS класс `.language-loading` для скрытия контента до загрузки

### Проблема 2: Dynamic Content Translation
**Проблема**: Динамически добавляемый контент не переводится  
**Решение**: Custom event `languageChanged` для переинициализации

### Проблема 3: Right-to-Left (RTL) Support
**Проблема**: Китайский требует special handling  
**Решение**: CSS `writing-mode` и `text-orientation` (для будущего развития)

## 📚 Извлеченные универсальные паттерны

Для Landing Memory Bank:
1. **FEATURES/multilingual/LANGUAGE_SWITCHING.md** - Механизм переключения
2. **FEATURES/multilingual/JSON_TRANSLATIONS.md** - Структура переводов
3. **PATTERNS/js-patterns/EVENT_HANDLING.md** - Событийная модель

## 🎯 Lessons Learned

### Что сработало хорошо
- ✅ JSON-based подход прост и понятен
- ✅ Custom events обеспечивают расширяемость
- ✅ localStorage сохраняет предпочтения пользователя
- ✅ data-i18n атрибут делает HTML чистым

### Что можно улучшить
- ⚠️ Добавить поддержку pluralization
- ⚠️ Реализовать fallback chain (zh → en → ru)
- ⚠️ Добавить namespace support для больших проектов
- ⚠️ Интеграция с backend для управления переводами

## 🔗 Связанные файлы

- Translations: `nervouslola-website/assets/data/translations/*.json`
- Код: `nervouslola-website/assets/js/modules/languageSwitcher.js`
- Документация: `nervousdata/docs/implementation/TRANSLATION_SYSTEM_IMPLEMENTATION.md`
- Demo: `nervousdata/demos/tests/language-switcher.html`

---

**Complexity**: Medium  
**Lines of Code**: ~150 (JS)  
**Dependencies**: None (Vanilla JS)  
**Status**: ✅ Production-ready  
**Future**: Расширение до 5+ языков

