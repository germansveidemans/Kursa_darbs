import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook, load_workbook
import pandas

# def Fill_cells(options, driver):
    
#     option_cena = options[1][0].split("-")
#     option_gads = options[0][1].split("-")
#     option_tilpums = options[0][2]
    
#     if option_tilpums.find("-") != 0:
#         option_tilpums = option_tilpums.split("-")
        
#     option_dzinejs = options[0][3]
#     option_atrkarba = options[0][4]
#     option_virstips = options[0][5]
#     option_krasa = options[0][6]
    
    
#     find = driver.find_element(By.ID, "mtd_97")
#     find.click()
    
#     find = driver.find_element(By.ID, "f_o_8_min")
#     find.send_keys(option_cena[0])
#     find = driver.find_element(By.ID, "f_o_8_max")
#     find.send_keys(option_cena[1])
#     time.sleep(1)
    
#     find = driver.find_element(By.ID, "f_o_18_min")
#     find.send_keys(option_gads[0])
#     find = driver.find_element(By.ID, "f_o_18_max")
#     find.send_keys(option_gads[1])
#     time.sleep(1)
    
#     find = driver.find_element(By.ID, "f_o_15_min")
#     find.send_keys(option_tilpums[0])
#     find = driver.find_element(By.ID, "f_o_15_max")
#     if len(option_tilpums) > 1:
#         find.send_keys(option_tilpums[1])
#     find.send_keys(option_tilpums[0])
#     time.sleep(1)
    
#     find = driver.find_element(By.ID, "f_o_34")
#     find.send_keys(option_dzinejs)
#     time.sleep(1)
    
#     find = driver.find_element(By.ID, "f_o_35")
#     find.send_keys(option_atrkarba)
#     time.sleep(1)
    
#     find = driver.find_element(By.ID, "f_o_32")
#     find.send_keys(option_virstips)
#     time.sleep(1)
    
#     if option_krasa != "-":
#         find = driver.find_element(By.ID, "f_o_17")
#         find.send_keys(option_krasa)
    
#     return
    
# options_csv = pandas.read_csv("options.csv")
# options = options_csv.values.tolist()

# service = Service()
# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service = service, options = option)

# url = "https://www.ss.com/"
# driver.get(url)

# Fill_cells(options,driver)
# sludinajumi_id = []
# saites = []

# sl_class = driver.find_elements(By.CLASS_NAME, "msga2-o")
# for i in sl_class:
#     info = i.text
#     if info != "-":
#         sludinajumi_id.append(info)
#     hh = i.find_element(By.TAG_NAME, 'a').get_attribute("href")
#     saites.append(hh)
    
    
# sludinajumi = []
# for a in range(0, len(sludinajumi_id)-1, 4):
#     b = [' '.join(sludinajumi_id[a:(a+4)])]
#     sludinajumi.append(b)
    
# print(sludinajumi)
# nobraukums = []
# sl_class = driver.find_elements(By.CLASS_NAME, "msga2-r")
# for i in sl_class:
#     info = i.text
#     nobraukums.append(info)
# print(nobraukums)

# driver.quit()

sludinajumi = ['Bmw\n320', '1994', '2.0', '4,400 €', 'Mazda\nMazda6', '2008', '2.0', '3,300 €', 'Bmw\n318', '2007', '2.0', '4,500 €', 'Honda\nAccord', '2008', '2.0', '4,200 €', 'Honda\nAccord', '2006', '2.0', '3,500 €', 'Audi\nA4', '2005', '2.0', '3,495 €', 'Hyundai\nSonata', '2007', '2.0', '4,450 €', 'Subaru\nLegacy', '2006', '2.0', '3,300 €', 'Audi\nA6', '2006', '2.0', '3,995 €', 'Ford\nMondeo', '2010', '2.0', '3,950 €', 'Bmw\n320', '1997', '2.0', '3,800 €', 'Ford\nSierra', '1991', '2.0', '3,800 €', 'Lexus\nIS', '1999', '2.0', '3,850 €', 'Toyota\nAvensis', '2010', '2.0', '3,800 €', 'Toyota\nAvensis', '2007', '2.0', '4,500 €', 'Skoda\nOctavia', '2006', '2.0', '4,590 €', 'Mazda\nMazda6', '2007', '2.0', '3,300 €', 'Mercedes\nC200', '2000', '2.0', '3,200 €', 'Ford\nMondeo', '2010', '2.0', '3,250 €', 'Bmw\n320', '2006', '2.0', '3,000 €', 'Audi\nA6', '1994', '2.0', '3,150 €', 'Audi\nA6', '1994', '2.0', '3,100 €', 'Mazda\nMazda6', '2008', '2.0', '3,490 €', 'Audi\n90', '1994', '2.0', '3,445 €']

marka = []
for i in range(0,len(sludinajumi)-1,4):
    marka.append(sludinajumi[i])
    
gads = []
for i in range(1,len(sludinajumi)-1,4):
    gads.append(sludinajumi[i])
tilpums = []
for i in range(2,len(sludinajumi)-1,4):
    tilpums.append(sludinajumi[i])
    
cena = []
for i in range(3,len(sludinajumi)-1,4):
    cena.append(sludinajumi[i])
    
# result_wb = Workbook()
# w_results = result_wb.active
# w_results.append(["Marka","Gads","Dz.Tilpums","Nobraukums", "Cena", "Saite"])

# for marka, gads, tilpums, nobraukums, cena, saite in zip(sludinajums[_][0],sludinajums[_][1],sludinajums[_][2], nobraukums, sludinajums[_][3],saite):
