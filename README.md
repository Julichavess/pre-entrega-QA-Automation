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
   git clone

2. Instalar dependencias:
   pip install -r requirements.txt
   `pip install selenium pytest pytest-html webdriver-manager`

## Ejecucion de pruebas
Para correr los tests y generar el reporte:
pytest tests/test_login.py tests/test_inventory.py tests/test_cart.py -v
`pytest tests/test_saucedemo.py -v --html=reports/reporte.html`