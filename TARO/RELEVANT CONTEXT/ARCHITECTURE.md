# Архитектура проекта

## Обзор
Статический одностраничный лендинг на HTML/CSS/JS. Дизайн‑токены в `:root`, модульные стили и скрипты.

## Ключевые файлы
- `taro-landing-site/index.html` — разметка и подключения.
- `taro-landing-site/styles/main.css` — токены, базовые стили, секции, адаптивность.
- `taro-landing-site/styles/components.css` — компоненты.
- `taro-landing-site/styles/tarot-canvas.css` — декоративный холст.
- `taro-landing-site/scripts/main.js` — инициализация UI, lazy, preload.
- `taro-landing-site/scripts/resize-manager.js` — обработка ресайза.
- `taro-landing-site/scripts/tarot-canvas.js` — анимации/холст.
- `taro-landing-site/assets/` — изображения и ресурсы.
- `RELEVANT CONTEXT/` — документация.

## Секции страницы
- `header.site-header` — навигация, бургер.
- `section.hero` — фон, H1, подзаголовок, CTA.
- `section.about` — о специалисте.
- `section.services` — карточки услуг.
- `section.process` — шаги.
- `section.testimonials` — отзывы.
- `section.faq` — аккордеон.
- `section.contact` — контакты/CTA.
- `footer.site-footer` — копирайт, ссылки.

## Токены (SoT)
Заданы в `styles/main.css` (`:root`): цвета, типографика (`--font-family-*`, `--text-*`, веса), тени, радиусы, контейнеры, отступы, переходы.

## Типографика (сводка)
- Заголовки h1–h6: Inter.
- Текстовый контент (не заголовки/кнопки): Source Sans 3.
- Hero H1: El Messiri (600).

## Зависимости
- Google Fonts: Inter, Source Sans 3, El Messiri.
- Font Awesome (CDN) для иконок.

## Адаптивность
Mobile‑first, CSS Grid и Flexbox, брейкпоинты в `main.css`.

## Стандарты
Самодокументируемость, явные зависимости, Single Source of Truth.
