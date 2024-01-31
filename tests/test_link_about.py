# import datetime
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# from pages.cart_page import Cart_page
# from pages.client_information import Client_information
# from pages.finish_page import Finish_page
# from pages.login_page import Login_page
# from pages.main_page import Main_page
#
#
#
# def test_link_about():
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     options = webdriver.ChromeOptions()
#     options.page_load_strategy = 'eager'
#     options.add_experimental_option("detach", True)
#     g = Service()
#     driver = webdriver.Chrome(options=options, service=g)
#
#     print("Start test")
#
#     login = Login_page(driver)
#     login.authorization()
#
#     mp = Main_page(driver)
#     mp.select_menu_about()
#
#     print("Finish Test")
#     time.sleep(10)
#     driver.quit()
