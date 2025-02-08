import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = True
driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
l = 0
Result = [

    # 'https://www.abilityone.com/spc-reg-high-traffic-series-sorbent-pad-roll/product/CM52973?recset=-3edf1204%3A185a99010fb%3A264-20',
    # 'https://www.abilityone.com/spc-reg-env-trade-maxx-enhanced-oil-only-sorbent-pads/product/CM52969?recset=-3edf1204%3A185a99010fb%3A264-20',
    # 'https://www.abilityone.com/spc-reg-gp-trade-maxx-enhanced-sorbent-pads/product/CM52972?recset=-3edf1204%3A185a99010fb%3A264-20',
    # 'https://www.abilityone.com/spc-reg-mro-plus-trade-sorbent-pads/product/CM52975?recset=-3edf1204%3A185a99010fb%3A264-20',
    # 'https://www.abilityone.com/cascade-reg-professional-fryer-boil-out/product/CM68690?recset=-3edf1204%3A185a99010fb%3A277-20',
    'https://www.abilityone.com/kess-lemon-d-dishwashing-liquid/product/CM49977?recset=-3edf1204%3A185a99010fb%3A277-20',
    # 'https://www.abilityone.com/diversey-trade-oxivir-reg-tb-one-step-disinfectant-cleaner/product/CM47134?recset=-3edf1204%3A185a99010fb%3A277-20',
    # 'https://www.abilityone.com/diversey-trade-emerel-reg-plus-cream-cleanser/product/CM62711?recset=-3edf1204%3A185a99010fb%3A277-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-wavebrake-reg-20-dirty-water-bucket/product/CM123710?recset=-3edf1204%3A185a99010fb%3A288-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-wavebrake-reg-bucket/product/CM50806?recset=-3edf1204%3A185a99010fb%3A288-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-microfiber-finish-bucket/product/CM50685?recset=-3edf1204%3A185a99010fb%3A288-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-wavebrake-reg-20-bucket/product/CM123709?recset=-3edf1204%3A185a99010fb%3A288-20',
    # 'https://www.abilityone.com/georgia-pacific-reg-professional-safe-t-gard-trade-half-fold-toilet-seat-covers/product/CM41542?recset=-3edf1204%3A185a99010fb%3A291-20',
    # 'https://www.abilityone.com/boardwalk-reg-jumbo-twin-toilet-tissue-dispenser/product/CM69671?recset=-3edf1204%3A185a99010fb%3A291-20',
    # 'https://www.abilityone.com/boardwalk-reg-standard-twin-toilet-tissue-dispenser/product/CM69662?recset=-3edf1204%3A185a99010fb%3A291-20',
    # 'https://www.abilityone.com/georgia-pacific-reg-professional-safe-t-gard-trade-toilet-seat-cover-dispenser/product/CM60108?recset=-3edf1204%3A185a99010fb%3A291-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-reg-resin-step-on-container/product/CM68013?recset=-3edf1204%3A185a99010fb%3A2a8-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-reg-stainless-steel-step-on-container/product/CM68099?recset=-3edf1204%3A185a99010fb%3A2a8-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-reg-confidential-document-waste-receptacle-with-lid/product/CM17494?recset=-3edf1204%3A185a99010fb%3A2a8-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-deskside-recycling-container/product/CM31200?recset=-3edf1204%3A185a99010fb%3A2a8-20',
    # 'https://www.abilityone.com/therapure-reg-tpp240m-hepa-type-air-purifier/product/CM63729?recset=-3edf1204%3A185a99010fb%3A2bf-20',
    # 'https://www.abilityone.com/therapure-reg-tpp230m-hepa-type-air-purifier/product/CM52862?recset=-3edf1204%3A185a99010fb%3A2bf-20',
    # 'https://www.abilityone.com/therapure-reg-tpp220m-hepa-type-air-purifier/product/CM63728?recset=-3edf1204%3A185a99010fb%3A2bf-20',
    # 'https://www.abilityone.com/aeramax-reg-air-purifiers/product/CM62148?recset=-3edf1204%3A185a99010fb%3A2bf-20',
    # 'https://www.abilityone.com/skilcraft-reg-meter-mist-refills/product/34515?recset=-3edf1204%3A185a99010fb%3A2d2-20',
    # 'https://www.abilityone.com/skilcraft-reg-zep-reg-meter-mist-3000-ultra-dispenser/product/34510?recset=-3edf1204%3A185a99010fb%3A2d2-20',
    # 'https://www.abilityone.com/fresh-products-fusion-metered-aerosols/product/CM49699?recset=-3edf1204%3A185a99010fb%3A2d2-20',
    # 'https://www.abilityone.com/refresh-air-freshener/product/3455?recset=-3edf1204%3A185a99010fb%3A2d2-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-deluxe-carry-caddy/product/CM50601?recset=-3edf1204%3A185a99010fb%3A2e3-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-executive-carry-caddy/product/CM64186?recset=-3edf1204%3A185a99010fb%3A2e3-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-caddy-bag/product/CM123983?recset=-3edf1204%3A185a99010fb%3A2e3-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-standard-brute-reg-rim-caddy/product/CM50768?recset=-3edf1204%3A185a99010fb%3A2e3-20',
    # 'https://www.abilityone.com/unger-reg-sanitary-brush/product/CM34515?recset=-3edf1204%3A185a99010fb%3A305-20',
    # 'https://www.abilityone.com/unger-reg-smartfit-trade-sanitary-brush/product/CM51253?recset=-3edf1204%3A185a99010fb%3A305-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-iron-shaped-handle-scrub-brush/product/CM50665?recset=-3edf1204%3A185a99010fb%3A305-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-synthetic-fill-tile-grout-brush/product/CM50783?recset=-3edf1204%3A185a99010fb%3A305-20',
    # 'https://www.abilityone.com/alera-reg-16-3-speed-oscillating-pedestal-fan/product/CM120346?recset=-3edf1204%3A185a99010fb%3A319-20',
    # 'https://www.abilityone.com/alera-reg-wall-mount-fan/product/CM122169?recset=-3edf1204%3A185a99010fb%3A319-20',
    # 'https://www.abilityone.com/alera-reg-3-speed-box-fan/product/CM122168?recset=-3edf1204%3A185a99010fb%3A319-20',
    # 'https://www.abilityone.com/alera-reg-12-3-speed-oscillating-desk-fan/product/CM70410?recset=-3edf1204%3A185a99010fb%3A319-20',
    # 'https://www.abilityone.com/skilcraft-reg-toilet-tissue/product/33510?recset=-3edf1204%3A185a99010fb%3A338-20',
    # 'https://www.abilityone.com/duck-sorb-reg-woolzorb-trade-pad/product/64090?recset=-3edf1204%3A185a99010fb%3A338-20',
    # 'https://www.abilityone.com/skilcraft-reg-urinal-screen-kit-with-non-para-block/product/310040?recset=-3edf1204%3A185a99010fb%3A338-20',
    # 'https://www.abilityone.com/duck-sorb-reg-wool-pillow/product/64075?recset=-3edf1204%3A185a99010fb%3A338-20',
    # 'https://www.abilityone.com/skilcraft-reg-laser-toner-cartridges-hp-compatible/product/212920?recset=-3edf1204%3A185a99010fb%3A373-20',
    # 'https://www.abilityone.com/hp-t0a38an-t6m14an-ink/product/CM71608?recset=-3edf1204%3A185a99010fb%3A373-20',
    # 'https://www.abilityone.com/innovera-reg-7970-inkjet-cartridge/product/CM23885?recset=-3edf1204%3A185a99010fb%3A373-20',
    # 'https://www.abilityone.com/innovera-reg-e285aj-toner/product/CM52389?recset=-3edf1204%3A185a99010fb%3A373-20',
    # 'https://www.abilityone.com/first-aid-only-trade-refill-for-smartcompliance-trade-general-business-cabinet/product/CM46071?recset=-3edf1204%3A185a99010fb%3A397-20',
    # 'https://www.abilityone.com/first-aid-only-trade-ansi-2015-compliant-first-aid-kit-refill/product/CM70278?recset=-3edf1204%3A185a99010fb%3A397-20',
    # 'https://www.abilityone.com/physicianscare-reg-by-first-aid-only-reg-first-aid-refill-components-eye-wash/product/CM29643?recset=-3edf1204%3A185a99010fb%3A397-20',
    # 'https://www.abilityone.com/first-aid-kit-field/product/62025?recset=-3edf1204%3A185a99010fb%3A397-20',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040?recset=-3edf1204%3A185a99010fb%3A3b6-20',
    # 'https://www.abilityone.com/boardwalk-reg-hand-sanitizer-gel/product/CM70342?recset=-3edf1204%3A185a99010fb%3A3b6-20',
    # 'https://www.abilityone.com/oasis-conditioning-shampoo/product/CM123432?recset=-3edf1204%3A185a99010fb%3A3b6-20',
    # 'https://www.abilityone.com/hand-cleaning-towelettes/product/81029?recset=-3edf1204%3A185a99010fb%3A3b6-20',
    # 'https://www.abilityone.com/accelerate-or-cr-kit/product/52510?recset=-3edf1204%3A185a99010fb%3A3d1-20',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040?recset=-3edf1204%3A185a99010fb%3A41e-20',
    # 'https://www.abilityone.com/boardwalk-reg-hand-sanitizer-gel/product/CM70342?recset=-3edf1204%3A185a99010fb%3A41e-20',
    # 'https://www.abilityone.com/stethoscope/product/5541?recset=-3edf1204%3A185a99010fb%3A41e-20',
    # 'https://www.abilityone.com/mcr-trade-safety-disposable-vinyl-gloves-5010xl/product/CM56958?recset=-3edf1204%3A185a99010fb%3A41e-20',
    # 'https://www.abilityone.com/alkaline-batteries/product/45515?recset=-3edf1204%3A185a99010fb%3A439-20',
    # 'https://www.abilityone.com/fellowes-reg-indoor-outdoor-heavy-duty-extension-cord/product/CM15914?recset=-3edf1204%3A185a99010fb%3A439-20',
    # 'https://www.abilityone.com/tripp-lite-protect-it-trade-seven-outlet-surge-suppressor/product/CM40472?recset=-3edf1204%3A185a99010fb%3A439-20',
    # 'https://www.abilityone.com/tripp-lite-power-strip-for-nonpatient-care-areas/product/CM67666?recset=-3edf1204%3A185a99010fb%3A439-20',
    # 'https://www.abilityone.com/avery-reg-page-size-heavyweight-three-hole-punched-sheet-protector/product/CM6719?recset=-3edf1204%3A185a99010fb%3A453-20',
    # 'https://www.abilityone.com/avery-reg-heavyweight-and-super-heavyweight-easy-load-non-glare-sheet-protector/product/CM6716?recset=-3edf1204%3A185a99010fb%3A453-20',
    # 'https://www.abilityone.com/avery-reg-touchguard-trade-protection-heavy-duty-view-binders-with-slant-rings/product/CM41523?recset=-3edf1204%3A185a99010fb%3A453-20',
    # 'https://www.abilityone.com/avery-reg-heavyweight-and-super-heavyweight-easy-load-diamond-clear-sheet-protector/product/CM6718?recset=-3edf1204%3A185a99010fb%3A453-20',
    # 'https://www.abilityone.com/appointment-planner-monthly/product/23012?recset=-3edf1204%3A185a99010fb%3A466-20',
    # 'https://www.abilityone.com/12-month-wall-calendars-wirebound/product/2305?recset=-3edf1204%3A185a99010fb%3A466-20',
    # 'https://www.abilityone.com/3-month-vertical-wall-calendar-wirebound/product/2306?recset=-3edf1204%3A185a99010fb%3A466-20',
    # 'https://www.abilityone.com/reversible-and-erasable-non-dated-90-120-day-flexible-planner/product/23045?recset=-3edf1204%3A185a99010fb%3A466-20',
    # 'https://www.abilityone.com/award-certificate-binder/product/22510?recset=-3edf1204%3A185a99010fb%3A484-20',
    # 'https://www.abilityone.com/c-line-reg-zip-n-go-trade-reusable-envelope-with-outer-pocket/product/CM47412?recset=-3edf1204%3A185a99010fb%3A484-20',
    # 'https://www.abilityone.com/case-logic-reg-16-laptop-backpack/product/CM71754?recset=-3edf1204%3A185a99010fb%3A484-20',
    # 'https://www.abilityone.com/case-logic-reg-primary-17-laptop-clamshell-case/product/CM122841?recset=-3edf1204%3A185a99010fb%3A484-20',
    # 'https://www.abilityone.com/sentry-reg-safe-hd2100-safe/product/CM123603?recset=-3edf1204%3A185a99010fb%3A496-20',
    # 'https://www.abilityone.com/sentry-reg-safe-waterproof-fire-resistant-file/product/CM65333?recset=-3edf1204%3A185a99010fb%3A496-20',
    # 'https://www.abilityone.com/mmf-industries-trade-fraudstopper-reg-tamper-evident-deposit-bags/product/CM17790?recset=-3edf1204%3A185a99010fb%3A496-20',
    # 'https://www.abilityone.com/mmf-industries-trade-freezfraud-tamper-evident-deposit-bags/product/CM42347?recset=-3edf1204%3A185a99010fb%3A496-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-photographic-learning-cards/product/CM40285?recset=-3edf1204%3A185a99010fb%3A4ab-20',
    # 'https://www.abilityone.com/chenille-kraft-reg-wonderfoam-reg-magnetic-alphabet-letters/product/CM24905?recset=-3edf1204%3A185a99010fb%3A4ab-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-chairback-buddy-pocket-chart/product/CM46996?recset=-3edf1204%3A185a99010fb%3A4ab-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-hundreds-pocket-chart/product/CM35200?recset=-3edf1204%3A185a99010fb%3A4ab-20',
    # 'https://www.abilityone.com/skilcraft-reg-westcott-reg-titanium-scissors/product/27020?recset=-3edf1204%3A185a99010fb%3A4c3-20',
    # 'https://www.abilityone.com/skilcraft-reg-westcott-reg-titanium-scissors-with-non-stick-blades/product/27025?recset=-3edf1204%3A185a99010fb%3A4c3-20',
    # 'https://www.abilityone.com/stainless-steel-shears/product/27010?recset=-3edf1204%3A185a99010fb%3A4c3-20',
    # 'https://www.abilityone.com/paper-trimmer/product/213230?recset=-3edf1204%3A185a99010fb%3A4c3-20',
    # 'https://www.abilityone.com/post-it-reg-flags-arrow-message-1-2-flags/product/CM12819?recset=-3edf1204%3A185a99010fb%3A4e6-20',
    # 'https://www.abilityone.com/post-it-reg-flags-small-flags/product/CM17503?recset=-3edf1204%3A185a99010fb%3A4e6-20',
    # 'https://www.abilityone.com/post-it-reg-flags-portable-flags/product/CM45286?recset=-3edf1204%3A185a99010fb%3A4e6-20',
    # 'https://www.abilityone.com/post-it-reg-flags-arrow-flags-in-a-desk-grip-dispenser/product/CM24164?recset=-3edf1204%3A185a99010fb%3A4e6-20',
    # 'https://www.abilityone.com/double-pocket-portfolio/product/290155?recset=-3edf1204%3A185a99010fb%3A50c-20',
    # 'https://www.abilityone.com/recycled-file-folders-processed-chlorine-free/product/290175?recset=-3edf1204%3A185a99010fb%3A50c-20',
    # 'https://www.abilityone.com/double-ply-recycled-file-folders-processed-chlorine-free/product/290160?recset=-3edf1204%3A185a99010fb%3A50c-20',
    # 'https://www.abilityone.com/reinforced-tab-top-file-folders/product/290201?recset=-3edf1204%3A185a99010fb%3A50c-20',
    # 'https://www.abilityone.com/saunders-cruiser-mate-reg-aluminum-storage-clipboard/product/CM22279?recset=-3edf1204%3A185a99010fb%3A525-20',
    # 'https://www.abilityone.com/saunders-snapak-reg-aluminum-side-open-forms-folder/product/CM5872?recset=-3edf1204%3A185a99010fb%3A525-20',
    # 'https://www.abilityone.com/saunders-slimmate-reg-storage-clipboard/product/CM32122?recset=-3edf1204%3A185a99010fb%3A525-20',
    # 'https://www.abilityone.com/universal-reg-storage-clipboard-with-pen-compartment/product/CM123503?recset=-3edf1204%3A185a99010fb%3A525-20',
    # 'https://www.abilityone.com/us-government-pen/product/14125?recset=-3edf1204%3A185a99010fb%3A546-20',
    # 'https://www.abilityone.com/stick-pen/product/14120?recset=-3edf1204%3A185a99010fb%3A546-20',
    # 'https://www.abilityone.com/framed-slant-d-ring-view-binder/product/2545?recset=-3edf1204%3A185a99010fb%3A546-20',
    # 'https://www.abilityone.com/quartet-reg-skilcraft-reg-total-erase-reg-white-board/product/2015125?recset=-3edf1204%3A185a99010fb%3A546-20',
    # 'https://www.abilityone.com/us-government-pen/product/14125?recset=-3edf1204%3A185a99010fb%3A563-20',
    # 'https://www.abilityone.com/skilcraft-reg-jaws-reg-just-add-water-system-cleaning-kit/product/3715?recset=-3edf1204%3A185a99010fb%3A563-20',
    # 'https://www.abilityone.com/insect-repellent-trash-bags/product/312525?recset=-3edf1204%3A185a99010fb%3A563-20',
    # 'https://www.abilityone.com/corrosion-preventative-compound-interior-protected/product/310530?recset=-3edf1204%3A185a99010fb%3A563-20',
    # 'https://www.abilityone.com/skilcraft-reg-toilet-tissue/product/33510?recset=-3edf1204%3A185a99010fb%3A594-20',
    # 'https://www.abilityone.com/duck-sorb-reg-woolzorb-trade-pad/product/64090?recset=-3edf1204%3A185a99010fb%3A594-20',
    # 'https://www.abilityone.com/skilcraft-reg-urinal-screen-kit-with-non-para-block/product/310040?recset=-3edf1204%3A185a99010fb%3A594-20',
    # 'https://www.abilityone.com/duck-sorb-reg-wool-pillow/product/64075?recset=-3edf1204%3A185a99010fb%3A594-20',
    # 'https://www.abilityone.com/spc-reg-high-traffic-series-sorbent-pad-roll/product/CM52973?recset=-3edf1204%3A185a99010fb%3A5c8-20',
    # 'https://www.abilityone.com/spc-reg-env-trade-maxx-enhanced-oil-only-sorbent-pads/product/CM52969?recset=-3edf1204%3A185a99010fb%3A5c8-20',
    # 'https://www.abilityone.com/spc-reg-gp-trade-maxx-enhanced-sorbent-pads/product/CM52972?recset=-3edf1204%3A185a99010fb%3A5c8-20',
    # 'https://www.abilityone.com/spc-reg-mro-plus-trade-sorbent-pads/product/CM52975?recset=-3edf1204%3A185a99010fb%3A5c8-20',
    # 'https://www.abilityone.com/cascade-reg-professional-fryer-boil-out/product/CM68690?recset=-3edf1204%3A185a99010fb%3A5ee-20',
    # 'https://www.abilityone.com/diversey-trade-oxivir-reg-tb-one-step-disinfectant-cleaner/product/CM47134?recset=-3edf1204%3A185a99010fb%3A5ee-20',
    # 'https://www.abilityone.com/kess-lemon-d-dishwashing-liquid/product/CM49977?recset=-3edf1204%3A185a99010fb%3A5ee-20',
    # 'https://www.abilityone.com/diversey-trade-emerel-reg-plus-cream-cleanser/product/CM62711?recset=-3edf1204%3A185a99010fb%3A5ee-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-wavebrake-reg-20-dirty-water-bucket/product/CM123710?recset=-3edf1204%3A185a99010fb%3A603-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-wavebrake-reg-bucket/product/CM50806?recset=-3edf1204%3A185a99010fb%3A603-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-microfiber-finish-bucket/product/CM50685?recset=-3edf1204%3A185a99010fb%3A603-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-wavebrake-reg-20-bucket/product/CM123709?recset=-3edf1204%3A185a99010fb%3A603-20',
    # 'https://www.abilityone.com/georgia-pacific-reg-professional-safe-t-gard-trade-half-fold-toilet-seat-covers/product/CM41542?recset=-3edf1204%3A185a99010fb%3A628-20',
    # 'https://www.abilityone.com/boardwalk-reg-jumbo-twin-toilet-tissue-dispenser/product/CM69671?recset=-3edf1204%3A185a99010fb%3A628-20',
    # 'https://www.abilityone.com/boardwalk-reg-standard-twin-toilet-tissue-dispenser/product/CM69662?recset=-3edf1204%3A185a99010fb%3A628-20',
    # 'https://www.abilityone.com/georgia-pacific-reg-professional-safe-t-gard-trade-toilet-seat-cover-dispenser/product/CM60108?recset=-3edf1204%3A185a99010fb%3A628-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-reg-resin-step-on-container/product/CM68013?recset=-3edf1204%3A185a99010fb%3A647-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-reg-stainless-steel-step-on-container/product/CM68099?recset=-3edf1204%3A185a99010fb%3A647-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-deskside-recycling-container/product/CM31200?recset=-3edf1204%3A185a99010fb%3A647-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-reg-confidential-document-waste-receptacle-with-lid/product/CM17494?recset=-3edf1204%3A185a99010fb%3A647-20',
    # 'https://www.abilityone.com/skilcraft-reg-meter-mist-refills/product/34515?recset=-3edf1204%3A185a99010fb%3A696-20',
    # 'https://www.abilityone.com/skilcraft-reg-zep-reg-meter-mist-3000-ultra-dispenser/product/34510?recset=-3edf1204%3A185a99010fb%3A696-20',
    # 'https://www.abilityone.com/fresh-products-fusion-metered-aerosols/product/CM49699?recset=-3edf1204%3A185a99010fb%3A696-20',
    # 'https://www.abilityone.com/refresh-air-freshener/product/3455?recset=-3edf1204%3A185a99010fb%3A696-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-deluxe-carry-caddy/product/CM50601?recset=-3edf1204%3A185a99010fb%3A6b0-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-executive-carry-caddy/product/CM64186?recset=-3edf1204%3A185a99010fb%3A6b0-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-caddy-bag/product/CM123983?recset=-3edf1204%3A185a99010fb%3A6b0-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-standard-brute-reg-rim-caddy/product/CM50768?recset=-3edf1204%3A185a99010fb%3A6b0-20',
    # 'https://www.abilityone.com/unger-reg-sanitary-brush/product/CM34515?recset=-3edf1204%3A185a99010fb%3A6cf-20',
    # 'https://www.abilityone.com/unger-reg-smartfit-trade-sanitary-brush/product/CM51253?recset=-3edf1204%3A185a99010fb%3A6cf-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-iron-shaped-handle-scrub-brush/product/CM50665?recset=-3edf1204%3A185a99010fb%3A6cf-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-synthetic-fill-tile-grout-brush/product/CM50783?recset=-3edf1204%3A185a99010fb%3A6cf-20',
    # 'https://www.abilityone.com/alera-reg-16-3-speed-oscillating-pedestal-fan/product/CM120346?recset=-3edf1204%3A185a99010fb%3A6ef-20',
    # 'https://www.abilityone.com/alera-reg-wall-mount-fan/product/CM122169?recset=-3edf1204%3A185a99010fb%3A6ef-20',
    # 'https://www.abilityone.com/alera-reg-3-speed-box-fan/product/CM122168?recset=-3edf1204%3A185a99010fb%3A6ef-20',
    # 'https://www.abilityone.com/alera-reg-12-3-speed-oscillating-desk-fan/product/CM70410?recset=-3edf1204%3A185a99010fb%3A6ef-20',
    # 'https://www.abilityone.com/skilcraft-reg-toilet-tissue/product/33510?recset=-3edf1204%3A185a99010fb%3A71b-20',
    # 'https://www.abilityone.com/duck-sorb-reg-woolzorb-trade-pad/product/64090?recset=-3edf1204%3A185a99010fb%3A71b-20',
    # 'https://www.abilityone.com/skilcraft-reg-urinal-screen-kit-with-non-para-block/product/310040?recset=-3edf1204%3A185a99010fb%3A71b-20',
    # 'https://www.abilityone.com/duck-sorb-reg-wool-pillow/product/64075?recset=-3edf1204%3A185a99010fb%3A71b-20',
    # 'https://www.abilityone.com/skilcraft-reg-laser-toner-cartridges-hp-compatible/product/212920?recset=-3edf1204%3A185a99010fb%3A739-20',
    # 'https://www.abilityone.com/hp-t0a38an-t6m14an-ink/product/CM71608?recset=-3edf1204%3A185a99010fb%3A739-20',
    # 'https://www.abilityone.com/innovera-reg-7970-inkjet-cartridge/product/CM23885?recset=-3edf1204%3A185a99010fb%3A739-20',
    # 'https://www.abilityone.com/hp-n9h57fn-cn684wn-ink/product/CM33350?recset=-3edf1204%3A185a99010fb%3A739-20',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040?recset=-3edf1204%3A185a99010fb%3A759-20',
    # 'https://www.abilityone.com/mcr-trade-safety-disposable-vinyl-gloves-5010xl/product/CM56958?recset=-3edf1204%3A185a99010fb%3A759-20',
    # 'https://www.abilityone.com/boardwalk-reg-hand-sanitizer-gel/product/CM70342?recset=-3edf1204%3A185a99010fb%3A759-20',
    # 'https://www.abilityone.com/hand-cleaning-towelettes/product/81029?recset=-3edf1204%3A185a99010fb%3A759-20',
    # 'https://www.abilityone.com/first-aid-only-trade-refill-for-smartcompliance-trade-general-business-cabinet/product/CM46071?recset=-3edf1204%3A185a99010fb%3A770-20',
    # 'https://www.abilityone.com/first-aid-only-trade-ansi-2015-compliant-first-aid-kit-refill/product/CM70278?recset=-3edf1204%3A185a99010fb%3A770-20',
    # 'https://www.abilityone.com/physicianscare-reg-by-first-aid-only-reg-first-aid-refill-components-eye-wash/product/CM29643?recset=-3edf1204%3A185a99010fb%3A770-20',
    # 'https://www.abilityone.com/first-aid-kit-field/product/62025?recset=-3edf1204%3A185a99010fb%3A770-20',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040?recset=-3edf1204%3A185a99010fb%3A78c-20',
    # 'https://www.abilityone.com/oasis-conditioning-shampoo/product/CM123432?recset=-3edf1204%3A185a99010fb%3A78c-20',
    # 'https://www.abilityone.com/boardwalk-reg-hand-sanitizer-gel/product/CM70342?recset=-3edf1204%3A185a99010fb%3A78c-20',
    # 'https://www.abilityone.com/gojo-reg-supro-max-trade-hand-cleaner/product/CM2270?recset=-3edf1204%3A185a99010fb%3A78c-20',
    # 'https://www.abilityone.com/accelerate-or-cr-kit/product/52510?recset=-3edf1204%3A185a99010fb%3A79b-20',
    # 'https://www.abilityone.com/boardwalk-reg-nitrile-flock-lined-gloves/product/CM11465?recset=-3edf1204%3A185a99010fb%3A7b3-20',
    # 'https://www.abilityone.com/kleenguard-trade-g40-nitrile-coated-gloves/product/CM44206?recset=-3edf1204%3A185a99010fb%3A7b3-20',
    # 'https://www.abilityone.com/first-aid-only-trade-smartcompliance-refill-finger-cots/product/CM72658?recset=-3edf1204%3A185a99010fb%3A7b3-20',
    # 'https://www.abilityone.com/boardwalk-reg-cow-split-leather-double-palm-gloves/product/CM72752?recset=-3edf1204%3A185a99010fb%3A7b3-20',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040?recset=-3edf1204%3A185a99010fb%3A7d5-20',
    # 'https://www.abilityone.com/boardwalk-reg-hand-sanitizer-gel/product/CM70342?recset=-3edf1204%3A185a99010fb%3A7d5-20',
    # 'https://www.abilityone.com/hand-cleaning-towelettes/product/81029?recset=-3edf1204%3A185a99010fb%3A7d5-20',
    # 'https://www.abilityone.com/mcr-trade-safety-disposable-vinyl-gloves-5010xl/product/CM56958?recset=-3edf1204%3A185a99010fb%3A7d5-20',
    # 'https://www.abilityone.com/us-government-pen/product/14125?recset=-3edf1204%3A185a99010fb%3A7e1-20',
    # 'https://www.abilityone.com/framed-slant-d-ring-view-binder/product/2545?recset=-3edf1204%3A185a99010fb%3A7e1-20',
    # 'https://www.abilityone.com/stick-pen/product/14120?recset=-3edf1204%3A185a99010fb%3A7e1-20',
    # 'https://www.abilityone.com/quartet-reg-skilcraft-reg-total-erase-reg-white-board/product/2015125?recset=-3edf1204%3A185a99010fb%3A7e1-20',
    # 'https://www.abilityone.com/alkaline-batteries/product/45515?recset=-3edf1204%3A185a99010fb%3A815-20',
    # 'https://www.abilityone.com/fellowes-reg-indoor-outdoor-heavy-duty-extension-cord/product/CM15914?recset=-3edf1204%3A185a99010fb%3A815-20',
    # 'https://www.abilityone.com/tripp-lite-protect-it-trade-seven-outlet-surge-suppressor/product/CM40472?recset=-3edf1204%3A185a99010fb%3A815-20',
    # 'https://www.abilityone.com/tripp-lite-power-strip-for-nonpatient-care-areas/product/CM67666?recset=-3edf1204%3A185a99010fb%3A815-20',
    # 'https://www.abilityone.com/avery-reg-page-size-heavyweight-three-hole-punched-sheet-protector/product/CM6719?recset=-3edf1204%3A185a99010fb%3A831-20',
    # 'https://www.abilityone.com/avery-reg-heavyweight-and-super-heavyweight-easy-load-non-glare-sheet-protector/product/CM6716?recset=-3edf1204%3A185a99010fb%3A831-20',
    # 'https://www.abilityone.com/avery-reg-touchguard-trade-protection-heavy-duty-view-binders-with-slant-rings/product/CM41523?recset=-3edf1204%3A185a99010fb%3A831-20',
    # 'https://www.abilityone.com/avery-reg-heavyweight-and-super-heavyweight-easy-load-diamond-clear-sheet-protector/product/CM6718?recset=-3edf1204%3A185a99010fb%3A831-20',
    # 'https://www.abilityone.com/appointment-planner-monthly/product/23012?recset=-3edf1204%3A185a99010fb%3A84e-20',
    # 'https://www.abilityone.com/12-month-wall-calendars-wirebound/product/2305?recset=-3edf1204%3A185a99010fb%3A84e-20',
    # 'https://www.abilityone.com/3-month-vertical-wall-calendar-wirebound/product/2306?recset=-3edf1204%3A185a99010fb%3A84e-20',
    # 'https://www.abilityone.com/reversible-and-erasable-non-dated-90-120-day-flexible-planner/product/23045?recset=-3edf1204%3A185a99010fb%3A84e-20',
    # 'https://www.abilityone.com/award-certificate-binder/product/22510?recset=-3edf1204%3A185a99010fb%3A872-20',
    # 'https://www.abilityone.com/case-logic-reg-16-laptop-backpack/product/CM71754?recset=-3edf1204%3A185a99010fb%3A872-20',
    # 'https://www.abilityone.com/c-line-reg-zip-n-go-trade-reusable-envelope-with-outer-pocket/product/CM47412?recset=-3edf1204%3A185a99010fb%3A872-20',
    # 'https://www.abilityone.com/pocket-padfolio/product/22520?recset=-3edf1204%3A185a99010fb%3A872-20',
    # 'https://www.abilityone.com/sentry-reg-safe-hd2100-safe/product/CM123603?recset=-3edf1204%3A185a99010fb%3A893-20',
    # 'https://www.abilityone.com/sentry-reg-safe-waterproof-fire-resistant-file/product/CM65333?recset=-3edf1204%3A185a99010fb%3A893-20',
    # 'https://www.abilityone.com/mmf-industries-trade-fraudstopper-reg-tamper-evident-deposit-bags/product/CM17790?recset=-3edf1204%3A185a99010fb%3A893-20',
    # 'https://www.abilityone.com/mmf-industries-trade-freezfraud-tamper-evident-deposit-bags/product/CM42347?recset=-3edf1204%3A185a99010fb%3A893-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-photographic-learning-cards/product/CM40285?recset=-3edf1204%3A185a99010fb%3A8ab-20',
    # 'https://www.abilityone.com/chenille-kraft-reg-wonderfoam-reg-magnetic-alphabet-letters/product/CM24905?recset=-3edf1204%3A185a99010fb%3A8ab-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-chairback-buddy-pocket-chart/product/CM46996?recset=-3edf1204%3A185a99010fb%3A8ab-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-hundreds-pocket-chart/product/CM35200?recset=-3edf1204%3A185a99010fb%3A8ab-20',
    # 'https://www.abilityone.com/skilcraft-reg-westcott-reg-titanium-scissors/product/27020?recset=-3edf1204%3A185a99010fb%3A8bc-20',
    # 'https://www.abilityone.com/skilcraft-reg-westcott-reg-titanium-scissors-with-non-stick-blades/product/27025?recset=-3edf1204%3A185a99010fb%3A8bc-20',
    # 'https://www.abilityone.com/stainless-steel-shears/product/27010?recset=-3edf1204%3A185a99010fb%3A8bc-20',
    # 'https://www.abilityone.com/paper-trimmer/product/213230?recset=-3edf1204%3A185a99010fb%3A8bc-20',
    # 'https://www.abilityone.com/post-it-reg-flags-arrow-message-1-2-flags/product/CM12819?recset=-3edf1204%3A185a99010fb%3A8e4-20',
    # 'https://www.abilityone.com/post-it-reg-flags-small-flags/product/CM17503?recset=-3edf1204%3A185a99010fb%3A8e4-20',
    # 'https://www.abilityone.com/post-it-reg-flags-portable-flags/product/CM45286?recset=-3edf1204%3A185a99010fb%3A8e4-20',
    # 'https://www.abilityone.com/post-it-reg-flags-arrow-flags-in-a-desk-grip-dispenser/product/CM24164?recset=-3edf1204%3A185a99010fb%3A8e4-20',
    # 'https://www.abilityone.com/double-pocket-portfolio/product/290155?recset=-3edf1204%3A185a99010fb%3A909-20',
    # 'https://www.abilityone.com/recycled-file-folders-processed-chlorine-free/product/290175?recset=-3edf1204%3A185a99010fb%3A909-20',
    # 'https://www.abilityone.com/double-ply-recycled-file-folders-processed-chlorine-free/product/290160?recset=-3edf1204%3A185a99010fb%3A909-20',
    # 'https://www.abilityone.com/reinforced-tab-top-file-folders/product/290201?recset=-3edf1204%3A185a99010fb%3A909-20',
    # 'https://www.abilityone.com/saunders-cruiser-mate-reg-aluminum-storage-clipboard/product/CM22279?recset=-3edf1204%3A185a99010fb%3A920-20',
    # 'https://www.abilityone.com/saunders-snapak-reg-aluminum-side-open-forms-folder/product/CM5872?recset=-3edf1204%3A185a99010fb%3A920-20',
    # 'https://www.abilityone.com/saunders-slimmate-reg-storage-clipboard/product/CM32122?recset=-3edf1204%3A185a99010fb%3A920-20',
    # 'https://www.abilityone.com/universal-reg-storage-clipboard-with-pen-compartment/product/CM123503?recset=-3edf1204%3A185a99010fb%3A920-20',
    # 'https://www.abilityone.com/us-government-pen/product/14125?recset=-3edf1204%3A185a99010fb%3A941-20',
    # 'https://www.abilityone.com/framed-slant-d-ring-view-binder/product/2545?recset=-3edf1204%3A185a99010fb%3A941-20',
    # 'https://www.abilityone.com/stick-pen/product/14120?recset=-3edf1204%3A185a99010fb%3A941-20',
    # 'https://www.abilityone.com/clean-click-trade-/product/1450?recset=-3edf1204%3A185a99010fb%3A941-20',

]

