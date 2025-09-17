#!/usr/bin/env python3
"""
Automated System Test - KingSpeech Landing
Автоматический запуск тестов без интерактивного ввода
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from test_system_comprehensive import ComprehensiveSystemTester

def main():
    """Автоматический запуск тестов"""
    print("🚀 KingSpeech Automated System Test")
    print("Running tests without GAS integration...")
    print()
    
    # Создание тестера без GAS URL
    tester = ComprehensiveSystemTester(gas_url=None)
    
    try:
        # Запуск тестов
        results = tester.run_all_tests()
        
        # Итоговый статус
        success_rate = results['summary']['success_rate']
        print(f"\n📊 Final Success Rate: {success_rate:.1%}")
        
        if success_rate >= 0.8:
            print("🎉 System is ready for production!")
            return 0
        elif success_rate >= 0.6:
            print("⚠️  System needs some improvements before production")
            return 1
        else:
            print("❌ System needs significant improvements")
            return 2
            
    except Exception as e:
        print(f"💥 Test execution failed: {e}")
        return 3

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
