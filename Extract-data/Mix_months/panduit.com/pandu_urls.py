import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver.maximize_window()
Result = [
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-basket/basket.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-conduit-supports/cable-conduit-brackets.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-conduit-supports/cable-conduit-hangers.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-conduit-supports/cable-conduit-managers-grommets.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-wire-ties-mounts-straps/cable-bundling-straps-tools.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-conduit-supports/cable-conduit-clamps-clips.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-cleats/cable-cleats.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/abrasion-protection/cable-entry-systems.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-basket/cable-exits.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-wire-ties-mounts-straps/cable-jumper-troughs.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-wire-ties-mounts-straps/cable-marking-pens.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/abrasion-protection/cable-sleeves-tools-wraps.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-wire-ties-mounts-straps/cable-tie-accessories.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-wire-ties-mounts-straps/cable-tie-installation-tools-accessories.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-wire-ties-mounts-straps/cable-tie-kits.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-wire-ties-mounts-straps/cable-tie-mounts.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-wire-ties-mounts-straps/cable-wire-ties.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/abrasion-protection/corrugated-loom-tubing-fittings.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/abrasion-protection/duct-seal.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/fiber-routing-systems/fiber-competitive-adapter-fittings.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/fiber-routing-systems/fiber-routing-adapters.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/fiber-routing-systems/fiber-routing-bends-crosses-tees-end-caps.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/fiber-routing-systems/fiber-routing-channel-covers.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/fiber-routing-systems/fiber-routing-couplers.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/fiber-routing-systems/fiber-routing-mounting-brackets-hardware.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/fiber-routing-systems/fiber-routing-reducers.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/fiber-routing-systems/fiber-routing-spillouts.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/fiber-routing-systems/fiber-routing-system-installation-tools.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-wire-ties-mounts-straps/flat-cable-mounts.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/electrical-tape/friction-tape.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/abrasion-protection/grommet-edging.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-basket/hardware.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/harness-boards-accessories/harness-board-accessories.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/harness-boards-accessories/harness-board-building-elements.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/abrasion-protection/heat-shrink-tubing-accessories.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/hook-and-loop-cable-ties/hook-and-loop-cable-ties.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-basket/intersection.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/electrical-tape/mastic-tape.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-basket/mounting-brackets.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/surface-raceway-systems/multichannel-raceway.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/abrasion-protection/non-shrink-tubing.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/power-communication-poles-accessories/power-communication-pole-accessories.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/power-communication-poles-accessories/power-communication-poles.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/electrical-tape/pvc-electrical-tape.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/electrical-tape/rubber-tape.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/surface-raceway-systems/single-channel-raceway.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/surface-raceway-systems/surface-raceway-installation-tools.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/surface-raceway-systems/surface-raceway-receptacles.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/surface-raceway-systems/surface-raceway-snap-on-faceplates.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/hook-and-loop-cable-ties/ultra-cinch-hook-and-loop-cable-ties.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-basket/accessories.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-basket/wire-basket-splices.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-mesh-cable-tray-systems/wire-mesh-accessories.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-mesh-cable-tray-systems/wire-mesh-cable-tray-installation-tools.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-mesh-cable-tray-systems/wire-mesh-connectors.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-mesh-cable-tray-systems/wire-mesh-mounting-brackets.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-mesh-cable-tray-systems/wire-mesh-pathways.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wire-mesh-cable-tray-systems/wire-mesh-waterfalls.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/cable-conduit-supports/wire-saddles-standoffs-retainers.html',
    'https://www.panduit.com/en/products/wire-routing-management-protection/wiring-duct-accessories/wiring-duct-duct-covers.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wiring-duct-accessories/wiring-duct-accessories.html',
    # 'https://www.panduit.com/en/products/wire-routing-management-protection/wiring-duct-accessories/wiring-duct-tools.html',
    # 'https://www.panduit.com/en/products/wire-termination/crimpers-cutters-strippers-accessories/cable-tool-accessories.html',
    # 'https://www.panduit.com/en/products/wire-termination/crimpers-cutters-strippers-accessories/crimping-tool-kits.html',
    # 'https://www.panduit.com/en/products/wire-termination/crimpers-cutters-strippers-accessories/crimping-tools-pumps-accessories.html',
    # 'https://www.panduit.com/en/products/wire-termination/crimpers-cutters-strippers-accessories/cutters-strippers.html',
    # 'https://www.panduit.com/en/products/wire-termination/terminals-terminal-kits/disconnects.html',
    # 'https://www.panduit.com/en/products/wire-termination/terminals-terminal-kits/ferrules.html',
    # 'https://www.panduit.com/en/products/wire-termination/terminals-terminal-kits/fork-terminals.html',
    # 'https://www.panduit.com/en/products/wire-termination/lugs-splices-split-bolts-accessories/htap-connectors--covers-and-kits.html',
    # 'https://www.panduit.com/en/products/wire-termination/lugs-splices-split-bolts-accessories/lug-splice-connector-accessories.html',
    # 'https://www.panduit.com/en/products/wire-termination/lugs-splices-split-bolts-accessories/mechanical-compression-lugs-splices.html',
    # 'https://www.panduit.com/en/products/wire-termination/terminals-terminal-kits/pin-terminals.html',
    # 'https://www.panduit.com/en/products/wire-termination/terminals-terminal-kits/ring-terminals.html',
    # 'https://www.panduit.com/en/products/wire-termination/lugs-splices-split-bolts-accessories/splices.html',
    # 'https://www.panduit.com/en/products/wire-termination/lugs-splices-split-bolts-accessories/split-bolts.html',
    # 'https://www.panduit.com/en/products/wire-termination/crimpers-cutters-strippers-accessories/stud-punches.html',
    # 'https://www.panduit.com/en/products/wire-termination/terminals-terminal-kits/terminal-kits-accessories.html',
    # 'https://www.panduit.com/en/products/wire-termination/terminals-terminal-kits/wire-joints.html',
    # 'https://www.panduit.com/en/products/contractor-products/cable-tie-accessories/4-way-mounts.html',
    # 'https://www.panduit.com/en/products/contractor-products/supports-and-fasteners/acoustical.html',
    # 'https://www.panduit.com/en/products/contractor-products/cable-tie-accessories/adhesive-backed-mounts.html',
    # 'https://www.panduit.com/en/products/contractor-products/cable-tie-accessories/anchor-mounts.html',
    # 'https://www.panduit.com/en/products/contractor-products/supports-and-fasteners/beam-purlin.html',
    # 'https://www.panduit.com/en/products/contractor-products/terminals/blade-terminal.html',
    # 'https://www.panduit.com/en/products/contractor-products/terminals/bullet-connectors.html',
    # 'https://www.panduit.com/en/products/contractor-products/supports-and-fasteners/cable-conduit.html',
    # 'https://www.panduit.com/en/products/contractor-products/cable-ties/clamp-style-cable-ties.html',
    # 'https://www.panduit.com/en/products/contractor-products/supports-and-fasteners/communication-low-voltage.html',
    # 'https://www.panduit.com/en/products/contractor-products/stainless-steel/custom-strapping.html',
    # 'https://www.panduit.com/en/products/contractor-products/supports-and-fasteners/dry-wall.html',
    # 'https://www.panduit.com/en/products/contractor-products/stainless-steel/fully-coated-stainless-steel-ties.html',
    # 'https://www.panduit.com/en/products/contractor-products/supports-and-fasteners/hangers-hanging-systems.html',
    # 'https://www.panduit.com/en/products/contractor-products/cable-ties/heavy-cable-ties.html',
    # 'https://www.panduit.com/en/products/contractor-products/cable-ties/intermediate-cable-ties.html',
    # 'https://www.panduit.com/en/products/contractor-products/cable-ties/light-heavy-cable-ties.html',
    # 'https://www.panduit.com/en/products/contractor-products/cable-ties/miniature-cable-ties.html',
    # 'https://www.panduit.com/en/products/contractor-products/supports-and-fasteners/miscellaneous.html',
    # 'https://www.panduit.com/en/products/contractor-products/wire-markers/pre-printed.html',
    # 'https://www.panduit.com/en/products/contractor-products/cable-ties/releasable-cable-tie.html',
    # 'https://www.panduit.com/en/products/contractor-products/stainless-steel/stainless-steel-cable-ties.html',
    # 'https://www.panduit.com/en/products/contractor-products/cable-ties/standard-cable-ties.html',
    # 'https://www.panduit.com/en/products/contractor-products/cable-tie-accessories/standard-screw-applied-mounts.html',
    # 'https://www.panduit.com/en/products/contractor-products/electrical-tape/stronghold-tm--friction-tape.html',
    # 'https://www.panduit.com/en/products/contractor-products/electrical-tape/stronghold-tm--mastic-tape.html',
    # 'https://www.panduit.com/en/products/contractor-products/electrical-tape/stronhold-tm--pvc-tape.html',
    # 'https://www.panduit.com/en/products/contractor-products/electrical-tape/stronghold-tm--rubber-tape.html',
    # 'https://www.panduit.com/en/products/contractor-products/terminals/disconnects.html',
    # 'https://www.panduit.com/en/products/contractor-products/terminals/fork-terminals.html',
    # 'https://www.panduit.com/en/products/contractor-products/terminals/pin-terminals.html',
    # 'https://www.panduit.com/en/products/contractor-products/terminals/ring-terminals.html',
    # 'https://www.panduit.com/en/products/contractor-products/terminals/splices.html',
    # 'https://www.panduit.com/en/products/contractor-products/terminals/wire-joints.html',
    # 'https://www.panduit.com/en/products/contractor-products/supports-and-fasteners/stud-wall.html',
    # 'https://www.panduit.com/en/products/contractor-products/wire-markers/write-on.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/automated-labeling/accessories.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/safety-identification-tape/barricade-warning-tape.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/tags/blank-write-on-tags.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/labels-markers-printers/desktop-printer-labels.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/signs-accessories/desktop-printer-signs.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/tags/desktop-printer-tags.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/safety-identification-tape/floor-marking-tape.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/labels-markers-printers/label-marker-accessories.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/automated-labeling/label-applicators.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/labels-markers-printers/label-printers-accessories.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/automated-labeling/labels.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/letters-numbers/letters-numbers.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/labels-markers-printers/metal-marker-plates-tags-machines.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/labels-markers-printers/pipe-conduit-snap-on-labels.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/labels-markers-printers/portable-printer-labels-cassettes.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/labels-markers-printers/pre-printed-write-on-safety-qa-labels.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/labels-markers-printers/pre-printed-write-on-wire-identification-labels.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/automated-labeling/ribbons.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/tags/safety-compliance-tags.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/signs-accessories/pre-printed-write-on-safety-signs.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/sign-label-printing-software/sign-label-printing-software.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/signs-accessories/sign-carriers.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/safety-identification-tape/thermal-transfer-printable-tape.html',
    # 'https://www.panduit.com/en/products/signs-labels-identification/safety-identification-tape/underground-hazard-tape.html',
    # 'https://www.panduit.com/en/products/safety-security/active-safety-devices/absence-of-voltage-tester-accessories.html',
    # 'https://www.panduit.com/en/products/safety-security/active-safety-devices/absence-of-voltage-tester-kits.html',
    # 'https://www.panduit.com/en/products/safety-security/active-safety-devices/absence-of-voltage-testers.html',
    # 'https://www.panduit.com/en/products/safety-security/active-safety-devices/data-access-ports.html',
    # 'https://www.panduit.com/en/products/safety-security/ghs-safety-training-kits-components/ghs-safety-training-kits-components.html',
    # 'https://www.panduit.com/en/products/safety-security/lockout-tagout/group-lockout-boxes.html',
    # 'https://www.panduit.com/en/products/safety-security/lockout-tagout/lockout-tagout-devices.html',
    # 'https://www.panduit.com/en/products/safety-security/lockout-tagout/lockout-tagout-hasps.html',
    # 'https://www.panduit.com/en/products/safety-security/lockout-tagout/lockout-tagout-kits-stations.html',
    # 'https://www.panduit.com/en/products/safety-security/padlocks-cabinet-locks/padlock-accessories.html',
    # 'https://www.panduit.com/en/products/safety-security/padlocks-cabinet-locks/padlock-labels.html',
    # 'https://www.panduit.com/en/products/safety-security/padlocks-cabinet-locks/padlocks.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/ups-accessories/batteries.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/ups-accessories/environmental---security.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/pdu-accessories/environmental-sensors.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/intelligent-connectivity-accessories/expansion-modules.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/industrial-uninterruptible-power-supplies--iups-/industrial-uninterruptible-power-supplies--iups-.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/intelligent-connectivity-accessories/intelligent-connectivity-accessories.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/pdu-accessories/pdu-accessories.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/pdu-power-cords/power-cords.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/pdu-accessories/security-access-control-devices.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/power-distribution-units-(pdus)/pdus.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/ups-accessories/ups-accessories.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/ups-accessories/miscellaneous-accessories.html',
    # 'https://www.panduit.com/en/products/power-distribution-environmental-connectivity-hardware/uninterruptible-power-supplies-ups/uninterruptible-power-supplies.html',
    # 'https://www.panduit.com/en/products/monitoring-and-services/data-center-software/cooling-active-control-software.html',
    # 'https://www.panduit.com/en/products/monitoring-and-services/industrial-services/industrial-services.html',
    # 'https://www.panduit.com/en/products/monitoring-and-services/industrial-monitoring/industrial-software.html',
    # 'https://www.panduit.com/en/products/monitoring-and-services/data-center-software/On-premise-Data-Center-Infrastructure-Management-Software.html',
    # 'https://www.panduit.com/en/products/monitoring-and-services/data-center-software/SaaS-Data-Center-Infrastructure-Management-Software.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-mechanical-connectors/access-floor-grounding-clamps.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-esd-hardware-accessories/auxiliary-cable-brackets.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-compression-connectors-covers/cross-connectors.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-compression-connectors-covers/ctap-connectors.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-compression-connectors-covers/direct-burial-lugs.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-compression-connectors-covers/e-style-connectors.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/bonding-straps-jumpers/equipment-bonding-kits.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-esd-hardware-accessories/esd-port-kits-and-wrist-straps.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-compression-connectors-covers/FIG8-Compression-Connectors.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/bonding-straps-jumpers/flat-braided-bonding-straps.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-mechanical-connectors/flat-surface-grounding-clamps.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-mechanical-connectors/GPWC-Grounding-Pipe-Clamps.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-compression-connectors-covers/ground-plates.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-esd-hardware-accessories/grounding-bonding-hardware.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/bonding-straps-jumpers/grounding-bonding-pigtails.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-busbars-strips/grounding-busbar-kits.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-busbars-strips/grounding-busbars.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-compression-connectors-covers/grounding-pigtail-compression-connectors.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-mechanical-connectors/grounding-rod-clamps.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-busbars-strips/grounding-strip-kits.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-esd-hardware-accessories/Joint-Compound.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-esd-hardware-accessories/mounting-hardware-kits.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-mechanical-connectors/one-hole-lugs.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-mechanical-connectors/pipe-tube-grounding-clamps.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/bonding-straps-jumpers/power-pigtails.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-mechanical-connectors/service-post-connectors.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-compression-connectors-covers/direct-burial-accessories.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-mechanical-connectors/u-bolt-grounding-clamps.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-mechanical-connectors/universal-beam-grounding-clamps.html',
    # 'https://www.panduit.com/en/products/grounding-bonding/grounding-busbars-strips/universal-grounding-bars.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-cable-assemblies/aoc--active-optical-cables-.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-tools-accessories/fiber-optic-accessories.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-adapters-connectors/fiber-optic-adapters.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-cable-assemblies/fiber-optic-breakout-harnesses.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-panels-cassettes-enclosures/fiber-optic-cassettes.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-tools-accessories/fiber-optic-cleaning-supplies.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-adapters-connectors/fiber-optic-connectors.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-panels-cassettes-enclosures/fiber-optic-enclosure-accessories.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-panels-cassettes-enclosures/fiber-optic-enclosures.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-cable-assemblies/fiber-optic-interconnects-patch-cords-pigtails.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-panels-cassettes-enclosures/fiber-optic-panels.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-tools-accessories/fiber-optic-termination-kits.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-tools-accessories/fiber-optic-tools.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/fiber-optic-cable-assemblies/fiber-optic-trunk-cable-assemblies.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/bulk-fiber-optic-cable/hybrid-powered-fiber-optic-cable.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/bulk-fiber-optic-cable/indoor-fiber-optic-cable.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/bulk-fiber-optic-cable/indoor-outdoor-fiber-optic-cable.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/industrial-fiber-optic-systems/industrial-fiber-optic-cable.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/industrial-fiber-optic-systems/industrial-fiber-optic-faceplates-outlets-adapters.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/industrial-fiber-optic-systems/industrial-fiber-optic-patch-cords-pigtails.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/industrial-fiber-optic-systems/outdoor-fiber-closures-and-accessories.html',
    # 'https://www.panduit.com/en/products/fiber-optic-systems/bulk-fiber-optic-cable/outside-plant-fiber-optic-cable.html',
    # 'https://www.panduit.com/en/products/copper-systems/physical-security-devices/block-out-devices.html',
    # 'https://www.panduit.com/en/products/copper-systems/cable-trunks-switch-harnesses/cable-trunks-switch-harnesses.html',
    # 'https://www.panduit.com/en/products/copper-systems/cross-connect-system/connecting-blocks.html',
    # 'https://www.panduit.com/en/products/copper-systems/connectors/connector-tools-accessories.html',
    # 'https://www.panduit.com/en/products/copper-systems/copper-system-tools-accessories/copper-system-tools-accessories.html',
    # 'https://www.panduit.com/en/products/copper-systems/cross-connect-system/cross-connect-bases.html',
    # 'https://www.panduit.com/en/products/copper-systems/cross-connect-system/cross-connect-patch-connectors.html',
    # 'https://www.panduit.com/en/products/copper-systems/cross-connect-system/cross-connect-rack-mount-kits.html',
    # 'https://www.panduit.com/en/products/copper-systems/cross-connect-system/cross-connect-tools-accessories.html',
    # 'https://www.panduit.com/en/products/copper-systems/cross-connect-system/cross-connect-tower-kits.html',
    # 'https://www.panduit.com/en/products/copper-systems/cross-connect-system/cross-connect-patch-cords.html',
    # 'https://www.panduit.com/en/products/copper-systems/direct-attach-cable-assemblies/direct-attach-cable-assemblies.html',
    # 'https://www.panduit.com/en/products/copper-systems/bulk-copper-cable/enterprise-data-center-copper-cable.html',
    # 'https://www.panduit.com/en/products/copper-systems/faceplates-boxes/faceplate-accessories.html',
    # 'https://www.panduit.com/en/products/copper-systems/faceplates-boxes/faceplate-frame-system.html',
    # 'https://www.panduit.com/en/products/copper-systems/faceplates-boxes/faceplates.html',
    # 'https://www.panduit.com/en/products/copper-systems/industrial-copper-systems/industrial-copper-cable.html',
    # 'https://www.panduit.com/en/products/copper-systems/industrial-copper-systems/industrial-copper-connectors.html',
    # 'https://www.panduit.com/en/products/copper-systems/industrial-copper-systems/industrial-copper-faceplates-outlets-panels.html',
    # 'https://www.panduit.com/en/products/copper-systems/industrial-copper-systems/industrial-copper-patch-cords.html',
    # 'https://www.panduit.com/en/products/copper-systems/industrial-copper-systems/industrial-overmolded-cordsets.html',
    # 'https://www.panduit.com/en/products/copper-systems/connectors/jack-modules.html',
    # 'https://www.panduit.com/en/products/copper-systems/physical-security-devices/lock-in-devices.html',
    # 'https://www.panduit.com/en/products/copper-systems/industrial-copper-systems/mcc-cable-assemblies.html',
    # 'https://www.panduit.com/en/products/copper-systems/patch-panels-accessories/modular-patch-panels.html',
    # 'https://www.panduit.com/en/products/copper-systems/connectors/modular-plugs.html',
    # 'https://www.panduit.com/en/products/copper-systems/patch-cords-accessories/patch-cord-accessories.html',
    # 'https://www.panduit.com/en/products/copper-systems/patch-cords-accessories/patch-cords.html',
    # 'https://www.panduit.com/en/products/copper-systems/patch-panels-accessories/patch-panel-accessories.html',
    # 'https://www.panduit.com/en/products/copper-systems/patch-panels-accessories/patch-panel-kits.html',
    # 'https://www.panduit.com/en/products/copper-systems/patch-panels-accessories/patch-panel-labels.html',
    # 'https://www.panduit.com/en/products/copper-systems/patch-panels-accessories/populated-patch-panels.html',
    # 'https://www.panduit.com/en/products/copper-systems/connectors/power-over-ethernet--poe-.html',
    # 'https://www.panduit.com/en/products/copper-systems/cross-connect-system/punchdown-base-kits.html',
    # 'https://www.panduit.com/en/products/copper-systems/faceplates-boxes/surface-mount-boxes.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/thermal-management-containment/air-inlet-exhaust-duct.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/thermal-management-containment/air-sealing-accessories.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/thermal-management-containment/aisle-containment.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/cabinets-accessories/cabinet-accessories.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/cabinets-accessories/cabinets.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/cable-managers-accessories/cable-manager-accessories.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/enclosures-accessories/enclosure-accessories.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/enclosures-accessories/enclosures.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/cable-managers-accessories/horizontal-cable-managers.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/cabinets-accessories/micro-data-centers.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/enclosures-accessories/pre-configured-enclosures.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/racks-accessories/rack-accessories.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/racks-accessories/racks.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/cable-managers-accessories/vertical-cable-managers.html',
    # 'https://www.panduit.com/en/products/cabinets-thermal-management-racks-enclosures/thermal-management-containment/vertical-exhaust-duct.html',
    # 'https://www.panduit.com/en/products/audio-video-systems/above-floor-raceway-and-fittings/above-floor-raceway-fittings.html',
    # 'https://www.panduit.com/en/products/audio-video-systems/atlona-active-devices.html',
    # 'https://www.panduit.com/en/products/audio-video-systems/audio-video-modules/audio-video-modules.html',
    # 'https://www.panduit.com/en/products/audio-video-systems/audio-video-patch-cords/audio-video-patch-cords.html',
    # 'https://www.panduit.com/en/products/audio-video-systems/pass-through-faceplate-inserts/pass-through-faceplate-inserts.html',
    # 'https://www.panduit.com/en/products/audio-video-systems/table-boxes/table-boxes.html',
    # 'https://www.panduit.com/en/products/audio-video-systems/wall-boxes-and-accessories/wall-boxes-and-accessories.html',
    # 'https://www.panduit.com/en/products/audio-video-systems/wall-mount-cabinets/wall-mount-cabinets.html',

]
for url in Result:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    driver.get(url)
    # driver.get(driver.current_url)
    time.sleep(5)
    print("Products Urls", url)

    # links = driver.find_element(By.XPATH, "//div[@id='coveo-full-results']").find_elements(By.TAG_NAME, 'a')
    # for x in links:
    #     url_links = (x.get_attribute('href'))
    #     data_urls = ("'" + url_links + "',")
    #     print("up", data_urls)

    l = driver.find_element(By.XPATH, "//span[@class='CoveoQuerySummary']")
    c = l.text.replace(',', '').split()[-1]
    print("count = ", c)
    length = round(int(c) / 30 + 1)
    print(length)
    for l in range(1, length):
        print(l)
        s = l*30

        hg = '#first='+str(s)+'&sort=%40mpt_weight%20descending%3B%40mpt_rev_rank%20ascending'
        h = url+hg
        print(h)
        driver.get(h)
        time.sleep(4)

        # button = driver.find_element(By.XPATH, "//span[@class='coveo-pager-next-icon']//*[name()='svg']")
        # driver.execute_script("arguments[0].click();", button)
        # # driver.find_element(By.XPATH, "//span[@class='coveo-pager-next-icon']//*[name()='svg']").click()
        # print(l)
        # time.sleep(3)
        # links = driver.find_element(By.XPATH, "//div[@id='coveo-full-results']").find_elements(By.TAG_NAME, 'a')
        # for x in links:
        #     url_links = (x.get_attribute('href'))
        #     data_urls = ("'" + url_links + "',")
        #     print(data_urls)
        # save_details: url_links = open("urls_links.xlsx", "a+", encoding="utf-8")
        # save_details.write("\n" + data_urls)
        # print("End")
        # save_details.close()
        # print("\n ***** Record stored into urls  files. *****")
        # print(i)



