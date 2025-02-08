import requests
from bs4 import BeautifulSoup
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from typing.io import TextIO

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
l = 0
mylist = [

    # 'https://www.zoro.com/search?q=panduit%20SG370SG-L',
    # 'https://www.zoro.com/search?q=panduit%20PWT150',
    # 'https://www.zoro.com/search?q=panduit%20PW50F-T20',
    # 'https://www.zoro.com/search?q=panduit%20PW75F-C20',
    # 'https://www.zoro.com/search?q=panduit%20PW100F-C20',
    # 'https://www.zoro.com/search?q=panduit%20PW150F-L20',
    # 'https://www.zoro.com/search?q=panduit%20GES62F-A-C',
    # 'https://www.zoro.com/search?q=panduit%20GES99F-A-C',
    # 'https://www.zoro.com/search?q=panduit%20JP2W',
    # 'https://www.zoro.com/search?q=panduit%20PLT1.5IG-C',
    # 'https://www.zoro.com/search?q=panduit%20PLT1.5IG-C0',
    # 'https://www.zoro.com/search?q=panduit%20PLT10LHG-L',
    # 'https://www.zoro.com/search?q=panduit%20PLT1MG-C',
    # 'https://www.zoro.com/search?q=panduit%20PLT1MG-C0',
    # 'https://www.zoro.com/search?q=panduit%20PLT1M-M',
    # 'https://www.zoro.com/search?q=panduit%20PLT1M-M0',
    # 'https://www.zoro.com/search?q=panduit%20PLT2IG-C',
    # 'https://www.zoro.com/search?q=panduit%20PLT2IG-C0',
    # 'https://www.zoro.com/search?q=panduit%20PLT2I-M',
    # 'https://www.zoro.com/search?q=panduit%20PLT2I-M0',
    # 'https://www.zoro.com/search?q=panduit%20PLT2MG-C',
    # 'https://www.zoro.com/search?q=panduit%20PLT2MG-C0',
    # 'https://www.zoro.com/search?q=panduit%20PLT2M-M',
    # 'https://www.zoro.com/search?q=panduit%20PLT2M-M0',
    # 'https://www.zoro.com/search?q=panduit%20PLT2SG-C',
    # 'https://www.zoro.com/search?q=panduit%20PLT2SG-C0',
    # 'https://www.zoro.com/search?q=panduit%20PLT2S-M0',
    # 'https://www.zoro.com/search?q=panduit%20PLT3IG-C',
    # 'https://www.zoro.com/search?q=panduit%20PLT3IG-C0',
    # 'https://www.zoro.com/search?q=panduit%20PLT3I-M',
    # 'https://www.zoro.com/search?q=panduit%20PLT3SG-C',
    # 'https://www.zoro.com/search?q=panduit%20PLT3SG-C0',
    # 'https://www.zoro.com/search?q=panduit%20PLT4IG-C',
    # 'https://www.zoro.com/search?q=panduit%20PLT4IG-C0',
    # 'https://www.zoro.com/search?q=panduit%20PLT4SG-C',
    # 'https://www.zoro.com/search?q=panduit%20PLT4S-M0',
    # 'https://www.zoro.com/search?q=panduit%20PLT6LHG-L',
    # 'https://www.zoro.com/search?q=panduit%20PLT6LHG-L0',
    # 'https://www.zoro.com/search?q=panduit%20PLT7LHG-L',
    # 'https://www.zoro.com/search?q=panduit%20PLT7LHG-L0',
    # 'https://www.zoro.com/search?q=panduit%20PLT8LHG-L',
    # 'https://www.zoro.com/search?q=panduit%20PLT8LHG-L0',
    # 'https://www.zoro.com/search?q=panduit%20PLT9LHG-L',
    # 'https://www.zoro.com/search?q=panduit%20PLT9LHG-L0',
    # 'https://www.zoro.com/search?q=panduit%20GB4B1028TPI-1',
    # 'https://www.zoro.com/search?q=panduit%20GB4N0016TPI-1',
    # 'https://www.zoro.com/search?q=panduit%20MRT6S-C4',
    # 'https://www.zoro.com/search?q=panduit%20MRT1.5LH-L4',
    # 'https://www.zoro.com/search?q=panduit%20MRT2LH-L4',
    # 'https://www.zoro.com/search?q=panduit%20MRT6LH-L4',
    # 'https://www.zoro.com/search?q=panduit%20MRS1S-C4',
    # 'https://www.zoro.com/search?q=panduit%20MRS1.5LH-L4',
    # 'https://www.zoro.com/search?q=panduit%20MRS4LH-L4',
    # 'https://www.zoro.com/search?q=panduit%20GS4MT',
    # 'https://www.zoro.com/search?q=panduit%20MTRTLS',
    # 'https://www.zoro.com/search?q=panduit%20BT3I-M0',
    # 'https://www.zoro.com/search?q=panduit%20BT2S-C0',
    # 'https://www.zoro.com/search?q=panduit%20BT2S-M0',
    # 'https://www.zoro.com/search?q=panduit%20BT2LH-L',
    # 'https://www.zoro.com/search?q=panduit%20BT4LH-L',
    # 'https://www.zoro.com/search?q=panduit%20BT4LH-TL0',
    # 'https://www.zoro.com/search?q=panduit%20BT5LH-L',
    # 'https://www.zoro.com/search?q=panduit%20BT7LH-L',
    # 'https://www.zoro.com/search?q=panduit%20BT8LH-L',
    # 'https://www.zoro.com/search?q=panduit%20BT9LH-L',
    # 'https://www.zoro.com/search?q=panduit%20BC4LH-S25-L',
    # 'https://www.zoro.com/search?q=panduit%20HLT3I-X0',
    # 'https://www.zoro.com/search?q=panduit%20HLS5S-X0',
    # 'https://www.zoro.com/search?q=panduit%20HLM-15R0',
    # 'https://www.zoro.com/search?q=panduit%20TTS-35RX0',
    # 'https://www.zoro.com/search?q=panduit%20D4H6',
    # 'https://www.zoro.com/search?q=panduit%20SD3H6',
    # 'https://www.zoro.com/search?q=panduit%20SD4H6',
    # 'https://www.zoro.com/search?q=panduit%20DB-C',
    # 'https://www.zoro.com/search?q=panduit%20DCT',
    # 'https://www.zoro.com/search?q=panduit%20HN2X2WH6',
    # 'https://www.zoro.com/search?q=panduit%20G2X2WH6',
    # 'https://www.zoro.com/search?q=panduit%20G2X3LG6',
    # 'https://www.zoro.com/search?q=panduit%20G2X3WH6',
    # 'https://www.zoro.com/search?q=panduit%20G2X4LG6',
    # 'https://www.zoro.com/search?q=panduit%20G2X4WH6',
    # 'https://www.zoro.com/search?q=panduit%20G2X5WH6',
    # 'https://www.zoro.com/search?q=panduit%20G3X3LG6',
    # 'https://www.zoro.com/search?q=panduit%20G3X4LG6',
    # 'https://www.zoro.com/search?q=panduit%20G3X4WH6',
    # 'https://www.zoro.com/search?q=panduit%20G3X5LG6',
    # 'https://www.zoro.com/search?q=panduit%20G3X5WH6',
    # 'https://www.zoro.com/search?q=panduit%20G4X3LG6',
    # 'https://www.zoro.com/search?q=panduit%20G4X4LG6',
    # 'https://www.zoro.com/search?q=panduit%20G4X5LG6',
    # 'https://www.zoro.com/search?q=panduit%20G4X5WH6',
    # 'https://www.zoro.com/search?q=panduit%20G1.5X1.5LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20G1.5X2LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20G1.5X3LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20G1.5X4LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20G1X1.5LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20G1X1LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20G1X2LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20F1X4LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20F2X2LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20F2X3LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20F2X4LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20F3X3LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20F3X4LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20F4X4LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20F4X5LG6-A',
    # 'https://www.zoro.com/search?q=panduit%20CWD3WH6',
    # 'https://www.zoro.com/search?q=panduit%20G1.5X1.5LG6',
    # 'https://www.zoro.com/search?q=panduit%20G1.5X2LG6',
    # 'https://www.zoro.com/search?q=panduit%20G1.5X2WH6',
    # 'https://www.zoro.com/search?q=panduit%20G1.5X3LG6',
    # 'https://www.zoro.com/search?q=panduit%20G1.5X4LG6',
    # 'https://www.zoro.com/search?q=panduit%20G1X1.5LG6',
    # 'https://www.zoro.com/search?q=panduit%20G1X1.5WH6',
    # 'https://www.zoro.com/search?q=panduit%20G1X1LG6',
    # 'https://www.zoro.com/search?q=panduit%20G1X2LG6',
    # 'https://www.zoro.com/search?q=panduit%20G1X3LG6',
    # 'https://www.zoro.com/search?q=panduit%20G1X4LG6',
    # 'https://www.zoro.com/search?q=panduit%20G1X4WH6',
    # 'https://www.zoro.com/search?q=panduit%20G2X2LG6',
    # 'https://www.zoro.com/search?q=panduit%20MMP350H-CAL',
    # 'https://www.zoro.com/search?q=panduit%20MIM187',
    # 'https://www.zoro.com/search?q=panduit%20JP75DW-L20',
    # 'https://www.zoro.com/search?q=panduit%20JP75W-L20',
    # 'https://www.zoro.com/search?q=panduit%20JP4W-X20',
    # 'https://www.zoro.com/search?q=panduit%20JP75DW-L2',
    # 'https://www.zoro.com/search?q=panduit%20JP2W-L2',
    # 'https://www.zoro.com/search?q=panduit%20JP131W-L6',
    # 'https://www.zoro.com/search?q=panduit%20JP2DW-L6',
    # 'https://www.zoro.com/search?q=panduit%20JP2DW-L',
    # 'https://www.zoro.com/search?q=panduit%20JP4W-X',
    # 'https://www.zoro.com/search?q=panduit%20PES-S1',
    # 'https://www.zoro.com/search?q=panduit%20PVS0204C171Y',
    # 'https://www.zoro.com/search?q=panduit%20KP-HSTT2',
    # 'https://www.zoro.com/search?q=panduit%20PSL-DCJB',
    # 'https://www.zoro.com/search?q=panduit%20PSL-DCJB-BL',
    # 'https://www.zoro.com/search?q=panduit%20PSL-DCJB-BU',
    # 'https://www.zoro.com/search?q=panduit%20PSL-DCJB-GR',
    # 'https://www.zoro.com/search?q=panduit%20PSL-DCJB-IG',
    # 'https://www.zoro.com/search?q=panduit%20PSL-DCJB-IG-C',
    # 'https://www.zoro.com/search?q=panduit%20CJ5E88TIG',
    # 'https://www.zoro.com/search?q=panduit%20CJ5E88TIW',
    # 'https://www.zoro.com/search?q=panduit%20CJ688TPBL',
    # 'https://www.zoro.com/search?q=panduit%20CJ688TPBU',
    # 'https://www.zoro.com/search?q=panduit%20CJ688TPEI',
    # 'https://www.zoro.com/search?q=panduit%20CJ688TPWH',
    # 'https://www.zoro.com/search?q=panduit%20CJ688TPIG',
    # 'https://www.zoro.com/search?q=panduit%20CJ688TPIW',
    # 'https://www.zoro.com/search?q=panduit%20DP245E88TGY',
    # 'https://www.zoro.com/search?q=panduit%20DP24688TGY',
    # 'https://www.zoro.com/search?q=panduit%20DP485E88TGY',
    # 'https://www.zoro.com/search?q=panduit%20DP48688TGY',
    # 'https://www.zoro.com/search?q=panduit%20CPP24WBLY',
    # 'https://www.zoro.com/search?q=panduit%20CPPL24WBLY',
    # 'https://www.zoro.com/search?q=panduit%20CPP48WBLY',
    # 'https://www.zoro.com/search?q=panduit%20CPPL48WBLY',
    # 'https://www.zoro.com/search?q=panduit%20SRB19BLY',
    # 'https://www.zoro.com/search?q=panduit%20CC688BL',
    # 'https://www.zoro.com/search?q=panduit%20CMFIW',
    # 'https://www.zoro.com/search?q=panduit%20CMFEI',
    # 'https://www.zoro.com/search?q=panduit%20CMFWH',
    # 'https://www.zoro.com/search?q=panduit%20CMBIW-X',
    # 'https://www.zoro.com/search?q=panduit%20CMBEI-X',
    # 'https://www.zoro.com/search?q=panduit%20CMBWH-X',
    # 'https://www.zoro.com/search?q=panduit%20CMBBL-X',
    # 'https://www.zoro.com/search?q=panduit%20CFPE4IWY',
    # 'https://www.zoro.com/search?q=panduit%20CFPE4EIY',
    # 'https://www.zoro.com/search?q=panduit%20CFPE4WHY',
    # 'https://www.zoro.com/search?q=panduit%20CFPE2IWY',
    # 'https://www.zoro.com/search?q=panduit%20CFPE2EIY',
    # 'https://www.zoro.com/search?q=panduit%20CFPE2WHY',
    # 'https://www.zoro.com/search?q=panduit%20CBX2IW-AY',
    # 'https://www.zoro.com/search?q=panduit%20CBX2EI-AY',
    # 'https://www.zoro.com/search?q=panduit%20CBX2WH-AY',
    # 'https://www.zoro.com/search?q=panduit%20CBX4IW-AY',
    # 'https://www.zoro.com/search?q=panduit%20CBX4EI-AY',
    # 'https://www.zoro.com/search?q=panduit%20CBX4WH-AY',
    # 'https://www.zoro.com/search?q=panduit%20CFFPL4BL',
    # 'https://www.zoro.com/search?q=panduit%20CF1062IWY',
    # 'https://www.zoro.com/search?q=panduit%20CF1062EIY',
    # 'https://www.zoro.com/search?q=panduit%20CF1062WHY',
    # 'https://www.zoro.com/search?q=panduit%20CF1064IWY',
    # 'https://www.zoro.com/search?q=panduit%20CF1064EIY',
    # 'https://www.zoro.com/search?q=panduit%20CF1064WHY',
    # 'https://www.zoro.com/search?q=panduit%20CFG2WH',
    # 'https://www.zoro.com/search?q=panduit%20CFG4IW',
    # 'https://www.zoro.com/search?q=panduit%20CFG4WH',
    # 'https://www.zoro.com/search?q=panduit%20CMHDMIIW',
    # 'https://www.zoro.com/search?q=panduit%20CMHDMIEI',
    # 'https://www.zoro.com/search?q=panduit%20CMHDMIWH',
    # 'https://www.zoro.com/search?q=panduit%20FMT1',
    # 'https://www.zoro.com/search?q=panduit%20CFAPPBL1',
    # 'https://www.zoro.com/search?q=panduit%20FOSMF',
    # 'https://www.zoro.com/search?q=panduit%20FSC24',
    # 'https://www.zoro.com/search?q=panduit%20FAPB',
    # 'https://www.zoro.com/search?q=panduit%20FMP6',
    # 'https://www.zoro.com/search?q=panduit%20FMS1',
    # 'https://www.zoro.com/search?q=panduit%20FMS2',
    # 'https://www.zoro.com/search?q=panduit%20FWME2',
    # 'https://www.zoro.com/search?q=panduit%20CMDSAQLCZBL',
    # 'https://www.zoro.com/search?q=panduit%20CMDSLCZBU',
    # 'https://www.zoro.com/search?q=panduit%20CMDBUSCZBU',
    # 'https://www.zoro.com/search?q=panduit%20R2P',
    # 'https://www.zoro.com/search?q=panduit%20WMPV45E',
    # 'https://www.zoro.com/search?q=panduit%20WMPSE',
    # 'https://www.zoro.com/search?q=panduit%20WMP1E',
    # 'https://www.zoro.com/search?q=panduit%20CMPH1',
    # 'https://www.zoro.com/search?q=panduit%20CMPH2',
    # 'https://www.zoro.com/search?q=panduit%20CMPHF1',
    # 'https://www.zoro.com/search?q=panduit%20LDPH5IW8-A',
    # 'https://www.zoro.com/search?q=panduit%20CFX5IW-X',
    # 'https://www.zoro.com/search?q=panduit%20RAFX5IW-X',
    # 'https://www.zoro.com/search?q=panduit%20ICFX5IW-X',
    # 'https://www.zoro.com/search?q=panduit%20OCFC5IW-X',
    # 'https://www.zoro.com/search?q=panduit%20ECFX5IW-X',
    # 'https://www.zoro.com/search?q=panduit%20DCEFXIW-X',
    # 'https://www.zoro.com/search?q=panduit%20TG70IW8',
    # 'https://www.zoro.com/search?q=panduit%20TG70BCIW-X',
    # 'https://www.zoro.com/search?q=panduit%20T70CCIW-X',
    # 'https://www.zoro.com/search?q=panduit%20TGECIW',
    # 'https://www.zoro.com/search?q=panduit%20TG70WR-X',
    # 'https://www.zoro.com/search?q=panduit%20TGEEIW',
    # 'https://www.zoro.com/search?q=panduit%20T70DB-X',
    # 'https://www.zoro.com/search?q=panduit%20T70PIW',
    # 'https://www.zoro.com/search?q=panduit%20T70PGIW',
    # 'https://www.zoro.com/search?q=panduit%20T45BIW8',
    # 'https://www.zoro.com/search?q=panduit%20T45CIW8',
    # 'https://www.zoro.com/search?q=panduit%20T45ICIW',
    # 'https://www.zoro.com/search?q=panduit%20T45OCIW',
    # 'https://www.zoro.com/search?q=panduit%20T45RAIW',
    # 'https://www.zoro.com/search?q=panduit%20T45TIW',
    # 'https://www.zoro.com/search?q=panduit%20T45CCIW-X',
    # 'https://www.zoro.com/search?q=panduit%20T45EEIW',
    # 'https://www.zoro.com/search?q=panduit%20T45ECIW',
    # 'https://www.zoro.com/search?q=panduit%20T45WCIW',
    # 'https://www.zoro.com/search?q=panduit%20T45RLDIW',
    # 'https://www.zoro.com/search?q=panduit%20JBX3510IW-A',
    # 'https://www.zoro.com/search?q=panduit%20JB1FSIW-A',
    # 'https://www.zoro.com/search?q=panduit%20JBP2FSIW',
    # 'https://www.zoro.com/search?q=panduit%20JBP1DIW',
    # 'https://www.zoro.com/search?q=panduit%20JBP2DIW',
    # 'https://www.zoro.com/search?q=panduit%20JBP2SIW',
    # 'https://www.zoro.com/search?q=panduit%20CP106IW-2G',
    # 'https://www.zoro.com/search?q=panduit%20T70BIW8G',
    # 'https://www.zoro.com/search?q=panduit%20T70CIW8',
    # 'https://www.zoro.com/search?q=panduit%20T70ICIW',
    # 'https://www.zoro.com/search?q=panduit%20T70OCIW',
    # 'https://www.zoro.com/search?q=panduit%20T70RAIW',
    # 'https://www.zoro.com/search?q=panduit%20T70TIW',
    # 'https://www.zoro.com/search?q=panduit%20T70TD',
    # 'https://www.zoro.com/search?q=panduit%20T70BCIW-X',
    # 'https://www.zoro.com/search?q=panduit%20T70EEIW',
    # 'https://www.zoro.com/search?q=panduit%20T70ECIW',
    # 'https://www.zoro.com/search?q=panduit%20T70DW8',
    # 'https://www.zoro.com/search?q=panduit%20T70HB3-X',
    # 'https://www.zoro.com/search?q=panduit%20T70WC2IW',
    # 'https://www.zoro.com/search?q=panduit%20T70WR-X',
    # 'https://www.zoro.com/search?q=panduit%20T70TRIW',
    # 'https://www.zoro.com/search?q=panduit%20T70TRCIW',
    # 'https://www.zoro.com/search?q=panduit%20T70BFI',
    # 'https://www.zoro.com/search?q=panduit%20FS3X2LG6NM',
    # 'https://www.zoro.com/search?q=panduit%20FS3X3LG6NM',
    # 'https://www.zoro.com/search?q=panduit%20FS3X4LG6NM',
    # 'https://www.zoro.com/search?q=panduit%20FS2X3LG6NM',
    # 'https://www.zoro.com/search?q=panduit%20LD5IW8-A',
    # 'https://www.zoro.com/search?q=panduit%20CF5IW-E',
    # 'https://www.zoro.com/search?q=panduit%20ICF5IW-E',
    # 'https://www.zoro.com/search?q=panduit%20OCF5IW-E',
    # 'https://www.zoro.com/search?q=panduit%20RAF5IW-E',
    # 'https://www.zoro.com/search?q=panduit%20TF5IW-E',
    # 'https://www.zoro.com/search?q=panduit%20ECF5IW-E',
    # 'https://www.zoro.com/search?q=panduit%20DCF5IW-X',
    # 'https://www.zoro.com/search?q=panduit%20PSL-PL1BLKY',
    # 'https://www.zoro.com/search?q=panduit%20PSL-PL1GRNY',
    # 'https://www.zoro.com/search?q=panduit%20PSL-PL1WHTY',
    # 'https://www.zoro.com/search?q=panduit%20PLT2I-C86',
    # 'https://www.zoro.com/search?q=panduit%20PLT3S-C86',
    # 'https://www.zoro.com/search?q=panduit%20PLT4S-C86',
    # 'https://www.zoro.com/search?q=panduit%20PLT2S-C86',
    # 'https://www.zoro.com/search?q=panduit%20PSL-PL1REDY',
    # 'https://www.zoro.com/search?q=panduit%20PLT1M-C86',
    # 'https://www.zoro.com/search?q=panduit%20CD-930G-1/0',
    # 'https://www.zoro.com/search?q=panduit%20CD-930G-250',
    # 'https://www.zoro.com/search?q=panduit%20CD-930G-500',
    # 'https://www.zoro.com/search?q=panduit%20RGESD2-1',
    # 'https://www.zoro.com/search?q=panduit%20RGESD2B-1',
    # 'https://www.zoro.com/search?q=panduit%20RGESDWS',
    # 'https://www.zoro.com/search?q=panduit%20MEHT187',
    # 'https://www.zoro.com/search?q=panduit%20META-X',

]

