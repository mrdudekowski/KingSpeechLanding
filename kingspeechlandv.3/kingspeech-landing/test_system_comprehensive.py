#!/usr/bin/env python3
"""
Comprehensive System Test - KingSpeech Landing
Тестирование всех компонентов системы согласно лучшим практикам LandingMemoryBank
"""

import requests
import json
import time
import os
import sys
from urllib.parse import urlencode
from datetime import datetime
import subprocess

class ComprehensiveSystemTester:
    def __init__(self, gas_url=None):
        self.gas_url = gas_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'KingSpeech-SystemTester/2.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        })
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'tests': {},
            'summary': {}
        }
    
    def run_all_tests(self):
        """Запуск всех тестов системы"""
        print("🚀 KingSpeech Comprehensive System Test")
        print("=" * 60)
        
        # 1. CSS Linting тесты
        print("\n📋 1. CSS Linting Tests")
        self.test_css_linting()
        
        # 2. JavaScript тесты
        print("\n⚡ 2. JavaScript Module Tests")
        self.test_javascript_modules()
        
        # 3. Form Manager тесты
        print("\n📝 3. Form Manager Tests")
        self.test_form_manager()
        
        # 4. GAS Integration тесты
        if self.gas_url:
            print("\n🔗 4. GAS Integration Tests")
            self.test_gas_integration()
        else:
            print("\n⚠️  4. GAS Integration Tests - SKIPPED (no URL provided)")
            self.results['tests']['gas_integration'] = {'status': 'skipped', 'reason': 'No GAS URL provided'}
        
        # 5. Performance тесты
        print("\n⚡ 5. Performance Tests")
        self.test_performance()
        
        # 6. Security тесты
        print("\n🔒 6. Security Tests")
        self.test_security()
        
        # 7. Accessibility тесты
        print("\n♿ 7. Accessibility Tests")
        self.test_accessibility()
        
        # Генерация отчета
        self.generate_report()
        
        return self.results
    
    def test_css_linting(self):
        """Тестирование CSS Linting системы"""
        print("   🔍 Testing CSS Linting...")
        
        try:
            # Проверяем наличие package.json
            if not os.path.exists('package.json'):
                self.results['tests']['css_linting'] = {
                    'status': 'failed',
                    'error': 'package.json not found'
                }
                print("   ❌ package.json not found")
                return
            
            # Запускаем CSS аудит
            result = subprocess.run(['npm', 'run', 'css:audit'], 
                                  capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                self.results['tests']['css_linting'] = {
                    'status': 'passed',
                    'output': result.stdout
                }
                print("   ✅ CSS Linting passed")
            else:
                self.results['tests']['css_linting'] = {
                    'status': 'failed',
                    'error': result.stderr,
                    'output': result.stdout
                }
                print("   ❌ CSS Linting failed")
                print(f"   Error: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            self.results['tests']['css_linting'] = {
                'status': 'failed',
                'error': 'Timeout - CSS audit took too long'
            }
            print("   ❌ CSS Linting timeout")
        except Exception as e:
            self.results['tests']['css_linting'] = {
                'status': 'failed',
                'error': str(e)
            }
            print(f"   ❌ CSS Linting error: {e}")
    
    def test_javascript_modules(self):
        """Тестирование JavaScript модулей"""
        print("   🔍 Testing JavaScript modules...")
        
        modules = [
            'js/modules/forms.js',
            'js/modules/gas-integration.js',
            'js/modules/navigation.js',
            'js/modules/carousel.js',
            'js/modules/animations.js'
        ]
        
        module_results = {}
        
        for module in modules:
            if os.path.exists(module):
                # Проверяем синтаксис
                try:
                    with open(module, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Простая проверка синтаксиса
                    if 'class ' in content and 'export' in content:
                        module_results[module] = {'status': 'passed', 'syntax': 'valid'}
                    else:
                        module_results[module] = {'status': 'warning', 'syntax': 'unusual'}
                except Exception as e:
                    module_results[module] = {'status': 'failed', 'error': str(e)}
            else:
                module_results[module] = {'status': 'missing'}
        
        self.results['tests']['javascript_modules'] = module_results
        
        # Подсчет результатов
        passed = sum(1 for r in module_results.values() if r.get('status') == 'passed')
        total = len(module_results)
        
        print(f"   📊 JavaScript modules: {passed}/{total} passed")
        
        for module, result in module_results.items():
            status_icon = "✅" if result.get('status') == 'passed' else "❌"
            print(f"   {status_icon} {module}: {result.get('status', 'unknown')}")
    
    def test_form_manager(self):
        """Тестирование Form Manager"""
        print("   🔍 Testing Form Manager...")
        
        # Проверяем наличие форм в HTML
        try:
            with open('index.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Ищем формы
            forms_found = html_content.count('<form')
            required_fields = html_content.count('required')
            data_attributes = html_content.count('data-form')
            
            form_manager_result = {
                'forms_found': forms_found,
                'required_fields': required_fields,
                'data_attributes': data_attributes,
                'has_validation': 'FormManager' in html_content or 'forms.js' in html_content
            }
            
            if forms_found > 0 and required_fields > 0:
                form_manager_result['status'] = 'passed'
                print("   ✅ Form Manager configuration looks good")
            else:
                form_manager_result['status'] = 'warning'
                print("   ⚠️  Form Manager configuration incomplete")
            
            self.results['tests']['form_manager'] = form_manager_result
            
        except Exception as e:
            self.results['tests']['form_manager'] = {
                'status': 'failed',
                'error': str(e)
            }
            print(f"   ❌ Form Manager test failed: {e}")
    
    def test_gas_integration(self):
        """Тестирование GAS Integration"""
        print("   🔍 Testing GAS Integration...")
        
        # Health check
        health_ok = self.test_gas_health()
        
        if not health_ok:
            self.results['tests']['gas_integration'] = {
                'status': 'failed',
                'error': 'GAS webhook not accessible'
            }
            return
        
        # Тест отправки заявки
        lead_test = self.test_lead_submission()
        
        # Тест валидации
        validation_test = self.test_validation()
        
        # Тест производительности
        performance_test = self.test_gas_performance()
        
        self.results['tests']['gas_integration'] = {
            'status': 'passed' if all([health_ok, lead_test, validation_test]) else 'failed',
            'health_check': health_ok,
            'lead_submission': lead_test,
            'validation': validation_test,
            'performance': performance_test
        }
    
    def test_gas_health(self):
        """Тест доступности GAS webhook"""
        try:
            response = self.session.get(self.gas_url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                print("   ✅ GAS webhook is healthy")
                return data.get('ok', False)
            else:
                print(f"   ❌ GAS webhook returned {response.status_code}")
                return False
        except Exception as e:
            print(f"   ❌ GAS health check failed: {e}")
            return False
    
    def test_lead_submission(self):
        """Тест отправки заявки"""
        test_data = {
            'name': 'Махно Чикибомбони',
            'email': 'godzillaonotole@gmail.com',
            'phone': '+7 (902) 556-81-19',
            'messenger': 'Telegram',
            'goal': 'Изучение английского языка',
            'website': ''  # Honeypot
        }
        
        try:
            response = self.session.post(self.gas_url, data=test_data, timeout=15)
            if response.status_code == 200:
                data = response.json()
                if data.get('ok'):
                    print("   ✅ Lead submission successful")
                    return True
                else:
                    print(f"   ❌ Lead submission failed: {data.get('message')}")
                    return False
            else:
                print(f"   ❌ Lead submission HTTP error: {response.status_code}")
                return False
        except Exception as e:
            print(f"   ❌ Lead submission error: {e}")
            return False
    
    def test_validation(self):
        """Тест валидации"""
        # Тест 1: Отсутствует имя
        invalid_data = {
            'email': 'test@example.com',
            'phone': '+7 (999) 123-45-67',
            'website': ''
        }
        
        try:
            response = self.session.post(self.gas_url, data=invalid_data, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if not data.get('ok'):
                    print("   ✅ Validation working - rejected invalid data")
                    return True
                else:
                    print("   ❌ Validation not working - accepted invalid data")
                    return False
            else:
                print("   ❌ Validation test HTTP error")
                return False
        except Exception as e:
            print(f"   ❌ Validation test error: {e}")
            return False
    
    def test_gas_performance(self):
        """Тест производительности GAS"""
        test_data = {
            'name': 'Performance Test',
            'email': 'perf@example.com',
            'phone': '+7 (999) 123-45-67',
            'website': ''
        }
        
        times = []
        successes = 0
        
        for i in range(3):  # 3 запроса для теста
            start_time = time.time()
            try:
                response = self.session.post(self.gas_url, data=test_data, timeout=10)
                end_time = time.time()
                
                request_time = end_time - start_time
                times.append(request_time)
                
                if response.status_code == 200:
                    data = response.json()
                    if data.get('ok'):
                        successes += 1
                
            except Exception as e:
                end_time = time.time()
                times.append(end_time - start_time)
        
        if times:
            avg_time = sum(times) / len(times)
            max_time = max(times)
            
            print(f"   📊 Performance: avg {avg_time:.2f}s, max {max_time:.2f}s")
            print(f"   📊 Success rate: {successes}/3")
            
            return {
                'avg_time': avg_time,
                'max_time': max_time,
                'success_rate': successes / 3,
                'acceptable': avg_time < 3.0 and successes >= 2
            }
        
        return {'acceptable': False}
    
    def test_performance(self):
        """Тестирование производительности"""
        print("   🔍 Testing performance...")
        
        # Проверяем размер файлов
        css_files = []
        js_files = []
        
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.css'):
                    css_files.append(os.path.join(root, file))
                elif file.endswith('.js'):
                    js_files.append(os.path.join(root, file))
        
        total_css_size = sum(os.path.getsize(f) for f in css_files if os.path.exists(f))
        total_js_size = sum(os.path.getsize(f) for f in js_files if os.path.exists(f))
        
        performance_result = {
            'css_files': len(css_files),
            'js_files': len(js_files),
            'total_css_size_kb': round(total_css_size / 1024, 2),
            'total_js_size_kb': round(total_js_size / 1024, 2),
            'css_acceptable': total_css_size < 200 * 1024,  # < 200KB
            'js_acceptable': total_js_size < 100 * 1024    # < 100KB
        }
        
        print(f"   📊 CSS: {performance_result['total_css_size_kb']}KB ({len(css_files)} files)")
        print(f"   📊 JS: {performance_result['total_js_size_kb']}KB ({len(js_files)} files)")
        
        if performance_result['css_acceptable'] and performance_result['js_acceptable']:
            print("   ✅ Performance acceptable")
        else:
            print("   ⚠️  Performance needs optimization")
        
        self.results['tests']['performance'] = performance_result
    
    def test_security(self):
        """Тестирование безопасности"""
        print("   🔍 Testing security...")
        
        security_checks = {
            'honeypot_present': False,
            'validation_present': False,
            'https_required': False,
            'cors_configured': False
        }
        
        # Проверяем HTML на наличие honeypot
        try:
            with open('index.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            if 'website' in html_content and 'hidden' in html_content.lower():
                security_checks['honeypot_present'] = True
            
            if 'required' in html_content and 'validation' in html_content.lower():
                security_checks['validation_present'] = True
                
        except Exception as e:
            print(f"   ⚠️  Security check error: {e}")
        
        # Проверяем GAS скрипт на CORS
        try:
            with open('gas-webhook-enhanced.gs', 'r', encoding='utf-8') as f:
                gas_content = f.read()
            
            if 'Access-Control-Allow-Origin' in gas_content:
                security_checks['cors_configured'] = True
                
        except Exception as e:
            print(f"   ⚠️  GAS security check error: {e}")
        
        security_score = sum(security_checks.values()) / len(security_checks)
        
        print(f"   📊 Security score: {security_score:.1%}")
        for check, status in security_checks.items():
            icon = "✅" if status else "❌"
            print(f"   {icon} {check}: {status}")
        
        self.results['tests']['security'] = {
            **security_checks,
            'score': security_score,
            'acceptable': security_score >= 0.75
        }
    
    def test_accessibility(self):
        """Тестирование доступности"""
        print("   🔍 Testing accessibility...")
        
        accessibility_checks = {
            'alt_texts': 0,
            'aria_labels': 0,
            'form_labels': 0,
            'heading_structure': False,
            'focus_management': False
        }
        
        try:
            with open('index.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Подсчитываем alt тексты
            accessibility_checks['alt_texts'] = html_content.count('alt=')
            
            # Подсчитываем aria-labels
            accessibility_checks['aria_labels'] = html_content.count('aria-label')
            
            # Подсчитываем labels для форм
            accessibility_checks['form_labels'] = html_content.count('<label')
            
            # Проверяем структуру заголовков
            if '<h1>' in html_content and '<h2>' in html_content:
                accessibility_checks['heading_structure'] = True
            
            # Проверяем focus management в JS
            if 'focus' in html_content.lower() or 'tabindex' in html_content:
                accessibility_checks['focus_management'] = True
                
        except Exception as e:
            print(f"   ⚠️  Accessibility check error: {e}")
        
        accessibility_score = sum([
            accessibility_checks['alt_texts'] > 0,
            accessibility_checks['aria_labels'] > 0,
            accessibility_checks['form_labels'] > 0,
            accessibility_checks['heading_structure'],
            accessibility_checks['focus_management']
        ]) / 5
        
        print(f"   📊 Accessibility score: {accessibility_score:.1%}")
        print(f"   📊 Alt texts: {accessibility_checks['alt_texts']}")
        print(f"   📊 Aria labels: {accessibility_checks['aria_labels']}")
        print(f"   📊 Form labels: {accessibility_checks['form_labels']}")
        
        self.results['tests']['accessibility'] = {
            **accessibility_checks,
            'score': accessibility_score,
            'acceptable': accessibility_score >= 0.6
        }
    
    def generate_report(self):
        """Генерация итогового отчета"""
        print("\n" + "=" * 60)
        print("📊 COMPREHENSIVE TEST REPORT")
        print("=" * 60)
        
        # Подсчет результатов
        total_tests = len(self.results['tests'])
        passed_tests = sum(1 for test in self.results['tests'].values() 
                          if test.get('status') == 'passed')
        failed_tests = sum(1 for test in self.results['tests'].values() 
                          if test.get('status') == 'failed')
        skipped_tests = sum(1 for test in self.results['tests'].values() 
                           if test.get('status') == 'skipped')
        
        self.results['summary'] = {
            'total_tests': total_tests,
            'passed_tests': passed_tests,
            'failed_tests': failed_tests,
            'skipped_tests': skipped_tests,
            'success_rate': passed_tests / total_tests if total_tests > 0 else 0
        }
        
        print(f"📈 Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"⏭️  Skipped: {skipped_tests}")
        print(f"📊 Success Rate: {self.results['summary']['success_rate']:.1%}")
        
        # Детальные результаты
        print("\n📋 Detailed Results:")
        for test_name, result in self.results['tests'].items():
            status = result.get('status', 'unknown')
            icon = "✅" if status == 'passed' else "❌" if status == 'failed' else "⏭️"
            print(f"   {icon} {test_name}: {status}")
        
        # Рекомендации
        print("\n💡 Recommendations:")
        if failed_tests > 0:
            print("   • Fix failed tests before deployment")
        if self.results['summary']['success_rate'] < 0.8:
            print("   • Overall system needs improvement")
        if 'gas_integration' in self.results['tests'] and self.results['tests']['gas_integration'].get('status') == 'skipped':
            print("   • Configure GAS integration for complete testing")
        
        # Сохранение отчета
        report_file = f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 Detailed report saved to: {report_file}")

def main():
    """Главная функция"""
    print("🚀 KingSpeech Comprehensive System Test")
    print("Testing all components according to LandingMemoryBank best practices")
    print()
    
    # Запрос GAS URL (опционально)
    gas_url = input("Enter GAS webhook URL (or press Enter to skip GAS tests): ").strip()
    if not gas_url:
        gas_url = None
        print("⚠️  GAS tests will be skipped")
    
    print()
    
    # Создание тестера
    tester = ComprehensiveSystemTester(gas_url)
    
    try:
        # Запуск тестов
        results = tester.run_all_tests()
        
        # Итоговый статус
        success_rate = results['summary']['success_rate']
        if success_rate >= 0.8:
            print("\n🎉 System is ready for production!")
        elif success_rate >= 0.6:
            print("\n⚠️  System needs some improvements before production")
        else:
            print("\n❌ System needs significant improvements")
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Testing interrupted by user")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")

if __name__ == "__main__":
    main()
