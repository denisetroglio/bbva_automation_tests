import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    # Capturar siempre en la fase 'call', tanto tests pasados como fallidos
    if report.when == "call":
        driver = item.funcargs.get("driver", None)

        if driver:
            try:
                screenshot = driver.get_screenshot_as_base64()
                pytest_html = item.config.pluginmanager.getplugin("html")

                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(screenshot, mime_type="image/png"))
                report.extra = extra

                print(f">>> Captura añadida para test: {item.name} (estado: {report.outcome})")
            except Exception as e:
                print(f">>> ERROR al capturar screenshot para {item.name}: {e}")
