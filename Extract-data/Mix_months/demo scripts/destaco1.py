from bs4 import BeautifulSoup
import requests
from typing import TextIO

myresult = [
    'https://www.destaco.com/rotary-positioning/part-handlers/rotary-part-handlers-500rpp/productdetails.500RPP2H32-3H32.html',
    'https://www.destaco.com/rotary-positioning/ac-motor-drives.html',
    'https://www.destaco.com/quote.html',
    'https://www.destaco.com/quote/requestquote.html',
    'https://www.destaco.com/productpages.html',
    'https://www.destaco.com/productpages/byproductcategory.html',
    'https://www.destaco.com/productpages/byproductcategory/clamping.html',
    'https://www.destaco.com/productpages/byproductcategory/gripping.html',
    'https://www.destaco.com/productpages/byproductcategory/linearpositioning.html',
    'https://www.destaco.com/productpages/byproductcategory/rotarypositioning.html',
    'https://www.destaco.com/productpages/byproductcategory/robotictooling.html',
    'https://www.destaco.com/productpages/bybrand.html',
    'https://www.destaco.com/productpages/bybrand/robohand.html',
    'https://www.destaco.com/productpages/bybrand/destaco.html',
    'https://www.destaco.com/productpages/bybrand/camco.html',
    'https://www.destaco.com/productpages/bybrand/ferguson.html',
    'https://www.destaco.com/ish-header.html',
    'https://www.destaco.com/ish-footer.html',
    'https://www.destaco.com/solutions.html',
    'https://www.destaco.com/solutions/by-markets.html',
    'https://www.destaco.com/solutions/by-markets/automotive.html',
    'https://www.destaco.com/solutions/by-markets/food-and-packaging.html',
    'https://www.destaco.com/solutions/by-markets/consumer-goods.html',
    'https://www.destaco.com/solutions/by-markets/life-science.html',
    'https://www.destaco.com/solutions/by-markets/aerospace.html',
    'https://www.destaco.com/solutions/by-applications-and-topics.html',
    'https://www.destaco.com/solutions/by-applications-and-topics/automation.html',
    'https://www.destaco.com/solutions/by-applications-and-topics/body-in-white.html',
    'https://www.destaco.com/solutions/by-applications-and-topics/stamping.html',
    'https://www.destaco.com/solutions/by-applications-and-topics/stainless-steel.html',
    'https://www.destaco.com/solutions/by-applications-and-topics/green-production.html',
    'https://www.destaco.com/solutions/by-applications-and-topics/e-mobility.html',
    'https://www.destaco.com/solutions/by-applications-and-topics/accelerate-digital-solutions.html',
    'https://www.destaco.com/solutions/by-applications-and-topics/custom-cams.html',
    'https://www.destaco.com/solutions/by-applications-and-topics/TestAccelerate.html',
    'https://www.destaco.com/solutions/by-applications-and-topics/transfer-press.html',
    'https://www.destaco.com/contact.html',
    'https://www.destaco.com/contact/product-finder.html',
    'https://www.destaco.com/contact/need-more-help.html',
    'https://www.destaco.com/contact/distributor-locator.html',
    'https://www.destaco.com/resources.html',
    'https://www.destaco.com/resources/case-studies.html',
    'https://www.destaco.com/resources/case-studies/tmmc-boosts-production-with-destaco-custom-transfer-tooling.html',
    'https://www.destaco.com/resources/case-studies/destaco-s-custom-solution-reduces-weight.html',
    'https://www.destaco.com/resources/case-studies/camco-conveyor-solution-moves-50-pounds-across-36-inches-every-3.html',
    'https://www.destaco.com/resources/case-studies/custom-product-modification-brings-20--productivity-increase-.html',
    'https://www.destaco.com/resources/case-studies/207-u-reduces-scrap-by-20-.html',
    'https://www.destaco.com/resources/case-studies/camco-conveyor-solution-indexes-20-pounds-across-12-inches-every.html',
    'https://www.destaco.com/resources/case-studies/packaging-glass-bottles-with-precision.html',
    'https://www.destaco.com/resources/case-studies/custom-stainless-steel-indexer-for-demanding-food-processing-env.html',
    'https://www.destaco.com/resources/case-studies/camco-conveyor-solution-indexes-36-pounds-across-54-inches-every.html',
    'https://www.destaco.com/resources/case-studies/custom-chassis-results-in-25--productivity-improvement.html',
    'https://www.destaco.com/resources/case-studies/swing-clamp-reduces-scrap-rate.html',
    'https://www.destaco.com/resources/case-studies/8316-swing-clamp-reduces-scrap-rate-by-98-.html',
    'https://www.destaco.com/resources/case-studies/gluing-end-blocks-to-sides-of-guitar-subassembly.html',
    'https://www.destaco.com/resources/case-studies/round-tooling-and-clamp-lifting-device-improves-productivity.html',
    'https://www.destaco.com/resources/case-studies/increase-productivity---time-savings-in-ac-application.html',
    'https://www.destaco.com/resources/case-studies/plastic-proximity-switch-mount-for-accurate-part-sensing.html',
    'https://www.destaco.com/resources/case-studies/arv-auto-release-venturi-reduces-air-consumption-by-60-.html',
    'https://www.destaco.com/resources/case-studies/parallel-grippers-for-efficient-pick-and-place-solution.html',
    'https://www.destaco.com/resources/case-studies/ctg-utilizes-destaco-indexer-solution-to-boost-efficiency-for-mu.html',
    'https://www.destaco.com/resources/case-studies/food-grade-gripper-needed-for-cheese-handling.html',
    'https://www.destaco.com/resources/case-studies/destaco-s-camco-conveyor-saves-over-25--on-costs-for-9--station-.html',
    'https://www.destaco.com/resources/case-studies/pneumatic-hold-down-clamps-help-reduce-cycle-time-by-70-.html',
    'https://www.destaco.com/resources/case-studies/multiple-grippers-moving-large---heavy-wood-panels.html',
    'https://www.destaco.com/resources/how-to-buy-guides.html',
    'https://www.destaco.com/resources/how-to-buy-guides/how-to-select-the-right-destaco-manual-clamp.html',
    'https://www.destaco.com/resources/how-to-buy-guides/how-to-calculate-exerting-force-clamping-force-holding-capacity.html',
    'https://www.destaco.com/resources/how-to-buy-guides/what-to-know-about-manual-quick-action-toggle-clamps.html',
    'https://www.destaco.com/resources/how-to-buy-guides/safety-characteristics-of-destaco-manual-clamps.html',
    'https://www.destaco.com/resources/how-to-buy-guides/questions-to-ask-before-selecting-your-air-gripper.html',
    'https://www.destaco.com/resources/how-to-buy-guides/what-to-know-before-selecting-your-grippers.html',
    'https://www.destaco.com/resources/how-to-buy-guides/understanding-precision-grippers.html',
    'https://www.destaco.com/resources/how-to-buy-guides/comparing-shielded-vs-sealed-grippers.html',
    'https://www.destaco.com/resources/how-to-buy-guides/clean-room-rated-gripper-solutions.html',
    'https://www.destaco.com/resources/how-to-buy-guides/comparing-scavenge-vs-purge-ports-on-grippers.html',
    'https://www.destaco.com/resources/how-to-buy-guides/how-to-calculate-inertia-of-load-reflected-to-motor-inertia-ratio.html',
    'https://www.destaco.com/resources/how-to-buy-guides/indexers-fixed-vs-flexible-automation.html',
    'https://www.destaco.com/resources/how-to-buy-guides/indexer-accuracy-vs-repeatability.html',
    'https://www.destaco.com/resources/how-to-buy-guides/how-to-increase-uptime-in-your-press-shops.html',
    'https://www.destaco.com/resources/how-to-buy-guides/how-to-choose-your-vacuum-cups.html',
    'https://www.destaco.com/resources/how-to-buy-guides/four-critical-considerations-when-selecting-a-robotic-end-effect.html',
    'https://www.destaco.com/resources/how-to-buy-guides/how-object-characteristics-affect-vacuum-cup-selection.html',
    'https://www.destaco.com/resources/how-to-buy-guides/when-selecting-a-vacuum-cup-what-is-durometer.html',
    'https://www.destaco.com/resources/how-to-buy-guides/end-effector-operating-parameters-in-metal-stamping.html',
    'https://www.destaco.com/resources/literature-library.html',
    'https://www.destaco.com/resources/video-library.html',
    'https://www.destaco.com/resources/custom-catalog.html',
    'https://www.destaco.com/resources/interactive-product-tour.html',
    'https://www.destaco.com/resources/interactive-product-tour/84n1-sheet-metal-gripper.html',
    'https://www.destaco.com/resources/interactive-product-tour/straight-line-action-clamp.html',
    'https://www.destaco.com/resources/interactive-product-tour/horizontal-hold-down-clamp.html',
    'https://www.destaco.com/resources/interactive-product-tour/vertical-hold-down-clamp.html',
    'https://www.destaco.com/resources/simple.html',
    'https://www.destaco.com/resources/simple/simple-need-help.html',
    'https://www.destaco.com/resources/simple/simple-need-help/need-simple-thank-you.html',
    'https://www.destaco.com/resources/simple/need-simple-test.html',
    'https://www.destaco.com/resources/Simple-Backup-8-23.html',
    'https://www.destaco.com/privacy-policy.html',
    'https://www.destaco.com/general-terms-and-conditions.html',
    'https://www.destaco.com/cad-issue-report.html',
    'https://www.destaco.com/cx-header.html',
    'https://www.destaco.com/cadrequestfrom.html',
    'https://www.destaco.com/error.html',
    'https://www.destaco.com/error/500.html',
    'https://www.destaco.com/error/404.html',
    'https://www.destaco.com/thank-you.html',
    'https://www.destaco.com/policies.html',
    'https://www.destaco.com/policies/transparency-in-supply-chain-disclosure.html',
    'https://www.destaco.com/terms-of-use.html',
    'https://www.destaco.com/ecomm-faq.html',
    'https://www.destaco.com/sizing.html',
    'https://www.destaco.com/product-sizing-tools.html',
    'https://www.destaco.com/sizing-tools.html',
    'https://www.destaco.com/sizing-tools/tool-changers.html',
    'https://www.destaco.com/sizing-tools/escapements.html',
    'https://www.destaco.com/sizing-tools/indexer.html',
    'https://www.destaco.com/sizing-tools/powerclamps.html',
    'https://www.destaco.com/sizing-tools/slides.html',
    'https://www.destaco.com/sizing-tools/pneumatic-rotaries.html',
    'https://www.destaco.com/sizing-tools/pneumatic-gripper.html',
    'https://www.destaco.com/sizing-tools/electric-grippers.html',
    'https://www.destaco.com/sizing-error.html',
    'https://www.destaco.com/sizing-thank-you.html',
    'https://www.destaco.com/cds-forms.html',
    'https://www.destaco.com/cds-forms/power-clamp-marketo-forms.html',
    'https://www.destaco.com/cds-forms/grippers-marketo-forms.html',
    'https://www.destaco.com/cds-forms/toolchangers-marketo-forms.html',
    'https://www.destaco.com/cds-forms/indexers-marketo-forms.html']
