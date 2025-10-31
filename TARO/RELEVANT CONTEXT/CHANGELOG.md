# Changelog

## 2025-10-31 — Типографика и шрифты
- Подключён Source Sans 3 для строчного текста (глобально для `p, ul, li, ...`).
- Заголовки оставлены на Inter; Hero H1 переведён на El Messiri (600).
- Удалён ненужный El Messiri (ранее) и повторно добавлен для Hero H1 по запросу.

### Откат
- Чтобы вернуть Hero H1 на Inter: заменить `font-family` и `font-weight` в `.hero-title` на `var(--font-family-primary)` и `--font-weight-bold`.
- Чтобы убрать Source Sans 3 из текста: удалить блок глобальных селекторов с `font-family: var(--font-family-body);` в `styles/main.css` и/или переопределить на `var(--font-family-primary)`.
