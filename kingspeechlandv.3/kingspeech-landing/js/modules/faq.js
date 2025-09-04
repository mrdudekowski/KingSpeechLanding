/**
 * FAQ Module - Управление FAQ секцией
 * Автоматическое закрывание при открытии другого вопроса
 */

export class FAQManager {
  constructor() {
    this.faqElements = document.querySelectorAll('.faq');
    this.init();
  }

  init() {
    if (this.faqElements.length === 0) {
      console.log('❓ FAQ Manager: No FAQ elements found');
      return;
    }

    this.faqElements.forEach((faq, index) => {
      const answer = faq.querySelector('.faq__answer');
      if (answer) {
        // Сохраняем оригинальную высоту контента
        this.setupFAQAnimation(faq, answer, index);
      }

      // Слушаем событие toggle на details элементе
      faq.addEventListener('toggle', (e) => {
        if (faq.open) {
          // Если FAQ открывается, закрываем все другие
          this.closeOtherFAQs(faq);
        }
      });
    });

    // Обработчик изменения размера окна
    window.addEventListener('resize', () => {
      this.updateFAQHeights();
    });
  }

  setupFAQAnimation(faq, answer, index) {
    // Временно открываем FAQ для измерения высоты
    const wasOpen = faq.open;
    faq.open = true;
    
    // Получаем реальную высоту контента
    const contentHeight = answer.scrollHeight;
    
    // Добавляем запас для мобильных устройств
    const isMobile = window.innerWidth <= 768;
    const adjustedHeight = isMobile ? contentHeight + 20 : contentHeight;
    
    // Возвращаем исходное состояние
    faq.open = wasOpen;
    
    // Устанавливаем CSS переменную с реальной высотой
    answer.style.setProperty('--content-height', `${adjustedHeight}px`);
    
  }

  closeOtherFAQs(openFAQ) {
    // Закрываем все другие FAQ
    this.faqElements.forEach(faq => {
      if (faq !== openFAQ && faq.open) {
        faq.open = false;
      }
    });
  }

  updateFAQHeights() {
    // Пересчитываем высоты при изменении размера окна
    this.faqElements.forEach((faq, index) => {
      const answer = faq.querySelector('.faq__answer');
      if (answer) {
        this.setupFAQAnimation(faq, answer, index);
      }
    });
  }
}

// Автоинициализация при загрузке DOM
document.addEventListener('DOMContentLoaded', () => {
  new FAQManager();
});
