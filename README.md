# Proyecto QA Automation - Julian Chaves

## Descripcion
Este proyecto automatiza el flujo de compra básico en la pagina SauceDemo para validar la integridad de la plataforma y la practica de QA Automation utilizando python, selenium webdriver y pytest.

## Tecnologias
- Python
- Selenium WebDriver
- Pytest
- Pytest-html
- Git

## Instalacion
1. Clonar el repositorio:
   `git clone https://github.com/Julichavess/pre-entrega-QA-Automation.git`

2. Instalar dependencias:
   `pip install selenium pytest pytest-html webdriver-manager`

## Ejecucion de pruebas
Para correr los tests y generar el reporte:
`pytest test/test_login_01.py test/test_inventory_02.py test/test_cart_03.py -v --html=reports/reporte.html`