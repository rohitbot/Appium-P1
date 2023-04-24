import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {

    "platformName": "android",
    "deviceName": "oneplus",
    "app": r"C:\Users\146698\Downloads\khan-academy-7-3-2.apk"
}

driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)

driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
driver.find_element(AppiumBy.XPATH,
                    "//android.widget.EditText[@content-desc='Enter an e-mail address or username']").send_keys("rohit")
driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password']").send_keys("bot123")
driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Sign in']/android.widget.TextView").click()
actual_error = driver.find_element(AppiumBy.XPATH,
                                   "//android.widget.TextView[@text='There was an issue signing in']").text
print(actual_error)

time.sleep(5)
print(driver.page_source)
time.sleep(5)
driver.quit()
