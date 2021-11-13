from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
import pandas as pd

app = Flask(__name__)

@app.route("/")
@app.route("/index")

def index():
    df_bundes_team = pd.DataFrame(columns = ['rank', 'team', 'game', 'win_pt', 'win', 'draw', 'lose', 'gf', 'ga', 'goal_diff'])
    print(df_bundes_team)
    
    #open webdriver
    chrome_driver = './chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver)

    bundes_football = "https://sports.news.naver.com/wfootball/record/index?category=bundesliga&tab=team"
    driver.get(bundes_football)
    driver.implicitly_wait(3)

    tr_len = len(driver.find_elements_by_css_selector('#wfootballTeamRecordBody > table > tbody > tr'))
    print(tr_len)
    for i in range(1, tr_len + 1):
        rank = driver.find_element_by_css_selector('#wfootballTeamRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(1) > div > strong').text
        team = driver.find_element_by_css_selector('#wfootballTeamRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(2) > div > span').text
        game = driver.find_element_by_css_selector('#wfootballTeamRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(3) > div > span').text
        win_pt = driver.find_element_by_css_selector('#wfootballTeamRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(4) > div > span').text
        win = driver.find_element_by_css_selector('#wfootballTeamRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(5) > div > span').text
        draw = driver.find_element_by_css_selector('#wfootballTeamRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(6) > div > span').text
        lose = driver.find_element_by_css_selector('#wfootballTeamRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(7) > div > span').text
        gf = driver.find_element_by_css_selector('#wfootballTeamRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(8) > div > span').text
        ga = driver.find_element_by_css_selector('#wfootballTeamRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(9) > div > span').text
        goal_diff = driver.find_element_by_css_selector('#wfootballTeamRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(10) > div > span').text
        print(rank, team, game, win_pt, win, draw, lose, gf, ga, goal_diff)
        df_bundes_team = df_bundes_team.append({'rank':rank, 'team':team, 'game':game, 'win_pt':win_pt, 'win':win, 'draw':draw, 'lose':lose, 'gf':gf, 'ga':ga, 'goal_diff':goal_diff}, ignore_index=True)
    print(df_bundes_team)
    driver.quit()
    return render_template('bundes.html', tables=[df_bundes_team.to_html(classes='data')], titles=df_bundes_team.columns.values)
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="1234", debug=True)