for url in Result:
    try:
        l += 1
        driver.get(url)
        time.sleep(5)
        print("Table Urls === ", l, url)

        item_d = []
        try:
            print("*********************************** Item: **************************************")
            item = driver.find_element(By.XPATH, '//*[@id="pdp_prodInfo"]/div/p[1]')
            item_d = item.text.strip()
            print("item_n1 = ", item_d)
        except:
            item_n1_d = "Not Found"
            print("item_n1 = ", item_n1_d)
        print(" ******************* singal click *********************")
        click_b = driver.find_elements(By.CSS_SELECTOR, "#headingThree > h4 > button")
        for x in click_b:
            x.send_keys("\n")
            time.sleep(3)
            button = x.find_element(By.XPATH, '//*[@id="collapseThree"]')
            print(button.text)
            attr_name1 = button.text.split('\n')
            for value1 in attr_name1:
                attr_name_new1 = value1.split(':')
                e = (attr_name_new1[0])
                f = (attr_name_new1[1:])
                print("specs1 e = ", e)
                print("specs1 f = ", f)

                save_details: TextIO = open("table_data1.xlsx", "a+", encoding="utf-8")
                save_details.write("\n" + url + "\t" + item_d + "\t" + e + "\t" + "rp_"+''.join(f))
                print("End")
                save_details.close()
                print("\n ***** Record stored into Table Specifications 1 . *****")
#
    except Exception as e:
        print(e)

