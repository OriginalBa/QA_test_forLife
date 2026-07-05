from selenium.webdriver.common.by import By


class PageBoxPO:
    full_name_locator = (By.ID, "userName")
    email_locator = (By.ID, "userEmail")
    submit_locator = (By.ID, "submit")
    current_locator = (By.ID, "currentAddress")
    permanent_locator = (By.ID, "permanentAddress")
    result_locator = (By.ID, "output")
    email_css_locator = (By.CSS_SELECTOR, "input[type='email']")

    def __init__(self, driver):
        self.driver = driver

    # Low Level action
    def input_full_name(self, name):
        self.driver.find_element(*self.full_name_locator).send_keys(name)

    def input_email(self, email):
        self.driver.find_element(*self.email_locator).send_keys(email)

    def input_current_address(self, address):
        self.driver.find_element(*self.current_locator).send_keys(address)

    def input_permanent_address(self, p_address):
        self.driver.find_element(*self.permanent_locator).send_keys(p_address)

    def click_submit(self):
        submit_btn = self.driver.find_element(*self.submit_locator)
        self.driver.execute_script("arguments[0].click();", submit_btn)
        submit_btn.click()

    def result(self):
        return self.driver.find_element(*self.result_locator).text

    def get_email_validation_message(self):
        email_field = self.driver.find_element(*self.email_css_locator)
        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", email_field)
        return validation_message
