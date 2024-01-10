import random
import requests
import pandas as pd
from bs4 import BeautifulSoup
import googlemaps
from datetime import datetime
import time

URL = "https://www.dealerrater.com/directory/New-Jersey/Used-Car-Dealer/"
page = requests.get(URL)
names = []
soup = BeautifulSoup(page.content, "html.parser")
for page in range(2,36):
    URL = f"https://www.dealerrater.com/directory/New-Jersey/Used-Car-Dealer/page{page}/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(id="dealerName")
    locs = [i.find_next('span').text for i in results]
    names.extend(locs)
names = set(names)


URL = 'https://en.wikipedia.org/wiki/List_of_current_automobile_marques'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all('li')
brands = [i.text for i in results]
cleaned_brands = []
for brand in brands:
    if len(brand) >= 6 and brand[-1]== ')' :
        #cleaned_brands.append(brand[:-7])
        if '[' in brand:
            index = brand.index('[')
            cleaned_brands.append(brand[:index])
            continue
        elif 'see' in brand:
            index = brand.index('see')
        elif '(' in brand:
            index = brand.index('(')
        else:
            index = brand.index(' ')
        cleaned_brands.append(brand[:index-1])
ex_brands = {'Kaiyi','Tauro Sport Auto','Vega','Yuanhang:','Rimac','Drako Motors','Fownix:','9ff','Buddy','Mega','Steinmetz','Force','Elio','Galpin','Autech','Škoda','Zotye','Callaway','Tata','Carver','Trion','Wheego','Ineos','BYD','AC','OAA','GAC','BJEV','VGV','Ronin','Maxus','Elfin','Wallscar','Esemka','Karry','Anteros','Thai Rung','Faraday Future','Fengon:','Techrules','DFSK','Arcfox','Morgan,','ZX','BJEV','XPeng','EVO:','Pratt & Miller','Hulas Motors','Dacia','Ghia','HSV','SSC','VDL Nedcar','Nio','Dallar','Noble','LEVC','Czinger','Kandi','Ranz','Wuling','Artega','Great Wall',' TRD',' TOGG','Aeolus','Beijing','Alternative Cars','Lifan','Soueast','VeilSide','EMC','Arrinera','Mobius','Carlsson','Mugen','Cirelli','Exeed','GAZ','Haval','Impul','Denza','Bolloré','ICKX','Bajaj','Rometsh','Spiess','JMC','SEAT','Koenig','Yuanhang','JAC','KGM','HKS','VGV','MTM','Detroit Electric','Yulon','Kiira','Chirey','Livan','VDL','Bufori','Qoros','WaterCar','Changhe','Paxton','Li Auto','Perodua','Lightning','VGV','FMC','TVR','Ora','Zenos Cars','Fownix','Fraser','VinFast','Valmet','Chery','Fisher Body','RTR','Dayun','Glickenhaus,','Magna Stenyr','Wiesmann','Chamonix','OAA,','Qvale','Lada','Englon','Radical','Kantanka','Vauxhall','Forthing','AC Propulsion','GTA','Zinoro','Alpina','Zinoro','Brabus','Tushek&Spigel','ZAZ','VGV','Foday','Daihatsu','Gazoo Racing','Forthing','SiTech','Nanjing','Geely','Vencer','IKCO','Citrus fruit','HiPhi','WCC','Sehol','Comau','FAW','EDAG','PAL-V','Napier','Trumpchi','Hoesch','Abart','Zeekr','Delage','Italdesign Giugiaro','Etox','GEM','DR','Jonway','Gemoetry','Dallar','Dinan','Baojun','Bordrin','G-Power','Roding','smart','Ciwei','Lobini','Loremo','Isdera','Zamyad','Foton','Pininfarina','Seres','HPD','Eibach','Westfield','Vandenbrink','Sportequipe:','Roewe','Skoda','Bestune','SWM','De la Chapelle','Arcimoto','Prodrive','Weiwang','Skyworth','Saleen','Renault Korea','Motrio','Yudo','Bestune', 'Davia', 'Gillet', 'Hozon', 'Jinbei', 'Borgward', 'Multimatic', 'Aiways', 'VUHL','Magneti Marelli','BAW','Elva','Venucia','Lynk & Co','BAIC','ICKX', 'Mahindra', 'Castagna', 'Voyah', 'Zedriv', 'BAC', 'Youxia', 'Gordini', 'BBS', 'IVM', 'Intermeccanica', 'Arash', 'SsangYong', 'STILLEN', 'BJEV', 'Wey', 'ALD', 'VLF', 'David Brown', 'Moskvitch', 'Lingenfelter', 'MOMO', 'Weltmeister', 'AC Schnizter', 'Ralliart', 'VOL Nedcar', 'Dallar', 'Aito:', 'MVM', 'KTM', 'Hongqi', 'Tiger', 'Factory Five', 'Donkervoort', 'Gibbs', 'Iveco Bus', 'Zagato', 'Omoda', 'Beijing', 'Changfeng', 'DS', 'Automotive Lighting', 'nanoFlowcell', 'Sinogold', 'Brilliance', 'Studie', 'Pars Khodro', 'Carly', 'Gyon', 'Renntech', 'Rinspeed'}
#cleaned_brands = [i for i in cleaned_brands if i not in ex_brands]
cleaned_brands.extend(['Rivian', 'Lucid', 'Tesla', 'Jaguar', 'Genesis' ])
cleaned_brands = set(cleaned_brands)
cleaned_brands = cleaned_brands-ex_brands
maps = []
for name in names:
    found = False
    for brand in cleaned_brands:
        if brand in name:
            maps.append(brand)
            found = True
            break
    if not found:
        maps.append('Unspecified')

