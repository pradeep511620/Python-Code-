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
    # 'https://www.abilityone.com/led-t8-tube-light/product/45055',
    # 'https://www.abilityone.com/covidien-in-room-locking-wall-mount-sharps-container-cabinet-system/product/CM72593',
    # 'https://www.abilityone.com/hospeco-reg-double-entry-swing-top-floor-receptacle/product/CM35591',
    # 'https://www.abilityone.com/hospeco-reg-feminine-hygiene-product-waste-receptacle/product/CM60113',
    # 'https://www.abilityone.com/hospeco-reg-wall-mount-sanitary-napkin-receptacle/product/CM9053',
    # 'https://www.abilityone.com/rolodex-trade-mesh-round-wastebasket/product/CM16286',
    # 'https://www.abilityone.com/refresh-air-freshener/product/3455',
    # 'https://www.abilityone.com/skilcraft-reg-meter-mist-refills/product/34515',
    # 'https://www.abilityone.com/skilcraft-reg-zep-reg-meter-mist-3000-ultra-dispenser/product/34510',
    # 'https://www.abilityone.com/air-wick-reg-aerosol-air-freshener/product/CM62354',
    # 'https://www.abilityone.com/air-wick-reg-essential-mist-refill/product/CM121862',
    # 'https://www.abilityone.com/air-wick-reg-essential-mist-starter-kit/product/CM121882',
    # 'https://www.abilityone.com/air-wick-reg-freshmatic-reg-life-scents-trade-ultra-refill/product/CM68102',
    # 'https://www.abilityone.com/air-wick-reg-freshmatic-reg-ultra-automatic-pure-refill/product/CM119644',
    # 'https://www.abilityone.com/air-wick-reg-freshmatic-reg-ultra-automatic-spray-refills/product/CM29418',
    # 'https://www.abilityone.com/air-wick-reg-life-scents-trade-scented-oil-refills/product/CM67983',
    # 'https://www.abilityone.com/air-wick-reg-scented-oil-refill/product/CM45754',
    # 'https://www.abilityone.com/air-wick-reg-scented-oil-warmer/product/CM63816',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-brute-reg-caddy-bag/product/CM8615',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-deluxe-carry-caddy/product/CM50601',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-executive-carry-caddy/product/CM64186',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-maid-caddy/product/CM50677',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-caddy-bag/product/CM123983',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-standard-brute-reg-rim-caddy/product/CM50768',
    # 'https://www.abilityone.com/boardwalk-reg-counter-brush/product/CM48988',
    # 'https://www.abilityone.com/boardwalk-reg-dual-surface-scrub-brush/product/CM48997',
    # 'https://www.abilityone.com/boardwalk-reg-dual-surface-vehicle-brush/product/CM48998',
    # 'https://www.abilityone.com/boardwalk-reg-grout-brush/product/CM44560',
    # 'https://www.abilityone.com/boardwalk-reg-polystyrene-vehicle-brush/product/CM12062',
    # 'https://www.abilityone.com/boardwalk-reg-scrub-brush/product/CM49036',
    # 'https://www.abilityone.com/boardwalk-reg-utility-brush/product/CM49046',
    # 'https://www.abilityone.com/carlisle-flo-pac-reg-utility-toothbrush-style-maintenance-brush/product/CM200220',
    # 'https://www.abilityone.com/carlisle-sparta-reg-handle-bottle-brush/product/CM63817',
    # 'https://www.abilityone.com/carlisle-reg-counter-radiator-brush/product/CM64242',
    # 'https://www.abilityone.com/o-cedar-reg-commercial-bi-level-floor-scrub-brush/product/CM68021',
    # 'https://www.abilityone.com/read-right-reg-tape-head-kleen-pad-trade-/product/CM13287',
    # 'https://www.abilityone.com/alera-reg-12-3-speed-oscillating-desk-fan/product/CM70410',
    # 'https://www.abilityone.com/alera-reg-16-3-speed-oscillating-pedestal-fan/product/CM120346',
    # 'https://www.abilityone.com/alera-reg-3-speed-box-fan/product/CM122168',
    # 'https://www.abilityone.com/honeywell-quietset-personal-table-fan/product/CM69960',
    # 'https://www.abilityone.com/honeywell-quietset-whole-room-tower-fan/product/CM120265',
    # 'https://www.abilityone.com/clc-controlled-life-cycle-plastic-bags/product/312510',
    # 'https://www.abilityone.com/trc-total-recycled-content-bag/product/312565',
    # 'https://www.abilityone.com/100-cotton-absorbent-towel/product/3305',
    # 'https://www.abilityone.com/100-cotton-dust-mop-head/product/35150',
    # 'https://www.abilityone.com/3-mat-entry-system-scraper-finger-tip/product/31105',
    # 'https://www.abilityone.com/3-mat-entry-system-scraper-loop-pile/product/311010',
    # 'https://www.abilityone.com/3-mat-entry-system-scraper-wiper-100-recycled/product/311015',
    # 'https://www.abilityone.com/3-mat-entry-system-scraper-wiper-vinyl-loop/product/311020',
    # 'https://www.abilityone.com/3-mat-entry-system-wiper/product/311025',
    # 'https://www.abilityone.com/3m-trade-twist-n-fill-bathroom-cleaner-4l/product/3955',
    # 'https://www.abilityone.com/3m-trade-twist-n-fill-bathroom-cleaner-non-acid-15l/product/39510',
    # 'https://www.abilityone.com/3m-trade-twist-n-fill-deodorizer/product/39515',
    # 'https://www.abilityone.com/remanufactured-toner-cartridges-hp-series/product/212935',
    # 'https://www.abilityone.com/skilcraft-reg-laser-toner-cartridges-hp-compatible/product/212920',
    # 'https://www.abilityone.com/skilcraft-reg-laser-toner-cartridges-hp-compatible/product/212920',
    # 'https://www.abilityone.com/skilcraft-reg-laser-toner-cartridges-hp-compatible/product/212920',
    # 'https://www.abilityone.com/brother-brtlc3011bkbrtlc3011cbrtlc3011mbrtlc3011y-ink-cartridge/product/CM123111',
    # 'https://www.abilityone.com/brother-brttn210bk-brttn210c-brttn210m-brttn210y-toner/product/CM39098',
    # 'https://www.abilityone.com/brother-lc101bk-lc101c-lc101m-lc101y-lc1013pks-ink/product/CM61905',
    # 'https://www.abilityone.com/brother-lc1033pks-ink/product/CM59812',
    # 'https://www.abilityone.com/brother-lc103bk-lc103c-lc103m-lc103y-lc1032pks-lc1033pks-ink/product/CM61906',
    # 'https://www.abilityone.com/brother-lc103bk-lc107bk-ink/product/CM55481',
    # 'https://www.abilityone.com/brother-lc109bk-ink/product/CM61907',
    # 'https://www.abilityone.com/brother-lc10ebk-lc10ec-lc10em-lc10ey-ink/product/CM68612',
    # 'https://www.abilityone.com/brother-lc2013pks-lc201bk-lc201m-lc201y-ink/product/CM68595',
    # 'https://www.abilityone.com/brother-lc2033pks-lc205y-ink/product/CM64885',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040',
    # 'https://www.abilityone.com/better-touch-trade-hot-cold-therapy-packs/product/5545',
    # 'https://www.abilityone.com/biobased-liquid-hand-soap/product/855',
    # 'https://www.abilityone.com/body-fluids-barrier-kit/product/5570',
    # 'https://www.abilityone.com/comb/product/81025',
    # 'https://www.abilityone.com/cotton-tip-applicator/product/5520',
    # 'https://www.abilityone.com/first-aid-kit-15-person/product/62035',
    # 'https://www.abilityone.com/first-aid-kit-50-person/product/62040',
    # 'https://www.abilityone.com/first-aid-kit-8-person/product/62030',
    # 'https://www.abilityone.com/first-aid-kit-emergency-first-response/product/62045',
    # 'https://www.abilityone.com/first-aid-kit-field/product/62025',
    # 'https://www.abilityone.com/first-aid-kit-general-purpose-small-office/product/62015',
    # 'https://www.abilityone.com/better-touch-trade-hot-cold-therapy-packs/product/5545',
    # 'https://www.abilityone.com/body-fluids-barrier-kit/product/5570',
    # 'https://www.abilityone.com/cotton-tip-applicator/product/5520',
    # 'https://www.abilityone.com/first-aid-kit-15-person/product/62035',
    # 'https://www.abilityone.com/first-aid-kit-50-person/product/62040',
    # 'https://www.abilityone.com/first-aid-kit-8-person/product/62030',
    # 'https://www.abilityone.com/first-aid-kit-emergency-first-response/product/62045',
    # 'https://www.abilityone.com/first-aid-kit-field/product/62025',
    # 'https://www.abilityone.com/first-aid-kit-general-purpose-small-office/product/62015',
    # 'https://www.abilityone.com/first-aid-kit-individual/product/6205',
    # 'https://www.abilityone.com/first-aid-kit-industrial-construction/product/62050',
    # 'https://www.abilityone.com/first-aid-kit-office/product/62010',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040',
    # 'https://www.abilityone.com/biobased-liquid-hand-soap/product/855',
    # 'https://www.abilityone.com/comb/product/81025',
    # 'https://www.abilityone.com/gojo-reg-skilcraft-reg-antibacterial-foam-handwash/product/8515',
    # 'https://www.abilityone.com/gojo-reg-skilcraft-reg-citrus-ginger-foam-hand-shower-wash/product/8520',
    # 'https://www.abilityone.com/gojo-reg-skilcraft-reg-citrus-ginger-foam-hand-shower-wash/product/8520',
    # 'https://www.abilityone.com/gojo-reg-skilcraft-reg-citrus-ginger-foam-hand-shower-wash/product/8520',
    # 'https://www.abilityone.com/gojo-reg-skilcraft-reg-dispenser/product/8555',
    # 'https://www.abilityone.com/gojo-reg-skilcraft-reg-fmx-dispenser/product/8560',
    # 'https://www.abilityone.com/gojo-reg-skilcraft-reg-green-certified-foam-hand-cleaner/product/8524',
    # 'https://www.abilityone.com/gojo-reg-skilcraft-reg-lotion-hand-soap/product/8530',
    # 'https://www.abilityone.com/gojo-reg-skilcraft-reg-ltx-12-reg-foam-hand-wash-refill/product/8535',
    # 'https://www.abilityone.com/gojo-reg-skilcraft-reg-luxury-foam-antibacterial-handwash/product/8540',
    # 'https://www.abilityone.com/gojo-reg-skilcraft-reg-mild-hand-soap-pump-bottle/product/8545',
    # 'https://www.abilityone.com/ansellpro-conform-reg-natural-rubber-latex-gloves/product/CM32655',
    # 'https://www.abilityone.com/ansellpro-dura-touch-reg-pvc-gloves/product/CM32656',
    # 'https://www.abilityone.com/ansellpro-golden-grab-it-reg-ii-heavy-duty-multipurpose-gloves/product/CM53166',
    # 'https://www.abilityone.com/ansellpro-hyflex-reg-cr-gloves/product/CM53918',
    # 'https://www.abilityone.com/ansellpro-hyflex-reg-foam-nitrile-coated-nylon-knit-gloves/product/CM48870',
    # 'https://www.abilityone.com/ansellpro-hyflex-reg-kevlar-reg-work-gloves/product/CM52047',
    # 'https://www.abilityone.com/ansellpro-hynit-reg-nitrile-gloves/product/CM200546',
    # 'https://www.abilityone.com/ansellpro-powerflex-reg-multi-purpose-gloves/product/CM52916',
    # 'https://www.abilityone.com/ansellpro-scorpio-reg-neoprene-gloves/product/CM52917',
    # 'https://www.abilityone.com/boardwalk-reg-black-pu-palm-coated-gloves/product/CM72749',
    # 'https://www.abilityone.com/boardwalk-reg-flock-lined-latex-cleaning-gloves/product/CM15556',
    # 'https://www.abilityone.com/boardwalk-reg-neoprene-flock-lined-gloves/product/CM49023',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040',
    # 'https://www.abilityone.com/better-touch-trade-hot-cold-therapy-packs/product/5545',
    # 'https://www.abilityone.com/biobased-liquid-hand-soap/product/855',
    # 'https://www.abilityone.com/body-fluids-barrier-kit/product/5570',
    # 'https://www.abilityone.com/comb/product/81025',
    # 'https://www.abilityone.com/cotton-tip-applicator/product/5520',
    # 'https://www.abilityone.com/first-aid-kit-15-person/product/62035',
    # 'https://www.abilityone.com/first-aid-kit-50-person/product/62040',
    # 'https://www.abilityone.com/first-aid-kit-8-person/product/62030',
    # 'https://www.abilityone.com/first-aid-kit-emergency-first-response/product/62045',
    # 'https://www.abilityone.com/first-aid-kit-field/product/62025',
    # 'https://www.abilityone.com/first-aid-kit-general-purpose-small-office/product/62015',
    # 'https://www.abilityone.com/sign-here-self-stick-flags/product/210630',
    # 'https://www.abilityone.com/while-you-were-out-message-pad/product/210905',
    # 'https://www.abilityone.com/12-marker-dry-erase-system/product/11220',
    # 'https://www.abilityone.com/12-month-wall-calendars-wirebound/product/2305',
    # 'https://www.abilityone.com/2-hole-punch/product/213205',
    # 'https://www.abilityone.com/3-hole-punch-heavy-duty/product/213210',
    # 'https://www.abilityone.com/3-hole-punch-medium-duty/product/213215',
    # 'https://www.abilityone.com/3-in-1-freedom-liberty-collection/product/175',
    # 'https://www.abilityone.com/3-month-vertical-wall-calendar-wirebound/product/2306',
    # 'https://www.abilityone.com/3-month-vertical-wall-calendar-wirebound/product/2306',
    # 'https://www.abilityone.com/3-month-vertical-wall-calendar-wirebound/product/2306',
    # 'https://www.abilityone.com/3-ring-flexible-binder/product/2510',
    # 'https://www.abilityone.com/3-ring-flexible-binder/product/2510',
    # 'https://www.abilityone.com/3-ring-flexible-poly-binder/product/2515',
    # 'https://www.abilityone.com/4-piece-stamp-kit/product/212015',
    # 'https://www.abilityone.com/alkaline-batteries/product/45515',
    # 'https://www.abilityone.com/belkin-reg-pivot-plug-surge-protector/product/CM554',
    # 'https://www.abilityone.com/belkin-reg-professional-series-surgemaster-surge-protector/product/CM24046',
    # 'https://www.abilityone.com/belkin-reg-six-outlet-power-strip/product/CM121685',
    # 'https://www.abilityone.com/belkin-reg-surgeplus-trade-usb-wall-mount-charger/product/CM72580',
    # 'https://www.abilityone.com/dorcy-reg-led-flashlight-pack/product/CM124065',
    # 'https://www.abilityone.com/energizer-reg-led-pen-light/product/CM15208',
    # 'https://www.abilityone.com/fellowes-reg-indoor-outdoor-heavy-duty-extension-cord/product/CM15914',
    # 'https://www.abilityone.com/fellowes-reg-seven-outlet-metal-power-strip/product/CM12747',
    # 'https://www.abilityone.com/fellowes-reg-ten-outlet-power-guard-surge-protector/product/CM12120',
    # 'https://www.abilityone.com/ge-dimmable-halogen-a-line-bulb/product/CM41695',
    # 'https://www.abilityone.com/ge-incandescent-reveal-reg-br30-light-bulb/product/CM124007',
    # 'https://www.abilityone.com/case-bound-3-ring-binders/product/2525',
    # 'https://www.abilityone.com/equipment-record-folder/product/2570',
    # 'https://www.abilityone.com/flight-crew-check-binder/product/2575',
    # 'https://www.abilityone.com/framed-slant-d-ring-view-binder/product/2545',
    # 'https://www.abilityone.com/index-maker-reg-dividers/product/2105',
    # 'https://www.abilityone.com/index-sheet-sets/product/21020',
    # 'https://www.abilityone.com/legal-divider-numerical-tabs/product/21025',
    # 'https://www.abilityone.com/long-format-check-list-binder/product/2580',
    # 'https://www.abilityone.com/multiple-index-sheets/product/21010',
    # 'https://www.abilityone.com/round-ring-view-binders/product/2535',
    # 'https://www.abilityone.com/12-month-wall-calendars-wirebound/product/2305',
    # 'https://www.abilityone.com/3-month-vertical-wall-calendar-wirebound/product/2306',
    # 'https://www.abilityone.com/appointment-planner-monthly/product/23012',
    # 'https://www.abilityone.com/appointment-planner-weekly/product/23011',
    # 'https://www.abilityone.com/calendar-pad-stand/product/23025',
    # 'https://www.abilityone.com/calendar-wall-board/product/23055',
    # 'https://www.abilityone.com/erasable-custom-wall-calendar/product/23030',
    # 'https://www.abilityone.com/in-out-erasable-scheduler/product/23035',
    # 'https://www.abilityone.com/reversible-and-erasable-non-dated-30-60-day-flexible-planner/product/23040',
    # 'https://www.abilityone.com/reversible-and-erasable-non-dated-90-120-day-flexible-planner/product/23045',
    # 'https://www.abilityone.com/at-a-glance-reg-today-is-daily-wall-calendar-refill/product/CM35845',
    # 'https://www.abilityone.com/at-a-glance-reg-today-is-wall-calendar/product/CM13975',
    # 'https://www.abilityone.com/acu-digital-camo-leadership-record-book-cover/product/22521',
    # 'https://www.abilityone.com/award-certificate-binder/product/22510',
    # 'https://www.abilityone.com/pocket-padfolio/product/22520',
    # 'https://www.abilityone.com/vinyl-steno-pad-holder/product/22535',
    # 'https://www.abilityone.com/writing-portfolio/product/22540',
    # 'https://www.abilityone.com/writing-portfolio-economy/product/22550',
    # 'https://www.abilityone.com/writing-portfolio-deluxe-with-brass-clip/product/22545',
    # 'https://www.abilityone.com/advantus-clear-pencil-box/product/CM30142',
    # 'https://www.abilityone.com/advantus-super-stacker-reg-crayon-box/product/CM66287',
    # 'https://www.abilityone.com/advantus-super-stacker-reg-large-pencil-box/product/CM71819',
    # 'https://www.abilityone.com/advantus-super-stacker-reg-pencil-box/product/CM66286',
    # 'https://www.abilityone.com/boogie-board-trade-blackboard-folio/product/CM123911',
    # 'https://www.abilityone.com/bates-reg-tally-i-hand-model-counter/product/CM5523',
    # 'https://www.abilityone.com/bates-reg-tally-ii-desk-model-counter/product/CM5522',
    # 'https://www.abilityone.com/dri-mark-reg-counterfeit-money-detection-system/product/CM9141',
    # 'https://www.abilityone.com/dri-mark-reg-smart-money-reg-pen/product/CM24832',
    # 'https://www.abilityone.com/dri-mark-reg-tri-test-counterfeit-bill-detector/product/CM55068',
    # 'https://www.abilityone.com/fireking-reg-depository-security-safe/product/CM120417',
    # 'https://www.abilityone.com/fireking-reg-small-personal-safe/product/CM10058',
    # 'https://www.abilityone.com/max-electronic-checkwriter/product/CM33618',
    # 'https://www.abilityone.com/mmf-industries-trade-bill-strap-rack/product/CM40986',
    # 'https://www.abilityone.com/pap-r-products-automatic-coin-rolls/product/CM14506',
    # 'https://www.abilityone.com/pap-r-products-currency-straps/product/CM18215',
    # 'https://www.abilityone.com/pap-r-products-flat-coin-wrappers/product/CM15540',
    # 'https://www.abilityone.com/baumgartens-reg-shaped-timer/product/CM43626',
    # 'https://www.abilityone.com/c-line-reg-reusable-dry-erase-pockets/product/CM55135',
    # 'https://www.abilityone.com/carson-dellosa-publishing-adjustable-tri-section-chart/product/CM35201',
    # 'https://www.abilityone.com/carson-dellosa-publishing-chairback-buddy-pocket-chart/product/CM46996',
    # 'https://www.abilityone.com/carson-dellosa-publishing-deluxe-scheduling-pocket-chart/product/CM35208',
    # 'https://www.abilityone.com/carson-dellosa-publishing-ez-spin/product/CM122958',
    # 'https://www.abilityone.com/carson-dellosa-publishing-hundreds-pocket-chart/product/CM35200',
    # 'https://www.abilityone.com/carson-dellosa-publishing-storage-pocket-chart/product/CM35222',
    # 'https://www.abilityone.com/champion-sports-dual-timer-clock/product/CM9454',
    # 'https://www.abilityone.com/charles-leonard-dry-erase-pocket-class-pack/product/CM72615',
    # 'https://www.abilityone.com/chenille-kraft-reg-wonderfoam-reg-magnetic-alphabet-letters/product/CM24905',
    # 'https://www.abilityone.com/creativity-street-reg-wonderfoam-reg-early-learning/product/CM123028',
    # 'https://www.abilityone.com/hot-forged-carbon-steel-shears/product/27005',
    # 'https://www.abilityone.com/paper-trimmer/product/213230',
    # 'https://www.abilityone.com/skilcraft-reg-westcott-reg-titanium-scissors/product/27020',
    # 'https://www.abilityone.com/skilcraft-reg-westcott-reg-titanium-scissors-with-non-stick-blades/product/27025',
    # 'https://www.abilityone.com/stainless-steel-shears/product/27010',
    # 'https://www.abilityone.com/straight-trimmers-shears/product/27015',
    # 'https://www.abilityone.com/astrodesigns-reg-pre-printed-paper/product/CM122953',
    # 'https://www.abilityone.com/avery-reg-fabric-transfers/product/CM16720',
    # 'https://www.abilityone.com/bates-reg-numbering-machine-ink/product/CM36523',
    # 'https://www.abilityone.com/boardwalk-reg-easy-grip-tape-measure/product/CM122749',
    # 'https://www.abilityone.com/carson-dellosa-publishing-border-storage-pocket-chart/product/CM8586',
    # 'https://www.abilityone.com/champion-sports-alphabet-bean-bag-set/product/CM6397',
    # 'https://www.abilityone.com/while-you-were-out-message-pad/product/210905',
    # 'https://www.abilityone.com/executive-message-recording-pad/product/210910',
    # 'https://www.abilityone.com/3m-trade-adjustable-height-monitor-stand/product/CM8219',
    # 'https://www.abilityone.com/3m-trade-adjustable-monitor-stand/product/CM70606',
    # 'https://www.abilityone.com/3m-trade-adjustable-notebook-riser/product/CM40729',
    # 'https://www.abilityone.com/3m-trade-desktop-document-holder/product/CM9314',
    # 'https://www.abilityone.com/3m-trade-extra-wide-adjustable-monitor-stand/product/CM24798',
    # 'https://www.abilityone.com/3m-trade-in-line-document-holder/product/CM15894',
    # 'https://www.abilityone.com/3m-trade-monitor-whiteboard/product/CM122779',
    # 'https://www.abilityone.com/3m-trade-rotary-desk-organizer/product/CM6925',
    # 'https://www.abilityone.com/3m-trade-swing-arm-copy-clip-document-holder/product/CM13236',
    # 'https://www.abilityone.com/3m-trade-vertical-notebook-computer-riser-with-cable-management/product/CM13635',
    # 'https://www.abilityone.com/8-section-classification-folder/product/29055',
    # 'https://www.abilityone.com/classification-folder/product/29060',
    # 'https://www.abilityone.com/double-pocket-portfolio/product/290155',
    # 'https://www.abilityone.com/double-ply-recycled-file-folders-processed-chlorine-free/product/290160',
    # 'https://www.abilityone.com/end-tab-classification-folder-six-part/product/29080',
    # 'https://www.abilityone.com/end-tab-classification-folder-two-part/product/29070',
    # 'https://www.abilityone.com/expanding-file-1-31/product/29010',
    # 'https://www.abilityone.com/expanding-file-a-z/product/29005',
    # 'https://www.abilityone.com/expanding-filing-wallet/product/29015',
    # 'https://www.abilityone.com/expanding-folder-heavy-duty/product/290100',
    # 'https://www.abilityone.com/file-backer/product/290220',
    # 'https://www.abilityone.com/file-folder-17-pt-kraft/product/290105',
    # 'https://www.abilityone.com/aluminum-clipboard/product/2355',
    # 'https://www.abilityone.com/aluminum-spring-back-binder/product/23515',
    # 'https://www.abilityone.com/composition-board-clipboard/product/23510',
    # 'https://www.abilityone.com/recycled-plastic-clipboard/product/23520',
    # 'https://www.abilityone.com/acroprint-reg-cards-for-acroprint-model-es1000/product/CM13394',
    # 'https://www.abilityone.com/acroprint-reg-cards-for-model-atr120-electronic-time-clock/product/CM13393',
    # 'https://www.abilityone.com/acroprint-reg-cards-for-model-atr240-and-atr360-top-loading-time-clocks/product/CM52740',
    # 'https://www.abilityone.com/acroprint-reg-cards-for-model-att310-electronic-totalizing-time-recorder/product/CM13752',
    # 'https://www.abilityone.com/acroprint-reg-heavy-duty-time-recorders/product/CM37371',
    # 'https://www.abilityone.com/acroprint-reg-time-card-for-atr480-totalizing-electronic-time-clock/product/CM120705',
    # 'https://www.abilityone.com/acroprint-reg-timeqplus-proximity-badges/product/CM35794',
    # 'https://www.abilityone.com/adams-reg-2-part-sales-book/product/CM200039',
    # 'https://www.abilityone.com/sign-here-self-stick-flags/product/210630',
    # 'https://www.abilityone.com/12-marker-dry-erase-system/product/11220',
    # 'https://www.abilityone.com/2-hole-punch/product/213205',
    # 'https://www.abilityone.com/3-hole-punch-heavy-duty/product/213210',
    # 'https://www.abilityone.com/3-hole-punch-medium-duty/product/213215',
    # 'https://www.abilityone.com/3-in-1-freedom-liberty-collection/product/175',
    #
    # 'https://www.abilityone.com/duck-sorb-reg-13-gallon-spill-kit-oil-only/product/64010?recset=-3edf1204%3A185b886138b%3A1567-20',
    # 'https://www.abilityone.com/duck-sorb-reg-21-gallon-spill-kit-oil-only/product/64020?recset=-3edf1204%3A185b886138b%3A1567-20',
    # 'https://www.abilityone.com/duck-sorb-reg-13-gallon-spill-kit-universal/product/64015?recset=-3edf1204%3A185b886138b%3A1567-20',
    # 'https://www.abilityone.com/duck-sorb-reg-21-gallon-spill-kit-universal/product/64025?recset=-3edf1204%3A185b886138b%3A1567-20',
    # 'https://www.abilityone.com/cascade-reg-professional-fryer-boil-out/product/CM68690?recset=-3edf1204%3A185b886138b%3A1572-20',
    # 'https://www.abilityone.com/kess-lemon-d-dishwashing-liquid/product/CM49977?recset=-3edf1204%3A185b886138b%3A1572-20',
    # 'https://www.abilityone.com/diversey-trade-oxivir-reg-tb-one-step-disinfectant-cleaner/product/CM47134?recset=-3edf1204%3A185b886138b%3A1572-20',
    # 'https://www.abilityone.com/diversey-trade-emerel-reg-plus-cream-cleanser/product/CM62711?recset=-3edf1204%3A185b886138b%3A1572-20',
    # 'https://www.abilityone.com/scott-reg-pro-trade-coreless-twin-jumbo-roll-tissue-dispenser/product/CM68138?recset=-3edf1204%3A185b886138b%3A1584-20',
    # 'https://www.abilityone.com/scott-reg-essential-trade-coreless-twin-jumbo-roll-tissue-dispenser/product/CM44264?recset=-3edf1204%3A185b886138b%3A1584-20',
    # 'https://www.abilityone.com/georgia-pacific-reg-professional-jumbo-jr-bathroom-tissue-dispenser/product/CM39024?recset=-3edf1204%3A185b886138b%3A1584-20',
    # 'https://www.abilityone.com/scott-reg-pro-coreless-srb-tissue-dispenser/product/CM64381?recset=-3edf1204%3A185b886138b%3A1584-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-vented-round-brute-reg-container/product/CM24967?recset=-3edf1204%3A185b886138b%3A1590-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-brute-reg-container/product/CM50578?recset=-3edf1204%3A185b886138b%3A1590-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-reg-plastic-recycling-container-with-venting-channels/product/CM35000?recset=-3edf1204%3A185b886138b%3A1590-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-reg-with-venting-channels/product/CM23472?recset=-3edf1204%3A185b886138b%3A1590-20',
    # 'https://www.abilityone.com/therapure-reg-tpp240m-hepa-type-air-purifier/product/CM63729?recset=-3edf1204%3A185b886138b%3A1597-20',
    # 'https://www.abilityone.com/therapure-reg-tpp230m-hepa-type-air-purifier/product/CM52862?recset=-3edf1204%3A185b886138b%3A1597-20',
    # 'https://www.abilityone.com/therapure-reg-tpp220m-hepa-type-air-purifier/product/CM63728?recset=-3edf1204%3A185b886138b%3A1597-20',
    # 'https://www.abilityone.com/aeramax-reg-air-purifiers/product/CM62148?recset=-3edf1204%3A185b886138b%3A1597-20',
    # 'https://www.abilityone.com/big-d-industries-odor-control-fogger/product/CM48970?recset=-3edf1204%3A185b886138b%3A159f-20',
    # 'https://www.abilityone.com/clorox-reg-commercial-solutions-odor-defense/product/CM119680?recset=-3edf1204%3A185b886138b%3A159f-20',
    # 'https://www.abilityone.com/misty-reg-handheld-air-deodorizer/product/CM50186?recset=-3edf1204%3A185b886138b%3A159f-20',
    # 'https://www.abilityone.com/zep-commercial-reg-smoke-odor-eliminator/product/CM63841?recset=-3edf1204%3A185b886138b%3A159f-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-caddy-bag/product/CM123983?recset=-3edf1204%3A185b886138b%3A15a6-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-deluxe-carry-caddy/product/CM50601?recset=-3edf1204%3A185b886138b%3A15a6-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-executive-carry-caddy/product/CM64186?recset=-3edf1204%3A185b886138b%3A15a6-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-standard-brute-reg-rim-caddy/product/CM50768?recset=-3edf1204%3A185b886138b%3A15a6-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-iron-shaped-handle-scrub-brush/product/CM50665?recset=-3edf1204%3A185b886138b%3A15bb-20',
    # 'https://www.abilityone.com/boardwalk-reg-scrub-brush/product/CM49036?recset=-3edf1204%3A185b886138b%3A15bb-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-bi-level-deck-scrub-brush/product/CM8502?recset=-3edf1204%3A185b886138b%3A15bb-20',
    # 'https://www.abilityone.com/unger-reg-smartfit-trade-sanitary-brush/product/CM51253?recset=-3edf1204%3A185b886138b%3A15bb-20',
    # 'https://www.abilityone.com/honeywell-chillout-reg-usb-or-ac-adapter-personal-fan/product/CM64931?recset=-3edf1204%3A185b886138b%3A15c4-20',
    # 'https://www.abilityone.com/alera-reg-wall-mount-fan/product/CM122169?recset=-3edf1204%3A185b886138b%3A15c4-20',
    # 'https://www.abilityone.com/alera-reg-3-speed-box-fan/product/CM122168?recset=-3edf1204%3A185b886138b%3A15c4-20',
    # 'https://www.abilityone.com/holmes-reg-7-lil-blizzard-oscillating-personal-table-fan/product/CM8120?recset=-3edf1204%3A185b886138b%3A15c4-20',
    # 'https://www.abilityone.com/clc-controlled-life-cycle-plastic-bags/product/312510?recset=-3edf1204%3A185b886138b%3A15cf-20',
    # 'https://www.abilityone.com/bucket-and-caddy-cleaning-kit/product/35130?recset=-3edf1204%3A185b886138b%3A15cf-20',
    # 'https://www.abilityone.com/window-squeegee/product/31565?recset=-3edf1204%3A185b886138b%3A15cf-20',
    # 'https://www.abilityone.com/astm-6400-compostable-bag/product/31255?recset=-3edf1204%3A185b886138b%3A15cf-20',
    # 'https://www.abilityone.com/skilcraft-reg-laser-toner-cartridges-hp-compatible/product/212920?recset=-3edf1204%3A185b886138b%3A15de-20',
    # 'https://www.abilityone.com/hp-t0a38an-t6m14an-ink/product/CM71608?recset=-3edf1204%3A185b886138b%3A15de-20',
    # 'https://www.abilityone.com/hp-c1q11a-c1q12a-b3p13a-b3p24a-ink/product/CM63165?recset=-3edf1204%3A185b886138b%3A15de-20',
    # 'https://www.abilityone.com/hp-c9425a-c9435a-85-inkjet-cartridge/product/CM21554?recset=-3edf1204%3A185b886138b%3A15de-20',
    # 'https://www.abilityone.com/first-aid-only-trade-refill-for-smartcompliance-trade-general-business-cabinet/product/CM46071?recset=-3edf1204%3A185b886138b%3A15f2-20',
    # 'https://www.abilityone.com/first-aid-only-trade-ansi-2015-compliant-first-aid-kit-refill/product/CM70278?recset=-3edf1204%3A185b886138b%3A15f2-20',
    # 'https://www.abilityone.com/first-aid-kit-office/product/62010?recset=-3edf1204%3A185b886138b%3A15f2-20',
    # 'https://www.abilityone.com/first-aid-kit-field/product/62025?recset=-3edf1204%3A185b886138b%3A15f2-20',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040?recset=-3edf1204%3A185b886138b%3A1606-20',
    # 'https://www.abilityone.com/hand-cleaning-towelettes/product/81029?recset=-3edf1204%3A185b886138b%3A1606-20',
    # 'https://www.abilityone.com/boardwalk-reg-hand-sanitizer-gel/product/CM70342?recset=-3edf1204%3A185b886138b%3A1606-20',
    # 'https://www.abilityone.com/kleenex-reg-instant-hand-sanitizer/product/CM44221?recset=-3edf1204%3A185b886138b%3A1606-20',
    # 'https://www.abilityone.com/accelerate-or-cr-kit/product/52510?recset=-3edf1204%3A185b886138b%3A160c-20',
    # 'https://www.abilityone.com/mcr-trade-safety-sensatouch-clear-vinyl-disposable-medical-grade-gloves/product/CM200396?recset=-3edf1204%3A185b886138b%3A1614-20',
    # 'https://www.abilityone.com/mcr-trade-safety-economy-leather-drivers-gloves/product/CM39457?recset=-3edf1204%3A185b886138b%3A1614-20',
    # 'https://www.abilityone.com/mcr-trade-safety-economy-foam-nitrile-gloves/product/CM39456?recset=-3edf1204%3A185b886138b%3A1614-20',
    # 'https://www.abilityone.com/mcr-trade-safety-economy-pu-coated-work-gloves/product/CM71625?recset=-3edf1204%3A185b886138b%3A1614-20',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040?recset=-3edf1204%3A185b886138b%3A161a-20',
    # 'https://www.abilityone.com/boardwalk-reg-hand-sanitizer-gel/product/CM70342?recset=-3edf1204%3A185b886138b%3A161a-20',
    # 'https://www.abilityone.com/hand-cleaning-towelettes/product/81029?recset=-3edf1204%3A185b886138b%3A161a-20',
    # 'https://www.abilityone.com/mcr-trade-safety-cotton-inspector-gloves-8600c/product/CM54946?recset=-3edf1204%3A185b886138b%3A161a-20',
    # 'https://www.abilityone.com/alkaline-batteries/product/45515?recset=-3edf1204%3A185b886138b%3A1628-20',
    # 'https://www.abilityone.com/fellowes-reg-indoor-outdoor-heavy-duty-extension-cord/product/CM15914?recset=-3edf1204%3A185b886138b%3A1628-20',
    # 'https://www.abilityone.com/tripp-lite-protect-it-trade-seven-outlet-surge-suppressor/product/CM40472?recset=-3edf1204%3A185b886138b%3A1628-20',
    # 'https://www.abilityone.com/tripp-lite-power-strip-for-nonpatient-care-areas/product/CM67666?recset=-3edf1204%3A185b886138b%3A1628-20',
    # 'https://www.abilityone.com/avery-reg-page-size-heavyweight-three-hole-punched-sheet-protector/product/CM6719?recset=-3edf1204%3A185b886138b%3A1633-20',
    # 'https://www.abilityone.com/avery-reg-heavyweight-and-super-heavyweight-easy-load-non-glare-sheet-protector/product/CM6716?recset=-3edf1204%3A185b886138b%3A1633-20',
    # 'https://www.abilityone.com/avery-reg-touchguard-trade-protection-heavy-duty-view-binders-with-slant-rings/product/CM41523?recset=-3edf1204%3A185b886138b%3A1633-20',
    # 'https://www.abilityone.com/avery-reg-heavyweight-and-super-heavyweight-easy-load-diamond-clear-sheet-protector/product/CM6718?recset=-3edf1204%3A185b886138b%3A1633-20',
    # 'https://www.abilityone.com/appointment-planner-monthly/product/23012?recset=-3edf1204%3A185b886138b%3A1640-20',
    # 'https://www.abilityone.com/12-month-wall-calendars-wirebound/product/2305?recset=-3edf1204%3A185b886138b%3A1640-20',
    # 'https://www.abilityone.com/3-month-vertical-wall-calendar-wirebound/product/2306?recset=-3edf1204%3A185b886138b%3A1640-20',
    # 'https://www.abilityone.com/reversible-and-erasable-non-dated-90-120-day-flexible-planner/product/23045?recset=-3edf1204%3A185b886138b%3A1640-20',
    # 'https://www.abilityone.com/award-certificate-binder/product/22510?recset=-3edf1204%3A185b886138b%3A1652-20',
    # 'https://www.abilityone.com/c-line-reg-zip-n-go-trade-reusable-envelope-with-outer-pocket/product/CM47412?recset=-3edf1204%3A185b886138b%3A1652-20',
    # 'https://www.abilityone.com/pocket-padfolio/product/22520?recset=-3edf1204%3A185b886138b%3A1652-20',
    # 'https://www.abilityone.com/case-logic-reg-16-laptop-backpack/product/CM71754?recset=-3edf1204%3A185b886138b%3A1652-20',
    # 'https://www.abilityone.com/sentry-reg-safe-hd2100-safe/product/CM123603?recset=-3edf1204%3A185b886138b%3A1663-20',
    # 'https://www.abilityone.com/sentry-reg-safe-waterproof-fire-resistant-file/product/CM65333?recset=-3edf1204%3A185b886138b%3A1663-20',
    # 'https://www.abilityone.com/mmf-industries-trade-fraudstopper-reg-tamper-evident-deposit-bags/product/CM17790?recset=-3edf1204%3A185b886138b%3A1663-20',
    # 'https://www.abilityone.com/mmf-industries-trade-freezfraud-tamper-evident-deposit-bags/product/CM42347?recset=-3edf1204%3A185b886138b%3A1663-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-photographic-learning-cards/product/CM40285?recset=-3edf1204%3A185b886138b%3A1671-20',
    # 'https://www.abilityone.com/chenille-kraft-reg-wonderfoam-reg-magnetic-alphabet-letters/product/CM24905?recset=-3edf1204%3A185b886138b%3A1671-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-chairback-buddy-pocket-chart/product/CM46996?recset=-3edf1204%3A185b886138b%3A1671-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-hundreds-pocket-chart/product/CM35200?recset=-3edf1204%3A185b886138b%3A1671-20',
    # 'https://www.abilityone.com/skilcraft-reg-westcott-reg-titanium-scissors/product/27020?recset=-3edf1204%3A185b886138b%3A1678-20',
    # 'https://www.abilityone.com/skilcraft-reg-westcott-reg-titanium-scissors-with-non-stick-blades/product/27025?recset=-3edf1204%3A185b886138b%3A1678-20',
    # 'https://www.abilityone.com/stainless-steel-shears/product/27010?recset=-3edf1204%3A185b886138b%3A1678-20',
    # 'https://www.abilityone.com/universal-reg-general-purpose-stainless-steel-scissors/product/CM4017?recset=-3edf1204%3A185b886138b%3A1678-20',
    # 'https://www.abilityone.com/double-pocket-portfolio/product/290155?recset=-3edf1204%3A185b886138b%3A16af-20',
    # 'https://www.abilityone.com/recycled-file-folders-processed-chlorine-free/product/290175?recset=-3edf1204%3A185b886138b%3A16af-20',
    # 'https://www.abilityone.com/double-ply-recycled-file-folders-processed-chlorine-free/product/290160?recset=-3edf1204%3A185b886138b%3A16af-20',
    # 'https://www.abilityone.com/file-folder-colored/product/290165?recset=-3edf1204%3A185b886138b%3A16af-20',
    # 'https://www.abilityone.com/saunders-cruiser-mate-reg-aluminum-storage-clipboard/product/CM22279?recset=-3edf1204%3A185b886138b%3A16bb-20',
    # 'https://www.abilityone.com/saunders-snapak-reg-aluminum-side-open-forms-folder/product/CM5872?recset=-3edf1204%3A185b886138b%3A16bb-20',
    # 'https://www.abilityone.com/universal-reg-storage-clipboard-with-pen-compartment/product/CM123503?recset=-3edf1204%3A185b886138b%3A16bb-20',
    # 'https://www.abilityone.com/saunders-slimmate-reg-storage-clipboard/product/CM32122?recset=-3edf1204%3A185b886138b%3A16bb-20',
    # 'https://www.abilityone.com/us-government-pen/product/14125?recset=-3edf1204%3A185b886138b%3A16c7-20',
    # 'https://www.abilityone.com/framed-slant-d-ring-view-binder/product/2545?recset=-3edf1204%3A185b886138b%3A16c7-20',
    # 'https://www.abilityone.com/stick-pen/product/14120?recset=-3edf1204%3A185b886138b%3A16c7-20',
    # 'https://www.abilityone.com/clean-click-trade-/product/1450?recset=-3edf1204%3A185b886138b%3A16c7-20',
    # 'https://www.abilityone.com/us-government-pen/product/14125?recset=-3edf1204%3A185b886138b%3A16d5-20',
    # 'https://www.abilityone.com/skilcraft-reg-jaws-reg-just-add-water-system-cleaning-kit/product/3715?recset=-3edf1204%3A185b886138b%3A16d5-20',
    # 'https://www.abilityone.com/recyclable-plastic-trigger-spray-bottle/product/32015?recset=-3edf1204%3A185b886138b%3A16d5-20',
    # 'https://www.abilityone.com/glass-pro-professional-strength-cleaner/product/3755?recset=-3edf1204%3A185b886138b%3A16d5-20',
    # 'https://www.abilityone.com/clc-controlled-life-cycle-plastic-bags/product/312510?recset=-3edf1204%3A185b886138b%3A16de-20',
    # 'https://www.abilityone.com/bucket-and-caddy-cleaning-kit/product/35130?recset=-3edf1204%3A185b886138b%3A16de-20',
    # 'https://www.abilityone.com/window-squeegee/product/31565?recset=-3edf1204%3A185b886138b%3A16de-20',
    # 'https://www.abilityone.com/astm-6400-compostable-bag/product/31255?recset=-3edf1204%3A185b886138b%3A16de-20',
    # 'https://www.abilityone.com/duck-sorb-reg-13-gallon-spill-kit-oil-only/product/64010?recset=-3edf1204%3A185b886138b%3A1701-20',
    # 'https://www.abilityone.com/duck-sorb-reg-21-gallon-spill-kit-oil-only/product/64020?recset=-3edf1204%3A185b886138b%3A1701-20',
    # 'https://www.abilityone.com/duck-sorb-reg-13-gallon-spill-kit-universal/product/64015?recset=-3edf1204%3A185b886138b%3A1701-20',
    # 'https://www.abilityone.com/duck-sorb-reg-21-gallon-spill-kit-universal/product/64025?recset=-3edf1204%3A185b886138b%3A1701-20',
    # 'https://www.abilityone.com/cascade-reg-professional-fryer-boil-out/product/CM68690?recset=-3edf1204%3A185b886138b%3A1710-20',
    # 'https://www.abilityone.com/diversey-trade-oxivir-reg-tb-one-step-disinfectant-cleaner/product/CM47134?recset=-3edf1204%3A185b886138b%3A1710-20',
    # 'https://www.abilityone.com/kess-lemon-d-dishwashing-liquid/product/CM49977?recset=-3edf1204%3A185b886138b%3A1710-20',
    # 'https://www.abilityone.com/diversey-trade-emerel-reg-plus-cream-cleanser/product/CM62711?recset=-3edf1204%3A185b886138b%3A1710-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-wavebrake-reg-20-dirty-water-bucket/product/CM123710?recset=-3edf1204%3A185b886138b%3A1718-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-wavebrake-reg-bucket/product/CM50806?recset=-3edf1204%3A185b886138b%3A1718-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-microfiber-finish-bucket/product/CM50685?recset=-3edf1204%3A185b886138b%3A1718-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-wavebrake-reg-20-bucket/product/CM123709?recset=-3edf1204%3A185b886138b%3A1718-20',
    # 'https://www.abilityone.com/scott-reg-pro-trade-coreless-twin-jumbo-roll-tissue-dispenser/product/CM68138?recset=-3edf1204%3A185b886138b%3A1737-20',
    # 'https://www.abilityone.com/scott-reg-essential-trade-coreless-twin-jumbo-roll-tissue-dispenser/product/CM44264?recset=-3edf1204%3A185b886138b%3A1737-20',
    # 'https://www.abilityone.com/georgia-pacific-reg-professional-jumbo-jr-bathroom-tissue-dispenser/product/CM39024?recset=-3edf1204%3A185b886138b%3A1737-20',
    # 'https://www.abilityone.com/scott-reg-pro-coreless-srb-tissue-dispenser/product/CM64381?recset=-3edf1204%3A185b886138b%3A1737-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-vented-round-brute-reg-container/product/CM24967?recset=-3edf1204%3A185b886138b%3A1742-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-brute-reg-container/product/CM50578?recset=-3edf1204%3A185b886138b%3A1742-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-reg-plastic-recycling-container-with-venting-channels/product/CM35000?recset=-3edf1204%3A185b886138b%3A1742-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-reg-with-venting-channels/product/CM23472?recset=-3edf1204%3A185b886138b%3A1742-20',
    # 'https://www.abilityone.com/therapure-reg-tpp240m-hepa-type-air-purifier/product/CM63729?recset=-3edf1204%3A185b886138b%3A1753-20',
    # 'https://www.abilityone.com/therapure-reg-tpp230m-hepa-type-air-purifier/product/CM52862?recset=-3edf1204%3A185b886138b%3A1753-20',
    # 'https://www.abilityone.com/therapure-reg-tpp220m-hepa-type-air-purifier/product/CM63728?recset=-3edf1204%3A185b886138b%3A1753-20',
    # 'https://www.abilityone.com/aeramax-reg-air-purifiers/product/CM62148?recset=-3edf1204%3A185b886138b%3A1753-20',
    # 'https://www.abilityone.com/big-d-industries-odor-control-fogger/product/CM48970?recset=-3edf1204%3A185b886138b%3A175a-20',
    # 'https://www.abilityone.com/clorox-reg-commercial-solutions-odor-defense/product/CM119680?recset=-3edf1204%3A185b886138b%3A175a-20',
    # 'https://www.abilityone.com/misty-reg-handheld-air-deodorizer/product/CM50186?recset=-3edf1204%3A185b886138b%3A175a-20',
    # 'https://www.abilityone.com/zep-commercial-reg-smoke-odor-eliminator/product/CM63841?recset=-3edf1204%3A185b886138b%3A175a-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-slim-jim-caddy-bag/product/CM123983?recset=-3edf1204%3A185b886138b%3A1764-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-deluxe-carry-caddy/product/CM50601?recset=-3edf1204%3A185b886138b%3A1764-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-executive-carry-caddy/product/CM64186?recset=-3edf1204%3A185b886138b%3A1764-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-standard-brute-reg-rim-caddy/product/CM50768?recset=-3edf1204%3A185b886138b%3A1764-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-iron-shaped-handle-scrub-brush/product/CM50665?recset=-3edf1204%3A185b886138b%3A176e-20',
    # 'https://www.abilityone.com/boardwalk-reg-scrub-brush/product/CM49036?recset=-3edf1204%3A185b886138b%3A176e-20',
    # 'https://www.abilityone.com/rubbermaid-reg-commercial-bi-level-deck-scrub-brush/product/CM8502?recset=-3edf1204%3A185b886138b%3A176e-20',
    # 'https://www.abilityone.com/unger-reg-smartfit-trade-sanitary-brush/product/CM51253?recset=-3edf1204%3A185b886138b%3A176e-20',
    # 'https://www.abilityone.com/honeywell-chillout-reg-usb-or-ac-adapter-personal-fan/product/CM64931?recset=-3edf1204%3A185b886138b%3A177e-20',
    # 'https://www.abilityone.com/alera-reg-wall-mount-fan/product/CM122169?recset=-3edf1204%3A185b886138b%3A177e-20',
    # 'https://www.abilityone.com/alera-reg-3-speed-box-fan/product/CM122168?recset=-3edf1204%3A185b886138b%3A177e-20',
    # 'https://www.abilityone.com/holmes-reg-7-lil-blizzard-oscillating-personal-table-fan/product/CM8120?recset=-3edf1204%3A185b886138b%3A177e-20',
    # 'https://www.abilityone.com/clc-controlled-life-cycle-plastic-bags/product/312510?recset=-3edf1204%3A185b886138b%3A1784-20',
    # 'https://www.abilityone.com/bucket-and-caddy-cleaning-kit/product/35130?recset=-3edf1204%3A185b886138b%3A1784-20',
    # 'https://www.abilityone.com/window-squeegee/product/31565?recset=-3edf1204%3A185b886138b%3A1784-20',
    # 'https://www.abilityone.com/astm-6400-compostable-bag/product/31255?recset=-3edf1204%3A185b886138b%3A1784-20',
    # 'https://www.abilityone.com/skilcraft-reg-laser-toner-cartridges-hp-compatible/product/212920?recset=-3edf1204%3A185b886138b%3A1791-20',
    # 'https://www.abilityone.com/innovera-reg-7970-inkjet-cartridge/product/CM23885?recset=-3edf1204%3A185b886138b%3A1791-20',
    # 'https://www.abilityone.com/hp-c9425a-c9435a-85-inkjet-cartridge/product/CM21554?recset=-3edf1204%3A185b886138b%3A1791-20',
    # 'https://www.abilityone.com/hp-n9h57fn-cn684wn-ink/product/CM33350?recset=-3edf1204%3A185b886138b%3A1791-20',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040?recset=-3edf1204%3A185b886138b%3A1796-20',
    # 'https://www.abilityone.com/mcr-trade-safety-cotton-inspector-gloves-8600c/product/CM54946?recset=-3edf1204%3A185b886138b%3A1796-20',
    # 'https://www.abilityone.com/boardwalk-reg-hand-sanitizer-gel/product/CM70342?recset=-3edf1204%3A185b886138b%3A1796-20',
    # 'https://www.abilityone.com/mcr-trade-safety-disposable-vinyl-gloves-5010xl/product/CM56958?recset=-3edf1204%3A185b886138b%3A1796-20',
    # 'https://www.abilityone.com/first-aid-only-trade-refill-for-smartcompliance-trade-general-business-cabinet/product/CM46071?recset=-3edf1204%3A185b886138b%3A17a4-20',
    # 'https://www.abilityone.com/first-aid-only-trade-ansi-2015-compliant-first-aid-kit-refill/product/CM70278?recset=-3edf1204%3A185b886138b%3A17a4-20',
    # 'https://www.abilityone.com/first-aid-kit-office/product/62010?recset=-3edf1204%3A185b886138b%3A17a4-20',
    # 'https://www.abilityone.com/first-aid-kit-field/product/62025?recset=-3edf1204%3A185b886138b%3A17a4-20',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040?recset=-3edf1204%3A185b886138b%3A17ae-20',
    # 'https://www.abilityone.com/hand-cleaning-towelettes/product/81029?recset=-3edf1204%3A185b886138b%3A17ae-20',
    # 'https://www.abilityone.com/boardwalk-reg-hand-sanitizer-gel/product/CM70342?recset=-3edf1204%3A185b886138b%3A17ae-20',
    # 'https://www.abilityone.com/oasis-conditioning-shampoo/product/CM123432?recset=-3edf1204%3A185b886138b%3A17ae-20',
    # 'https://www.abilityone.com/accelerate-or-cr-kit/product/52510?recset=-3edf1204%3A185b886138b%3A17bc-20',
    # 'https://www.abilityone.com/mcr-trade-safety-sensatouch-clear-vinyl-disposable-medical-grade-gloves/product/CM200396?recset=-3edf1204%3A185b886138b%3A17ca-20',
    # 'https://www.abilityone.com/mcr-trade-safety-economy-leather-drivers-gloves/product/CM39457?recset=-3edf1204%3A185b886138b%3A17ca-20',
    # 'https://www.abilityone.com/mcr-trade-safety-economy-foam-nitrile-gloves/product/CM39456?recset=-3edf1204%3A185b886138b%3A17ca-20',
    # 'https://www.abilityone.com/kleenguard-trade-g10-nitrile-gloves/product/CM44205?recset=-3edf1204%3A185b886138b%3A17ca-20',
    # 'https://www.abilityone.com/piddle-pak-crew-relief-bag/product/81040?recset=-3edf1204%3A185b886138b%3A17dc-20',
    # 'https://www.abilityone.com/mcr-trade-safety-disposable-vinyl-gloves-5010xl/product/CM56958?recset=-3edf1204%3A185b886138b%3A17dc-20',
    # 'https://www.abilityone.com/boardwalk-reg-hand-sanitizer-gel/product/CM70342?recset=-3edf1204%3A185b886138b%3A17dc-20',
    # 'https://www.abilityone.com/hand-cleaning-towelettes/product/81029?recset=-3edf1204%3A185b886138b%3A17dc-20',
    # 'https://www.abilityone.com/us-government-pen/product/14125?recset=-3edf1204%3A185b886138b%3A17e7-20',
    'https://www.abilityone.com/framed-slant-d-ring-view-binder/product/2545?recset=-3edf1204%3A185b886138b%3A17e7-20',
    'https://www.abilityone.com/stick-pen/product/14120?recset=-3edf1204%3A185b886138b%3A17e7-20',
    # 'https://www.abilityone.com/skilcraft-reg-47gb-dvd-r-100-pack-with-spindle/product/25585?recset=-3edf1204%3A185b886138b%3A17e7-20',
    # 'https://www.abilityone.com/alkaline-batteries/product/45515?recset=-3edf1204%3A185b886138b%3A17fa-20',
    # 'https://www.abilityone.com/fellowes-reg-indoor-outdoor-heavy-duty-extension-cord/product/CM15914?recset=-3edf1204%3A185b886138b%3A17fa-20',
    # 'https://www.abilityone.com/tripp-lite-protect-it-trade-seven-outlet-surge-suppressor/product/CM40472?recset=-3edf1204%3A185b886138b%3A17fa-20',
    # 'https://www.abilityone.com/tripp-lite-power-strip-for-nonpatient-care-areas/product/CM67666?recset=-3edf1204%3A185b886138b%3A17fa-20',
    # 'https://www.abilityone.com/avery-reg-page-size-heavyweight-three-hole-punched-sheet-protector/product/CM6719?recset=-3edf1204%3A185b886138b%3A1803-20',
    # 'https://www.abilityone.com/avery-reg-heavyweight-and-super-heavyweight-easy-load-non-glare-sheet-protector/product/CM6716?recset=-3edf1204%3A185b886138b%3A1803-20',
    # 'https://www.abilityone.com/avery-reg-touchguard-trade-protection-heavy-duty-view-binders-with-slant-rings/product/CM41523?recset=-3edf1204%3A185b886138b%3A1803-20',
    # 'https://www.abilityone.com/avery-reg-heavyweight-and-super-heavyweight-easy-load-diamond-clear-sheet-protector/product/CM6718?recset=-3edf1204%3A185b886138b%3A1803-20',
    # 'https://www.abilityone.com/appointment-planner-monthly/product/23012?recset=-3edf1204%3A185b886138b%3A180c-20',
    # 'https://www.abilityone.com/12-month-wall-calendars-wirebound/product/2305?recset=-3edf1204%3A185b886138b%3A180c-20',
    # 'https://www.abilityone.com/3-month-vertical-wall-calendar-wirebound/product/2306?recset=-3edf1204%3A185b886138b%3A180c-20',
    # 'https://www.abilityone.com/reversible-and-erasable-non-dated-90-120-day-flexible-planner/product/23045?recset=-3edf1204%3A185b886138b%3A180c-20',
    # 'https://www.abilityone.com/award-certificate-binder/product/22510?recset=-3edf1204%3A185b886138b%3A181a-20',
    # 'https://www.abilityone.com/pocket-padfolio/product/22520?recset=-3edf1204%3A185b886138b%3A181a-20',
    # 'https://www.abilityone.com/case-logic-reg-16-laptop-backpack/product/CM71754?recset=-3edf1204%3A185b886138b%3A181a-20',
    # 'https://www.abilityone.com/c-line-reg-zip-n-go-trade-reusable-envelope-with-outer-pocket/product/CM47412?recset=-3edf1204%3A185b886138b%3A181a-20',
    # 'https://www.abilityone.com/sentry-reg-safe-hd2100-safe/product/CM123603?recset=-3edf1204%3A185b886138b%3A1836-20',
    # 'https://www.abilityone.com/sentry-reg-safe-waterproof-fire-resistant-file/product/CM65333?recset=-3edf1204%3A185b886138b%3A1836-20',
    # 'https://www.abilityone.com/mmf-industries-trade-fraudstopper-reg-tamper-evident-deposit-bags/product/CM17790?recset=-3edf1204%3A185b886138b%3A1836-20',
    # 'https://www.abilityone.com/mmf-industries-trade-freezfraud-tamper-evident-deposit-bags/product/CM42347?recset=-3edf1204%3A185b886138b%3A1836-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-photographic-learning-cards/product/CM40285?recset=-3edf1204%3A185b886138b%3A1854-20',
    # 'https://www.abilityone.com/chenille-kraft-reg-wonderfoam-reg-magnetic-alphabet-letters/product/CM24905?recset=-3edf1204%3A185b886138b%3A1854-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-chairback-buddy-pocket-chart/product/CM46996?recset=-3edf1204%3A185b886138b%3A1854-20',
    # 'https://www.abilityone.com/carson-dellosa-publishing-hundreds-pocket-chart/product/CM35200?recset=-3edf1204%3A185b886138b%3A1854-20',
    # 'https://www.abilityone.com/skilcraft-reg-westcott-reg-titanium-scissors/product/27020?recset=-3edf1204%3A185b886138b%3A1863-20',
    # 'https://www.abilityone.com/skilcraft-reg-westcott-reg-titanium-scissors-with-non-stick-blades/product/27025?recset=-3edf1204%3A185b886138b%3A1863-20',
    # 'https://www.abilityone.com/stainless-steel-shears/product/27010?recset=-3edf1204%3A185b886138b%3A1863-20',
    # 'https://www.abilityone.com/universal-reg-general-purpose-stainless-steel-scissors/product/CM4017?recset=-3edf1204%3A185b886138b%3A1863-20',
    # 'https://www.abilityone.com/post-it-reg-flags-arrow-message-1-2-flags/product/CM12819?recset=-3edf1204%3A185b886138b%3A1873-20',
    # 'https://www.abilityone.com/post-it-reg-flags-portable-flags/product/CM45286?recset=-3edf1204%3A185b886138b%3A1873-20',
    # 'https://www.abilityone.com/post-it-reg-flags-small-flags/product/CM17503?recset=-3edf1204%3A185b886138b%3A1873-20',
    # 'https://www.abilityone.com/post-it-reg-flags-arrow-flags-in-a-desk-grip-dispenser/product/CM24164?recset=-3edf1204%3A185b886138b%3A1873-20',
    # 'https://www.abilityone.com/double-pocket-portfolio/product/290155?recset=-3edf1204%3A185b886138b%3A1888-20',
    # 'https://www.abilityone.com/sunworks-reg-construction-paper/product/CM17722?recset=-3edf1204%3A185bde68225%3A-6a8-20',
    # 'https://www.abilityone.com/recycled-file-folders-processed-chlorine-free/product/290175?recset=-3edf1204%3A185b886138b%3A1888-20',
    # 'https://www.abilityone.com/double-ply-recycled-file-folders-processed-chlorine-free/product/290160?recset=-3edf1204%3A185b886138b%3A1888-20',
    # 'https://www.abilityone.com/file-folder-colored/product/290165?recset=-3edf1204%3A185b886138b%3A1888-20',
    # 'https://www.abilityone.com/saunders-cruiser-mate-reg-aluminum-storage-clipboard/product/CM22279?recset=-3edf1204%3A185b886138b%3A18a0-20',
    # 'https://www.abilityone.com/saunders-snapak-reg-aluminum-side-open-forms-folder/product/CM5872?recset=-3edf1204%3A185b886138b%3A18a0-20',
    # 'https://www.abilityone.com/universal-reg-storage-clipboard-with-pen-compartment/product/CM123503?recset=-3edf1204%3A185b886138b%3A18a0-20',
    # 'https://www.abilityone.com/saunders-slimmate-reg-storage-clipboard/product/CM32122?recset=-3edf1204%3A185b886138b%3A18a0-20',
    # 'https://www.abilityone.com/us-government-pen/product/14125?recset=-3edf1204%3A185b886138b%3A18a8-20',
    # 'https://www.abilityone.com/clean-click-trade-/product/1450?recset=-3edf1204%3A185b886138b%3A18a8-20',
    # 'https://www.abilityone.com/framed-slant-d-ring-view-binder/product/2545?recset=-3edf1204%3A185b886138b%3A18a8-20',
    # 'https://www.abilityone.com/screen-and-lens-cleaner-kit/product/24576?recset=-3edf1204%3A185b886138b%3A18a8-20',
    # 'https://www.abilityone.com/first-aid-only-trade-refill-for-smartcompliance-trade-general-business-cabinet/product/CM46071?recset=-3edf1204%3A185b886138b%3A18b2-20',
    # 'https://www.abilityone.com/first-aid-only-trade-ansi-2015-compliant-first-aid-kit-refill/product/CM70278?recset=-3edf1204%3A185b886138b%3A18b2-20',
    # 'https://www.abilityone.com/first-aid-kit-office/product/62010?recset=-3edf1204%3A185b886138b%3A18b2-20',
    # 'https://www.abilityone.com/first-aid-kit-field/product/62025?recset=-3edf1204%3A185b886138b%3A18b2-20',

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
        time.sleep(5)
        print("products urls === ", url)
        description_d = ""
        item_n1_d = ""
        # try:
        #     # =================================================== Find Breadcrumb =================================================
        #     print("********************************* Breadcrumb : ***********************************")
        #     Breadcrumb = driver.find_element(By.XPATH, '//*[@id="breadcrumbs"]/div/div/div')
        #     Breadcrumb_d = Breadcrumb.text.replace("\n", " ")
        #     print("Breadcrumb = ", Breadcrumb_d)
        #     print(type(Breadcrumb_d))
        # except:
        #     Breadcrumb_d = " Not Found"
        #     print("Breadcrumb = ", Breadcrumb_d)
        #
        # try:
        #     # =================================================== Find Title =================================================
        #     print("*********************************** title : **************************************")
        #     title = driver.find_element(By.CLASS_NAME, 'pdp_prodInfo-title')
        #     title_d = title.text if title else "Not Found"
        #     print("Title = ", title_d)
        #     print(type(title_d))
        # except:
        #     title_d = "Not Found"
        #     print("title_d", title_d)
        #
        # try:
        #     print("*********************************** Price 1: **************************************")
        #     price1 = driver.find_element(By.XPATH, '//*[@id="pdp_prodInfo"]/p[2]')
        #     price1_d = price1.text.strip() if price1 else "Not Found"
        #     print("price1 = ", price1_d)
        #     print(type(price1_d))
        # except:
        #     price1_d = "Not Found"
        #     print("price1 = ", price1_d)
        #
        # try:
        #     print("*********************************** Item N 1: **************************************")
        #     item_n1 = driver.find_element(By.XPATH, '//*[@id="pdp_prodInfo"]/div/p[1]')
        #     item_n1_d = item_n1.text.strip() if item_n1 else "Not Found"
        #     print("item_n1 = ", price1_d)
        #     print(type(item_n1_d))
        # except:
        #     item_n1_d = "Not Found"
        #     print("item_n1 = ", item_n1_d)
        #
        # try:
        #     # =================================================== Find Description =================================================
        #     print("*********************************** Descriptions 1 : **************************************")
        #     description = driver.find_element(By.CLASS_NAME, 'panel-body').find_elements(By.TAG_NAME, 'p')
        #     for zz in description:
        #         time.sleep(3)
        #         description_d = zz.text.replace("\n", " ") if zz else "Not Found"
        #         print("description1 = ", description_d)
        #         print(type(description_d))
        #         save_details: TextIO = open("ability one files.xlsx", "a+", encoding="utf-8")
        #         save_details.write(
        #             "\n" + url + "\t" + Breadcrumb_d + "\t" + title_d + "\t" + price1_d + "\t" + item_n1_d + "\t" + str(
        #                 description_d))
        #         print("End")
        #         save_details.close()
        #         print("\n ***** Record stored into ability one other files. *****")
        #         print()
        #
        # except Exception as e:
        #     description_d = "Not Found"
        #     print("description_d = ", description_d)
        #     print("error", e)

        image_d = ""
        item_d = ""
        try:
            sku1 = driver.find_elements(By.TAG_NAME, "option")
            # print(sku1)
            count = 0
            if len(sku1) != 0:
                for x in sku1:
                    count += 1
                    x.click()
                    time.sleep(5)
                    print("asdjfakl", x.text)
                    # =================================================== Find price =================================================
                    # print("*********************************** Price : **************************************")
                    # price = driver.find_element(By.XPATH, '//*[@id="pdp_prodInfo"]/p[2]')
                    # print(count)
                    # print("Selected option", x.text)
                    # price_D = price.text
                    # print("price = ", price_D)

                    # =================================================== Find item number =================================================
                    # print("*********************************** Item N : **************************************")
                    # item = driver.find_elements(By.XPATH, '//*[@id="pdp_prodInfo"]/div/p[1]/span')
                    # for item_n in item:
                    #     time.sleep(3)
                    #     item_d = item_n.text if item_n else "Not Found"
                    #     print('item_d = ', item_d)
                    #     save_details: TextIO = open("main files ability one.xlsx", "a+", encoding="utf-8")
                    #     save_details.write(
                    #         "\n" + url + "\t" + Breadcrumb_d + "\t" + title_d + "\t" + price_D + "\t" + item_d + "\t" + image_d + "\t" + description_d)
                    #     print("End")
                    #     save_details.close()
                    #     print("\n ***** Record stored into ability one. *****")
                    #
                    #     print("image_d = ", image_d, "Not Found")
            else:
                print("For Loop Data Not Found")

        except Exception as e:
            print("Error = 1 ", e)

    except Exception as e:
        print("Error", e)
        pass
