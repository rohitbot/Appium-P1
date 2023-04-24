import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {

            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"C:\Users\146698\Downloads\khan-academy-7-3-2.apk"
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestArts(AppiumConfig):
    def test_the_himalayas_topics(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']").click()

        self.driver.implicitly_wait(0)
        # to check when we donot know how much swipe is requried
        while len(self.driver.find_elements(AppiumBy.XPATH, "//*[@text='Art of Asia']")) == 0:
            self.driver.swipe(902, 1174, 902, 794, 1000)

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Art of Asia']").click()
        self.driver.implicitly_wait(30)


        self.driver.implicitly_wait(0)
        # to check when we donot know how much swipe is requried
        while len(self.driver.find_elements(AppiumBy.XPATH, "//*[contains(@text,'Himala')]")) == 0:
            self.driver.swipe(902, 1174, 902, 794, 1000)

        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Himala')]").click()
        self.driver.implicitly_wait(30)


