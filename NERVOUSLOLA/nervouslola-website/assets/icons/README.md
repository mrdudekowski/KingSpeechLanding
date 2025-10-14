# 🎨 SVG Icon System - Nervous Lola

## 📋 Обзор

Современная система иконок на основе SVG sprites для кофейни "Нервная Лола".

**Технология:** SVG Sprites  
**Подход:** Inline SVG с <use>  
**Архитектура:** BEM naming convention  
**Browser Support:** 98%+ (все современные браузеры)

---

## 🗂️ Структура

```
assets/icons/
├── sprite.svg          # Основной SVG спрайт (все иконки в одном файле)
├── individual/         # Отдельные SVG файлы (источники) - TODO
└── README.md          # Эта документация
```

---

## 📐 Доступные иконки

### 1. Coffee (Кофе)
**ID:** `icon-coffee`  
**Использование:** Меню категория "Кофе"

### 2. Teapot (Чайник)
**ID:** `icon-teapot`  
**Использование:** Меню категория "Тизаны"

### 3. Hot Chocolate (Горячий шоколад)
**ID:** `icon-hotchoc`  
**Использование:** Меню категория "Не кофе"

### 4. Rum (Ром)
**ID:** `icon-rum`  
**Использование:** Меню категория "Напитки с алкогольной ароматикой"

---

## 🔧 Использование

### 1. Inline спрайт в HTML

**В начале `<body>` добавить:**
```html
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <!-- Содержимое sprite.svg -->
</svg>
```

### 2. Использование иконки

```html
<!-- Базовое использование -->
<svg class="icon">
  <use href="#icon-coffee"></use>
</svg>

<!-- С модификаторами размера -->
<svg class="icon icon--lg">
  <use href="#icon-teapot"></use>
</svg>

<!-- С кастомным цветом -->
<svg class="icon icon--primary">
  <use href="#icon-hotchoc"></use>
</svg>

<!-- Декоративная иконка (accessibility) -->
<svg class="icon" aria-hidden="true">
  <use href="#icon-rum"></use>
</svg>
```

---

## 🎨 CSS Стили

**Файл:** `assets/css/components/icons.css`

```css
/* Базовый класс */
.icon {
  display: inline-block;
  width: 24px;
  height: 24px;
  fill: currentColor;
  vertical-align: middle;
}

/* Модификаторы размера */
.icon--sm { width: 16px; height: 16px; }
.icon--md { width: 24px; height: 24px; }
.icon--lg { width: 32px; height: 32px; }
.icon--xl { width: 48px; height: 48px; }

/* Цветовые модификаторы */
.icon--primary { color: var(--color-primary); }
.icon--white { color: white; }
```

---

## ✅ Преимущества

1. **Один HTTP запрос** - все иконки в одном файле
2. **Масштабируемость** - SVG масштабируются без потери качества
3. **Стилизация через CSS** - цвет, размер, hover эффекты
4. **Малый размер** - SVG легче PNG
5. **Accessibility** - поддержка ARIA атрибутов
6. **Performance** - GPU acceleration для анимаций

---

## 🔧 Добавление новой иконки

1. Создать SVG файл (24x24 viewBox)
2. Оптимизировать через SVGO
3. Добавить `<symbol>` в `sprite.svg`:

```xml
<symbol id="icon-новая-иконка" viewBox="0 0 24 24">
  <path d="..." fill="currentColor"/>
</symbol>
```

4. Документировать в README
5. Использовать в HTML через `<use href="#icon-новая-иконка">`

---

## 📊 Рекомендации

### ✅ DO:
- Использовать `fill="currentColor"` для легкого изменения цвета
- Добавлять `aria-hidden="true"` для декоративных иконок
- Использовать BEM модификаторы для вариаций
- Оптимизировать SVG перед добавлением

### ❌ DON'T:
- Не использовать inline стили в SVG
- Не делать иконки слишком сложными
- Не забывать про viewBox
- Не использовать PNG вместо SVG

---

**Создано:** 2025-10-09  
**Подход:** @landing_memory_bank/ARCHITECTURE/css/BEM_NAMING.md  
**Источник знаний:** Context7 webpack documentation


