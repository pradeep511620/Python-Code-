import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

Result = [
    'https://www.oatey.com/products/oatey-heavy-duty-gray-pvc-cement-829232139',
    'https://www.oatey.com/products/oatey-regular-clear-pvc-cement-1733423448',
    'https://www.oatey.com/products/oatey-heavy-duty-clear-pvc-cement-947141659',
    'https://www.oatey.com/products/oatey-all-purpose-cement--1970824977',
    'https://www.oatey.com/products/oatey-great-white-pipe-joint-compound-with-ptfe--275767012',
    'https://www.oatey.com/products/oatey-great-blue-pipe-joint-compound--561466668',
    'https://www.oatey.com/products/hercules-megaloc--1330684393',
    'https://www.oatey.com/products/harvey-tfe-paste-499646949',
    'https://www.oatey.com/products/oatey-no-95-tinning-flux-617577034',
    'https://www.oatey.com/products/oatey-no-5-paste-flux-584191109',
    'https://www.oatey.com/products/oatey-955-lead-free-plumbing-wire-solder--1659545085',
    'https://www.oatey.com/products/oatey-safeflo-lead-free-plumbing-wire-solder-kit-644067528',
    'https://www.oatey.com/products/oatey-fixit-stick-epoxy-putty-1829259701',
    'https://www.oatey.com/products/oatey-plumbers-putty--1165995750',
    'https://www.oatey.com/products/oatey-plumbers-putty--1165995750',
    'https://www.oatey.com/products/hercules-plastic-seal-339930492',
    'https://www.oatey.com/products/oatey-dark-thread-cutting-oil--2027589389',
    'https://www.oatey.com/products/oatey-1-oz-plumbers-grease--1101740680',
    'https://www.oatey.com/products/hercules-for-hands-hand-cleaning-towels-1618048549',
    'https://www.oatey.com/products/harvey-heat-proof-faucet-valve-grease--857817204',
    'https://www.oatey.com/products/hercules-clobber-drain-and-waste-system-cleaner--2095099000',
    'https://www.oatey.com/products/hercules-sizzle-drain-waste-system-cleaner--684453514',
    'https://www.oatey.com/products/hercules-glug-crystals-drain-opener--473237018',
    'https://www.oatey.com/products/hercules-clobber-drain-and-waste-system-cleaner--2095099000',
    'https://www.oatey.com/products/hercules-cryotek--100-antifreeze-306735881',
    'https://www.oatey.com/products/hercules-haymaker-tankless-water-heater-descaler--78801589',
    'https://www.oatey.com/products/hercules-boiler-heating-system-cleaner--1728813847',
    'https://www.oatey.com/products/hercules-cryotek--100-antifreeze-306735881',
    'https://www.oatey.com/products/oatey-liquilock-water-absorbing-crystals--1792398291',
    'https://www.oatey.com/products/harvey-noseep-no-5-wax-gaskets--1973066564',
    'https://www.oatey.com/products/oatey-reinforced-wax-bowl-ring-with-sleeve-611318407',
    'https://www.oatey.com/products/harvey-toilet-bolt-sets--531366645',
    'https://www.oatey.com/products/oatey-130-series-shower-drain-for-tile-bases-990314353',
    'https://www.oatey.com/products/oatey-testable-130-series-drain-pvc-round-low-profile-only--622984351',
    'https://www.oatey.com/products/oatey-140-series--101-pnc-plastic-nocaulk-shower-drains-1484090017',
    'https://www.oatey.com/products/oatey-twistnset-replacement-closet-flange-1098867162',
    'https://www.oatey.com/products/oatey-pvc-shower-pan-liner-1982292245',
    'https://www.oatey.com/products/oatey-dam-corners-1523188552',
    'https://www.oatey.com/products/oatey-oateyweld--1014141545',
    'https://www.oatey.com/products/oatey-130-series-shower-drain-for-tile-bases-990314353',
    'https://www.oatey.com/products/oatey-quadtro-single-lever-washing-machine-outlet-boxes-848912322',
    'https://www.oatey.com/products/oatey-metal-washing-machine-outlet-boxes-1261872593',
    'https://www.oatey.com/products/oatey-firerated-washing-machine-outlet-boxes-1260870643',
    'https://www.oatey.com/products/oatey-moda-washing-machine-single-boxes-1684836794',
    'https://www.oatey.com/products/oatey-rain-collar-for-nocalk-roof-flashings--1862141846',
    'https://www.oatey.com/products/oatey-master-flash-roof-flashings--936284941',
    'https://www.oatey.com/products/oatey-retro-master-flash-roof-flashings--947814875',
    'https://www.oatey.com/products/oatey-allflash-nocalk-roof-flashingsgalvanized-base-1617790699',
    'https://www.oatey.com/products/oatey-chrome-inline-vent--1440121105',
    'https://www.oatey.com/products/oatey-surevent-160-branch-24-stack-dfu-capacity-air-admittance-valve-wpvc-schedule-40-adapter-298571896',
    'https://www.oatey.com/products/oatey-surevent-160-branch-24-stack-dfu-capacity-air-admittance-valve-wabs-schedule-40-adapter-971792893',
    'https://www.oatey.com/products/oatey-sure-vent-air-admittance-valve-wall-box-wmetal-grille-faceplate-583786964',
    'https://www.oatey.com/products/oatey-metal-hanger-strap-640168637',
    'https://www.oatey.com/products/oatey-dwv-jhook--410025140',
    'https://www.oatey.com/products/oatey-insulating-pipe-clamps--1262532430',
    'https://www.oatey.com/products/oatey-holdrite-pipe-support-bracket-673732472',
    'https://www.oatey.com/products/dearborn112-brass-tubular-branch-tailpieces-hose--clamp--936490857',
    'https://www.oatey.com/products/oatey-integral-floor-drains-with-ptrap-valves--1277106382',
    'https://www.oatey.com/products/dearborn114-brass-tubular-ptrap-with-cleanout--892459767',
    'https://www.oatey.com/products/dearborn112-brass-tubular-ptrap-cleanout-975492141',
    'https://www.oatey.com/products/dearborn-schedule-40-bath-waste-unilift-half-kits--1447858356',
    'https://www.oatey.com/products/dearborn-true-blue-bathwaste-full-kits--1262019937',
    'https://www.oatey.com/products/dearborn-true-blue-bathwaste-roughin-kits--2005387207',
    'https://www.oatey.com/products/dearborn-true-blue-bathwaste-trim-kits--1381514324',
    'https://www.oatey.com/products/dearborn-18-deep-locking-cup-sink-basket-strainer-625544490',
    'https://www.oatey.com/products/dearborn-l7-sink-basket-strainers--773682640',
    'https://www.oatey.com/products/dearborn-14-shallow-locking-cup-sink-basket-strainer-893022040',
    'https://www.oatey.com/products/dearborn-14-shallow-locking-cup-sink-basket-strainer-893022040',
    'https://www.oatey.com/products/cherne-cleanseal-27093287',
    'https://www.oatey.com/products/cherne-multisize-underground-testball-1989624144',
    'https://www.oatey.com/products/cherne-singlesize-plumbing-testball--1719859634',
    'https://www.oatey.com/products/cherne-singlesize-plumbing-muniball--942936444',
    'https://www.oatey.com/products/cherne-insideofpipe-gripper-1775571796',
    'https://www.oatey.com/products/cherne-cleanout-gripper-plugs--1845547802',
    'https://www.oatey.com/products/cherne-endofpipe-gripper-1524150069',
    'https://www.oatey.com/products/cherne-kwik-n-sure--1694231260',
    'https://www.oatey.com/products/cherne-airloc-low-pressure-air-testing-control-panel-426269867',
    'https://www.oatey.com/products/cherne-econopump-test-pump--1200498495',
    'https://www.oatey.com/products/cherne-airloc-leak-locators-1256507960',
    'https://www.oatey.com/products/oatey-washing-machine-pan-914415061',
    'https://www.oatey.com/products/oatey-plastic-water-heater-pans-1112-adapter-112--996480874',
    'https://www.oatey.com/products/oatey-aluminum-water-heater-pans--1-to-112-pvc-adapter-1250491028',
    'https://www.oatey.com/products/oatey-washing-machine-pan-914415061',
    'https://www.oatey.com/products/oatey-pvc-floor-sinks-accessories-357315865',
    'https://www.oatey.com/products/oateyadjustable-drain-cleanouts-104521805',
    'https://www.oatey.com/products/oatey-flanged-general-purpose-commercial-drain-cleanout-components-141499627',
    'https://www.oatey.com/products/oatey-6-pvc-adjustable-commercial-drain--1006500314',
    'https://www.oatey.com/products/oatey-6-9-plastic-access-panel-1145262674',
    'https://www.oatey.com/products/oatey-bath-tub-protectors--1276667916',
    'https://www.oatey.com/products/oatey-quiet-pipes-aa-hammer-arrestors-tee-fitting--625418267',
    'https://www.oatey.com/products/oatey-endcap-pvc-test-caps--1657647381',

]
for url in Result:
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        # print(soup.prettify())
        opts = Options()
        opts.headless = True
        driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver", options=opts)
        driver.get(url)
        time.sleep(3)
        print("Product urls === ", url)
        #   =============================================== table =============================================================
        try:
            print("************************************* table : ****************************************")

            attr_n = []
            attr_v = []
            table = driver.find_elements(by=By.CLASS_NAME, value='spec-details')
            i = 0
            for x in table:
                dt = x.find_elements(By.TAG_NAME, 'td')
                for tdd in dt:
                    i = i + 1
                    if i % 2 != 0:

                        if tdd.text != '':
                            attr_n.append(tdd.text)
                    else:
                        if tdd.text != '':
                            attr_v.append(tdd.text)
            # print(attr_n)
            for m, n, in zip(attr_n, attr_v):
                print(m, "====", n)
                # save_details: TextIO = open("otey_table1.xlsx", "a+", encoding="utf-8")
                # save_details.write("\n" + url + "\t" + m + "\t" + n)
                # print("End")
                # save_details.close()
                # print("\n ***** Record stored into otey table  files. *****")
        except:
            pass
    except Exception as e:
        print(e)
