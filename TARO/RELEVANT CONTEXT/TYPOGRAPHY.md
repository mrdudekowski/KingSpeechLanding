# Типографика

## Подключения (index.html)
- Inter: `<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">`
- El Messiri: `<link href="https://fonts.googleapis.com/css2?family=El+Messiri:wght@400..700&display=swap" rel="stylesheet">`
- Source Sans 3: `<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,200..900;1,200..900&display=swap" rel="stylesheet">`

## Правила применения
- Заголовки h1–h6: Inter (через селекторы заголовков и `.section-title`, `.service-title`, `.step-title`).
- Текстовый контент (не заголовки и не кнопки): Source Sans 3 — задан глобально для `p, ul, ol, li, span, strong, em, small, blockquote, figcaption, time, address, label, input, textarea, select, option, table, td, th` и ряда текстовых классов.
- Hero H1: El Messiri (600), задан в `.hero-title`.

## Веса и размеры
- Веса определены в токенах: `--font-weight-light|normal|medium|semibold|bold`.
- Размеры текста: `--text-xs|sm|base|lg|xl|2xl|3xl|4xl|5xl`.

## Дополнительно
- `-webkit-font-smoothing`/`-moz-osx-font-smoothing` включены для body.
- Не использовать вес 300 для El Messiri (нет такого начертания).

## Примеры (main.css)
- Hero H1:
  ```css
  .hero-title {
    font-family: 'El Messiri', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    font-weight: 600;
  }
  ```
- Текстовый контент (фрагмент):
  ```css
  p, ul, li, span, strong, em, small, blockquote, figcaption, time, address,
  label, input, textarea, select, option, table, td, th,
  .about-description, .service-description, .step-description,
  .testimonial-text, .contact-description, .modal-subtitle, .footer-link,
  .nav-menu a {
    font-family: var(--font-family-body);
  }
  ```
