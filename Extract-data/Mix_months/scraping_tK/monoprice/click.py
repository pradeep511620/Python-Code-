

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from typing import TextIO

browser = webdriver.Chrome(r"/home/tajender/Downloads/chromedriver")
l =[

# 'https://www.monoprice.com/product?p_id=44328',
# 'https://www.monoprice.com/product?p_id=610037',
# 'https://www.monoprice.com/product?p_id=610036',
# 'https://www.monoprice.com/product?p_id=610035',
# 'https://www.monoprice.com/product?p_id=44167',
# 'https://www.monoprice.com/product?p_id=44168',
# 'https://www.monoprice.com/product?p_id=625883',
'https://www.monoprice.com/product?p_id=40515',
# 'https://www.monoprice.com/product?p_id=42652',
# 'https://www.monoprice.com/product?p_id=12962',
# 'https://www.monoprice.com/product?p_id=7013',
# 'https://www.monoprice.com/product?p_id=43332',
# 'https://www.monoprice.com/product?p_id=44329',
# 'https://www.monoprice.com/product?p_id=38626',
# 'https://www.monoprice.com/product?p_id=43326',
# 'https://www.monoprice.com/product?p_id=7556',
# 'https://www.monoprice.com/product?p_id=38643',
# 'https://www.monoprice.com/product?p_id=12735',
# 'https://www.monoprice.com/product?p_id=43374',
# 'https://www.monoprice.com/product?p_id=7649',
# 'https://www.monoprice.com/product?p_id=41034',
# 'https://www.monoprice.com/product?p_id=11339',
# 'https://www.monoprice.com/product?p_id=34663',
# 'https://www.monoprice.com/product?p_id=16052',
# 'https://www.monoprice.com/product?p_id=31019',
# 'https://www.monoprice.com/product?p_id=40645',
# 'https://www.monoprice.com/product?p_id=41485',
# 'https://www.monoprice.com/product?p_id=44492',
# 'https://www.monoprice.com/product?p_id=13676',
# 'https://www.monoprice.com/product?p_id=13674',
# 'https://www.monoprice.com/product?p_id=18617',
# 'https://www.monoprice.com/product?p_id=13071',
# 'https://www.monoprice.com/product?p_id=894',
# 'https://www.monoprice.com/product?p_id=18596',
# 'https://www.monoprice.com/product?p_id=41357',
# 'https://www.monoprice.com/product?p_id=18608',
# 'https://www.monoprice.com/product?p_id=5978',
# 'https://www.monoprice.com/product?p_id=36642',
# 'https://www.monoprice.com/product?p_id=928',
# 'https://www.monoprice.com/product?p_id=940',
# 'https://www.monoprice.com/product?p_id=475',
# 'https://www.monoprice.com/product?p_id=697',
# 'https://www.monoprice.com/product?p_id=39033',
# 'https://www.monoprice.com/product?p_id=6375',
# 'https://www.monoprice.com/product?p_id=13370',
# 'https://www.monoprice.com/product?p_id=21806',
# 'https://www.monoprice.com/product?p_id=2181',
# 'https://www.monoprice.com/product?p_id=3619',
# 'https://www.monoprice.com/product?p_id=42364',
# 'https://www.monoprice.com/product?p_id=15888',
# 'https://www.monoprice.com/product?p_id=6007',
# 'https://www.monoprice.com/product?p_id=13364',
# 'https://www.monoprice.com/product?p_id=39028',
# 'https://www.monoprice.com/product?p_id=559',
# 'https://www.monoprice.com/product?p_id=37918',
# 'https://www.monoprice.com/product?p_id=41230',
# 'https://www.monoprice.com/product?p_id=13368',
# 'https://www.monoprice.com/product?p_id=3572',
# 'https://www.monoprice.com/product?p_id=85',
# 'https://www.monoprice.com/product?p_id=6363',
# 'https://www.monoprice.com/product?p_id=2897',
# 'https://www.monoprice.com/product?p_id=628',
# 'https://www.monoprice.com/product?p_id=623',
# 'https://www.monoprice.com/product?p_id=91',
# 'https://www.monoprice.com/product?p_id=6922',
# 'https://www.monoprice.com/product?p_id=566',
# 'https://www.monoprice.com/product?p_id=320',
# 'https://www.monoprice.com/product?p_id=16183',
# 'https://www.monoprice.com/product?p_id=38604',
# 'https://www.monoprice.com/product?p_id=38579',
# 'https://www.monoprice.com/product?p_id=38583',
# 'https://www.monoprice.com/product?p_id=24440',
# 'https://www.monoprice.com/product?p_id=27934',
# 'https://www.monoprice.com/product?p_id=24284',
# 'https://www.monoprice.com/product?p_id=33457',
# 'https://www.monoprice.com/product?p_id=18789',
# 'https://www.monoprice.com/product?p_id=27402',
# 'https://www.monoprice.com/product?p_id=38606',
# 'https://www.monoprice.com/product?p_id=13752',
# 'https://www.monoprice.com/product?p_id=3896',
# 'https://www.monoprice.com/product?p_id=6149',
# 'https://www.monoprice.com/product?p_id=16377',
# 'https://www.monoprice.com/product?p_id=13749',
# 'https://www.monoprice.com/product?p_id=8490',
# 'https://www.monoprice.com/product?p_id=30715',
# 'https://www.monoprice.com/product?p_id=38601',
# 'https://www.monoprice.com/product?p_id=38596',
# 'https://www.monoprice.com/product?p_id=7531',
# 'https://www.monoprice.com/product?p_id=13746',
# 'https://www.monoprice.com/product?p_id=33463',
# 'https://www.monoprice.com/product?p_id=40075',
# 'https://www.monoprice.com/product?p_id=40087',
# 'https://www.monoprice.com/product?p_id=40099',
# 'https://www.monoprice.com/product?p_id=41091',
# 'https://www.monoprice.com/product?p_id=41096',
# 'https://www.monoprice.com/product?p_id=40065',
# 'https://www.monoprice.com/product?p_id=40095',
# 'https://www.monoprice.com/product?p_id=35048',
# 'https://www.monoprice.com/product?p_id=24199',
# 'https://www.monoprice.com/product?p_id=7691',
# 'https://www.monoprice.com/product?p_id=7687',
# 'https://www.monoprice.com/product?p_id=24208',
# 'https://www.monoprice.com/product?p_id=35116',
# 'https://www.monoprice.com/product?p_id=40084',
# 'https://www.monoprice.com/product?p_id=44320',
# 'https://www.monoprice.com/product?p_id=40093',
# 'https://www.monoprice.com/product?p_id=41081',
# 'https://www.monoprice.com/product?p_id=7692',
# 'https://www.monoprice.com/product?p_id=35065',
# 'https://www.monoprice.com/product?p_id=27314',
# 'https://www.monoprice.com/product?p_id=2683',
# 'https://www.monoprice.com/product?p_id=18534',
# 'https://www.monoprice.com/product?p_id=2743',
# 'https://www.monoprice.com/product?p_id=33465',
# 'https://www.monoprice.com/product?p_id=10147',
# 'https://www.monoprice.com/product?p_id=11936',
# 'https://www.monoprice.com/product?p_id=1419',
# 'https://www.monoprice.com/product?p_id=38082',
# 'https://www.monoprice.com/product?p_id=38075',
# 'https://www.monoprice.com/product?p_id=42155',
# 'https://www.monoprice.com/product?p_id=42153',
# 'https://www.monoprice.com/product?p_id=42163',
# 'https://www.monoprice.com/product?p_id=42157',
# 'https://www.monoprice.com/product?p_id=42161',
# 'https://www.monoprice.com/product?p_id=42159',
# 'https://www.monoprice.com/product?p_id=18632',
# 'https://www.monoprice.com/product?p_id=18629',
# 'https://www.monoprice.com/product?p_id=648',
# 'https://www.monoprice.com/product?p_id=38076',
# 'https://www.monoprice.com/product?p_id=21680',
# 'https://www.monoprice.com/product?p_id=2764',
# 'https://www.monoprice.com/product?p_id=4754',
# 'https://www.monoprice.com/product?p_id=601415',
# 'https://www.monoprice.com/product?p_id=4793',
# 'https://www.monoprice.com/product?p_id=33837',
# 'https://www.monoprice.com/product?p_id=18673',
# 'https://www.monoprice.com/product?p_id=14558',
# 'https://www.monoprice.com/product?p_id=35796',
# 'https://www.monoprice.com/product?p_id=4768',
# 'https://www.monoprice.com/product?p_id=601492',
# 'https://www.monoprice.com/product?p_id=4761',
# 'https://www.monoprice.com/product?p_id=4777',
# 'https://www.monoprice.com/product?p_id=18821',
# 'https://www.monoprice.com/product?p_id=601296',
# 'https://www.monoprice.com/product?p_id=9441',
# 'https://www.monoprice.com/product?p_id=8533',
# 'https://www.monoprice.com/product?p_id=601606',
# 'https://www.monoprice.com/product?p_id=9448',
# 'https://www.monoprice.com/product?p_id=8766',
# 'https://www.monoprice.com/product?p_id=5496',
# 'https://www.monoprice.com/product?p_id=35315',
# 'https://www.monoprice.com/product?p_id=8761',
# 'https://www.monoprice.com/product?p_id=601550',
# 'https://www.monoprice.com/product?p_id=14568',
# 'https://www.monoprice.com/product?p_id=601051',
# 'https://www.monoprice.com/product?p_id=4784',
# 'https://www.monoprice.com/product?p_id=601045',
# 'https://www.monoprice.com/product?p_id=18814',
# 'https://www.monoprice.com/product?p_id=41698',
# 'https://www.monoprice.com/product?p_id=41704',
# 'https://www.monoprice.com/product?p_id=6394',
# 'https://www.monoprice.com/product?p_id=41708',
# 'https://www.monoprice.com/product?p_id=6395',
# 'https://www.monoprice.com/product?p_id=39431',
# 'https://www.monoprice.com/product?p_id=38354',
# 'https://www.monoprice.com/product?p_id=31220',
# 'https://www.monoprice.com/product?p_id=38274',
# 'https://www.monoprice.com/product?p_id=43108',
# 'https://www.monoprice.com/product?p_id=92',
# 'https://www.monoprice.com/product?p_id=1587',
# 'https://www.monoprice.com/product?p_id=93',
# 'https://www.monoprice.com/product?p_id=442',
# 'https://www.monoprice.com/product?p_id=448',
# 'https://www.monoprice.com/product?p_id=1596',
# 'https://www.monoprice.com/product?p_id=12790',
# 'https://www.monoprice.com/product?p_id=38296',
# 'https://www.monoprice.com/product?p_id=12786',
# 'https://www.monoprice.com/product?p_id=12802',
# 'https://www.monoprice.com/product?p_id=21670',
# 'https://www.monoprice.com/product?p_id=24260',
# 'https://www.monoprice.com/product?p_id=38294',
# 'https://www.monoprice.com/product?p_id=38178',
# 'https://www.monoprice.com/product?p_id=9437',
# 'https://www.monoprice.com/product?p_id=9436',
# 'https://www.monoprice.com/product?p_id=8243',
# 'https://www.monoprice.com/product?p_id=8246',
# 'https://www.monoprice.com/product?p_id=21912',
# 'https://www.monoprice.com/product?p_id=2944',
# 'https://www.monoprice.com/product?p_id=38174',
# 'https://www.monoprice.com/product?p_id=38170',
# 'https://www.monoprice.com/product?p_id=6542',
# 'https://www.monoprice.com/product?p_id=5860',
# 'https://www.monoprice.com/product?p_id=42649',
# 'https://www.monoprice.com/product?p_id=21848',
# 'https://www.monoprice.com/product?p_id=5384',
# 'https://www.monoprice.com/product?p_id=5376',
# 'https://www.monoprice.com/product?p_id=7248',
# 'https://www.monoprice.com/product?p_id=27556',
# 'https://www.monoprice.com/product?p_id=310',
# 'https://www.monoprice.com/product?p_id=15664',
# 'https://www.monoprice.com/product?p_id=10046',
# 'https://www.monoprice.com/product?p_id=1039',
# 'https://www.monoprice.com/product?p_id=6727',
# 'https://www.monoprice.com/product?p_id=6725',
# 'https://www.monoprice.com/product?p_id=6731',
# 'https://www.monoprice.com/product?p_id=34518',
# 'https://www.monoprice.com/product?p_id=34515',
# 'https://www.monoprice.com/product?p_id=34511',
# 'https://www.monoprice.com/product?p_id=34485',
# 'https://www.monoprice.com/product?p_id=34491',
# 'https://www.monoprice.com/product?p_id=34488',
# 'https://www.monoprice.com/product?p_id=34482',
# 'https://www.monoprice.com/product?p_id=7089',
# 'https://www.monoprice.com/product?p_id=7266',
# 'https://www.monoprice.com/product?p_id=39758',
# 'https://www.monoprice.com/product?p_id=39754',
# 'https://www.monoprice.com/product?p_id=8627',
# 'https://www.monoprice.com/product?p_id=8626',
# 'https://www.monoprice.com/product?p_id=7308',
# 'https://www.monoprice.com/product?p_id=7261',
# 'https://www.monoprice.com/product?p_id=42826',
# 'https://www.monoprice.com/product?p_id=18514',
# 'https://www.monoprice.com/product?p_id=24794',
# 'https://www.monoprice.com/product?p_id=39168',
# 'https://www.monoprice.com/product?p_id=24433',
# 'https://www.monoprice.com/product?p_id=13682',
# 'https://www.monoprice.com/product?p_id=34199',
# 'https://www.monoprice.com/product?p_id=6816',
# 'https://www.monoprice.com/product?p_id=24761',
# 'https://www.monoprice.com/product?p_id=13614',
# 'https://www.monoprice.com/product?p_id=33393',
# 'https://www.monoprice.com/product?p_id=15698',
# 'https://www.monoprice.com/product?p_id=24434',
# 'https://www.monoprice.com/product?p_id=13683',
# 'https://www.monoprice.com/product?p_id=11942',
# 'https://www.monoprice.com/product?p_id=34198',
# 'https://www.monoprice.com/product?p_id=12235',
# 'https://www.monoprice.com/product?p_id=24463',
# 'https://www.monoprice.com/product?p_id=30456',
# 'https://www.monoprice.com/product?p_id=14886',
# 'https://www.monoprice.com/product?p_id=27853',
# 'https://www.monoprice.com/product?p_id=12182',
# 'https://www.monoprice.com/product?p_id=8097',
# 'https://www.monoprice.com/product?p_id=12987',
# 'https://www.monoprice.com/product?p_id=15526',
# 'https://www.monoprice.com/product?p_id=16358',
# 'https://www.monoprice.com/product?p_id=29407',
# 'https://www.monoprice.com/product?p_id=15525',
# 'https://www.monoprice.com/product?p_id=3021',
# 'https://www.monoprice.com/product?p_id=3012',
# 'https://www.monoprice.com/product?p_id=27836',
# 'https://www.monoprice.com/product?p_id=15722',
# 'https://www.monoprice.com/product?p_id=31292',
# 'https://www.monoprice.com/product?p_id=34827',
# 'https://www.monoprice.com/product?p_id=42763',
# 'https://www.monoprice.com/product?p_id=36277',
# 'https://www.monoprice.com/product?p_id=33048',
# 'https://www.monoprice.com/product?p_id=42267',
# 'https://www.monoprice.com/product?p_id=39765',
# 'https://www.monoprice.com/product?p_id=38610',
# 'https://www.monoprice.com/product?p_id=610292',
# 'https://www.monoprice.com/product?p_id=610040',
# 'https://www.monoprice.com/product?p_id=610017',
# 'https://www.monoprice.com/product?p_id=610192',
# 'https://www.monoprice.com/product?p_id=610263',
# 'https://www.monoprice.com/product?p_id=610503',
# 'https://www.monoprice.com/product?p_id=610712',
# 'https://www.monoprice.com/product?p_id=610164',
# 'https://www.monoprice.com/product?p_id=610887',
# 'https://www.monoprice.com/product?p_id=610370',
# 'https://www.monoprice.com/product?p_id=610885',
# 'https://www.monoprice.com/product?p_id=612751',
# 'https://www.monoprice.com/product?p_id=40394',
# 'https://www.monoprice.com/product?p_id=15638',
# 'https://www.monoprice.com/product?p_id=31235',
# 'https://www.monoprice.com/product?p_id=15640',
# 'https://www.monoprice.com/product?p_id=43353',
# 'https://www.monoprice.com/product?p_id=42014',
# 'https://www.monoprice.com/product?p_id=42018',
# 'https://www.monoprice.com/product?p_id=42027',
# 'https://www.monoprice.com/product?p_id=42757',
# 'https://www.monoprice.com/product?p_id=42755',
# 'https://www.monoprice.com/product?p_id=21594',
# 'https://www.monoprice.com/product?p_id=35380',
# 'https://www.monoprice.com/product?p_id=41033',
# 'https://www.monoprice.com/product?p_id=18592',
# 'https://www.monoprice.com/product?p_id=41694',
# 'https://www.monoprice.com/product?p_id=43103',
# 'https://www.monoprice.com/product?p_id=6390',
# 'https://www.monoprice.com/product?p_id=6397',
# 'https://www.monoprice.com/product?p_id=41703',
# 'https://www.monoprice.com/product?p_id=41697',
# 'https://www.monoprice.com/product?p_id=43106',
# 'https://www.monoprice.com/product?p_id=39752',
# 'https://www.monoprice.com/product?p_id=7262',
# 'https://www.monoprice.com/product?p_id=7688',
# 'https://www.monoprice.com/product?p_id=43328',
# 'https://www.monoprice.com/product?p_id=43327',
# 'https://www.monoprice.com/product?p_id=43329',
# 'https://www.monoprice.com/product?p_id=29406',
# 'https://www.monoprice.com/product?p_id=42754',
# 'https://www.monoprice.com/product?p_id=40517',
# 'https://www.monoprice.com/product?p_id=12994',
# 'https://www.monoprice.com/product?p_id=34549',
# 'https://www.monoprice.com/product?p_id=41038',
# 'https://www.monoprice.com/product?p_id=610261',
# 'https://www.monoprice.com/product?p_id=16080',
# 'https://www.monoprice.com/product?p_id=8095',
# 'https://www.monoprice.com/product?p_id=31263',
# 'https://www.monoprice.com/product?p_id=31264',
# 'https://www.monoprice.com/product?p_id=39169',
# 'https://www.monoprice.com/product?p_id=39170',
# 'https://www.monoprice.com/product?p_id=7643',
# 'https://www.monoprice.com/product?p_id=38609',
# 'https://www.monoprice.com/product?p_id=16379',
# 'https://www.monoprice.com/product?p_id=42015',
# 'https://www.monoprice.com/product?p_id=625903',
# 'https://www.monoprice.com/product?p_id=610502',
# 'https://www.monoprice.com/product?p_id=36300',
# 'https://www.monoprice.com/product?p_id=36288',
# 'https://www.monoprice.com/product?p_id=36286',
# 'https://www.monoprice.com/product?p_id=36278',
# 'https://www.monoprice.com/product?p_id=36283',
# 'https://www.monoprice.com/product?p_id=36287',
# 'https://www.monoprice.com/product?p_id=42266',
# 'https://www.monoprice.com/product?p_id=33049',
# 'https://www.monoprice.com/product?p_id=12280',
# 'https://www.monoprice.com/product?p_id=41484',
# 'https://www.monoprice.com/product?p_id=601630',
# 'https://www.monoprice.com/product?p_id=8770',
# 'https://www.monoprice.com/product?p_id=24287',
# 'https://www.monoprice.com/product?p_id=24288',
# 'https://www.monoprice.com/product?p_id=37921',
# 'https://www.monoprice.com/product?p_id=38614',
# 'https://www.monoprice.com/product?p_id=24444',
# 'https://www.monoprice.com/product?p_id=18675',
# 'https://www.monoprice.com/product?p_id=1044',
# 'https://www.monoprice.com/product?p_id=42764',
# 'https://www.monoprice.com/product?p_id=610500',
# 'https://www.monoprice.com/product?p_id=610886',
# 'https://www.monoprice.com/product?p_id=43354',
# 'https://www.monoprice.com/product?p_id=42707',
# 'https://www.monoprice.com/product?p_id=42865',
# 'https://www.monoprice.com/product?p_id=41040',
# 'https://www.monoprice.com/product?p_id=3339',
# 'https://www.monoprice.com/product?p_id=6372',
# 'https://www.monoprice.com/product?p_id=42651',
# 'https://www.monoprice.com/product?p_id=21847',
# 'https://www.monoprice.com/product?p_id=30455',

]