#gmaps = googlemaps.Client(key='Insert_Personal_Key')

        
# results = gmaps.places(query = 'Mercedes-Benz Dealership New Jersey')
# names_res = results['results']
#print(names_res[0].keys())
# res_lat = [i['geometry']['location']['lat'] for i in names_res]
# res_lng = [i['geometry']['location']['lng'] for i in names_res]



#print([names_res[0]['geometry']['location']['lat'],names_res[0]['geometry']['location']['lng']])
all_dealers = {}
# for i, brand in enumerate(random.sample(sorted(cleaned_brands), 5)):
for brand in cleaned_brands:

    results = gmaps.places(query = f'{brand} Dealership New Jersey')
    # Keys are ['formatted_address', 'name',, 'types', 'user_ratings_total'])
    res_names = results['results']
    res_addys = [i['formatted_address'] for i in res_names]
    res_lat = [i['geometry']['location']['lat'] for i in res_names]
    res_lng = [i['geometry']['location']['lng'] for i in res_names]
    res_names = [i['name'] for i in res_names]

    for i,v in enumerate(res_names):
        all_dealers[v]={'address': res_addys[i], 'lat': res_lat[i], 'lng': res_lng[i]}
   # print(res_names)
    time.sleep(2)
    while('next_page_token' in results.keys()):
        results = gmaps.places(query = f'{brand} Dealership New Jersey', page_token=str(results['next_page_token']))
        s_dealer_names = results['results']
        s_dealer_addys = [i['formatted_address'] for i in s_dealer_names]
        s_dealer_lat = [i['geometry']['location']['lat'] for i in s_dealer_names]
        s_dealer_lng = [i['geometry']['location']['lng'] for i in s_dealer_names]
        s_dealer_names = [i['name'] for i in s_dealer_names]
        for i,v in enumerate(s_dealer_names):
            all_dealers[v]={'address': s_dealer_addys[i], 'lat': s_dealer_lat[i], 'lng': s_dealer_lng[i]}
        time.sleep(2)
for name in names:
    results = gmaps.places(query = name)
    # Keys are ['formatted_address', 'name',, 'types', 'user_ratings_total'])
    res_names = results['results']
    res_addys = [i['formatted_address'] for i in res_names]
    res_lat = [i['geometry']['location']['lat'] for i in res_names]
    res_lng = [i['geometry']['location']['lng'] for i in res_names]
    res_names = [i['name'] for i in res_names]

    for i,v in enumerate(res_names):
        all_dealers[v]={'address': res_addys[i], 'lat': res_lat[i], 'lng': res_lng[i]}
   # print(res_names)
    time.sleep(2)
print(all_dealers)
final_names = all_dealers.keys()
final_addys = []
final_cords = []
for name in final_names:
    final_addys.append(all_dealers[name]['address'])
    final_cords.append([all_dealers[name]['lat'], all_dealers[name]['lng']])
final_df = pd.DataFrame({'names': final_names, 'addresses': final_addys, 'coords': final_cords})
final_df.to_csv('final_cars.csv', header=False, index=False)



# header = {
#   "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
#   "X-Requested-With": "XMLHttpRequest"
# }

# r = requests.get(URL, headers=header)

# dfs = pd.read_html(r.text)
# print(dfs)
