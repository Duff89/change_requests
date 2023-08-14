import time

from selenium.webdriver.chrome.options import Options
from seleniumwire import undetected_chromedriver as uc


def interceptor(request):
    if request.url == 'https://www.sberbank.ru/proxy/services/rates/public/actual?regionId=038&rateType=ERNP-2&isoCodes[]=EUR&isoCodes[]=USD':
        print("Change")
        request.create_response(
            status_code=200,
            headers={'Contect-Type': 'application/javascript;charset=UTF-8'},
            body='{"EUR":'
                 '{"startDateTime":1692021791000,"lotSize":1.00,"rateList":[{"rangeAmountBottom":0.00,"rangeAmountUpper":9999999999.99,"rateSell":33.70,"rateBuy":31.10}]},'
                 '"USD":{"startDateTime":1692021791000,"lotSize":1.00,"rateList":[{"rangeAmountBottom":0.00,"rangeAmountUpper":9999999999.99,"rateSell":26.90,"rateBuy":25.90,"symbolBuy":"UP"}]}}'
        )


options = Options()
options.add_argument('--ignore-certificate-errors')
driver = uc.Chrome(version_main=108, options=options)
driver.request_interceptor = interceptor
driver.get("https://www.sberbank.ru/ru/person")
time.sleep(500)
