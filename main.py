from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import logging
import time
import os
from random import randrange

# Configure logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

options = Options()
options.headless = True

workspace_url = os.getenv('WORKSPACE_URL')
auth_email = os.getenv('AUTH_EMAIL')
auth_password = os.getenv('AUTH_PASSWORD')
end_hour = os.getenv('END_HOUR', None)
if end_hour is not None:
    end_hour = int(end_hour)
end_minutes = os.getenv('END_MINUTES', '0').split(':')

logging.info('Starting webdriver')
with webdriver.Firefox(options=options) as driver:
    driver.get(workspace_url)

    # Configuring time
    if end_hour is not None:
        if len(end_minutes) > 1:
            rand_stop_minute = randrange(int(end_minutes[0]), int(end_minutes[1]))
        else:
            rand_stop_minute = int(end_minutes[0])

    # Login
    logging.info('Logging in')
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(auth_email)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(auth_password)
    driver.find_element_by_xpath('//*[@id="signin_btn"]').click()

    # Waiting for logged in
    while True:
        # Skipping app opening prompt
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/p/a').click()
        except NoSuchElementException:
            pass

        # Looking for menu
        try:
            driver.find_element_by_class_name('p-channel_sidebar__name')
            logging.info('Logged in')
            break
        except NoSuchElementException:
            logging.info('Awaiting for logging in')
            time.sleep(1)

    while True:
        if end_hour is not None:
            now = time.gmtime()
            if now.tm_hour >= end_hour:
                if now.tm_hour > end_hour or now.tm_min >= rand_stop_minute:
                    logging.info('It\'s time to finish work')
                    break
        logging.info('Sleeping')
        time.sleep(60)

    logging.info('Shutting down')
    driver.close()
