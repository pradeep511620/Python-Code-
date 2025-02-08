import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from typing import TextIO
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = False
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
browser = webdriver.Chrome(r"/home/tajender/Downloads/chromedriver",options=opts)
l =[

# 'https://www.southwire.com//wire-cable/armored-power-cable/2-c-3-c-or-4-c-cu-600v-xlpe-xhhw-2-aluminum-interlocked-armor-pvc-control-cable-with-ground/p/55541399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/2-c-3-c-or-4-c-cu-600v-xlpe-xhhw-2-aluminum-interlocked-armor-pvc-control-cable-with-ground/p/57842699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/2-c-3-c-or-4-c-cu-600v-xlpe-xhhw-2-aluminum-interlocked-armor-pvc-control-cable-with-ground/p/55514999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/2-c-3-c-or-4-c-cu-600v-xlpe-xhhw-2-aluminum-interlocked-armor-pvc-control-cable-with-ground/p/57350299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/2-c-3-c-or-4-c-cu-600v-xlpe-xhhw-2-aluminum-interlocked-armor-pvc-control-cable-with-ground/p/56845799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/2-c-3-c-or-4-c-cu-600v-xlpe-xhhw-2-aluminum-interlocked-armor-pvc-control-cable-with-ground/p/56845899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/2-c-3-c-or-4-c-cu-600v-xlpe-xhhw-2-aluminum-interlocked-armor-pvc-control-cable-with-ground/p/57350099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67865499',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67865199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67481699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67864799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67991699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67991999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67856199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67479999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67480299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67480699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67480999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-600-or-1000-volt-cu-fr-xlpe-xhhw-2-cpe-jacket-power-cable-halo-flex-type-tc-er-hl/p/67481399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-15kv-220-nlepr-133-aia-pvc-mv-105/p/57768899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-15kv-220-nlepr-133-aia-pvc-mv-105/p/59778199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-15kv-220-nlepr-133-aia-pvc-mv-105/p/57773899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-15kv-220-nlepr-133-aia-pvc-mv-105/p/59756199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-15kv-220-nlepr-133-aia-pvc-mv-105/p/57768799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-15kv-220-nlepr-133-aia-pvc-mv-105-50-ground-silicone-free/p/57598899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-35kv-420-nlepr-133-armor-x-pvc-mv-105/p/59115399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-5kv-115-nlepr-133-aia-pvc-mv-105/p/59778099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-600v-or-1000-v-xlpe-xhhw-2-pvc-power-cable-with-ground-silicone-free-/p/67735399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-50-ground-silicone-free/p/64933299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-50-ground-silicone-free/p/64665899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-al-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-at-50-silicone-free/p/57622099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-175-nlepr-100-aia-pvc-mv-105/p/55692899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-cpe-mv-105/p/64944399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-cpe-mv-105/p/64690799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-lszh-mv-105/p/58567799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-lszh-mv-105/p/58567599',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-lszh-mv-105/p/58567699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-pvc-mv-105/p/55167199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-pvc-mv-105/p/55695199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-pvc-mv-105/p/95788699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-pvc-mv-105/p/55164899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-pvc-mv-105/p/56080199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-pvc-mv-105/p/55161499',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-pvc-mv-105/p/55697799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-pvc-mv-105-50-ground-silicone-free/p/67941999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-pvc-mv-105-50-ground-silicone-free/p/57871299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-aia-pvc-mv-105-50-ground-silicone-free/p/60521299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-armor-x-pvc-mv-105/p/89066399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-armor-x-pvc-mv-105/p/89066499',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-armor-x-pvc-mv-105/p/89066599',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-armor-x-pvc-mv-105/p/89066699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-armor-x-pvc-mv-105/p/89066799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-armor-x-pvc-mv-105/p/89066899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-armor-x-pvc-mv-105/p/89066999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-armor-x-pvc-mv-105/p/55043999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-gsia-pvc-mv-105/p/61010599',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-gsia-pvc-mv-105/p/58197299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-gsia-pvc-mv-105/p/44727699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-gsia-pvc-mv-105/p/61103899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-15kv-220-nlepr-133-gsia-pvc-mv-105/p/40916999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-2-4kv-90-epr-armor-x-pvc-mv-105-vfd-type-mc-hl/p/89061599',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-2-4kv-90-epr-armor-x-pvc-mv-105-vfd-type-mc-hl/p/89061699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-2-4kv-90-epr-armor-x-pvc-mv-105-vfd-type-mc-hl/p/89061799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-2-4kv-90-epr-armor-x-pvc-mv-105-vfd-type-mc-hl/p/89061999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-2-4kv-90-epr-armor-x-pvc-mv-105-vfd-type-mc-hl/p/89062099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-2-4kv-90-epr-armor-x-pvc-mv-105-vfd-type-mc-hl/p/89062199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-2-4kv-90-epr-armor-x-pvc-mv-105-vfd-type-mc-hl/p/89062299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-cpe-mv-105/p/67757799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-lszh-mv-105/p/58324699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-lszh-mv-105/p/57665199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-lszh-mv-105/p/56493699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-lszh-mv-105/p/56493599',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-lszh-mv-105/p/56493499',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-pvc-mv-105/p/55660599',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-pvc-mv-105/p/55661399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-pvc-mv-105/p/55662199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-pvc-mv-105/p/55663999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-pvc-mv-105/p/55664799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-pvc-mv-105/p/55665499',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-pvc-mv-105/p/55666299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-pvc-mv-105/p/55667099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-pvc-mv-105/p/55668899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-aia-pvc-mv-105/p/55669699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-armor-x-mc-hl-pvc-mv-105-vfd/p/89063699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-armor-x-mc-hl-pvc-mv-105-vfd/p/89063899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-armor-x-mc-hl-pvc-mv-105-vfd/p/89063999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-armor-x-mc-hl-pvc-mv-105-vfd/p/89064099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-armor-x-mc-hl-pvc-mv-105-vfd/p/89064199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-armor-x-mc-hl-pvc-mv-105-vfd/p/89064299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-armor-x-mc-hl-pvc-mv-105-vfd/p/89064399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-armor-x-mc-hl-pvc-mv-105-vfd/p/89064499',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-gsia-pvc-mv-105/p/55960199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-5kv-115-nlepr-133-gsia-pvc-mv-105/p/95828099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-at-50-silicone-free-/p/57688899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-at-50-silicone-free-/p/55259899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/60693999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/60694799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/60695499',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/56046699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/56047499',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/56048299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/89033999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/38367999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/60137799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/38364699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/38061899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/89039199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free-/p/89040599',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/55059399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/89051399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/89051499',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/89051599',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/89051699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/89051799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/89051899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/89051999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/89052099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/89052199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/89052299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground-vfd/p/89052399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-or-4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-cable-with-three-grounds-vfd-cable/p/55058699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-or-4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-cable-with-three-grounds-vfd-cable/p/55058799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-or-4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-cable-with-three-grounds-vfd-cable/p/55058899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-or-4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-cable-with-three-grounds-vfd-cable/p/55058999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-or-4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-cable-with-three-grounds-vfd-cable/p/55059199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/3-c-or-4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-cable-with-three-grounds-vfd-cable/p/55059299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-al-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-50-ground-silicone-free/p/64465699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-al-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-50-ground-silicone-free/p/64465299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-al-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-50-ground-silicone-free/p/58765899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-50-ground-silicone-free/p/55145299',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-50-ground-silicone-free/p/95237499',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free/p/57446099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free/p/89022999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free/p/60541099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-aia-pvc-power-cable-with-ground-silicone-free/p/56340799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground/p/89052799',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground/p/89052899',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground/p/89052999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground/p/89053099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground/p/89053199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground/p/89053399',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground/p/89053599',
# 'https://www.southwire.com//wire-cable/armored-power-cable/4-c-cu-600v-xlpe-xhhw-2-armor-x-pvc-power-cable-with-ground/p/89053699',
# 'https://www.southwire.com//wire-cable/armored-power-cable/600v-cu-pvc-pairs-armor-x-pvc-spos-instrumentation/p/89055999',
# 'https://www.southwire.com//wire-cable/armored-power-cable/600v-cu-pvc-pairs-armor-x-pvc-spos-instrumentation/p/89056099',
# 'https://www.southwire.com//wire-cable/armored-power-cable/600v-cu-pvc-pairs-armor-x-pvc-spos-instrumentation/p/89056199',
# 'https://www.southwire.com//wire-cable/armored-power-cable/600v-cu-pvc-triads-armor-x-pvc-stos-instrumentation/p/89056799',
# # 'https://www.southwire.com//wire-cable/armored-power-cable/cu-600v-xlpe-xhhw-2-armor-x-pvc-control-cable-with-ground/p/55060799',
# # 'https://www.southwire.com//wire-cable/armored-power-cable/cu-600v-xlpe-xhhw-2-armor-x-pvc-control-cable-with-ground/p/55061199',
# # 'https://www.southwire.com//wire-cable/armored-power-cable/cu-600v-xlpe-xhhw-2-armor-x-pvc-control-cable-with-ground/p/55061399',
# # 'https://www.southwire.com//wire-cable/armored-power-cable/hvteck-al-3-c-175nlepr-ts-pvc-aia-pvc-15kv-100-csa/p/57814999',
# # 'https://www.southwire.com//wire-cable/building-wire/simpull-barrel-cable-drum/p/58120301',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/28827421',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63946801',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/55053901',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/55048201',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/28828201',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63947601',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/55054201',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/55048401',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/28829001',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63948401',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/55583201',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/28893601',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63949201',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/28894401',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63950001',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63968201',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63970801',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-pcs-duo-cable/p/67807101',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-pcs-duo-cable/p/67962801',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-pcs-duo-cable/p/67962901',
# # 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-pcs-duo-cable/p/67963001',
# # 'https://www.southwire.com//wire-cable/building-wire/copper-uf-b/p/13054201',
# # 'https://www.southwire.com//wire-cable/building-wire/copper-uf-b/p/13057501',
# # 'https://www.southwire.com//wire-cable/building-wire/copper-uf-b/p/13049201',
# # 'https://www.southwire.com//wire-cable/building-wire/copper-uf-b/p/13058301',
# # 'https://www.southwire.com//wire-cable/building-wire/copper-uf-b/p/13050001',
# # 'https://www.southwire.com//wire-cable/building-wire/copper-uf-b/p/13059101',
# # 'https://www.southwire.com//wire-cable/building-wire/copper-uf-b/p/20858701',
# # 'https://www.southwire.com//wire-cable/building-wire/copper-uf-b/p/14783501',
# # 'https://www.southwire.com//wire-cable/building-wire/copper-uf-b/p/21469201',
# # 'https://www.southwire.com//wire-cable/building-wire/copper-uf-b/p/14782701',
# # 'https://www.southwire.com//wire-cable/flexible-cord/300v-american-mustang-sjoow-cord-with-yellow-jacket-105-c/p/59834001',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-plus-sjeoow-cord-with-yellow-jacket-105-c/p/65419403',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-plus-sjeoow-cord-with-yellow-jacket-105-c/p/65424402',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-plus-sjeoow-cord-with-yellow-jacket-105-c/p/65428501',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-plus-sjeoow-cord-with-yellow-jacket-105-c/p/65431901',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-sjeoow-cord-with-black-jacket-105-c/p/55044501',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-sjeoow-cord-with-black-jacket-105-c/p/55040301',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-sjeoow-cord-with-black-jacket-105-c/p/55043503',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-sjeoow-cord-with-black-jacket-105-c/p/55043301',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-sjeoow-cord-with-black-jacket-105-c/p/55062702',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-sjeoow-cord-with-black-jacket-105-c/p/55039601',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-sjeoow-cord-with-black-jacket-105-c/p/55076701',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-sjeoow-cord-with-black-jacket-105-c/p/55044801',
# 'https://www.southwire.com//wire-cable/flexible-cord/300v-seoprene-sjeoow-cord-with-black-jacket-105-c/p/55062801',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-american-mustang-soow-cord-with-yellow-jacket-105-c/p/57021401',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-american-mustang-soow-cord-with-yellow-jacket-105-c/p/63073001',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-american-mustang-soow-cord-with-yellow-jacket-105-c/p/63072701',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-american-mustang-soow-cord-with-yellow-jacket-105-c/p/59833401',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-american-mustang-soow-cord-with-yellow-jacket-105-c/p/63072101',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-american-mustang-soow-cord-with-yellow-jacket-105-c/p/59698101',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-american-mustang-soow-cord-with-yellow-jacket-105-c/p/59532701',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-american-mustang-soow-cord-with-yellow-jacket-105-c/p/63072201',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-american-mustang-soow-cord-with-yellow-jacket-105-c/p/63072401',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-american-mustang-soow-cord-with-yellow-jacket-105-c/p/63072501',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-control-with-black-jacket-90-c/p/55823602',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-control-with-black-jacket-90-c/p/55823702',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-control-with-black-jacket-90-c/p/55823301',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-control-with-black-jacket-90-c/p/55814601',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-control-with-black-jacket-90-c/p/56997905',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-control-with-black-jacket-90-c/p/56998001',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/55810002',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/55809902',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/55810202',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/55809402',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/55809502',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/55810401',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/55809702',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/55809602',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/55810301',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/56003902',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/63072601',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/59696101',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/56004102',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/56004202',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/56206802',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/56092599',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/56206702',
# # 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-cord-with-black-jacket-90-c/p/56092899',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/56997299',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/55808802',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/55809302',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/55810502',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/56997303',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/55809202',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/55809102',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/55816101',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/55813799',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/55809002',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/56997502',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/55813602',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/55808999',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-royal-soow-power-cord-non-ul-csa-with-black-jacket-90-c/p/56997601',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-plus-seoow-cord-with-yellow-jacket-105-c/p/59833501',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-plus-seoow-cord-with-yellow-jacket-105-c/p/65570402',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-plus-seoow-cord-with-yellow-jacket-105-c/p/59833601',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-plus-seoow-cord-with-yellow-jacket-105-c/p/65572001',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-plus-seoow-cord-with-yellow-jacket-105-c/p/65573801',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-plus-seoow-cord-with-yellow-jacket-105-c/p/65576101',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-plus-seoow-cord-with-yellow-jacket-105-c/p/65578701',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-plus-seoow-cord-with-yellow-jacket-105-c/p/65579501',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-plus-seoow-power-cord-non-ul-csa-with-yellow-jacket-105-c/p/65582901',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-plus-seoow-power-cord-non-ul-csa-with-yellow-jacket-105-c/p/65585201',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/59875801',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/59872802',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/59872901',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/55046402',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/56279102',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/59537501',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/58988801',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/55039801',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/59873901',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/59874001',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/59874101',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/55039501',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-control-with-black-jacket-105-c/p/59874501',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-with-black-jacket-105-c/p/56964501',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-with-black-jacket-105-c/p/55039510',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-with-black-jacket-105-c/p/55039701',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-cord-with-black-jacket-105-c/p/55039301',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-non-ul-csa-with-black-jacket-105-c/p/55045001',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-non-ul-csa-with-black-jacket-105-c/p/55114001',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-non-ul-csa-with-black-jacket-105-c/p/55040501',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-non-ul-csa-with-black-jacket-105-c/p/59833001',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-non-ul-csa-with-black-jacket-105-c/p/59833101',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-non-ul-csa-with-black-jacket-105-c/p/55040401',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-non-ul-csa-with-black-jacket-105-c/p/59833301',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-non-ul-csa-with-black-jacket-105-c/p/55047301',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-with-black-jacket-105-c/p/59832701',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-with-black-jacket-105-c/p/59832801',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-with-black-jacket-105-c/p/58693901',
# 'https://www.southwire.com//wire-cable/flexible-cord/600v-seoprene-seoow-power-cord-with-black-jacket-105-c/p/59832901',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/28827421',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63946801',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/55053901',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/55048201',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/28828201',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63947601',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/55054201',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/55048401',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/28829001',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63948401',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/55583201',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/28893601',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63949201',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/28894401',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63950001',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63968201',
# 'https://www.southwire.com//wire-cable/building-wire/romex-brand-simpull-type-nm-b-cable/p/63970801',
# 'https://www.southwire.com//wire-cable/industrial-flexible/3-c-cu-2000v-epdm-cpe-type-g-gc-industrial-grade-cable-90-c/p/55816507',
# 'https://www.southwire.com//wire-cable/industrial-flexible/3-c-cu-2000v-epdm-cpe-type-g-gc-industrial-grade-cable-90-c/p/55816707',
# 'https://www.southwire.com//wire-cable/industrial-flexible/4-c-cu-2000v-epdm-cpe-type-w-industrial-grade-cable-90-c/p/55815201',
# 'https://www.southwire.com//wire-cable/industrial-flexible/4-c-cu-2000v-epdm-cpe-type-w-industrial-grade-cable-90-c/p/55815499',
# 'https://www.southwire.com//wire-cable/leadwire/brake-cable/p/FBK0661800',
# 'https://www.southwire.com//wire-cable/leadwire/brake-cable/p/FBK1200800',
# 'https://www.southwire.com//wire-cable/leadwire/brake-cable/p/55833225',
# 'https://www.southwire.com//wire-cable/leadwire/brake-cable/p/55804208',
# 'https://www.southwire.com//wire-cable/leadwire/brake-cable/p/55833001',
# 'https://www.southwire.com//wire-cable/leadwire/brake-cable/p/FBK0562400',
# 'https://www.southwire.com//wire-cable/leadwire/brake-cable/p/56036001',
# 'https://www.southwire.com//wire-cable/leadwire/brake-cable/p/56452702',
# 'https://www.southwire.com//wire-cable/leadwire/brake-cable/p/56655901',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/fire-alarm-fplp/p/G40005-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/fire-alarm-fplp/p/G40505-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/fire-alarm-fplp/p/G50013-12A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/fire-alarm-fplp/p/G50054-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/fire-alarm-fplp/p/G60004-12A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/fire-alarm-fplr/p/F40015-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/fire-alarm-fplr/p/F40003-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/fire-alarm-fplr/p/F60112-1C',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/circuit-defender-2-hour-rated/p/SC4001-2Q',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/circuit-defender-2-hour-rated/p/SC5001-2Q',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/circuit-defender-2-hour-rated/p/SC6001-2Q',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/access-control-cable/p/H91601-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-shielded/p/P20032-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-shielded/p/P20270-11A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-shielded/p/P20019-16A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-shielded/p/P30017-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-shielded/p/P40133-19B',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-shielded/p/P40032-12B',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-shielded/p/P40073-14A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-shielded/p/P40040-12A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-shielded/p/P50001-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-unshielded/p/P20031-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-unshielded/p/P20035-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-unshielded/p/P40020-10B',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-unshielded/p/P40031-14B',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-unshielded/p/P40065-14A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-unshielded/p/P40168-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-unshielded/p/P50032-14A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-unshielded/p/P50012-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-unshielded/p/P50059-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-plenum-unshielded/p/P60035-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-riser-shielded/p/R20007-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-riser-shielded/p/R20016-1B',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-riser-shielded/p/R20030-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-riser-shielded/p/R40013-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-riser-shielded/p/R40003-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-riser-shielded/p/R40005-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-riser-shielded/p/R40611-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-riser-shielded/p/R60052-15A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-riser-shielded/p/R60209-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/multi-conductor-security-riser-unshielded/p/R50003-19A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/low-voltage-dimming-or-luminaire-cable/p/P51641-1B',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/instrumentation-and-building-management-control-cable/p/M10003-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/instrumentation-and-building-management-control-cable/p/R21342-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/instrumentation-and-building-management-control-cable/p/L40008-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/instrumentation-and-building-management-control-cable/p/L40009-1A',
# 'https://www.southwire.com//wire-cable/low-voltage-cable/instrumentation-and-building-management-control-cable/p/R50325-1A',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/1-c-cu-15kv-220-nlepr-133-cpe-mv-105-silicone-free/p/64690499',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/1-c-cu-35kv-345-nlepr-100-simpull-pvc-mv-105/p/59936499',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/1-c-cu-5kv-115-nlepr-133-lszh-mv-105/p/57467599',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-al-15kv-220-nlepr-133-pvc-mv-105/p/59930599',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-al-5kv-115-nlepr-133-pvc-mv-105/p/59906599',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-al-5kv-115-nlepr-133-pvc-mv-105/p/59907099',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-al-5kv-115-nlepr-133-pvc-mv-105/p/58187601',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-al-5kv-115-nlepr-133-pvc-mv-105/p/58093299',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-175-nlepr-100-cpe-mv-105/p/64937399',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-175-nlepr-100-cpe-mv-105/p/64937199',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-175-nlepr-100-cpe-mv-105/p/67943999',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-cpe-mv-105/p/58404199',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-cpe-mv-105/p/58404299',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-cpe-mv-105/p/56025199',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-cpe-mv-105/p/56378599',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-cpe-mv-105/p/56123299',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-cpe-mv-105-silicone-free/p/55825499',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-pvc-mv-105-silicone-free/p/95649099',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-pvc-mv-105-silicone-free/p/95830699',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-pvc-mv-105-silicone-free/p/95628499',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-pvc-mv-105-silicone-free/p/55828899',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-pvc-mv-105-silicone-free/p/95832299',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-15kv-220-nlepr-133-pvc-mv-105-silicone-free/p/95833077',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-25kv-320-nlepr-133-pvc-mv-105/p/64737999',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-25kv-320-nlepr-133-pvc-mv-105/p/67930599',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-35kv-420-nlepr-133-pvc-mv-105/p/57833799',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-35kv-420-nlepr-133-pvc-mv-105/p/59785399',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-cpe-mv-105/p/55234599',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-cpe-mv-105/p/55184899',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-cpe-mv-105/p/56103899',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-cpe-mv-105/p/56045099',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-cpe-mv-105/p/56123099',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-pvc-mv-105/p/64338099',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-pvc-mv-105/p/95630099',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-pvc-mv-105/p/95837199',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-pvc-mv-105/p/55817199',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-pvc-mv-105/p/95745677',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-pvc-mv-105/p/95838699',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-pvc-mv-105/p/95517977',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-pvc-mv-105/p/95839777',
# 'https://www.southwire.com//wire-cable/medium-voltage-power-cable/3-c-cu-5kv-115-nlepr-133-pvc-mv-105/p/55749699',
# 'https://www.southwire.com//wire-cable/medium-voltage-primary-underground-distribution/35kv-aluminum-xlp-mv-lldpe-jacket/p/61463301',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/55017701',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/55018001',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/58909002',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/55079601',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/55091401',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/55017211',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/58626402',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/56332402',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/58640702',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/55116701',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/55112101',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/55127801',
# 'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/58771401',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/55135602',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/59011502',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/58466102',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc/p/59301201',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-pvc-jacketed/p/56428902',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-pvc-jacketed/p/55337902',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-pvc-jacketed/p/55256499',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-pvc-jacketed/p/58797501',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-pvc-jacketed/p/55280802',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-pvc-jacketed/p/55295402',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-pvc-jacketed/p/67941402',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/55527201',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/55527301',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/55527401',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/55510301',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/55510401',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/55510501',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/56719302',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/55527501',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/55527701',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/55527801',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/56719702',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/56720002',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/59666402',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/56703002',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/59798902',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/59799102',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-type-mc-all-purpose/p/56703701',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/56038901',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/56039201',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/55527901',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/55528001',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/55528101',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/56083401',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/56639502',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/55528201',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/55528301',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/55528501',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/56271602',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/56722802',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/58720502',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/64451502',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/58626502',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/58394702',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/67810199',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/59668502',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/59668702',
'https://www.southwire.com//wire-cable/metal-clad-cable/hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/58403102',
'https://www.southwire.com//wire-cable/metal-clad-cable/pvc-jacketed-hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/58495001',
'https://www.southwire.com//wire-cable/metal-clad-cable/pvc-jacketed-hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/59911101',
'https://www.southwire.com//wire-cable/metal-clad-cable/pvc-jacketed-hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/64464501',
'https://www.southwire.com//wire-cable/metal-clad-cable/pvc-jacketed-hcf-mcap-type-mc-all-purpose-hospital-care-facility/p/59799902',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/67434902',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/55279502',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/55499001',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/67431302',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/55299601',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/59267802',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/55485203',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/67765599',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/64748802',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/67915801',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/59353501',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/64704602',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/59273603',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-neutral-per-phase/p/67736402',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-isolated-ground/p/55110401',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-isolated-ground/p/56241902',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-isolated-ground/p/58769701',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-isolated-ground/p/55129802',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-isolated-ground/p/55130202',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-isolated-ground/p/69601301',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-isolated-ground/p/55518402',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-isolated-ground/p/55518903',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-isolated-ground/p/56114789',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-isolated-ground/p/55999889',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-isolated-ground/p/56788589',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/55132202',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/55132401',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/55135403',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/58085001',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/67937002',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/56382202',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/55133602',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/58640203',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/56669801',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/64052302',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/58584801',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/55298602',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/67916101',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/67825402',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/57352801',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/57353002',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/58364202',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/64059802',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-multi-circuit/p/67786699',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-oversized-neutral/p/55065502',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-oversized-neutral/p/55065402',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-oversized-neutral/p/56576002',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-oversized-neutral/p/55133002',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-oversized-neutral/p/55520902',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-oversized-neutral/p/55363301',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-oversized-neutral/p/69100602',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-oversized-neutral/p/55298502',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-oversized-neutral/p/55298302',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-oversized-neutral/p/56871402',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-blue-armor/p/55276401',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-blue-armor/p/55276801',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-blue-armor/p/55276501',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-blue-armor/p/55277001',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-blue-armor/p/55277101',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-blue-armor/p/55276201',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-mc-blue-armor/p/55298801',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/61029301',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/61029401',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/61029601',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/55327001',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/55327601',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/61029701',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/61029801',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/61029901',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/61030001',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/89060702',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/89060802',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/89069002',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/89069102',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/89069202',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/89069301',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/89069501',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/89069601',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/55327502',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/55327899',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/89069801',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-type-ac/p/89069903',
'https://www.southwire.com//wire-cable/metal-clad-cable/mc-pcs-duo-power-control-signal-cable/p/67482702',
'https://www.southwire.com//wire-cable/metal-clad-cable/mc-pcs-duo-pvc-jacketed-power-control-signal-cable/p/59618502',
'https://www.southwire.com//wire-cable/metal-clad-cable/mc-pcs-duo-pvc-jacketed-power-control-signal-cable/p/59618701',
'https://www.southwire.com//wire-cable/metal-clad-cable/mc-pcs-duo-pvc-jacketed-power-control-signal-cable/p/67755702',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-pcs-duo-power-control-signal-cable-type-mc-all-purpose/p/64405102',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-pcs-duo-power-control-signal-cable-type-mc-all-purpose/p/64873801',
'https://www.southwire.com//wire-cable/metal-clad-cable/mcap-pcs-duo-power-control-signal-cable-type-mc-all-purpose/p/67796102',
'https://www.southwire.com//wire-cable/metal-clad-cable/mc-pcs-hcf-duo-power-control-signal-cable-for-healthcare-facilities/p/67433202',
'https://www.southwire.com//wire-cable/metal-clad-cable/mc-pcs-hcf-duo-power-control-signal-cable-for-healthcare-facilities/p/59127901',
'https://www.southwire.com//wire-cable/metal-clad-cable/mc-pcs-hcf-duo-power-control-signal-cable-for-healthcare-facilities/p/59225101',
'https://www.southwire.com//wire-cable/metal-clad-cable/mc-pcs-hcf-duo-power-control-signal-cable-for-healthcare-facilities/p/67775402',
'https://www.southwire.com//wire-cable/metal-clad-cable/mc-pcs-hcf-duo-power-control-signal-cable-for-healthcare-facilities/p/59225501',
'https://www.southwire.com//wire-cable/metal-clad-cable/mc-pcs-hcf-duo-power-control-signal-cable-for-healthcare-facilities/p/67776102',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/55454902',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/67774703',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/55468702',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/55312402',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/55455102',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/55468902',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/55312802',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/55453702',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/55453902',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/55496903',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/56168402',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/55454002',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/58339703',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/59089702',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/64733502',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/59802802',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/59956103',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/55316103',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/59913002',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/58516703',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/67936001',
'https://www.southwire.com//wire-cable/metal-clad-cable/red-alert-type-mc-fplp-fire-alarm-and-control/p/67791502',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55171501',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55172801',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55171601',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55172901',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55173401',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55777903',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55988902',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55171701',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55173001',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55173501',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55731202',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc/p/55778103',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc-blue-armor/p/64395001',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc-blue-armor/p/57109701',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc-blue-armor/p/57111101',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc-blue-armor/p/57114801',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc-blue-armor/p/57115001',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc-blue-armor/p/57115501',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-mc-blue-armor/p/57116001',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/64707899',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/55429399',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/58206899',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/56265699',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/56246999',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/64683599',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/55428801',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/55981399',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/58574799',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/56103299',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/55398999',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/55255299',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/67733899',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/58648399',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/56158799',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/58185299',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/56554599',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/59937999',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/55514699',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/55383999',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/56010799',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/57994999',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/56137589',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/56420299',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/67739199',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/58368499',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/57923299',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/56767199',
'https://www.southwire.com//wire-cable/metal-clad-cable/armorlite-feeder-metal-clad-cable-with-copper-thhn-conductors/p/58580399',
'https://www.southwire.com//wire-cable/metal-clad-cable/pvc-jacketed-alumaflex-riser-mc-feeder-with-aluminum-thhn-conductors/p/59808099',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58232501',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58232601',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58232901',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58426601',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58233101',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58233401',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58426202',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58426902',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58764601',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58764801',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58575602',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58575102',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58575302',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-hcf-mcap-type-mc-all-purpose-health-care-facility/p/58923101',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-ac/p/55278301',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-ac/p/55274901',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-ac/p/55275701',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-ac/p/55336703',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-ac/p/55275902',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-ac/p/59060003',
'https://www.southwire.com//wire-cable/metal-clad-cable/duraclad-type-ac/p/55279302',
'https://www.southwire.com//wire-cable/mining-cable/cu-600v-remote-power-drill-cord-cable-90-c/p/57141599',
'https://www.southwire.com//wire-cable/mining-cable/cu-600v-remote-power-drill-cord-cable-90-c/p/57140299',
'https://www.southwire.com//wire-cable/mining-cable/cu-600v-remote-power-drill-cord-cable-90-c/p/57173199',
'https://www.southwire.com//wire-cable/mining-cable/cu-600v-remote-power-drill-cord-cable-90-c/p/57171099',
'https://www.southwire.com//wire-cable/mining-cable/cu-600v-remote-power-drill-cord-cable-90-c/p/58392099',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/67562099',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/58372789',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/58222289',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/58212389',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/59655099',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/58212499',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/57853799',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/56321199',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/57853699',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/67349799',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/58212789',
'https://www.southwire.com//wire-cable/power-control/multiconductor-600v-2000v/p/58001399',
'https://www.southwire.com//wire-cable/power-control/single-conductor-2000v/p/58358699',
'https://www.southwire.com//wire-cable/power-control/single-conductor-2000v/p/59754099',
'https://www.southwire.com//wire-cable/power-control/single-conductor-600v-2000v/p/59317399',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/40856701',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44339001',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/55769489',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44340801',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/55343801',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44341601',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/59198699',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44342401',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/59198889',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44343289',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44344001',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/55456889',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44345701',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/55672089',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44346589',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/60202989',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44347301',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44474589',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44348189',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/59199989',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44350789',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/59200199',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/44352389',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/55251389',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/60477789',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/60481989',
'https://www.southwire.com//wire-cable/power-control/unshielded-multiconductor-600v-2000v/p/60209489',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-control-cable/p/60666801',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-control-cable/p/60429001',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-control-cable/p/61836001',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-control-cable/p/61994501',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-control-cable/p/61949801',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-shielded-control-cable/p/60368901',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-shielded-control-cable/p/60369102',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-shielded-control-cable/p/60369201',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-shielded-control-cable/p/61930701',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-shielded-control-cable/p/62294602',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-shielded-control-cable/p/61843501',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-shielded-control-cable/p/66221601',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-tp-shielded-control-cable/p/60370703',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-ts-control-cable/p/62593401',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-ts-control-cable/p/62583801',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-ts-control-cable/p/62583301',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-ts-control-cable/p/62582801',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-ts-control-cable/p/62582401',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-ts-control-cable/p/60751301',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-ts-control-cable/p/62219501',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-cpe-ts-control-cable/p/60751201',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-lszh-tp-control-cable/p/66099101',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-lszh-tp-control-cable/p/62415201',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-lszh-tp-control-cable/p/66098801',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-lszh-tp-shielded-control-cable/p/62555401',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-lszh-tp-shielded-control-cable/p/66250601',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-lszh-tp-shielded-control-cable/p/62556101',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-lszh-tp-shielded-control-cable/p/66250401',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-lszh-tp-shielded-control-cable/p/62555901',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-control-cable/p/61879101',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-control-cable/p/62409701',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-control-cable/p/61948801',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-control-cable/p/60761301',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-control-cable/p/61908601',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-control-cable/p/61888801',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-control-cable/p/61909001',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-control-cable/p/61908901',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-control-cable/p/61952401',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/61880825',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/61880925',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/66258001',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/61881325',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/61881425',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/60675801',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/60410701',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/60409101',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/61954701',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/61893301',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/62330501',
'https://www.southwire.com//wire-cable/substation/cu-frxlpe-pvc-shielded-control-cable/p/60668901',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-control-cable/p/62064601',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-control-cable/p/60677601',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-control-cable/p/61685601',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-control-cable/p/61917302',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-control-cable/p/60689601',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-control-cable/p/61793208',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-control-cable/p/61911701',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-control-cable/p/61917901',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-shielded-control-cable/p/60676801',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-shielded-control-cable/p/61916202',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-shielded-control-cable/p/61698401',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-shielded-control-cable/p/60676901',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-shielded-control-cable/p/62229601',
'https://www.southwire.com//wire-cable/substation/cu-pe-pvc-shielded-control-cable/p/66247201',

]
l5=[]
l6=[]
for url in l:
    print(url)
    browser.get(url)
    r=browser.page_source
    soup = BeautifulSoup(r, 'html.parser')
    first_click = soup.find('select',class_='form-select').find_all('option')
    for fr in first_click:
        asd=fr.get('selected')
        if asd is not None:
            fir=fr.text
    try:
        second_click = browser.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[6]/div[2]/div[3]/div[2]/a').get_attribute('title')
    except:
        second_click = browser.find_element(By.XPATH,
                                            '/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[5]/div[2]/div[3]/div[2]/a').get_attribute(
            'title')

    third_click = browser.find_elements(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[6]/div[2]/div[4]/select/option')


    fourth_click = browser.find_elements(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[6]/div[2]/div[5]/select/option')

    print(len(first_click))
    print(second_click)
    print(len(third_click))
    if len(third_click)==0:
        third_click = browser.find_elements(By.XPATH,
                                            '/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[5]/div[2]/div[4]/select')
    print(len(third_click))
    print(len(fourth_click))
    if  len(fourth_click)==0:
        fourth_click = browser.find_elements(By.XPATH,
                                             '/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[5]/div[2]/div[5]/select/option')
    print(len(fourth_click))
    for i2 in range(1,int(len(third_click))+1):
        try:
            browser.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[6]/div[2]/div[4]/select/option['+str(i2)+']').click()
        except:
            browser.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[5]/div[2]/div[4]/select/option['+str(i2)+']').click()
            print("SFADFDS")
        time.sleep(2)
        fourth_click = browser.find_elements(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[6]/div[2]/div[5]/select/option')
        if len(fourth_click)==0:
            fourth_click=browser.find_elements(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[5]/div[2]/div[5]/select/option')
        for i3 in range(1, int(len(fourth_click)) + 1):
            try:
                browser.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[6]/div[2]/div[5]/select/option['+str(i3)+']').click()
            except:
                browser.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[5]/div[2]/div[5]/select/option[' + str(i3) + ']').click()
                print("ddd")
            l5.append(fir.strip())
            l5.append(second_click.strip())
            try:
                l5.append(browser.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[6]/div[2]/div[4]/select/option['+str(i2)+']').text)
                l5.append(browser.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[6]/div[2]/div[5]/select/option['+str(i3)+']').text)
            except:
                l5.append(browser.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[5]/div[2]/div[4]/select/option[' + str(i2) + ']').text)
                l5.append(browser.find_element(By.XPATH,
                                               '/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/div[5]/div[2]/div[5]/select/option[' + str(
                                                   i3) + ']').text)
            time.sleep(2)
            head=browser.find_elements(By.CLASS_NAME,'variant-selector__entry-name')
            for he in head:
                l6.append(he.text)
            r = browser.page_source
            soup = BeautifulSoup(r, 'html.parser')
            bread = soup.find('ol', class_='breadcrumb').find_all('li')
            breadcrumb = []
            for br in bread:
                breadcrumb.append(br.text.strip())
            print(breadcrumb)
            title = soup.find('h1', class_='info-panel__name info-panel__name--large').text
            print(title)
            try:
                images = ''
                al_im = []
                images = soup.find('div', class_='slideshow').find('a').get('href')
                print(images)
                all_images = soup.find('div', class_='slideshow').find_all('a')
                for al in all_images:
                    al_im.append(al.get('href'))
            except:
                pass
            no = soup.find('div', class_='product-badges mb-3').find_all('span')
            model = ''
            south = ''
            for r1 in no:
                if "Southwire" in r1.text:
                    south = r1.text
                elif "Model" in r1.text:
                    model = r1.text
            print(south)
            print(model)
            description = soup.find('h2', class_='info-panel__description').text
            print(description)
            pd = soup.find('div', class_='d-flex flex-wrap').find('a').get('href')
            print(pd)
            deta = soup.find('div', id='product-tabs').find_all('div', role='tabpanel')
            at = []
            va = []
            t1 = []
            t2 = []
            t3 = []
            t4 = []
            pdf = []
            try:
                for df in deta:
                    a = df.find('h4')
                    print(a.text)

                    if "Specifications" not in a.text and "Resources" not in a.text:
                        b = df.find('div', class_='tab-panel__content tab-panel__content--skinny').text.replace('\n',
                                                                                                                '|')
                        at.append(a.text)
                        va.append(b)

                    if "Specifications" in a.text:
                        ta = df.find_all('tr')
                        l = 0
                        for tg in ta:
                            rt = tg.find('td', class_='specifications__table-sku-heading')
                            rv = tg.find('span', class_='imperial').text.strip()
                            me = rt.text.strip().split('\n')
                            t1.append(me[0])
                            if len(me) > 1:
                                t2.append(me[0].replace(" " + rv, me[1]))
                            else:
                                t2.append(me[0])
                            rb = tg.find_all('td', class_='specifications__table-sku-value')

                            for br in rb:
                                l += 1
                                if l % 2 == 0:
                                    t3.append(br.text.strip().split('\n'))
                                else:
                                    t4.append(br.text.strip().split('\n'))

                    if "Resources" in a.text:
                        p = df.find('div', class_='tab-panel__content').find_all('a')
                        for pf in p:
                            pdf.append(pf.get('href'))
            except:
                pass

            for z, x, c, g in zip(t1, t2, t3, t4):
                print(z, ":", x, ":", g, ":", c)
                if len(c) == 1:
                    c.append('')
                save_details: TextIO = open("south_click.txt", "a+", encoding="utf-8")
                save_details.write(
                    "\n" + url + "\t" + '->'.join(
                        breadcrumb) + "\t" + south + "\t" + model + "\t" + title + "\t" + description + "\t" + images + "\t" + ','.join(
                        al_im) + "\t" + pd + "\t" + "Imperial" + "\t" + z + "\t" + "rp_" + g[0] + "\t" + c[
                        0] + "\t" + ','.join(pdf))

                save_details.write(
                    "\n" + url + "\t" + '->'.join(
                        breadcrumb) + "\t" + south + "\t" + model + "\t" + title + "\t" + description + "\t" + images + "\t" + ','.join(
                        al_im) + "\t" + pd + "\t" + "Metric" + "\t" +
                    x + "\t" + "rp_" + g[1] + "\t" + c[1] + "\t" + ','.join(pdf))
                save_details.close()

            for ji, hi in zip(at, va):
                save_details: TextIO = open("south_click.txt", "a+", encoding="utf-8")
                save_details.write(
                    "\n" + url + "\t" + '->'.join(
                        breadcrumb) + "\t" + south + "\t" + model + "\t" + title + "\t" + description + "\t" + images + "\t" + ','.join(
                        al_im) + "\t" + pd + "\t" + "" + "\t" +
                    ji + "\t" + hi + "\t" + "" + "\t" + ','.join(pdf))
                print("End")
                save_details.close()
            for i6, i5 in zip(l6, l5):
                save_details: TextIO = open("south_click.txt", "a+", encoding="utf-8")
                save_details.write(
                    "\n" + url + "\t" + '->'.join(
                        breadcrumb) + "\t" + south + "\t" + model + "\t" + title + "\t" + description + "\t" + images + "\t" + ','.join(
                        al_im) + "\t" + pd + "\t" + "" + "\t" +
                    i6 + "\t" + i5 + "\t" + "" + "\t" + ','.join(pdf))
                print("End")
                save_details.close()
            l5.clear()
            l6.clear()



