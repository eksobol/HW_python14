from selene import browser, be


def test_desktop_browser(browser_desktop_settings):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).click()
    browser.element('#password').should(be.visible)


def test_mobile_browser(browser_mobile_settings):
    browser.open('https://github.com/mobile')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('.js-continue-button').should(be.visible)