for url in l:
    browser.get(url)
    l = browser.find_element(By.CLASS_NAME, 'prod-breadcrumb')
    v=l.get_attribute("innerHTML")

    print(v)

    # first_click = browser.find_elements(By.XPATH,'//*[@id="addCart"]/div[2]/div[1]/form[1]/div/span')
    # # second_click = browser.find_elements(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[2]/div/span')
    # # third_click = browser.find_elements(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[3]/div/span')
    # # import pdb;
    # #
    # # pdb.set_trace()
    # r = []
    # s3 = []
    # first_loop = (len(first_click) + 1)
    # # second_loop = (len(second_click) + 1)
    # # third_loop = (len(third_click) + 1)
    # # try:
    # # if len(click_count) == 1:
    # #     save_details: TextIO = open("1.txt", "a+", encoding="utf-8")
    # #     save_details.write(
    # #         "\n" + "'" + i + "'" + "\t" + "1")
    # #     print("End")
    # #     save_details.close()
    # for entry1 in range(1, first_loop):
    #     first_click = browser.find_element(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[1]/div/span['+str(entry1)+']').click()
    #     time.sleep(4)
    #     try:
    #         c=browser.find_element(By.XPATH,'//*[@id="ltkpopup-close-button"]').click()
    #
    #     except:
    #         pass
    #     # print(data)
    #     data = browser.page_source
    #     soup = BeautifulSoup(data, 'html.parser')
    #     l = soup.find('div', class_='prod-breadcrumb').find_all('a')
    #     Breadcrumb = []
    #     for i in l:
    #         Breadcrumb.append(i.text)
    #     print(Breadcrumb)
    #
    #     title = soup.find('div', class_='product-name').text
    #     print(title)
    #
    #     item_no = soup.find('div', class_='product-code').text
    #     print(item_no)
    #
    #     UPC = soup.find('div', class_='product-barcode').text
    #     print(UPC)
    #     price = soup.find('span', class_='sale-price').text.strip()
    #     print(price)
    #     images = soup.find('div', class_='lightbox-gallerylist').find_all('a')
    #     im = []
    #     for ie in images:
    #         im.append(ie.get('href'))
    #     print(im)
    #     value = soup.find('span', class_="mp-prod-attrform-label")
    #     c = value.text.split('\n')
    #     print(c[1], c[2])
    #
    #     save_details: TextIO = open("monopriceclick.txt", "a+", encoding="utf-8")
    #     save_details.write(
    #         "\n" + url + "\t" + item_no + "\t" + UPC + "\t" + '->'.join(Breadcrumb) + "\t" + ".".join(im) + "\t" + price + "\t"+c[1].replace(':','')+"\t"+c[2])
    #     save_details.close()
    #     print("End")
    #     print("***********************************************************************************")





