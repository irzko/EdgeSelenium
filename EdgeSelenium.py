from selenium.webdriver import EdgeOptions, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import getpass


def initDriver(profile=''):
    username = getpass.getuser()
    profile_path = r"C:\Users\{0}\AppData\Local\Microsoft\Edge\User Data\{1}".format(username, profile)
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument(
        "user-data-dir=" + profile_path)
    return Edge(options=options)
