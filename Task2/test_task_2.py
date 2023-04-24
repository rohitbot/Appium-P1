import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class AppiumConfig:

    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {

            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"C:\Users\146698\Downloads\com.bsl.hyundai_2021-08-09.apk",
            #"udid":"9321e790"
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()
class TestAndroidDeviceLocal(AppiumConfig):
    def test_signup_page(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Don’t allow']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Don’t allow']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='SIGN UP!']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Name*']").send_keys("Rohit Behera")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Mobile Number*']").send_keys("6789112345")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Email ID*']").send_keys("botrohit@gmail.com")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password*']").send_keys("welcome@123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Confirm Password*']").send_keys(
            "welcome@123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.CheckBox["
                                            "@resource-id='com.bsl.hyundai:id/checkAcceptTermsCondition']").click()


