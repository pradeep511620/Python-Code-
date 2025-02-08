import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
mylist = [
    'https://www.usnetting.com/fence/rolls/',
]
for url in mylist:
    driver.get(url)
    time.sleep(3)
    url_link = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]").find_elements(By.TAG_NAME,
                                                                                                           "a")
    for url_l in url_link:
        print(url_l.get_attribute('href'))
# Done Scripts of urls
done = [

    # two click image only

    'https://www.usnetting.com/barrier-netting/ez-barrier-nets/',  # svg click and image

    # No click Done
    'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-12-175/',
    'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-120-350/',
    'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-21-075/',
    'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-21-175/',
    'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-30-400/',
    'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-84-200/',
    'https://www.usnetting.com/fence/deer-fence/standard-duty-plastic-deer-fence/',

    # Number click and images Done
    'https://www.usnetting.com/fence/safety-fence/economy-plastic-safety-fence/',
    'https://www.usnetting.com/fence/safety-fence/heavy-duty-plastic-safety-fence/',
    'https://www.usnetting.com/fence/safety-fence/privacy-screen/',
    'https://www.usnetting.com/fence/snow-fence/heavy-duty-plastic-snow-fence/',
    'https://www.usnetting.com/fence/snow-fence/economy-plastic-snow-fence/',

    # Number click Done
    'https://www.usnetting.com/fence/safety-fence/guardrail-safety-netting/',
    'https://www.usnetting.com/fence/snow-fence/studded-steel-t-post/',
    'https://www.usnetting.com/safety-netting/guardrail-netting/',
    'https://www.usnetting.com/safety-netting/conveyor-netting/heavy-duty-conveyor-netting-w-debris-liner/',
    'https://www.usnetting.com/safety-netting/conveyor-netting/heavy-duty-conveyor-netting/',
    'https://www.usnetting.com/safety-netting/conveyor-netting/light-duty-conveyor-netting/',
    'https://www.usnetting.com/safety-solutions/wall-mounted-safety-nets/48-inch-tall-loading-dock-safety-net-with-debris-liner/',
    'https://www.usnetting.com/safety-solutions/wall-mounted-safety-nets/48-inch-tall-loading-dock-safety-net/',
    'https://www.usnetting.com/safety-solutions/wall-mounted-safety-nets/72-inch-tall-loading-dock-safety-net/',

    # No click number Done
    'https://www.usnetting.com/safety-netting/construction/temporary-fence/standard-duty-folded-temporary-fence/',
    'https://www.usnetting.com/safety-netting/construction/temporary-fence/heavy-duty-temporary-fence/',
    'https://www.usnetting.com/fence/snow-fence/fence-post-driver/',
    'https://www.usnetting.com/fence/snow-fence/sod-staples/',
    'https://www.usnetting.com/fence/snow-fence/t-post-puller/',
    'https://www.usnetting.com/fence/snow-fence/wooden-snow-fence/',
    'https://www.usnetting.com/hardware/bungee-clips/',
    'https://www.usnetting.com/hardware/hook-and-barrel-bungee-cord/',
    'https://www.usnetting.com/hardware/scaffold-clips/',
    'https://www.usnetting.com/hardware/secure-clips/',
    'https://www.usnetting.com/hardware/snaphooks/',
    'https://www.usnetting.com/hardware/stainless-steel-zip-ties/',


    'https://www.usnetting.com/safety-netting/debris-netting/heavy-duty-debris-netting-panels/',
    'https://www.usnetting.com/safety-netting/debris-netting/standard-duty-debris-netting-panels/',

    # number and images click
    'https://www.usnetting.com/safety-netting/debris-netting/rolls/heavy-duty-fire-retardant-debris-netting-roll/',
    'https://www.usnetting.com/safety-netting/debris-netting/rolls/standard-duty-fire-retardant-debris-netting-roll/',

    'https://www.usnetting.com/safety-netting/fall-safety-netting/',

    'https://www.usnetting.com/metal-netting/steel-chain-net/',



    # done 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/aluminet/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/black/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/blue/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/green/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/red/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/tan/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/white/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/',
    # 'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/aluminet/',
    # 'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/black/',
    # 'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/blue/',
    # 'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/green/',
    # 'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/red/',
    # 'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/tan/',
    # 'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/white/',done

    # Done 'https://www.usnetting.com/sports-netting/camo-netting/desert/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/flyway/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/greenbrown/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/killer/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/night/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/realtree/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/snow/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/urban/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/woodland/',
    # 'https://www.usnetting.com/sports-netting/custom-sports-netting/',
    # 'https://www.usnetting.com/sports-netting/golf-netting/golf-cages/',

]
