from selenium import webdriver
from time import sleep


def mp3_download():
    browser.find_element_by_xpath(
        "//div[@id='select_main']//ul[1]//li[2]//a[1]").click()
    sleep(0.5)
    browser.find_element_by_css_selector("#advanced-options-link").click()
    sleep(0.5)
    browser.find_element_by_css_selector("#audioBitrate").click()
    sleep(0.5)
    browser.find_element_by_xpath("//a[@data-value='320']").click()
    sleep(0.5)
    browser.find_element_by_css_selector("#convert1").click()
    sleep(10)
    browser.find_element_by_css_selector("#downloadq").click()
    sleep(0.5)
    browser.switch_to.window(browser.window_handles[0])
    sleep(0.5)
    browser.execute_script(
        "window.alert('If Download Does Not Start , Simply Click The Download Button !   :D');")


def mp4_download():
    browser.find_element_by_xpath(
        "//a[@class='video-format active']//span[contains(text(),'.mp4')]").click()
    sleep(0.5)
    browser.find_element_by_css_selector("#advanced-options-link").click()
    sleep(0.5)
    browser.find_element_by_css_selector("#videoResolution").click()
    sleep(0.5)
    browser.find_element_by_xpath("//a[@data-value='1920x1080']").click()
    sleep(0.5)
    browser.find_element_by_css_selector("#convert1").click()
    sleep(150)
    browser.find_element_by_css_selector("#downloadq").click()
    sleep(0.5)
    browser.switch_to.window(browser.window_handles[0])
    sleep(0.5)
    browser.execute_script(
        "window.alert('If Download Does Not Start , Simply Click The Download Button !   :D');")


url = "https://www.onlinevideoconverter.com/youtube-converter"

yt_url = input("Enter YouTube URL : ")
choice = int(input(
    "\n1. High Quality AUDIO [.mp3]\n2. High Quality VIDEO [.mp4]\n\nEnter Choice : "))

browser = webdriver.Chrome("D:\\#Coding\\VSCode_Projects\\chromedriver")

browser.get(url)
browser.find_element_by_id("texturl").send_keys(yt_url)
browser.find_element_by_css_selector("#select_main").click()

if choice == 1:

    mp3_download()

if choice == 2:

    mp4_download()
