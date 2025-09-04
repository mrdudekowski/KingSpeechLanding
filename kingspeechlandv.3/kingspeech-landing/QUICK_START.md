# 🚀 Быстрый старт GAS + Telegram интеграции

## ⚡ За 5 минут

### 1. Создайте GAS проект
- Перейдите на [script.google.com](https://script.google.com)
- Создайте новый проект
- Вставьте код из `gas-webhook.gs`

### 2. Настройте переменные
В `gas-webhook.gs` замените:
```javascript
TELEGRAM_BOT_TOKEN: 'YOUR_BOT_TOKEN',     // ← Ваш токен бота
MANAGER_CHAT_ID: 'YOUR_CHAT_ID',         // ← ID чата
SPREADSHEET_ID: 'YOUR_SPREADSHEET_ID',   // ← ID таблицы
```

### 3. Разверните
- Нажмите "Развернуть" → "Веб-приложение"
- Доступ: "Все"
- Скопируйте URL

### 4. Обновите лендинг
В `js/modules/gas-integration.js` замените:
```javascript
GAS_WEBHOOK_URL: 'https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec'
```

### 5. Протестируйте
- Отправьте тестовую заявку
- Проверьте Telegram и Google Sheets

## 📋 Что нужно подготовить

### Telegram Bot
- Токен от @BotFather
- Chat ID (добавьте бота в чат)

### Google Sheets
- Таблица с листом "Leads"
- ID из URL таблицы

## ⚡ Готово!

Теперь все заявки с лендинга будут:
- ✅ Сохраняться в Google Sheets
- ✅ Отправляться в Telegram
- ✅ Защищены от спама
- ✅ Валидироваться

## 🔧 Подробная инструкция

См. `GAS_SETUP.md` для детального описания каждого шага.
