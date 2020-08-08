


#https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven





import requests as res
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def loginFunction():
    driver = webdriver.Chrome('D:\downloads\chromedriver')
    driver.get('https://www.linkedin.com')
    userName = driver.find_element_by_id('session_key')
    userName.send_keys('vishnudk179@gmail.com')
    password = driver.find_element_by_id('session_password')
    password.send_keys('Jaihanuman179#')
    # sleep(0.5)
    log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
    log_in_button.click()
    # article = driver.find_elements_by_id('ember755')
    article = driver.find_elements_by_class_name('break-words')
    article = [i.text for i in article]
    for ar in article:
        print(ar)
        print("===============================")
    time.sleep(2000)

def main_function():
    # print("Enter the specification")
    # query=input()
    driver2=webdriver.Chrome('D:\downloads\chromedriver')
    driver2.get('https://www.google.com')

    search_query = driver2.find_element_by_name('q')
    search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "London"')  
    search_query.send_keys(Keys.RETURN)
    # profileUrls=driver2.find_element_by_tag_name('a')
    # profileUrls = driver2.find_elements_by_xpath("//*[@href]")
    # profileUrls = driver2.find_elements_by_partial_link_text('')
    profileUrls = driver2.find_elements_by_class_name('r')
    # profileUrls = [url.text for url in profileUrls]
   

    time.sleep(1)


if __name__ == "__main__":
    # main_function()
    loginFunction()