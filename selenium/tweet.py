from selenium import webdriver
import time

twitter_password = ''

path = '/Users/Rodolfo/Desktop/chrome-bot/chromedriver'

option = webdriver.ChromeOptions()
option.add_argument('--incognito')

driver = webdriver.Chrome(path, chrome_options=option)

driver.get("http://www.lipsum.com/")

word_clicker = driver.find_element_by_xpath("""//*[@id="words"]""").click()
word_size_click = driver.find_element_by_xpath("""//*[@id="amount"]""").click()
word_size = driver.find_element_by_xpath("""//*[@id="amount"]""").clear()
word_size_choice = driver.find_element_by_xpath("""//*[@id="amount"]""")
word_size_choice.send_keys('20')

lorem_create = driver.find_element_by_xpath("""//*[@id="generate"]""").click()
paragraph = driver.find_element_by_css_selector('#lipsum')

new_paragraph = str(paragraph.text)

if len(new_paragraph) < 140:
    print('Tweet is Ok' + '\n')
else:
    print('Tweet is too long')
    time.sleep(10)
    driver.quit()

driver.get('https://twitter.com/')

login = driver.find_element_by_xpath("""//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]""").click()
username = driver.find_element_by_xpath(
    """//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input""")
username.send_keys('@letsget_awkward')

password = driver.find_element_by_xpath(
    """//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input""").click()
password_input = driver.find_element_by_xpath(
    """//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input""")
password_input.send_keys(twitter_password)

login_twitter = driver.find_element_by_xpath(
    """//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]""").click()

tweet_box = driver.find_element_by_xpath("""//*[@id="tweet-box-home-timeline"]""").click()
tweet_input = driver.find_element_by_xpath("""//*[@id="tweet-box-home-timeline"]""")
tweet_input.send_keys(new_paragraph + "sent at ")
send_tweet = driver.find_element_by_xpath(
    """//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button""").click()

print("You Successfully Tweeted " + new_paragraph + " to your Twitter Account!")
