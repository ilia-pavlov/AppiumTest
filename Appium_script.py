from appium import webdriver

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    "app": "/Users/iliapavlov/PycharmProjects/AppiumTest/app_binaries/app-adjoy-staging-release.apk",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