for url in mylist:
    try:
        l = l + 1
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        driver.get(url)
        driver.get(driver.current_url)
        # time.sleep(3)
        get_url = driver.current_url
        print("current = ", get_url)
        print("Products Urls", l, url)
        all_data = []
        all = driver.find_element(By.XPATH, "//ul[@class='product-identifiers pl-0 pb-2 product-specifications__identifiers my-4 pl-4']")
        data = all.find_elements(By.TAG_NAME, "li")
        for da in data:
            all_data.append(da.text)
        try:
            zoro = all_data[0]
        except:
            zoro = "Not Found"
            print("Not Found")
        try:
            mfr = all_data[1]
        except:
            mfr = "Not Found"
            print("Not Found")
        try:
            upc = all_data[2]
        except:
            upc = "Not Found"
            print("Not Found")

        print("zoro = ", zoro)
        print("mfr = ", mfr)
        print("upc = ", upc)
        save_details: TextIO = open("u.xlsx", "a+", encoding="utf-8")
        save_details.write("\n" + url + "\t" + get_url + "\t" + zoro + "\t" + mfr + "\t" + upc)
        save_details.close()
        print("\n ***** Record stored into upc  files. *****")

    except:
        save_details: TextIO = open("remaining_urlsu.xlsx", "a+", encoding="utf-8")
        save_details.write("\n" + url)
        save_details.close()
        print("\n ***** Record stored into upc  files. *****")
        print("Not Found")
