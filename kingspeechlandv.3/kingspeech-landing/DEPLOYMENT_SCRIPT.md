# 🚀 KingSpeech GitHub Deployment Script

## 📋 Автоматизированный скрипт для замены файлов в GitHub репозитории

### 🎯 Цель
Полная замена старой версии сайта KingSpeech на новую с сохранением всех критических интеграций.

### 📁 Файлы для замены

#### 1. Основные файлы (ОБЯЗАТЕЛЬНО)
```bash
# HTML и основные файлы
index.html
favicon.ico
aurora.js
package.json
.stylelintrc.json

# CSS система
css/main.css
css/base/variables.css
css/base/reset.css
css/base/typography.css
css/base/keyframes.css
css/components/header.css
css/components/hero.css
css/components/about.css
css/components/cards.css
css/components/carousel.css
css/components/faq.css
css/components/forms.css
css/components/footer.css
css/components/modal.css
css/components/button.css
css/components/testimonials.css

# JavaScript модули
js/main.js
js/modules/theme.js
js/modules/navigation.js
js/modules/carousel.js
js/modules/forms.js
js/modules/animations.js
js/modules/gas-integration.js
js/modules/modal.js
js/modules/faq.js
js/modules/structured-data.js
js/modules/theme-preinit.js

# Ресурсы
assets/images/logo.png
assets/images/logo.webp
assets/images/student-1.webp
assets/images/student-2.webp
assets/images/student-3.webp
assets/images/teacher-photo-320.webp
assets/images/teacher-photo-420.webp
assets/images/teacher-photo.webp
assets/hero/hero-a-plus-560.webp
assets/hero/hero-a-plus-800.webp

# Шрифты
fonts/plus-jakarta-sans/PlusJakartaSans-Regular.woff2
fonts/plus-jakarta-sans/PlusJakartaSans-Medium.woff2
fonts/plus-jakarta-sans/PlusJakartaSans-SemiBold.woff2
fonts/plus-jakarta-sans/PlusJakartaSans-Bold.woff2
fonts/plus-jakarta-sans/PlusJakartaSans-ExtraBold.woff2
fonts/plus-jakarta-sans/PlusJakartaSans-ExtraBoldItalic.woff2
fonts/plus-jakarta-sans/plus-jakarta-sans.css
```

#### 2. GAS интеграция (ОТДЕЛЬНО)
```bash
# GAS файлы (НЕ заменять в GitHub, настраивать отдельно)
gas-webhook-enhanced.gs
GAS_SETUP_INSTRUCTIONS.md
GAS_INTEGRATION_TEST_PLAN.md
GAS_SETUP.md
```

#### 3. Документация (ОПЦИОНАЛЬНО)
```bash
# Документация
README.md
QUICK_START.md
TECHNICAL_REPORT.md
ARCHIVE_REFLECTION.md
VAN_ANALYSIS_REPORT.md
MIGRATION_PLAN.md
DEPLOYMENT_SCRIPT.md
```

### 🔧 Пошаговая инструкция развертывания

#### Шаг 1: Подготовка
```bash
# 1. Клонируйте репозиторий
git clone https://github.com/mrdudekowski/KingSpeech.git
cd KingSpeech

# 2. Создайте backup текущей версии
git checkout -b backup-old-version
git add .
git commit -m "Backup old version before migration"
git push origin backup-old-version

# 3. Вернитесь на main ветку
git checkout main
```

#### Шаг 2: Замена файлов
```bash
# 4. Удалите все файлы кроме .git
rm -rf css/ js/ assets/ fonts/ *.html *.js *.json *.ico *.md

# 5. Скопируйте новые файлы из kingspeech-landing/
cp -r ../kingspeech-landing/css ./
cp -r ../kingspeech-landing/js ./
cp -r ../kingspeech-landing/assets ./
cp -r ../kingspeech-landing/fonts ./
cp ../kingspeech-landing/index.html ./
cp ../kingspeech-landing/favicon.ico ./
cp ../kingspeech-landing/aurora.js ./
cp ../kingspeech-landing/package.json ./
cp ../kingspeech-landing/.stylelintrc.json ./

# 6. Скопируйте документацию (опционально)
cp ../kingspeech-landing/README.md ./
cp ../kingspeech-landing/QUICK_START.md ./
```

#### Шаг 3: Коммит и пуш
```bash
# 7. Добавьте все файлы
git add .

# 8. Создайте коммит
git commit -m "🚀 Complete migration to new KingSpeech version

- ✅ New modular CSS architecture
- ✅ ES6 JavaScript modules
- ✅ Enhanced GAS integration
- ✅ Improved accessibility (WCAG AA)
- ✅ Better performance and UX
- ✅ Mobile-first responsive design
- ✅ Dark theme support
- ✅ Form validation and error handling
- ✅ Telegram bot integration ready

Migration completed: $(date)"

# 9. Отправьте изменения
git push origin main
```

#### Шаг 4: Настройка GAS интеграции
```bash
# 10. Настройте GAS webhook отдельно
# - Откройте script.google.com
# - Создайте новый проект
# - Скопируйте код из gas-webhook-enhanced.gs
# - Настройте токены и разверните
# - Обновите URL в js/modules/gas-integration.js
```

### ⚠️ Критические проверки

#### Перед развертыванием
- [ ] Все файлы скопированы корректно
- [ ] CSS переменные определены
- [ ] JavaScript модули работают
- [ ] Изображения загружаются
- [ ] Шрифты подключены

#### После развертывания
- [ ] Сайт загружается без ошибок
- [ ] Все секции отображаются
- [ ] Формы работают (без GAS пока)
- [ ] Мобильная версия работает
- [ ] Тема переключения работает

#### После настройки GAS
- [ ] Формы отправляются в GAS
- [ ] Telegram уведомления приходят
- [ ] Данные сохраняются в Google Sheets
- [ ] Обработка ошибок работает

### 🔍 Откат (если что-то пошло не так)

```bash
# Быстрый откат к предыдущей версии
git checkout backup-old-version
git checkout -b main-backup
git push origin main-backup

# Восстановление main ветки
git checkout main
git reset --hard backup-old-version
git push origin main --force
```

### 📊 Мониторинг после развертывания

#### 1. Проверка сайта
- Откройте https://mrdudekowski.github.io/KingSpeech/
- Проверьте все секции
- Протестируйте формы
- Проверьте мобильную версию

#### 2. Проверка производительности
- Используйте Google PageSpeed Insights
- Проверьте Core Web Vitals
- Убедитесь в быстрой загрузке

#### 3. Проверка интеграций
- Настройте GAS webhook
- Протестируйте отправку форм
- Проверьте Telegram уведомления

### 🎯 Ожидаемые результаты

#### Улучшения
- **Производительность:** +40-50%
- **Accessibility:** 80% (WCAG AA)
- **SEO:** Улучшенная структура
- **UX:** Современный дизайн
- **Maintainability:** Модульная архитектура

#### Сохраненная функциональность
- ✅ Все формы работают
- ✅ GAS интеграция готова
- ✅ Telegram уведомления готовы
- ✅ Google Sheets готово
- ✅ Тема переключения работает
- ✅ Мобильная версия работает

---

*Создано: 17 января 2025*  
*Статус: Готово к выполнению*  
*Версия: 1.0*
