from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# print(os.environ.get("gh_pass"))
# print(os.environ.get("gh_user"))

options = webdriver.FirefoxOptions()
options.set_preference("marionette", True)
browser = webdriver.Firefox(options=options)
browser.implicitly_wait(10)
browser.get("https://www.github.com")
link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()

user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

user_input.send_keys(os.environ.get("gh_user"))
pass_input.send_keys(os.environ.get("gh_pass"))
pass_input.send_keys(Keys.RETURN)

img_avatar = browser.find_element(By.CLASS_NAME, "AppHeader-user")
img_avatar.click()

your_profile = browser.find_element(By.LINK_TEXT, "Your profile")
your_profile.click()

profile = browser.find_element(
    By.CLASS_NAME, "p-nickname.vcard-username.d-block")
label = profile.get_attribute("innerHTML")

assert "facundoenriquez2" in label
