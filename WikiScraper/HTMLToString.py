import pandas as pd # library for data analysis

from bs4 import BeautifulSoup # library to parse HTML documents
from pathlib import Path 
import numpy as np
import re


i = 0
csvs = ['Battle_Brawlers_(Card_set).csv','Bakugan_Resurgence.csv','Age_of_Aurelus.csv','Armored_Elite.csv', 'Fusion_Force.csv','Shields_of_Vestroia.csv','PS1.csv', 'Secrets_of_the_Geogan.csv', 'GG.csv','EV.csv', 'EV2.csv', 'LE.csv', 'CP.csv']
while i < 1:
    
    filename = "./data/abilitycards/" + csvs[i]
    df = pd.read_csv(filename, dtype=str)
    #convert datafram to an array and replace all empty spaces with underscores
    text_list = df['Text'].to_numpy()
    card_text = []
    j = 0
    print('Converting text for : ' + csvs[i])
    while j < len(text_list):
        
        text_list[j] = str(text_list[j]).replace('<td colspan="3">',"")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Negate" title="Negate">Negate</a>', "Negate")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Action_Card" title="Action Card">Action Card</a>', "Action Card")
        text_list[j] = str(text_list[j]).replace('</td>',"")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Hero_Card" title="Hero Card">Hero Card</a>.', "Hero Card")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Pyrus#Reboot" title="Pyrus"><img alt="Pyrus" data-file-height="100" data-file-width="100" height="21" src="/images/thumb/6/6c/Bbp_pyrus.png/21px-Bbp_pyrus.png" srcset="/images/thumb/6/6c/Bbp_pyrus.png/32px-Bbp_pyrus.png 1.5x, /images/thumb/6/6c/Bbp_pyrus.png/42px-Bbp_pyrus.png 2x" width="21"/></a><span style="padding-left: 0.25em;">Â </span><a href="/wiki/Pyrus#Reboot" title="Pyrus">Pyrus</a>', "Pyrus")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Aquos#Reboot" title="Aquos"><img alt="Aquos" data-file-height="100" data-file-width="100" height="21" src="/images/thumb/e/ed/Bbp_aquos.png/21px-Bbp_aquos.png" srcset="/images/thumb/e/ed/Bbp_aquos.png/32px-Bbp_aquos.png 1.5x, /images/thumb/e/ed/Bbp_aquos.png/42px-Bbp_aquos.png 2x" width="21"/></a><span style="padding-left: 0.25em;">Â </span><a href="/wiki/Aquos#Reboot" title="Aquos">Aquos</a>', "Aquos")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Haos#Reboot" title="Haos"><img alt="Haos" data-file-height="100" data-file-width="100" height="21" src="/images/thumb/e/e0/Bbp_haos.png/21px-Bbp_haos.png" srcset="/images/thumb/e/e0/Bbp_haos.png/32px-Bbp_haos.png 1.5x, /images/thumb/e/e0/Bbp_haos.png/42px-Bbp_haos.png 2x" width="21"/></a><span style="padding-left: 0.25em;">Â </span><a href="/wiki/Haos#Reboot" title="Haos">Haos</a>', "Haos")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Darkus#Reboot" title="Darkus"><img alt="Darkus" data-file-height="100" data-file-width="100" height="21" src="/images/thumb/0/05/Bbp_darkus.png/21px-Bbp_darkus.png" srcset="/images/thumb/0/05/Bbp_darkus.png/32px-Bbp_darkus.png 1.5x, /images/thumb/0/05/Bbp_darkus.png/42px-Bbp_darkus.png 2x" width="21"/></a><span style="padding-left: 0.25em;">Â </span><a href="/wiki/Darkus#Reboot" title="Darkus">Darkus</a>' , "Darkus")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Ventus#Reboot" title="Ventus"><img alt="Ventus" data-file-height="100" data-file-width="100" height="21" src="/images/thumb/3/3a/Bbp_ventus.png/21px-Bbp_ventus.png" srcset="/images/thumb/3/3a/Bbp_ventus.png/32px-Bbp_ventus.png 1.5x, /images/thumb/3/3a/Bbp_ventus.png/42px-Bbp_ventus.png 2x" width="21"/></a><span style="padding-left: 0.25em;">Â </span><a href="/wiki/Ventus#Reboot" title="Ventus">Ventus</a>', "Ventus")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Aurelus" title="Aurelus"><img alt="Aurelus" src="/images/thumb/d/d6/Bbp_aurelus.png/21px-Bbp_aurelus.png" width="21" height="21" srcset="/images/thumb/d/d6/Bbp_aurelus.png/32px-Bbp_aurelus.png 1.5x, /images/thumb/d/d6/Bbp_aurelus.png/42px-Bbp_aurelus.png 2x" data-file-width="100" data-file-height="100"></a><span style="padding-left: 0.25em;">&nbsp;</span><a href="/wiki/Aurelus" title="Aurelus">Aurelus</a>' , "Aurelus")
        text_list[j] = str(text_list[j]).replace('<td><a href="/wiki/All-Faction" title="All-Faction"><img alt="All-Faction" src="/images/thumb/0/0d/Bbp_allfaction.png/21px-Bbp_allfaction.png" width="21" height="21" srcset="/images/thumb/0/0d/Bbp_allfaction.png/32px-Bbp_allfaction.png 1.5x, /images/thumb/0/0d/Bbp_allfaction.png/42px-Bbp_allfaction.png 2x" data-file-width="2281" data-file-height="2281"></a><span style="padding-left: 0.25em;">&nbsp;</span><a href="/wiki/All-Faction" title="All-Faction">All-Faction</a></td>', "All-Faction")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/B-Power" title="B-Power"><img alt="Icon-power.png" data-file-height="2071" data-file-width="2133" height="15" src="/images/thumb/d/d1/Icon-power.png/15px-Icon-power.png" srcset="/images/thumb/d/d1/Icon-power.png/23px-Icon-power.png 1.5x, /images/thumb/d/d1/Icon-power.png/30px-Icon-power.png 2x" width="15"/></a>', "B-Power")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Damage" title="Damage"><img alt="Icon-damage.png" data-file-height="1967" data-file-width="2084" height="24" src="/images/thumb/7/7f/Icon-damage.png/25px-Icon-damage.png" srcset="/images/thumb/7/7f/Icon-damage.png/38px-Icon-damage.png 1.5x, /images/thumb/7/7f/Icon-damage.png/50px-Icon-damage.png 2x" width="25"/></a>', "Damage")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Energy" title="Energy"><img alt="Battle Planet Energy Symbol.png" data-file-height="2758" data-file-width="2084" height="33" src="/images/thumb/8/80/Battle_Planet_Energy_Symbol.png/25px-Battle_Planet_Energy_Symbol.png" srcset="/images/thumb/8/80/Battle_Planet_Energy_Symbol.png/38px-Battle_Planet_Energy_Symbol.png 1.5x, /images/thumb/8/80/Battle_Planet_Energy_Symbol.png/50px-Battle_Planet_Energy_Symbol.png 2x" width="25"/></a> ', "Energy")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Fusion" title="Fusion"><img alt="Icon-BAA-Fusion.png" data-file-height="1248" data-file-width="2118" height="15" src="/images/thumb/9/95/Icon-BAA-Fusion.png/25px-Icon-BAA-Fusion.png" srcset="/images/thumb/9/95/Icon-BAA-Fusion.png/38px-Icon-BAA-Fusion.png 1.5x, /images/thumb/9/95/Icon-BAA-Fusion.png/50px-Icon-BAA-Fusion.png 2x" width="25"/></a>', "Fusion")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Baku-Gear" title="Baku-Gear">Baku-Gear</a>', "Baku-Gear")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Fist" title="Fist"><img alt="Battle Planet Fist Symbol.png" data-file-height="90" data-file-width="125" height="14" src="/images/thumb/4/4f/Battle_Planet_Fist_Symbol.png/20px-Battle_Planet_Fist_Symbol.png" srcset="/images/thumb/4/4f/Battle_Planet_Fist_Symbol.png/30px-Battle_Planet_Fist_Symbol.png 1.5x, /images/thumb/4/4f/Battle_Planet_Fist_Symbol.png/40px-Battle_Planet_Fist_Symbol.png 2x" width="20"/></a>',"Fist")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Flaming_Fist" title="Flaming Fist"><img alt="Battle Planet FlamingFist Symbol.png" data-file-height="92" data-file-width="125" height="15" src="/images/thumb/3/3a/Battle_Planet_FlamingFist_Symbol.png/20px-Battle_Planet_FlamingFist_Symbol.png" srcset="/images/thumb/3/3a/Battle_Planet_FlamingFist_Symbol.png/30px-Battle_Planet_FlamingFist_Symbol.png 1.5x, /images/thumb/3/3a/Battle_Planet_FlamingFist_Symbol.png/40px-Battle_Planet_FlamingFist_Symbol.png 2x" width="20"/></a>', "Flaming Fist")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Helix" title="Helix"><img alt="Battle Planet Helix Symbol.png" data-file-height="125" data-file-width="92" height="27" src="/images/thumb/3/3e/Battle_Planet_Helix_Symbol.png/20px-Battle_Planet_Helix_Symbol.png" srcset="/images/thumb/3/3e/Battle_Planet_Helix_Symbol.png/30px-Battle_Planet_Helix_Symbol.png 1.5x, /images/thumb/3/3e/Battle_Planet_Helix_Symbol.png/40px-Battle_Planet_Helix_Symbol.png 2x" width="20"/></a>', "Helix")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Magic_Shield" title="Magic Shield"><img alt="Battle Planet MagicShield Symbol.png" data-file-height="125" data-file-width="105" height="24" src="/images/thumb/0/06/Battle_Planet_MagicShield_Symbol.png/20px-Battle_Planet_MagicShield_Symbol.png" srcset="/images/thumb/0/06/Battle_Planet_MagicShield_Symbol.png/30px-Battle_Planet_MagicShield_Symbol.png 1.5x, /images/thumb/0/06/Battle_Planet_MagicShield_Symbol.png/40px-Battle_Planet_MagicShield_Symbol.png 2x" width="20"/></a>', "Magic Shield")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Shield" title="Shield"><img alt="Battle Planet Shield Symbol.png" data-file-height="125" data-file-width="93" height="27" src="/images/thumb/6/6a/Battle_Planet_Shield_Symbol.png/20px-Battle_Planet_Shield_Symbol.png" srcset="/images/thumb/6/6a/Battle_Planet_Shield_Symbol.png/30px-Battle_Planet_Shield_Symbol.png 1.5x, /images/thumb/6/6a/Battle_Planet_Shield_Symbol.png/40px-Battle_Planet_Shield_Symbol.png 2x" width="20"/></a>', "Shield")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/File:Add_Core_Icon.png" class="image"><img alt="Add Core Icon.png" src="/images/thumb/d/d7/Add_Core_Icon.png/25px-Add_Core_Icon.png" width="25" height="22" srcset="/images/thumb/d/d7/Add_Core_Icon.png/38px-Add_Core_Icon.png 1.5x, /images/thumb/d/d7/Add_Core_Icon.png/50px-Add_Core_Icon.png 2x" data-file-width="2406" data-file-height="2084"></a>', "Add Core")
        text_list[j] = str(text_list[j]).replace('<img alt="DrawaCard icon.png" data-file-height="2162" data-file-width="1960" height="28" src="/images/thumb/e/e2/DrawaCard_icon.png/25px-DrawaCard_icon.png" srcset="/images/thumb/e/e2/DrawaCard_icon.png/38px-DrawaCard_icon.png 1.5x, /images/thumb/e/e2/DrawaCard_icon.png/50px-DrawaCard_icon.png 2x" width="25"/>', "Draw")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/DoubleStrike" title="DoubleStrike"><img alt="Double Strike Icon.png" data-file-height="2175" data-file-width="2280" height="24" src="/images/thumb/8/8b/Double_Strike_Icon.png/25px-Double_Strike_Icon.png" srcset="/images/thumb/8/8b/Double_Strike_Icon.png/38px-Double_Strike_Icon.png 1.5x, /images/thumb/8/8b/Double_Strike_Icon.png/50px-Double_Strike_Icon.png 2x" width="25"/></a>', "DoubleStrike")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Dual_Baku-Gear" title="Dual Baku-Gear"><img alt="Icon-DoubleGear.png" src="/images/thumb/7/7f/Icon-DoubleGear.png/25px-Icon-DoubleGear.png" width="25" height="19" srcset="/images/thumb/7/7f/Icon-DoubleGear.png/38px-Icon-DoubleGear.png 1.5x, /images/thumb/7/7f/Icon-DoubleGear.png/50px-Icon-DoubleGear.png 2x" data-file-width="2221" data-file-height="1675"></a>', "Dual Baku-Gear")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/FrostStrike" title="FrostStrike"><img alt="FrostStrike Icon.png" data-file-height="2161" data-file-width="1886" height="29" src="/images/thumb/7/73/FrostStrike_Icon.png/25px-FrostStrike_Icon.png" srcset="/images/thumb/7/73/FrostStrike_Icon.png/38px-FrostStrike_Icon.png 1.5x, /images/thumb/7/73/FrostStrike_Icon.png/50px-FrostStrike_Icon.png 2x" width="25"/></a>', "FrostStrike")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/File:Remove_Core_Icon.png" class="image"><img alt="Remove Core Icon.png" src="/images/thumb/e/e3/Remove_Core_Icon.png/25px-Remove_Core_Icon.png" width="25" height="22" srcset="/images/thumb/e/e3/Remove_Core_Icon.png/38px-Remove_Core_Icon.png 1.5x, /images/thumb/e/e3/Remove_Core_Icon.png/50px-Remove_Core_Icon.png 2x" data-file-width="2406" data-file-height="2084"></a>', "Remove Core")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/File:Symbol_Reroll.png" class="image"><img alt="Symbol Reroll.png" src="/images/thumb/0/05/Symbol_Reroll.png/25px-Symbol_Reroll.png" width="25" height="27" srcset="/images/thumb/0/05/Symbol_Reroll.png/38px-Symbol_Reroll.png 1.5x, /images/thumb/0/05/Symbol_Reroll.png/50px-Symbol_Reroll.png 2x" data-file-width="530" data-file-height="562"></a>', "Reroll")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Scan" title="Scan"><img alt="Scan Icon.png" src="/images/thumb/e/e9/Scan_Icon.png/25px-Scan_Icon.png" width="25" height="25" srcset="/images/thumb/e/e9/Scan_Icon.png/38px-Scan_Icon.png 1.5x, /images/thumb/e/e9/Scan_Icon.png/50px-Scan_Icon.png 2x" data-file-width="444" data-file-height="436"></a>', "Scan")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/ShadowStrike" title="ShadowStrike"><img alt="ShadowStrike Icon.png" src="/images/thumb/0/02/ShadowStrike_Icon.png/25px-ShadowStrike_Icon.png" width="25" height="32" srcset="/images/thumb/0/02/ShadowStrike_Icon.png/38px-ShadowStrike_Icon.png 1.5x, /images/thumb/0/02/ShadowStrike_Icon.png/50px-ShadowStrike_Icon.png 2x" data-file-width="1712" data-file-height="2165"></a>', "ShadowStrike")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/File:Steal_Core_Icon.png" class="image"><img alt="Steal Core Icon.png" src="/images/thumb/6/60/Steal_Core_Icon.png/25px-Steal_Core_Icon.png" width="25" height="22" srcset="/images/thumb/6/60/Steal_Core_Icon.png/38px-Steal_Core_Icon.png 1.5x, /images/thumb/6/60/Steal_Core_Icon.png/50px-Steal_Core_Icon.png 2x" data-file-width="2406" data-file-height="2084"></a>', "Steal Core")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Team_Attack" title="Team Attack"><img alt="Team Attack Symbol.png" src="/images/thumb/5/5d/Team_Attack_Symbol.png/25px-Team_Attack_Symbol.png" width="25" height="20" srcset="/images/thumb/5/5d/Team_Attack_Symbol.png/38px-Team_Attack_Symbol.png 1.5x, /images/thumb/5/5d/Team_Attack_Symbol.png/50px-Team_Attack_Symbol.png 2x" data-file-width="2675" data-file-height="2137"></a>' , "Team Attack")
        text_list[j] = str(text_list[j]).replace('<a href="/wiki/Victor_(Reboot)" title="Victor (Reboot)"><img alt="Victor symbol.png" src="/images/thumb/4/45/Victor_symbol.png/25px-Victor_symbol.png" width="25" height="23" srcset="/images/thumb/4/45/Victor_symbol.png/38px-Victor_symbol.png 1.5x, /images/thumb/4/45/Victor_symbol.png/50px-Victor_symbol.png 2x" data-file-width="454" data-file-height="417"></a>', "Victor")
        text_list[j] = str(text_list[j]).replace("<p>", "")
        text_list[j] = str(text_list[j]).replace("</p>", "")
        text_list[j] = str(text_list[j]).replace("<i>", "")
        text_list[j] = str(text_list[j]).replace("</i>", "")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Boost"" title=""Boost"">Boost</a>', "Boost")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Energy_Card"" title=""Energy Card"">Energy cards</a>', "Energy cards")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Sync"" title=""Sync"">Sync</a>', "Sync")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/FrostStrike"" title=""FrostStrike"">FrostStrike</a>', "FrostStrike")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/ShadowStrike"" title=""ShadowStrike""><img alt=""ShadowStrike Icon.png"" data-file-height=""2165"" data-file-width=""1712"" height=""32"" src=""/images/thumb/0/02/ShadowStrike_Icon.png/25px-ShadowStrike_Icon.png"" srcset=""/images/thumb/0/02/ShadowStrike_Icon.png/38px-ShadowStrike_Icon.png 1.5x, /images/thumb/0/02/ShadowStrike_Icon.png/50px-ShadowStrike_Icon.png 2x"" width=""25""/></a>', "ShadowStrike")
        text_list[j] = str(text_list[j]).replace("&amp;", "&")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Rapid_Fire_(Armored_Alliance)"" title=""Rapid Fire (Armored Alliance)"">Rapid Fire</a>', "Rapid Fire")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Hero_Card"" title=""Hero Card"">Hero</a>.', "Hero")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Empower"" title=""Empower"">Empower</a>', "Empower")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Haos#Reboot"" title=""Haos""><img alt=""Haos"" data-file-height=""100"" data-file-width=""100"" height=""21"" src=""/images/thumb/e/e0/Bbp_haos.png/21px-Bbp_haos.png"" srcset=""/images/thumb/e/e0/Bbp_haos.png/32px-Bbp_haos.png 1.5x, /images/thumb/e/e0/Bbp_haos.png/42px-Bbp_haos.png 2x"" width=""21""/></a><span style=""padding-left: 0.25em;""> </span><a href=""/wiki/Haos#Reboot"" title=""Haos"">Haos</a>', "Haos")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Reroll"" title=""Reroll"">Reroll</a>',"Reroll")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Trifecta"" title=""Trifecta"">Trifecta</a>', "Trifecta")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Pyrus#Reboot"" title=""Pyrus""><img alt=""Pyrus"" data-file-height=""100"" data-file-width=""100"" height=""21"" src=""/images/thumb/6/6c/Bbp_pyrus.png/21px-Bbp_pyrus.png"" srcset=""/images/thumb/6/6c/Bbp_pyrus.png/32px-Bbp_pyrus.png 1.5x, /images/thumb/6/6c/Bbp_pyrus.png/42px-Bbp_pyrus.png 2x"" width=""21""/></a><span style=""padding-left: 0.25em;""> </span><a href=""/wiki/Pyrus#Reboot"" title=""Pyrus"">Pyrus</a>', "Pyrus")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Victor_(Reboot)"" title=""Victor (Reboot)""><img alt=""Victor symbol.png"" data-file-height=""417"" data-file-width=""454"" height=""23"" src=""/images/thumb/4/45/Victor_symbol.png/25px-Victor_symbol.png"" srcset=""/images/thumb/4/45/Victor_symbol.png/38px-Victor_symbol.png 1.5x, /images/thumb/4/45/Victor_symbol.png/50px-Victor_symbol.png 2x"" width=""25""/></a> (<a href=""/wiki/Victor_(Reboot)"" title=""Victor (Reboot)"">Victor</a>', "Victor")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Flip_Card"" title=""Flip Card"">Flip cards</a>', "Flip cards")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Darkus#Reboot"" title=""Darkus""><img alt=""Darkus"" data-file-height=""100"" data-file-width=""100"" height=""21"" src=""/images/thumb/0/05/Bbp_darkus.png/21px-Bbp_darkus.png"" srcset=""/images/thumb/0/05/Bbp_darkus.png/32px-Bbp_darkus.png 1.5x, /images/thumb/0/05/Bbp_darkus.png/42px-Bbp_darkus.png 2x"" width=""21""/></a><span style=""padding-left: 0.25em;""> </span><a href=""/wiki/Darkus#Reboot"" title=""Darkus"">Darkus</a>', "Darkus")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Aquos#Reboot"" title=""Aquos""><img alt=""Aquos"" data-file-height=""100"" data-file-width=""100"" height=""21"" src=""/images/thumb/e/ed/Bbp_aquos.png/21px-Bbp_aquos.png"" srcset=""/images/thumb/e/ed/Bbp_aquos.png/32px-Bbp_aquos.png 1.5x, /images/thumb/e/ed/Bbp_aquos.png/42px-Bbp_aquos.png 2x"" width=""21""/></a><span style=""padding-left: 0.25em;""> </span><a href=""/wiki/Aquos#Reboot"" title=""Aquos"">Aquos</a>', "Aquos")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Ventus#Reboot"" title=""Ventus""><img alt=""Ventus"" data-file-height=""100"" data-file-width=""100"" height=""21"" src=""/images/thumb/3/3a/Bbp_ventus.png/21px-Bbp_ventus.png"" srcset=""/images/thumb/3/3a/Bbp_ventus.png/32px-Bbp_ventus.png 1.5x, /images/thumb/3/3a/Bbp_ventus.png/42px-Bbp_ventus.png 2x"" width=""21""/></a><span style=""padding-left: 0.25em;""> </span><a href=""/wiki/Ventus#Reboot"" title=""Ventus"">Ventus</a>', "Ventus")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Action_Card"" title=""Action Card"">Action</a>', "Action Card")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Baku-Gear_Card"" title=""Baku-Gear Card"">Baku-Gear</a>', "Baku-Gear")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Evo_Card"" title=""Evo Card"">Evo</a>',"Evo Card")
        text_list[j] = str(text_list[j]).replace('<span style=""padding-left: 0.25em;""> </span><a href=""/wiki/Aquos#Reboot"" title=""Aquos"">Aquos</a>', "")
        print(text_list[1])
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Aquos#Reboot"" title=""Aquos""><img alt=""Aquos"" data-file-height=""100"" data-file-width=""100"" height=""21"" src=""/images/thumb/e/ed/Bbp_aquos.png/21px-Bbp_aquos.png"" srcset=""/images/thumb/e/ed/Bbp_aquos.png/32px-Bbp_aquos.png 1.5x, /images/thumb/e/ed/Bbp_aquos.png/42px-Bbp_aquos.png 2x"" width=""21""/></a>', "Aquos")
        text_list[j] = str(text_list[j]).replace('<a href=""/wiki/Stop"" title=""Stop""><img alt=""Battle Planet Stop Symbol.png"" data-file-height=""2232"" data-file-width=""2578"" height=""22"" src=""/images/thumb/f/fc/Battle_Planet_Stop_Symbol.png/25px-Battle_Planet_Stop_Symbol.png"" srcset=""/images/thumb/f/fc/Battle_Planet_Stop_Symbol.png/38px-Battle_Planet_Stop_Symbol.png 1.5x, /images/thumb/f/fc/Battle_Planet_Stop_Symbol.png/50px-Battle_Planet_Stop_Symbol.png 2x"" width=""25""/></a>', "Stop")
        card_text.append(text_list[j])
        j+=1
    

    card = 0
    while card < len(card_text):
        html = BeautifulSoup(card_text[card])
        title = html.find('a')
        m=re.compile('<a>(.*?)</a>',title)
        print(m)
        card += 1

    export_arry = np.array(card_text)
    df = pd.DataFrame(card_text, columns = ['Text'])
    print(df.head())
    i+=1
    # ##save csv
    # print("SAVING FILE...")
    # path = 'data/abilitycards/' + csvs[i] + 'converted.csv'
    # filepath = Path(path)  
    # filepath.parent.mkdir(parents=True, exist_ok=True)  
    # df.to_csv(filepath) 
    # i+=1



 

