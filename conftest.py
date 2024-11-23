import pytest
from selene import browser


# добавляем фикстуры

@pytest.fixture(params=[(1920, 1080), (1280, 832)])
def browser_desktop_settings(request):
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width

    yield
    print("Закрываем браузер!")


@pytest.fixture(params=[(360, 800), (700, 960)])
def browser_mobile_settings(request):
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width

    yield
    print("Закрываем браузер!")


@pytest.fixture(params=[(1280, 832), (700, 960)])
def browser_config(request):
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width
    browser_type = 'desktop' if int(width) == 1280 else 'mobile'

    yield browser_type
