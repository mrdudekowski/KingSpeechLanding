# 🔧 GAS Fix Instructions - KingSpeech

## ❌ Проблема
**Ошибка в GAS коде:** `TypeError: ContentService.createTextOutput(...).setMimeType(...).setHeader is not a function`

## ✅ Решение

### 1. Исправить код в GAS редакторе

Замените функцию `createResponse` в вашем GAS проекте на исправленную версию:

```javascript
/**
 * Создание HTTP ответа
 */
function createResponse(success, message, data) {
  const response = {
    ok: success,
    message: message,
    data: data,
    timestamp: new Date().toISOString(),
    version: '2.0.0'
  };
  
  const output = ContentService
    .createTextOutput(JSON.stringify(response, null, 2))
    .setMimeType(ContentService.MimeType.JSON);
  
  // Устанавливаем заголовки CORS
  output.setHeaders({
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Cache-Control': 'no-cache, no-store, must-revalidate'
  });
  
  return output;
}
```

### 2. Сохранить и развернуть

1. **Сохранить** изменения в GAS редакторе (Ctrl+S)
2. **Развернуть** как новую версию веб-приложения
3. **Проверить** работу по URL: https://script.google.com/macros/s/AKfycbyJKbFN2XXobtZskHRUCIHwNBGSPpKn05rLt_KpRkIpulK2_l78ISWq_t-jhQW91aqM/exec

### 3. Тестирование

После исправления проверьте:

1. **Health check:** Откройте GAS URL в браузере
   - Должен вернуть JSON с `"ok": true`
   - Не должно быть ошибок

2. **Тест формы:** Заполните форму на сайте
   - Данные должны сохраниться в Google Sheets
   - Уведомление должно прийти в Telegram

## 📊 Ожидаемый результат

После исправления:
- ✅ GAS webhook работает без ошибок
- ✅ Формы отправляются успешно
- ✅ Данные сохраняются в Google Sheets
- ✅ Уведомления приходят в Telegram
- ✅ CORS заголовки работают корректно

## 🎯 Следующие шаги

1. **Исправить GAS код** (5 минут)
2. **Протестировать интеграцию** (10 минут)
3. **Проверить все формы** (5 минут)

**Общее время:** 20 минут

---

*Исправление готово к применению: 17 января 2025*
