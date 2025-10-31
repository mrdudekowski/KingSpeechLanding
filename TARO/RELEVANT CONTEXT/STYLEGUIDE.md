# Руководство по стилю (Styleguide)

## Дизайн‑токены (`styles/main.css :root`)
- Цвета фона и поверхностей: `--color-background(-gradient)`, `--color-surface`, `--color-surface-light`.
- Цвета золота: `--color-gold-dark|medium|classic|light`.
- Изумрудные акценты: `--color-emerald-*`.
- Текст: `--color-text-primary|secondary|accent`.
- Бордеры: `--color-border`, `--color-border-light`.
- Типографика: `--font-family-primary`, `--text-*`, веса `--font-weight-*`.
- Радиусы: `--radius-*`.
- Тени: `--shadow-*`, `--shadow-gold-*`.
- Переходы: `--transition-*`.
- Контейнеры: `--container-max-width`, `--container-padding`.
- Отступы: `--spacing-*`.

## Типографика
- Заголовки: Inter (см. `main.css`, селекторы `h1..h6`, `.section-title`, `.service-title`, `.step-title`).
- Текст (строчный контент): Source Sans 3 (селекторы на `p, ul, li, ...`).
- Hero H1: El Messiri (600) в `.hero-title`.

## Сетка и отступы
- Контейнер: класс `.container` использует токены ширины и паддингов.
- Секции: `section { padding: var(--spacing-3xl) 0; }`.
- Сетка услуг: CSS Grid (см. `.services-grid`).
- Гибкая верстка: Flexbox для навигации, кнопок, списков.

## Кнопки (Buttons)
- Базовый класс: `.btn` — типографика, размеры, радиус, переходы.
- Варианты:
  - `.btn-primary` — золотой градиент, тени, hover‑подъем.
  - `.btn-secondary` — прозрачный фон, золотая рамка/hover‑заливка.
  - `.btn-outline` — прозрачный фон, светлая рамка.
- Состояния hover/active — только там, где не тач‑экраны (`@media (hover: none)` отключает эффекты).

## Навигация/меню
- `.site-header` с полупрозрачным фоном и blur.
- Бургер `.hamburger` + мобильное меню `.mobile-menu` (fixed, blur, трансформации, анимации дыхания ссылок).

## Карточки (Services, Testimonials)
- `.service-card` — прозрачный фон, рамки, blur, золотые тени на hover.
- Иконка `.service-icon` — круглые бэйджи с градиентами, орбиты (`::before/::after`).
- `.testimonial-card` — компактные карточки с акцентами.

## Hero
- `.hero` — фон с WebP, затемнение, fixed (на десктопе), мобильный `scroll`.
- `.hero-title` — крупный заголовок (El Messiri 600), аккуратный letter‑spacing.
- `.hero-subtitle` — средний размер, вторичный цвет текста.

## Анимации
- Лёгкие keyframes (`emerald-glow-soft`, `gentle-pulse`, `card-breathe`).
- GPU‑ускорение для анимируемых элементов (`translateZ(0)`, `backface-visibility`).

## Адаптивность
- Основные точки: 768px, 1200px и 480px для типовых уменьшений.
- На мобильных: уменьшенные размеры текста, отключение тяжелых hover‑эффектов, упрощённые фоновые атрибуты.

## Практики
- Использовать токены вместо "магических чисел".
- Компонентные классы — максимально изолировать влияние на соседей.
- Поддерживать контраст и читабельность.
