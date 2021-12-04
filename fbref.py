from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
import pandas as pd

df_bundes_table  = pd.DataFrame(columns= ['rank','team','match','win','draw','lose','gf','ga','gd','pts','xG','xGA','xGD','xGD_90'])
print(df_bundes_table)

chrome_driver='./chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)

fbref_bundes = "https://fbref.com/en/comps/20/Bundesliga-Stats"
driver.get(fbref_bundes)
driver.implicitly_wait(3)

tr_len = len(driver.find_elements_by_css_selector('#results111931_overall > tbody > tr'))

print(tr_len)

for i in range(1,tr_len+1):
    rank = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > th').text
    team = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(2) > a').text
    match = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(3)').text
    win = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(4)').text
    draw = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(5)').text
    lose = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(6)').text
    gf = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(7)').text
    ga = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(8)').text
    gd = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(9)').text
    pts = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(10)').text
    xG = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(11)').text
    xGA = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(12)').text
    xGD = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(13)').text
    xGD_90 = driver.find_element_by_css_selector('#results111931_overall > tbody > tr:nth-child('+ str(i) +') > td:nth-child(14)').text
    
    print(rank, team, match, win, draw, lose, gf, ga, gd, pts, xG, xGA, xGD, xGD_90)
    df_bundes_table = df_bundes_table.append({'rank':rank, 'team':team, 'match':match, 'win':win, 'draw':draw, 'lose':lose, 'gf':gf, 'ga':ga, 'gd':gd, 'pts':pts, 'xG':xG, 'xGA':xGA, 'xGD':xGD, 'xGD_90':xGD_90}, ignore_index=True)
print(df_bundes_table)

driver.quit()