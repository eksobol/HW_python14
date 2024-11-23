import pytest

from selene import browser, be, have


# тест с десктопной версией

@pytest.mark.parametrize("browser_desktop_settings", [(1920, 1080)], indirect=True)
def test_desktop_browser(browser_desktop_settings):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()
    browser.element('#password').should(be.visible)


# тест с мобильной версией

@pytest.mark.parametrize('browser_mobile_settings', [(360, 800)], indirect=True)
def test_mobile_browser(browser_mobile_settings):
    browser.open('https://github.com/mobile')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('.js-continue-button').should(be.visible)


# простой skip

@pytest.mark.skip()
@pytest.mark.skip(reason="Этот тест еще не закончен")
@pytest.mark.parametrize("browser_desktop_settings", [(1280, 832)])
def test_desktop_browser_v2(browser_desktop_settings):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()
    browser.element('#password').should(be.visible)


# тесты skip if
def test_sign_in_github_desktop_skip(browser_config):
    if browser_config == 'desktop':
        pytest.skip('Настройка для десктопной версии')
    browser.open('https://github.com/mobile')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('.js-continue-button').should(be.visible)


def test_sign_in_github_mobile_skip(browser_config):
    if browser_config == 'mobile':
        pytest.skip('Настройка для мобильной версии')
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()
