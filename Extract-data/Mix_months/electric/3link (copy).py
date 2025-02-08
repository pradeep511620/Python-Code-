import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
# driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
l = 0
Result = [
    # 'https://www.se.com/ww/en/product-range/45435153-acti9-active-afdd/?parent-subcategory-id=45435076',
    # 'https://www.se.com/ww/en/product-range/45435131-acti9-active-vigiarc/?parent-subcategory-id=45435076',
    # 'https://www.se.com/ww/en/product-range/64155-resi9-db60/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/61364-resi9-protection/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/64211-resi9-cx-enclosures/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/62107-wiser-energy/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/65817-easy9-devices/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/61956-easy9-mp-enclosures/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/867-micro-pragma/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/2605-resi9-mp/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/65251-acti9-ic40/?parent-subcategory-id=1605',
    # 'https://www.se.com/ww/en/product-range/7556-acti9-ic60/?parent-subcategory-id=1605',
    # 'https://www.se.com/ww/en/product-range/61088-acti9-c120/?parent-subcategory-id=1605',
    # 'https://www.se.com/ww/en/product-range/891-acti9-ng125/?parent-subcategory-id=1605',
    # 'https://www.se.com/ww/en/product-range/61703-acti9-ic60-lma/?parent-subcategory-id=1605',
    # 'https://www.se.com/ww/en/product-range/61704-acti9-ng125-lma/?parent-subcategory-id=1605',
    # 'https://www.se.com/ww/en/product-range/895-p25m/?parent-subcategory-id=1605',
    # 'https://www.se.com/ww/en/product-range/65253-acti9-vigi-ic40/?parent-subcategory-id=1620',
    # 'https://www.se.com/ww/en/product-range/7558-vigi-for-acti9-ic60/?parent-subcategory-id=1620',
    # 'https://www.se.com/ww/en/product-range/61094-vigi-for-acti9-c120/?parent-subcategory-id=1620',
    # 'https://www.se.com/ww/en/product-range/1083-vigi-for-acti9-ng125/?parent-subcategory-id=1620',
    # 'https://www.se.com/ww/en/product-range/65401-acti9-iid40/?parent-subcategory-id=1620',
    # 'https://www.se.com/ww/en/product-range/7559-acti9-iid/?parent-subcategory-id=1620',
    # 'https://www.se.com/ww/en/product-range/65400-acti9-icv40/?parent-subcategory-id=1620',
    # 'https://www.se.com/ww/en/product-range/61011-acti9-idpn-vigi/?parent-subcategory-id=1620',
    # 'https://www.se.com/ww/en/product-range/64209-acti9-ic60-rcbo-2p-3p-4p/?parent-subcategory-id=1620',
    # 'https://www.se.com/ww/en/product-range/61706-acti9-iprd1-prd1/?parent-subcategory-id=1615',
    # 'https://www.se.com/ww/en/product-range/61709-acti9-iprc-ipri-ipre/?parent-subcategory-id=1615',
    # 'https://www.se.com/ww/en/product-range/61708-acti9-iquick-pf-iquick-prd/?parent-subcategory-id=1615',
    # 'https://www.se.com/ww/en/product-range/7562-acti9-ipf-k/?parent-subcategory-id=1615',
    # 'https://www.se.com/ww/en/product-range/61707-acti9-iprd/?parent-subcategory-id=1615',
    # 'https://www.se.com/ww/en/product-range/45435000-acti9-afdd-/?parent-subcategory-id=86772',
    # 'https://www.se.com/ww/en/product-range/63604-acti9-idpn-n-arc/?parent-subcategory-id=86772',
    # 'https://www.se.com/ww/en/product-range/61532-acti9-iarc/?parent-subcategory-id=86772',
    # 'https://www.se.com/ww/en/product-range/896-acti9-sbi/?parent-subcategory-id=88726',
    # 'https://www.se.com/ww/en/product-range/7566-acti9-isw-sw/?parent-subcategory-id=1610',
    # 'https://www.se.com/ww/en/product-range/61705-acti9-iswna/?parent-subcategory-id=1610',
    # 'https://www.se.com/ww/en/product-range/1729-acti9-ng125-na/?parent-subcategory-id=1610',
    # 'https://www.se.com/ww/en/product-range/61089-acti9-ipc/?parent-subcategory-id=1625',
    # 'https://www.se.com/ww/en/product-range/61714-acti9-comb-busbars/?parent-subcategory-id=1625',
    # 'https://www.se.com/ww/en/product-range/7568-acti9-distribution-blocks/?parent-subcategory-id=1625',
    # 'https://www.se.com/ww/en/product-range/7569-multiclip/?parent-subcategory-id=1625',
    # 'https://www.se.com/ww/en/product-range/7577-acti9-accessories/?parent-subcategory-id=1625',
    # 'https://www.se.com/ww/en/product-range/63814-acti9-powertag-link-c/?parent-subcategory-id=1630',
    # 'https://www.se.com/ww/en/product-range/64481-acti9-smartlink/?parent-subcategory-id=1630',
    # 'https://www.se.com/ww/en/product-range/64482-acti9-powertag-link/?parent-subcategory-id=1630',
    # 'https://www.se.com/ww/en/product-range/61356-acti9-smartlink-modbus/?parent-subcategory-id=1630',
    # 'https://www.se.com/ww/en/product-range/7561-acti9-indication-and-tripping-auxiliaries/?parent-subcategory-id=1635',
    # 'https://www.se.com/ww/en/product-range/61712-acti9-ara/?parent-subcategory-id=1635',
    # 'https://www.se.com/ww/en/product-range/61711-acti9-rca/?parent-subcategory-id=1635',
    # 'https://www.se.com/ww/en/product-range/1084-acti9-auxiliaries-for-acti9-ng125/?parent-subcategory-id=1635',
    # 'https://www.se.com/ww/en/product-range/7563-acti9-ict/?parent-subcategory-id=1640',
    # 'https://www.se.com/ww/en/product-range/64061-acti9-ict+/?parent-subcategory-id=1640',
    # 'https://www.se.com/ww/en/product-range/7564-acti9-itl/?parent-subcategory-id=1640',
    # 'https://www.se.com/ww/en/product-range/64062-acti9-itl+/?parent-subcategory-id=1640',
    # 'https://www.se.com/ww/en/product-range/60180-acti9-reflex-ic60/?parent-subcategory-id=1640',
    # 'https://www.se.com/ww/en/product-range/61713-acti9-issw/?parent-subcategory-id=1640',
    # 'https://www.se.com/ww/en/product-range/7565-acti9-ipb/?parent-subcategory-id=1640',
    # 'https://www.se.com/ww/en/product-range/61092-acti9-icm-b-d-e-c-v-a/?parent-subcategory-id=1640',
    # 'https://www.se.com/ww/en/product-range/1153-trc/?parent-subcategory-id=1650',
    # 'https://www.se.com/ww/en/product-range/1898-ththp1+/?parent-subcategory-id=1650',
    # 'https://www.se.com/ww/en/product-range/2575-acti9-stdscu/?parent-subcategory-id=1650',
    # 'https://www.se.com/ww/en/product-range/61096-acti9-irt-irbn-irli-irc/?parent-subcategory-id=1650',
    # 'https://www.se.com/ww/en/product-range/62198-acti9-ih-ihp-ita/?parent-subcategory-id=1650',
    # 'https://www.se.com/ww/en/product-range/7613-acti9-iem-ime/?parent-subcategory-id=1650',
    # 'https://www.se.com/ww/en/product-range/836-acti9-cds/?parent-subcategory-id=1650',
    # 'https://www.se.com/ww/en/product-range/841-min/?parent-subcategory-id=1650',
    # 'https://www.se.com/ww/en/product-range/843-ic/?parent-subcategory-id=1650',
    # 'https://www.se.com/ww/en/product-range/61091-acti9-itr/?parent-subcategory-id=1645',
    # 'https://www.se.com/ww/en/product-range/61093-acti9-iso-iro/?parent-subcategory-id=1645',
    # 'https://www.se.com/ww/en/product-range/7567-acti9-iil/?parent-subcategory-id=1645',
    # 'https://www.se.com/ww/en/product-range/61095-acti9-c60hdc-acti9-c60pvdc/?parent-subcategory-id=80030',
    # 'https://www.se.com/ww/en/product-range/61516-acti9-c60nadc-c120nadc-sw60dc/?parent-subcategory-id=80030',
    # 'https://www.se.com/ww/en/product-range/61710-acti9-iprddcpv/?parent-subcategory-id=80030',
    # 'https://www.se.com/ww/en/product-range/1104-multi9/?parent-subcategory-id=1655',
    # 'https://www.se.com/ww/en/product-range/895-p25m/?parent-subcategory-id=1655',
    # 'https://www.se.com/ww/en/product-range/906-idrccb/?parent-subcategory-id=1655',
    # 'https://www.se.com/ww/en/product-range/7644-pratika/?parent-subcategory-id=2510',
    # 'https://www.se.com/in/en/product-range/2720-neo/?parent-subcategory-id=5620',
    # 'https://www.se.com/in/en/product-range/2722-zencelo/?parent-subcategory-id=5620',
    # 'https://www.se.com/in/en/product-range/2723-ulti/?parent-subcategory-id=5620',
    # 'https://www.se.com/in/en/product-range/62981-livia/?parent-subcategory-id=5620',
    # 'https://www.se.com/in/en/product-range/63294-opale/?parent-subcategory-id=5620',
    # 'https://www.se.com/in/en/product-range/63603-avataron/?parent-subcategory-id=5620',
    # 'https://www.se.com/in/en/product-range/65751-unica-pure/?parent-subcategory-id=5620',
    # 'https://www.se.com/in/en/product-range/66061-clipsal-x/?parent-subcategory-id=5620',
    # 'https://www.se.com/in/en/product-range/2078-argus-movement-detectors/?parent-subcategory-id=88041',
    # 'https://www.se.com/in/en/product-range/63545-masterpact-mtz/?parent-subcategory-id=4220',
    'https://www.se.com/in/en/product-range/1006-masterpact-nt/?parent-subcategory-id=4220',
    'https://www.se.com/in/en/product-range/1007-masterpact-nw/?parent-subcategory-id=4220',
    'https://www.se.com/in/en/product-range/1563-masterpact-nt-nw-navy/?parent-subcategory-id=4220',
    'https://www.se.com/in/en/product-range/1564-masterpact-ur/?parent-subcategory-id=4220',
    'https://www.se.com/in/en/product-range/62132-easypact-sps/?parent-subcategory-id=4220',
    'https://www.se.com/in/en/product-range/63429-compact-nsxm/?parent-subcategory-id=4230',
    'https://www.se.com/in/en/product-range/39910531-compact-nsx-new-generation/?parent-subcategory-id=4230',
    'https://www.se.com/in/en/product-range/1887-compact-nsx-630a/?parent-subcategory-id=4230',
    'https://www.se.com/in/en/product-range/1002-compact-ns-630a/?parent-subcategory-id=4230',
    'https://www.se.com/in/en/product-range/61297-compact-nsx-for-direct-current/?parent-subcategory-id=4230',
    'https://www.se.com/in/en/product-range/2591-fupact-nx/?parent-subcategory-id=4210',
    'https://www.se.com/in/en/product-range/1011-interpact-ins-inv-switches/?parent-subcategory-id=4210',
    'https://www.se.com/in/en/product-range/62074-compact-ins-inv/?parent-subcategory-id=4210',
    'https://www.se.com/in/en/product-range/1010-fupact-inf-isfl-isft/?parent-subcategory-id=4210',
    'https://www.se.com/in/en/product-range/64338-compact-nsxm-na/?parent-subcategory-id=4210',
    'https://www.se.com/in/en/product-range/996-compact-ns-switchesdisconnectors/?parent-subcategory-id=4210',
    'https://www.se.com/in/en/product-range/1566-masterpact-switch-disconnectors/?parent-subcategory-id=4210',
    'https://www.se.com/in/en/product-range/809-transferpact/?parent-subcategory-id=4260',
    'https://www.se.com/in/en/product-range/64117628-transferpact/?parent-subcategory-id=4260',
    # 'https://www.se.com/in/en/product-range/62410-enerlinx-fdm/?parent-subcategory-id=86477',
    # 'https://www.se.com/in/en/product-range/62413-enerlinx-if/?parent-subcategory-id=86477',
    # 'https://www.se.com/in/en/product-range/62412-enerlinx-io/?parent-subcategory-id=86477',
    # 'https://www.se.com/in/en/product-range/995-compact-ns80h-ma/?parent-subcategory-id=4240',
    # 'https://www.se.com/in/en/product-range/997-easypact-ezc/?parent-subcategory-id=23859433',
    # 'https://www.se.com/in/en/product-range/61052-easypact-cvs/?parent-subcategory-id=23859433',
    # 'https://www.se.com/in/en/product-range/61227-easypact-mvs/?parent-subcategory-id=23859433',
    # 'https://www.se.com/in/en/product-range/107042807-easypact-watsn/?parent-subcategory-id=23859433',
    # 'https://www.se.com/in/en/product-range/38501657-powerlogic-heattag/?parent-subcategory-id=38501516',
    # 'https://www.se.com/in/en/product-range/632-harmony-xb4/?parent-subcategory-id=89188',
    # 'https://www.se.com/in/en/product-range/633-harmony-xb5/?parent-subcategory-id=89188',
    # 'https://www.se.com/in/en/product-range/635-harmony-xb7/?parent-subcategory-id=89188',
    # 'https://www.se.com/in/en/product-range/62407-easy-harmony-xa2/?parent-subcategory-id=26828684',
    # 'https://www.se.com/in/en/product-range/634-harmony-9001-k/?parent-subcategory-id=89189',
    # 'https://www.se.com/in/en/product-range/1858-harmony-9001-sk/?parent-subcategory-id=89189',
    # 'https://www.se.com/in/en/product-range/709-harmony-xvl/?parent-subcategory-id=89187',
    # 'https://www.se.com/in/en/product-range/631-harmony-xb6/?parent-subcategory-id=89187',
    # 'https://www.se.com/in/en/product-range/2478-harmony-xb5s/?parent-subcategory-id=4850',
    # 'https://www.se.com/in/en/product-range/622-harmony-xpe/?parent-subcategory-id=4850',
    # 'https://www.se.com/in/en/product-range/1533-preventa-xy2-sb/?parent-subcategory-id=4850',
    # 'https://www.se.com/in/en/product-range/1534-preventa-xy2-au/?parent-subcategory-id=4850',
    # 'https://www.se.com/in/en/product-range/1041-harmony-xpe-atex-d/?parent-subcategory-id=4850',
    # 'https://www.se.com/in/en/product-range/60642-harmony-xb5r/?parent-subcategory-id=81654',
    # 'https://www.se.com/in/en/product-range/62193-harmony-exlhoist/?parent-subcategory-id=81654',
    # 'https://www.se.com/in/en/product-range/637-xd2g/?parent-subcategory-id=4820',
    # 'https://www.se.com/in/en/product-range/638-harmony-k/?parent-subcategory-id=4820',
    # 'https://www.se.com/in/en/product-range/662-harmony-xam-xap/?parent-subcategory-id=4810',
    # 'https://www.se.com/in/en/product-range/660-harmony-xald-xalk/?parent-subcategory-id=4810',
    # 'https://www.se.com/in/en/product-range/661-harmonyxac/?parent-subcategory-id=4810',
    # 'https://www.se.com/in/en/product-range/1445-harmony-xale/?parent-subcategory-id=4810',
    # 'https://www.se.com/in/en/product-range/1470-harmony-xalg/?parent-subcategory-id=4810',
    # 'https://www.se.com/in/en/product-range/1730-harmony-xalf/?parent-subcategory-id=4810',
    # 'https://www.se.com/in/en/product-range/970-sm624/?parent-subcategory-id=87899',
    # 'https://www.se.com/in/en/product-range/971-sm636/?parent-subcategory-id=87899',
    # 'https://www.se.com/in/en/product-range/984-mcset-123/?parent-subcategory-id=87898',
    # 'https://www.se.com/in/en/product-range/63274-pix-roll-on-floor/?parent-subcategory-id=87898',
    # 'https://www.se.com/in/en/product-range/60679-pix-36/?parent-subcategory-id=87898',
    # 'https://www.se.com/in/en/product-range/60924-pix-mv-air-insulated-switchgear/?parent-subcategory-id=87898',
    # 'https://www.se.com/in/en/product-range/60686-gma/?parent-subcategory-id=87901',
    # 'https://www.se.com/in/en/product-range/60685-gha/?parent-subcategory-id=87901',
    # 'https://www.se.com/in/en/product-range/1480-cbgs0/?parent-subcategory-id=87901',
    # 'https://www.se.com/in/en/product-range/60687-wi/?parent-subcategory-id=87901',
    # 'https://www.se.com/in/en/product-range/173798627-gv3n/?parent-subcategory-id=87901',
    # 'https://www.se.com/in/en/product-range/967-rm6/?parent-subcategory-id=87900',
    # 'https://www.se.com/in/en/product-range/60709-fbx/?parent-subcategory-id=87900',
    # 'https://www.se.com/in/en/product-range/60712-flusarc-36/?parent-subcategory-id=87900',
    # 'https://www.se.com/in/en/product-range/61301-premset/?parent-subcategory-id=87903',
    # 'https://www.se.com/in/en/product-range/61301-premset/?parent-subcategory-id=59089829',
    # 'https://www.se.com/in/en/product-range/65772-galaxy-vs/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/62414-galaxy-vm/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/22545656-galaxy-vl/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/63732-galaxy-vx/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/65643-easy-ups-3s/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/66001-easy-ups-3m/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/8297102-easy-ups-3l/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/61909-symmetra-px/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/66102-galaxy-lithiumion-battery-systems/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/65995-galaxy-vs-accessories/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/65920-easy-ups-3series-accessories/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/61910-symmetra-px-accessories/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/63672-gutor-pxc/?parent-subcategory-id=8030',
    # 'https://www.se.com/in/en/product-range/61883-backups-battery-backup/?parent-subcategory-id=8010',
    # 'https://www.se.com/in/en/product-range/61888-backups-pro/?parent-subcategory-id=8010',
    # 'https://www.se.com/in/en/product-range/65934-easy-ups/?parent-subcategory-id=8010',
    # 'https://www.se.com/in/en/product-range/61915-smartups/?parent-subcategory-id=8020',
    # 'https://www.se.com/in/en/product-range/61916-smartups-accessories/?parent-subcategory-id=8020',
    # 'https://www.se.com/in/en/product-range/61917-smartups-battery-systems/?parent-subcategory-id=8020',
    # 'https://www.se.com/in/en/product-range/61918-smartups-online-ups/?parent-subcategory-id=8020',
    # 'https://www.se.com/in/en/product-range/61919-symmetra/?parent-subcategory-id=8020',
    # 'https://www.se.com/in/en/product-range/61920-symmetra-accessories/?parent-subcategory-id=8020',
    # 'https://www.se.com/in/en/product-range/61921-symmetra-battery-systems/?parent-subcategory-id=8020',
    # 'https://www.se.com/in/en/product-range/65883-easy-ups-online/?parent-subcategory-id=8020',
    # 'https://www.se.com/in/en/product-range/82044159-smartups-ultra/?parent-subcategory-id=8020',
    # 'https://www.se.com/in/en/product-range/61927-additional-management-cards-and-options/?parent-subcategory-id=8040',
    # 'https://www.se.com/in/en/product-range/61929-battery-management/?parent-subcategory-id=8040',
    # 'https://www.se.com/in/en/product-range/61930-firmware-upgrades/?parent-subcategory-id=8040',
    # 'https://www.se.com/in/en/product-range/61931-interface-cables/?parent-subcategory-id=8040',
    # 'https://www.se.com/in/en/product-range/61932-powerchute-business-edition/?parent-subcategory-id=8040',
    # 'https://www.se.com/in/en/product-range/61933-powerchute-network-shutdown/?parent-subcategory-id=8040',
    # 'https://www.se.com/in/en/product-range/61934-powerchute-personal-edition/?parent-subcategory-id=8040',
    # 'https://www.se.com/in/en/product-range/61936-ups-network-management-cards/?parent-subcategory-id=8040',
    # 'https://www.se.com/in/en/product-range/62255-replacement-battery-cartridges/?parent-subcategory-id=8070',
    # 'https://www.se.com/in/en/product-range/66455-gutor-sdc-c/?parent-subcategory-id=88016',
    # 'https://www.se.com/in/en/product-range/61352-gutor-pxw/?parent-subcategory-id=88016',
    # 'https://www.se.com/in/en/product-range/61351-gutor-pxp/?parent-subcategory-id=88016',
    # 'https://www.se.com/in/en/product-range/61353-gutor-wxw/?parent-subcategory-id=88016',
    # 'https://www.se.com/in/en/product-range/61354-gutor-sdc/?parent-subcategory-id=88016',
    # 'https://www.se.com/in/en/product-range/66456-gutor-mdc/?parent-subcategory-id=88016',
    # 'https://www.se.com/in/en/product-range/63672-gutor-pxc/?parent-subcategory-id=88016',
    # 'https://www.se.com/in/en/product-range/61923-multistandard-offers/?parent-subcategory-id=8060',
    # 'https://www.se.com/in/en/product-range/61924-industrial-ups/?parent-subcategory-id=8060',
    # 'https://www.se.com/in/en/product-range/62271-marine/?parent-subcategory-id=8060',
    # 'https://www.se.com/in/en/product-range/61880-maintenance-bypass-panels/?parent-subcategory-id=89055',
    # 'https://www.se.com/in/en/product-range/2714-somove/?parent-subcategory-id=151300144',
    # 'https://www.se.com/in/en/product-range/62317-altivar-process-atv600/?parent-subcategory-id=86129',
    # 'https://www.se.com/in/en/product-range/62820-easy-altivar-610/?parent-subcategory-id=86129',
    # 'https://www.se.com/in/en/product-range/63124-altivar-process-atv900/?parent-subcategory-id=86129',
    # 'https://www.se.com/in/en/product-range/2253-altivar-12/?parent-subcategory-id=2905',
    # 'https://www.se.com/in/en/product-range/62880-easy-altivar-310/?parent-subcategory-id=2905',
    # 'https://www.se.com/in/en/product-range/63440-altivar-machine-atv320/?parent-subcategory-id=2905',
    # 'https://www.se.com/in/en/product-range/63441-altivar-machine-atv340/?parent-subcategory-id=2905',
    # 'https://www.se.com/in/en/product-range/777-other-vvd-products/?parent-subcategory-id=2905',
    # 'https://www.se.com/in/en/product-range/60162-altivar-212/?parent-subcategory-id=2945',
    # 'https://www.se.com/in/en/product-range/5745-altistart-22/?parent-subcategory-id=2940',
    # 'https://www.se.com/in/en/product-range/689-altistart-48/?parent-subcategory-id=2940',
    # 'https://www.se.com/in/en/product-range/779-altistart-01/?parent-subcategory-id=2940',
    # 'https://www.se.com/in/en/product-range/48782723-altivar-soft-starter-ats480/?parent-subcategory-id=2940',
    # 'https://www.se.com/in/en/product-range/61394-altivar-1200/?parent-subcategory-id=2920',
    # 'https://www.se.com/in/en/product-range/1155-altivar-71/?parent-subcategory-id=2950',
    # 'https://www.se.com/in/en/product-range/1422-altivar-61/?parent-subcategory-id=2950',
    # 'https://www.se.com/in/en/product-range/2373-altivar-71-plus/?parent-subcategory-id=2950',
    # 'https://www.se.com/in/en/product-range/2374-altivar-61-plus/?parent-subcategory-id=2950',
    # 'https://www.se.com/in/en/product-range/2656-altivar-312/?parent-subcategory-id=2950',
    # 'https://www.se.com/in/en/product-range/60326-altivar-303/?parent-subcategory-id=2950',
    # 'https://www.se.com/in/en/product-range/60843-altivar-71q/?parent-subcategory-id=2950',
    # 'https://www.se.com/in/en/product-range/60844-altivar-61q/?parent-subcategory-id=2950',
    # 'https://www.se.com/in/en/product-range/61444-altivar-312-solar/?parent-subcategory-id=2950',
    # 'https://www.se.com/in/en/product-range/7608-altivar-31c/?parent-subcategory-id=2950',
    # 'https://www.se.com/in/en/product-range/7609-altivar-32/?parent-subcategory-id=2950',
    # 'https://www.se.com/in/en/product-range/759-d-range/?parent-subcategory-id=3010',
    # 'https://www.se.com/in/en/product-range/2578-te-start/?parent-subcategory-id=3030',
    # 'https://www.se.com/in/en/product-range/65746-tesys-island/?parent-subcategory-id=1550',
    # 'https://www.se.com/in/en/product-range/1508-tesys-t/?parent-subcategory-id=1550',
    # 'https://www.se.com/in/en/product-range/682-tesys-u/?parent-subcategory-id=1550',
    # 'https://www.se.com/in/en/product-range/1160-tesys-lutm/?parent-subcategory-id=1550',
    # 'https://www.se.com/in/en/product-range/684-tesys-deca-frame-2/?parent-subcategory-id=38342932',
    # 'https://www.se.com/in/en/product-range/1446-tesys-deca-frame-3/?parent-subcategory-id=38342932',
    # 'https://www.se.com/in/en/product-range/672-tesys-gv3-version-1988/?parent-subcategory-id=38342932',
    # 'https://www.se.com/in/en/product-range/63428-tesys-deca-frame-4/?parent-subcategory-id=38342932',
    # 'https://www.se.com/in/en/product-range/66038-tesys-giga-circuitbreakers/?parent-subcategory-id=38342932',
    # 'https://www.se.com/in/en/product-range/699-tesys-quickfit/?parent-subcategory-id=38342932',
    # 'https://www.se.com/in/en/product-range/671-gk3/?parent-subcategory-id=38342932',
    # 'https://www.se.com/in/en/product-range/63062-tesys-h/?parent-subcategory-id=1510',
    # 'https://www.se.com/in/en/product-range/664-tesys-deca-contactors/?parent-subcategory-id=1510',
    # 'https://www.se.com/in/en/product-range/666-tesys-k-contactors/?parent-subcategory-id=1510',
    # 'https://www.se.com/in/en/product-range/714-tesys-model-sk/?parent-subcategory-id=1510',
    # 'https://www.se.com/in/en/product-range/26322422-tesys-giga-contactor/?parent-subcategory-id=1510',
    # 'https://www.se.com/in/en/product-range/665-tesys-f/?parent-subcategory-id=1510',
    # 'https://www.se.com/in/en/product-range/667-tesys-b/?parent-subcategory-id=1510',
    # 'https://www.se.com/in/en/product-range/767-tesys-k-d-sk-control-relays/?parent-subcategory-id=1510',
    # 'https://www.se.com/in/en/product-range/1885-tesys-deca-thermal-overload-relays/?parent-subcategory-id=1570',
    # 'https://www.se.com/in/en/product-range/26399648-tesys-giga-electronic-relay/?parent-subcategory-id=1570',
    # 'https://www.se.com/in/en/product-range/761-tesys-lr9-lr9d-lr9d/?parent-subcategory-id=1570',
    # 'https://www.se.com/in/en/product-range/679-tesys-lr2-k/?parent-subcategory-id=1570',
    # 'https://www.se.com/in/en/product-range/1163-tesys-deca-electronic-relays/?parent-subcategory-id=1520',
    # 'https://www.se.com/in/en/product-range/1164-tesys-deca-overcurrent-relays/?parent-subcategory-id=1520',
    # 'https://www.se.com/in/en/product-range/677-tesys-lt3/?parent-subcategory-id=1520',
    # 'https://www.se.com/in/en/product-range/624-tesys-minivario/?parent-subcategory-id=88157626',
    # 'https://www.se.com/in/en/product-range/670-gb2/?parent-subcategory-id=88157626',
    # 'https://www.se.com/in/en/product-range/674-tesys-gs/?parent-subcategory-id=88157626',
    # 'https://www.se.com/in/en/product-range/625-tesys-gv2me/?parent-subcategory-id=88157624',
    # 'https://www.se.com/in/en/product-range/681-tesys-le-dol-starters/?parent-subcategory-id=88157624',
    # 'https://www.se.com/in/en/product-range/683-tesys-gv2-lc/?parent-subcategory-id=88157624',
    # 'https://www.se.com/in/en/product-range/63104-easypact-tvs-motor-circuit-breaker/?parent-subcategory-id=86334',
    # 'https://www.se.com/in/en/product-range/60145-easypact-tvs/?parent-subcategory-id=86334',
    # 'https://www.se.com/in/en/product-range/62392-easypact-tvs-control-relay/?parent-subcategory-id=86334',
    # 'https://www.se.com/in/en/product-range/62393-easypact-tvs-thermal-overload-relay/?parent-subcategory-id=86334',


]
for url in Result:
    try:
        l = l + 1
        driver.get(url)
        r = driver.page_source
        soup = BeautifulSoup(r, "html.parser")
        # print(soup)
        time.sleep(15)
        print("products urls", l, url)
        # first urls printed here
        for j in range(1, 12 + 1):
            k = driver.execute_script('return document.querySelector("pes-tabs se-container.pes-tabs-content.centered-content.relative.ct-bg-standard.row-dir.flex-display.hydrated div:nth-child(1) pes-range-products-tab")\
            .shadowRoot.querySelector("se-container div.range-products-tab__main-block-container se-block product-cards-wrapper")\
            .shadowRoot.querySelector("div ul li:nth-child(' + str(j) + ') product-card")\
            .shadowRoot.querySelector("article div div.body product-card-main-info").shadowRoot.querySelector("div pes-router-link a")')
            u1 = k.get_attribute('href')
            print("data1...", u1)
            save_details: k = open("se_urls.xlsx", "a+", encoding="utf-8")
            save_details.write("\n" + "'"+u1+"',")
            save_details.close()
        print("\n ***** Record stored into urls  files. *****")

        # second urls get here
        # here is length
        counts = driver.execute_script(
            'return document.querySelector("pes-tabs se-container.pes-tabs-content.centered-content.relative.ct-bg-standard.row-dir.flex-display.hydrated div:nth-child(1) pes-range-products-tab").shadowRoot.querySelector("se-container div.range-products-tab__main-block-container se-block product-cards-wrapper").shadowRoot.querySelector("div div pdp-switch-card-view").shadowRoot.querySelector("span")')
        # print(counts.text)
        count = counts.text.split()[-2]
        print("count...", count)
        length = round(int(count) / 12 + 1)
        print("division...", length)
        for j in range(1, length):
            inc = j * 12
            adds = '&No=' + str(inc) + '&Nrpp=12'
            add_urls = url + adds
            print(add_urls)
            driver.get(add_urls)
            time.sleep(10)
            for m in range(1, 12 + 1):
                k = driver.execute_script('return document.querySelector("pes-tabs se-container.pes-tabs-content.centered-content.relative.ct-bg-standard.row-dir.flex-display.hydrated div:nth-child(1) pes-range-products-tab")\
                .shadowRoot.querySelector("se-container div.range-products-tab__main-block-container se-block product-cards-wrapper")\
                .shadowRoot.querySelector("div ul li:nth-child(' + str(m) + ') product-card")\
                .shadowRoot.querySelector("article div div.body product-card-main-info").shadowRoot.querySelector("div pes-router-link a")')
                uu = k.get_attribute('href')
                print("data2..", uu)
                save_details: k = open("se_urls.xlsx", "a+", encoding="utf-8")
                save_details.write("\n" + "'"+uu+"',")
                save_details.close()
            print("\n ***** Record stored into urls  files. *****")
    except:
        print("Not Found")

#
# for j in range(1, 12):
#     k = driver.execute_script('return document.querySelector("pes-tabs se-container.pes-tabs-content.centered-content.relative.ct-bg-standard.row-dir.flex-display.hydrated div:nth-child(1) pes-range-products-tab")\
#     .shadowRoot.querySelector("se-container div.range-products-tab__main-block-container se-block product-cards-wrapper")\
#     .shadowRoot.querySelector("div ul li:nth-child('+str(j)+') product-card")\
#     .shadowRoot.querySelector("article div div.body product-card-main-info").shadowRoot.querySelector("div pes-router-link a")')
#     print(k.get_attribute('href'))
