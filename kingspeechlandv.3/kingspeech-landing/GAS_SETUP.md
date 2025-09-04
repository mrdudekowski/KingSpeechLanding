# 🚀 Настройка GAS + Telegram интеграции

## Обзор
Система автоматически отправляет заявки с лендинга в Telegram и сохраняет их в Google Sheets через Google Apps Script.

## 📋 Быстрая настройка (5 минут)

### 1. Создайте GAS проект
1. Перейдите на [script.google.com](https://script.google.com)
2. Нажмите "Новый проект"
3. Переименуйте проект в "KingSpeech Webhook"
4. Удалите весь код по умолчанию
5. Скопируйте содержимое файла `gas-webhook.gs` и вставьте в редактор
6. Сохраните проект (Ctrl+S)

### 2. Настройте переменные
В файле `gas-webhook.gs` найдите секцию `CONFIG` и замените:

```javascript
const CONFIG = {
  TELEGRAM_BOT_TOKEN: 'YOUR_BOT_TOKEN',        // ← Замените
  MANAGER_CHAT_ID: 'YOUR_CHAT_ID',            // ← Замените  
  SPREADSHEET_ID: 'YOUR_SPREADSHEET_ID',      // ← Замените
  SHEET_NAME: 'Leads',                        // ← Оставьте или измените
};
```

### 3. Получите Telegram Bot Token
1. Найдите @BotFather в Telegram
2. Отправьте `/newbot` или используйте существующий бот
3. Скопируйте токен (формат: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 4. Получите Chat ID
1. Добавьте бота в нужный чат/группу
2. Отправьте сообщение в чат
3. Откройте в браузере: `https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates`
4. Найдите `"chat":{"id":-123456789}` - это ваш Chat ID

### 5. Создайте Google Sheets
1. Создайте новую таблицу в Google Sheets
2. Переименуйте первый лист в "Leads"
3. Скопируйте ID из URL: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit`
4. Предоставьте доступ к таблице для GAS (если потребуется)

### 6. Разверните GAS
1. Нажмите "Развернуть" → "Веб-приложение"
2. Выполнить как: "Я"
3. У кого есть доступ: "Все"
4. Скопируйте URL веб-приложения

### 7. Обновите лендинг
В файле `js/modules/gas-integration.js` замените:

```javascript
GAS_WEBHOOK_URL: 'https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec'
```

### 8. Протестируйте
1. Отправьте тестовую заявку с лендинга
2. Проверьте Telegram - должно прийти уведомление
3. Проверьте Google Sheets - должна появиться новая строка

## 🔧 Детальная настройка

### Структура Google Sheets
Таблица автоматически создаст колонки:
- Дата/время
- Имя
- Email
- Телефон
- Мессенджер
- Цель
- Страница
- Источник
- UTM Source
- UTM Medium
- UTM Campaign
- Источник данных

### Формат Telegram уведомлений
```
🎯 Новая заявка с лендинга

👤 Имя: Иван Петров
📧 Email: ivan@example.com
📱 Телефон: +7 (999) 123-45-67
💬 Мессенджер: Telegram
🎯 Цель: Изучение английского
🌐 Страница: /contact
🔗 Источник: google.com

⏰ Время: 25.12.2024, 15:30:45
```

### Защита от спама
- **Honeypot поле**: скрытое поле `website` (должно быть пустым)
- **Валидация**: проверка обязательных полей
- **Email валидация**: проверка формата email
- **Phone валидация**: проверка формата телефона

## 🧪 Тестирование

### Health Check
Откройте в браузере URL вашего GAS webhook:
```
https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec
```

Должен вернуться JSON:
```json
{
  "ok": true,
  "message": "GAS Webhook работает",
  "data": {
    "status": "healthy",
    "config": {
      "valid": true,
      "errors": []
    },
    "stats": {
      "total_leads": 0,
      "today_leads": 0
    }
  }
}
```

### Тестовая заявка
Используйте Python скрипт для тестирования:
```bash
python test_gas_integration.py
```

## 🚨 Устранение неполадок

### Ошибка CORS
- Убедитесь, что GAS развернут как веб-приложение
- Проверьте, что доступ установлен "Все"

### Ошибка Telegram
- Проверьте правильность Bot Token
- Убедитесь, что бот добавлен в чат
- Проверьте Chat ID

### Ошибка Google Sheets
- Проверьте правильность Spreadsheet ID
- Убедитесь, что лист называется "Leads"
- Предоставьте доступ GAS к таблице

### Ошибка валидации
- Проверьте, что заполнены обязательные поля
- Убедитесь, что honeypot поле пустое
- Проверьте формат email и телефона

## 📊 Мониторинг

### Логи GAS
1. Откройте GAS проект
2. Перейдите в "Выполнения"
3. Просмотрите логи выполнения

### Статистика
Используйте метод `getStats()` для получения статистики:
- Общее количество заявок
- Заявки за сегодня
- Дата последней заявки

## ✅ Готово!

После настройки все заявки с лендинга будут:
- ✅ Автоматически сохраняться в Google Sheets
- ✅ Отправляться в Telegram
- ✅ Защищены от спама
- ✅ Валидироваться
- ✅ Отслеживаться в аналитике

## 🔗 Полезные ссылки

- [Google Apps Script](https://script.google.com)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Google Sheets API](https://developers.google.com/sheets/api)