for row in myresult:
    try:
        product_url = row
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
        result = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(result.content, 'html.parser')
        # print(soup.prettify())

        print(product_url)
        print('*********Product Heading***********')
        try:
            head1 = soup.find("div", class_="dover-hero__heading")
            head = (head1.text.strip() if head1 else "not given")
            print(head)
        except:
            head = "not given"
        print('*********Breadcrumb***********')
        try:
            bread = soup.find('div', class_='breadcrumb').find_all("h6", {'itemprop': "name"})
            list1 = []
            for b in bread:
                list1.append(b.text.strip() if b else "not given")
            print(list1)
        except:
            list1 = []

        print('*********Product Title***********')
        try:
            tit1 = soup.find("h1", class_="heading h3")
            tit = (tit1.text.strip() if tit1 else "not given")
            print(tit)
        except:
            tit = "not given"

        # try:
        #     draw = soup.find("tbody", class_="wsite-multicol-tbody").find_all("span")
        #     draw1 = []
        #     for b in draw:
        #         draw1.append(b.text.strip() if b else "Not Found")
        #         print(draw1)
        # except:
        #     draw1 = []

        print('*********Product Description***********')
        try:
            desc1 = soup.find("div", class_="description")
            desc = (desc1.text.strip() if desc1 else "not given")
            print(desc)
        except:
            desc = "not given"

        print('*********pdfs***********')
        try:
            pdf1 = soup.find('div', class_='content-data pdf-link').find_all("a")
            list2 = []
            for p in pdf1:
                list2.append(p.get('href') if p else "not given")
            print(list2)
        except:
            list2 = []
        print('*********Product Image***********')
        try:
            image1 = soup.find("div", {"class": "dover-img js-dover-img"}).find('img')
            image = (image1['src'] if image1 else "not given")
            print(image)
        except:
            image = "not given"

        print("******Technical Specifications: ******")
        prod1 = soup.find_all("span", class_="destaco-product-details__content")
        prod = [p1.text.strip() for p1 in prod1 if p1 is not None]

        prod_i = []
        spec_i = []
        for i in range(0, len(prod)):
            if i % 2:
                spec_i.append(prod[i])
            else:
                prod_i.append(prod[i])

        i = 0

        while i < len(prod_i):
            j = 0
            while j < len(spec_i):
                z = (prod_i[i] if prod_i else "not given")
                print(z)
                i += 1

                x = (spec_i[j] if spec_i else "not given")
                print(x)

                j += 1
                save_details: TextIO = open("destacoSys.txt", "a+", encoding="utf-8")
                save_details.write("\n" + product_url + "\t" + head + "\t" + tit \
                                   + "\t" + desc + "\t" + image + "\t" + " , ".join(list1) + "\t" + " , ".join(list2) \
                                   + "\t" + "RP_" + z + "\t" + "RP_" + x)
                save_details.close()
                print("\n**Record stored into txt file.**")


    except:
        save_details: TextIO = open("Rem_destacoSys.txt", "a+", encoding="utf-8")
        save_details.write("\n" + product_url)
        save_details.close()
        print("\n**Record stored into txt file.**")
