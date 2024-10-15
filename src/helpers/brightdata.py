from decouple import config
from selenium.webdriver import Remote, ChromeOptions as Options
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection as Connection

AUTH = config("BRIGHTDATA_USERPASS", default=None)

def scrape(url=None):
    if AUTH == 'USER:PASS':
        raise Exception('Provide Scraping Browsers credentials in AUTH ' +
                        'environment variable or update the script.')
    print('Connecting to Browser...')
    server_addr = f'https://{AUTH}@brd.superproxy.io:9515'
    connection = Connection(server_addr, 'goog', 'chrome')
    driver = Remote(connection, options=Options())
    try:
        print(f'Connected! Navigating to {url}...')
        driver.get(url)
        print('Navigated! Waiting captcha to detect and solve...')
        result = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10 * 1000},
        })
        status = result['value']['status']
        print(f'Captcha status: {status}')
        data = driver.page_source
        return data
    finally:
        driver.quit()