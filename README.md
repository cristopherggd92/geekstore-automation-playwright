# GeekStore Automation Playwright

Proyecto de automatización de pruebas end-to-end para el sitio de demostración
[GeekStore](https://testing.geekqa.net/public_html/public/index.php), desarrollado
con Python, Pytest y Playwright.

## Cobertura actual

La prueba `test_open_browser` valida que Chromium pueda abrir el sitio y que la
URL cargada corresponda a `index.php`.

La suite usa los marcadores `smoke`, `regression` y `e2e`. Actualmente la prueba
de navegación pertenece a los grupos `smoke` y `regression`.

## Estructura

```text
config/            Configuración general y URL base
core/              Administración del navegador
pages/             Page Objects reutilizables
tests/             Casos de prueba Pytest
reports/           Reporte HTML generado al ejecutar las pruebas
```

## Requisitos e instalación

Se requiere Python 3.14 o una versión compatible.

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
```

## Ejecución

Ejecutar todas las pruebas:

```bat
pytest
```

Ejecutar solamente las pruebas de humo:

```bat
pytest -m smoke
```

La configuración actual abre el navegador durante la ejecución (`--headed`).
Para ralentizar las acciones y observar el flujo con mayor claridad:

```bat
pytest -m smoke --slowmo 500
```

Al finalizar se genera el reporte en `reports/report.html`.

## Clonar el repositorio

Para obtener una copia local del proyecto, reemplaza la URL por la del
repositorio remoto:

```bat
git clone <URL_DEL_REPOSITORIO>
cd geekstore-automation-playwright
```
