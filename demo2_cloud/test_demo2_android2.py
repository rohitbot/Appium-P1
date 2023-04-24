import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "app": "bs://6fffd8d50149f98651e64125d6166177d297e0a9",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "bstack:options": {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                # Set your access credentials
                "userName": "padmakshijain_U4kQfV",
                "accessKey": "1hKTbvmoUbEL8BtVqbyh"
            }
        }
        self.driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",
                                       desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAndroidDeviceCloud(AppiumConfig):
    class TestAndroidDeviceCloud(AppiumConfig):

        def test_invalid_login(self):
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
            print(self.driver.page_source)

        def test_invalid_sign_up_email_test(self):
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
            # click on setting icon
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Settings']").click()
            # click on sign in
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
            # click on sign up with email
            self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'email')]").click()

            # send firstnamea as john -
            self.driver.find_element(AppiumBy.XPATH, "//*[@content-desc='First name']").send_keys("padmakshi")
            # send lastname as peter -
            self.driver.find_element(AppiumBy.XPATH, "//*[@content-desc='Last name']").send_keys("jain")

            # send birthday Aug 20, 1995 - Birthday
            # self.driver.find_element(AppiumBy.XPATH, "//*[@text='Birthday']").send_keys("August 20, 1995")
            self.driver.find_element(AppiumBy.XPATH, "//*[@text='Birthday']").click()

            # choose Aug
            self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").click()
            self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").clear()
            self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']").send_keys(
                "Aug")

            # choose 20
            self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").click()
            self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[2]").clear()
            self.driver.find_element(AppiumBy.XPATH,
                                     "(//*[@resource-id='android:id/numberpicker_input'])[2]").send_keys("20")

            # choose 1995
            self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").click()
            self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='android:id/numberpicker_input'])[3]").clear()
            self.driver.find_element(AppiumBy.XPATH,
                                     "(//*[@resource-id='android:id/numberpicker_input'])[3]").send_keys("1995")

            self.driver.find_element(AppiumBy.XPATH, "//*[@text='OK']").click()
            self.driver.find_element(AppiumBy.XPATH , "//android.widget.EditText[@content-desc='Email address']").send_keys("test123")
            self.driver.find_element(AppiumBy.XPATH , "//android.widget.EditText[@content-desc='Password']").send_keys("welcom123")
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='CREATE']").click()
            actaul_error = self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='There was an "
                                                                   "issue signing in']").text
            assert_that(actaul_error).is_equal_to("There was an issue signing in")
