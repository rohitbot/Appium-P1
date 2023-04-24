from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap={
    "app":"bs://6fffd8d50149f98651e64125d6166177d297e0a9",
    "platformVersion":"9.0",
    "deviceName":"Google Pixel 3",
    "bstack:options": {
        "projectName": "First Appium project",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack first_test",
        # Set your access credentials
        "userName": "rohitbehera_LiqmJB",
        "accessKey": "hvknrqXW8eBGYNtZAw2y"
    }
}

driver=webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",desired_capabilities=des_cap)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Dismiss']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()

print(driver.page_source)

driver.quit()