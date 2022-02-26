from selenium.webdriver.common.by import By


class book_store_application:
    bsa_login = (By.XPATH, "//span[text()='Login']")
    bsa_profile = (By.XPATH, "//span[text()='Profile']")
    book_store = (By.XPATH, "//span[text()='Book Store']")
    bsa_new_user = (By.CSS_SELECTOR, "#newUser")
    bsa_user_name = (By.CSS_SELECTOR, "#userName")
    bsa_password = (By.CSS_SELECTOR, "#password")
    first_name = (By.CSS_SELECTOR, "#firstname")
    last_name = (By.CSS_SELECTOR, "#lastname")
    user_name = (By.CSS_SELECTOR, "#userName")
    password = (By.CSS_SELECTOR, "#password")
    captcha = (By.CSS_SELECTOR, "#g-recaptcha")
    register_button = (By.CSS_SELECTOR, "#register")
    go_to_login = (By.CSS_SELECTOR, "#gotologin")
    login = (By.CSS_SELECTOR, "#login")
    back_to_login = (By.CSS_SELECTOR, "#gotologin")
    search_box = (By.CSS_SELECTOR, "#searchBox")
    book_learning_js = (By.LINK_TEXT,"Learning JavaScript Design Patterns")

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element(*book_store_application.bsa_login).click()

    def click_new_user(self):
        self.driver.find_element(*book_store_application.bsa_new_user).click()

    def input_first_name(self):
        return self.driver.find_element(*book_store_application.first_name)

    def input_last_name(self):
        return self.driver.find_element(*book_store_application.last_name)

    def input_password(self):
        return self.driver.find_element(*book_store_application.password)

    def input_user_name(self):
        return self.driver.find_element(*book_store_application.user_name)

    def click_captcha(self):
        self.driver.find_element(*book_store_application.captcha).click()

    def click_register(self):
        self.driver.find_element(*book_store_application.register_button).click()

    def click_go_to_login(self):
        self.driver.find_element(*book_store_application.go_to_login).click()

    def login_username(self):
        return self.driver.find_element(*book_store_application.bsa_user_name)

    def login_password(self):
        return self.driver.find_element(*book_store_application.bsa_password)

    def click_login_book_store(self):
        self.driver.find_element(*book_store_application.login).click()

    def click_back_to_login(self):
        self.driver.find_element(*book_store_application.back_to_login).click()

    def click_book_store(self):
        self.driver.find_element(*book_store_application.book_store).click()

    def click_search_box(self):
        return self.driver.find_element(*book_store_application.search_box)

    def click_book_one(self):
        return self.driver.find_element(*book_store_application.book_learning_js).click()

