from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PracticeFormPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.ID, "gender-radio-1")
    MOBILE = (By.ID, "userNumber")
    SUBMIT = (By.ID, "submit")

    MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")

    def open(self):
        self.driver.get(self.URL)

    def fill_form(self, first, last, email, mobile):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.EMAIL, email)
        self.driver.execute_script("arguments[0].click();", self.find(self.GENDER_MALE))
        self.type(self.MOBILE, mobile)

    def submit(self):
        self.driver.execute_script("arguments[0].click();", self.find(self.SUBMIT))

    def get_modal_title(self):
        return self.get_text(self.MODAL_TITLE)

    def get_modal_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MODAL_TITLE)
        ).text

