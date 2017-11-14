### Author Alkiviadis Tsitsigkos
### November 2017, London UK

## Importing Required Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ConfigParser import SafeConfigParser
import glob


# Function Parsing Login Credentials From Locally Stored File
def config_parse():
    parser = SafeConfigParser()
    candidates = 'config.ini'
    files_present = parser.read(candidates)
    files_missing = set(candidates) - set(files_present)

    if True:
        print ('I found the configuration file!')
    else:
        print ('Missing file, please create one!')

    username = parser.get('vpn_profile','username')
    password = parser.get('vpn_profile','password')
    url = parser.get('vpn_profile', 'url')
    config = {'username': username, 'password': password, 'url': url}
    return config

# Make the Firefox Browser to Automatically Save Files
def vpn_access(url):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.folderList',2)
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.download.dir', '~/Downloads')
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain')
    driver = webdriver.Firefox(profile)
    driver.get(url)
    return driver


# Keycloak Login Screen and Download VPN Profile
def download_profile(driver):
    assert "HOD VPN" in driver.title
    ssologin = driver.find_element_by_id('zocial-365').click()
    # Collecting all windows, including the pop up window
    window_before = driver.window_handles[0]
    time.sleep(2)
    # Office 365 LoginPage - Passing the Credentials
    loginusername = driver.find_element_by_id('cred_userid_inputtext').send_keys(config['username'])
    loginuserpass = driver.find_element_by_id('cred_password_inputtext').send_keys(config['password'])
    login = driver.find_element_by_id('cred_sign_in_button')
    # Needed to make Python wait for 2 seconds due to the page refresh once the credentials are typed in the form
    time.sleep(4)
    login.click()
    time.sleep(2)
    # Download the profile
    vpntoken = driver.find_element_by_xpath('//div[@class="panel panel-default profile drop_shadow active" and @data-original-title="Click to download the VPN profile"]')
    vpntoken.click()
    driver.close()

if __name__ == '__main__':
  config=config_parse()
  driver=vpn_access(config['url'])
  download_profile(driver)
