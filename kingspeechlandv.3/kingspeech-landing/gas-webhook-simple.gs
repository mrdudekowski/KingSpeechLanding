/**
 * KingSpeech GAS Webhook - Simple Test Version
 * Максимально простая версия для тестирования
 */

const CONFIG = {
  TELEGRAM_BOT_TOKEN: 'YOUR_BOT_TOKEN',
  MANAGER_CHAT_ID: 'YOUR_CHAT_ID',
  SPREADSHEET_ID: 'YOUR_SPREADSHEET_ID',
  SHEET_NAME: 'LEADS'
};

/**
 * Обработка GET запросов (health check)
 */
function doGet(e) {
  try {
    console.log('🔍 Health check запрос');
    
    return ContentService
      .createTextOutput(JSON.stringify({
        ok: true,
        message: 'GAS Webhook работает',
        timestamp: new Date().toISOString(),
        version: '2.3.0-simple'
      }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    console.error('💥 Ошибка health check:', error);
    return ContentService
      .createTextOutput(JSON.stringify({
        ok: false,
        message: 'Ошибка: ' + error.toString()
      }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * Обработка POST запросов
 */
function doPost(e) {
  try {
    console.log('📥 Получен POST запрос');
    
    // Проверяем наличие данных
    if (!e || !e.postData) {
      return ContentService
        .createTextOutput(JSON.stringify({
          ok: false,
          message: 'No POST data received'
        }))
        .setMimeType(ContentService.MimeType.JSON);
    }
    
    console.log('📋 Данные:', e.postData.contents);
    
    // Парсим данные
    const params = new URLSearchParams(e.postData.contents);
    const data = {};
    for (const [key, value] of params.entries()) {
      data[key] = value.trim();
    }
    
    console.log('📋 Парсированные данные:', data);
    
    // Простая валидация
    if (!data.name) {
      return ContentService
        .createTextOutput(JSON.stringify({
          ok: false,
          message: 'Name is required'
        }))
        .setMimeType(ContentService.MimeType.JSON);
    }
    
    // Сохраняем в Sheets (если настроено)
    let sheetsResult = { success: false };
    if (CONFIG.SPREADSHEET_ID && CONFIG.SPREADSHEET_ID !== 'YOUR_SPREADSHEET_ID') {
      try {
        sheetsResult = saveToSheets(data);
      } catch (error) {
        console.error('❌ Ошибка Sheets:', error);
      }
    }
    
    // Отправляем в Telegram (если настроено)
    let telegramResult = { success: false };
    if (CONFIG.TELEGRAM_BOT_TOKEN && CONFIG.TELEGRAM_BOT_TOKEN !== 'YOUR_BOT_TOKEN') {
      try {
        telegramResult = sendToTelegram(data);
      } catch (error) {
        console.error('❌ Ошибка Telegram:', error);
      }
    }
    
    return ContentService
      .createTextOutput(JSON.stringify({
        ok: true,
        message: 'Заявка обработана',
        data: {
          sheets_saved: sheetsResult.success,
          telegram_sent: telegramResult.success,
          timestamp: new Date().toISOString()
        }
      }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    console.error('💥 Ошибка обработки POST:', error);
    return ContentService
      .createTextOutput(JSON.stringify({
        ok: false,
        message: 'Ошибка: ' + error.toString()
      }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * Сохранение в Google Sheets
 */
function saveToSheets(data) {
  try {
    const spreadsheet = SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);
    let sheet = spreadsheet.getSheetByName(CONFIG.SHEET_NAME);
    
    if (!sheet) {
      sheet = spreadsheet.insertSheet(CONFIG.SHEET_NAME);
      // Простые заголовки
      sheet.getRange(1, 1, 1, 3).setValues([['Время', 'Имя', 'Email']]);
    }
    
    const now = new Date();
    const formattedTime = Utilities.formatDate(now, 'Europe/Moscow', 'dd.MM.yyyy, HH:mm:ss');
    
    const newRow = sheet.getLastRow() + 1;
    sheet.getRange(newRow, 1, 1, 3).setValues([[
      formattedTime,
      data.name || '',
      data.email || ''
    ]]);
    
    console.log('✅ Данные сохранены в строку:', newRow);
    return { success: true, lead_id: newRow };
    
  } catch (error) {
    console.error('❌ Ошибка сохранения в Sheets:', error);
    return { success: false, error: error.toString() };
  }
}

/**
 * Отправка в Telegram
 */
function sendToTelegram(data) {
  try {
    const message = `🎯 Новая заявка с лендинга\n\n👤 Имя: ${data.name}\n📧 Email: ${data.email || 'Не указан'}\n📱 Телефон: ${data.phone || 'Не указан'}\n⏰ Время: ${new Date().toLocaleString('ru-RU')}`;
    
    const url = `https://api.telegram.org/bot${CONFIG.TELEGRAM_BOT_TOKEN}/sendMessage`;
    const payload = {
      chat_id: CONFIG.MANAGER_CHAT_ID,
      text: message,
      parse_mode: 'Markdown'
    };
    
    const response = UrlFetchApp.fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      payload: JSON.stringify(payload)
    });
    
    const result = JSON.parse(response.getContentText());
    
    if (result.ok) {
      console.log('✅ Telegram уведомление отправлено');
      return { success: true };
    } else {
      console.error('❌ Ошибка Telegram:', result.description);
      return { success: false, error: result.description };
    }
    
  } catch (error) {
    console.error('❌ Ошибка отправки в Telegram:', error);
    return { success: false, error: error.toString() };
  }
}

/**
 * Тестовая функция
 */
function testWebhook() {
  console.log('🧪 Тестирование webhook...');
  
  // Тест GET
  const getResult = doGet({});
  console.log('GET результат:', getResult.getContent());
  
  // Тест POST
  const testData = {
    postData: {
      contents: 'name=Test User&email=test@example.com&phone=+7 999 123 45 67'
    }
  };
  
  const postResult = doPost(testData);
  console.log('POST результат:', postResult.getContent());
  
  return 'Тест завершен';
}
