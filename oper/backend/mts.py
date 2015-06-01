from bs4 import BeautifulSoup as bs
import os
from urllib import request
from oper.models import TariffMTS
import psycopg2

URL = 'http://www.mts.ua/ua/mobile/tariffs/prosto-super-pervyj'
URL2 = 'http://www.mts.ua/ua/mobile/tariffs/smartfon-3g-pervyj'


def get_url(url):
    html = request.urlopen(url)
    return html.read()


def parse(html):
    parser = bs(html)
    mts_in_network_val = parser.find_all('span', class_='text-size-h4 color-red')
    r = []
    for i in mts_in_network_val:
        r.append(i.text)
    print(r)
    TariffMTS.objects.update_or_create(call_in_minutes=r[0],
                                       call_in_pay=r[1].replace(',', '.'),
                                       mobile_internet_pay=r[2].replace(',', '.'),
                                       sms_mms=r[3].replace(',', '.'),
                                       sms_mms_pay=r[4].replace(',', '.'),
                                       call_out_pay=r[5][:3].replace(',', '.'),
                                       call_rouming_pay=r[6].replace(',', '.'),
                                       )


def parse2(html):
    parser = bs(html)
    mts_in_network_val = parser.find_all('span', class_='text-size-h4 color-red')
    r = []
    for i in mts_in_network_val:
        r.append(i.text)
    TariffMTS.objects.update_or_create(call_in_pay=r[0].replace(',', '.'),
                                       sms_mms_pay=r[3].replace(',', '.'),
                                       call_out_pay=r[2].replace(',', '.'),
                                       call_rouming_pay=r[4].replace(',', '.'),
                                       treeG_pay=r[5],
                                       treeG_scope=r[6],
                                       )
    print(r)


def run():
    parse(get_url(URL))
    parse2(get_url(URL2))