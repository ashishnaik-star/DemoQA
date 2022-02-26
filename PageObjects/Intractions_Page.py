from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class interactions_form_po:
    expand_interactions = (By.XPATH, "//div[@class='accordion']/div[5]/span/div/div[2]")
    sortable_click = (By.XPATH, "//span[text()='Sortable']")
    sortable_grid_click = (By.CSS_SELECTOR, "#demo-tab-grid")
    selectable_menu = (By.XPATH, "//span[text()='Selectable']")
    resizable_menu = (By.XPATH, "//span[text()='Resizable']")
    droppable_menu = (By.XPATH, "//span[text()='Droppable']")
    dragabble_menu = (By.XPATH, "//span[text()='Dragabble']")
    selectable_grid_click = (By.CSS_SELECTOR, "#demo-tab-grid")
    list_one = (By.XPATH, "//div[@class='vertical-list-container mt-4']/div[text()='One']")
    list_two = (By.XPATH, "//div[@class='vertical-list-container mt-4']/div[text()='Two']")
    list_three = (By.XPATH, "//div[@class='vertical-list-container mt-4']/div[text()='Three']")
    grid_one = (By.XPATH, "//div[@class='grid-container mt-4']/div/div[text()='One']")
    grid_three = (By.XPATH, "//div[@class='grid-container mt-4']/div/div[text()='Three']")
    list_set_one = (By.XPATH, "//ul[@id='verticalListContainer']")
    resizable_drag = (By.XPATH, "//div[@id='resizableBoxWithRestriction']/span")
    resizable_drag_box_drag = (By.XPATH, "//div[@id='resizable']/span")
    simple_drag_me = (By.CSS_SELECTOR, "#draggable")
    droppable_accept = (By.CSS_SELECTOR, "#droppableExample-tab-accept")
    droppable_not_acceptable = (By.CSS_SELECTOR, "#notAcceptable")
    droppable_acceptable = (By.CSS_SELECTOR, "#acceptable")
    drag_box_dragme = (By.CSS_SELECTOR, "#dragBox")
    droppable_prevent_propogation = (By.CSS_SELECTOR, "#droppableExample-tab-preventPropogation")
    drag_box_propaogation = (By.XPATH, "//div[@id='ppDropContainer']/div[1]")
    revert_draggable = (By.CSS_SELECTOR, "#droppableExample-tab-revertable")
    revert_draggable_will_revert = (By.CSS_SELECTOR, "#revertable")
    revert_draggable_will_not_revert = (By.CSS_SELECTOR, "#notRevertable")
    axis_restricted = (By.CSS_SELECTOR, "#draggableExample-tab-axisRestriction")
    restricted_x = (By.CSS_SELECTOR, "#restrictedX")
    restricted_y = (By.CSS_SELECTOR, "#restrictedY")
    container_restricted = (By.CSS_SELECTOR, "#draggableExample-tab-containerRestriction")
    contained_box_ele = (By.CSS_SELECTOR, ".draggable.ui-widget-content.ui-draggable.ui-draggable-handle")
    contained_parant_ele = (By.CSS_SELECTOR, ".ui-widget-header.ui-draggable.ui-draggable-handle")
    cursor_style = (By.CSS_SELECTOR, "#draggableExample-tab-cursorStyle")
    cursor_centre = (By.CSS_SELECTOR, "#cursorCenter")
    cursor_top_left = (By.CSS_SELECTOR, "#cursorTopLeft")
    cursor_bottom = (By.CSS_SELECTOR, "#cursorBottom")

    def __init__(self, driver):
        self.driver = driver

    def expand_interactions_click(self):
        self.driver.find_element(*interactions_form_po.expand_interactions).click()

    def click_interactions_sortable(self):
        self.driver.find_element(*interactions_form_po.sortable_click).click()

    def click_sortable_grid(self):
        self.driver.find_element(*interactions_form_po.sortable_grid_click).click()

    def click_selectable_menu(self):
        self.driver.find_element(*interactions_form_po.selectable_menu).click()

    def click_all_list(self):
        for i in range(1, 5):
            self.driver.find_element(By.XPATH, f"//ul[@id='verticalListContainer']/li[{i}]").click()

    def click_selectable_grid(self):
        self.driver.find_element(*interactions_form_po.selectable_grid_click).click()

    def grid_click_all(self):
        for i in range(1, 4):
            for j in range(1,4):
                self.driver.find_element(By.XPATH, f"//div[@id='gridContainer']/div[@id='row{i}']/li[{j}]").click()

    def resizable_click(self):
        self.driver.find_element(*interactions_form_po.resizable_menu).click()

    def droppabe_click(self):
        self.driver.find_element(*interactions_form_po.droppable_menu).click()

    def droppable_accept_tab(self):
        self.driver.find_element(*interactions_form_po.droppable_accept).click()

    def droppable_prevent_prop(self):
        self.driver.find_element(*interactions_form_po.droppable_prevent_propogation).click()

    def revert_draggable_click(self):
        self.driver.find_element(*interactions_form_po.revert_draggable).click()

    def dragabble_click(self):
        self.driver.find_element(*interactions_form_po.dragabble_menu).click()

    def axis_restricted_click(self):
        self.driver.find_element(*interactions_form_po.axis_restricted).click()

    def container_restricted_click(self):
        self.driver.find_element(*interactions_form_po.container_restricted).click()

    def cursor_style_click(self):
        self.driver.find_element(*interactions_form_po.cursor_style).click()





