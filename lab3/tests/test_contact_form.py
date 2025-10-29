from pages.practice_form_page import PracticeFormPage

def test_practice_form_success(driver):
    page = PracticeFormPage(driver)
    page.open()
    page.fill_form("Oleg", "Stepanenko", "oleg@test.com", "1234567890")
    page.submit()
    assert "Thanks for submitting the form" in page.get_modal_title()

def test_practice_form_negative(driver):
    page = PracticeFormPage(driver)
    page.open()
    page.submit()
    first_name = page.find(page.FIRST_NAME)
    assert "field-error" in first_name.get_attribute("class") or first_name.get_attribute("required") == "true"
