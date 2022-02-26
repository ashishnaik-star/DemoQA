import pdb
import time

from PageObjects.Homepage import HomePageCls
from PageObjects.Intractions_Page import interactions_form_po
from Utilities.BaseClass import Baseclass


class Test_interactions(Baseclass):

    def test_interactions_sortable(self):
        Ip = HomePageCls(self.driver)
        Ip.Interactions_homepage().click()
        Ip1 = interactions_form_po(self.driver)
        Ip1.click_interactions_sortable()
        self.drag_vertical_with_yaxis(50, Ip1.list_one)
        self.drag_vertical_with_yaxis(200, Ip1.list_three)
        self.driver.get_screenshot_as_file(".\\Screenshots\\interactions_sortable_list.png")
        Ip1.click_sortable_grid()
        self.drag_both_axis(100, 100, Ip1.grid_one)
        self.drag_both_axis(100, 100, Ip1.grid_three)
        self.driver.get_screenshot_as_file(".\\Screenshots\\interactions_sortable_grid.png")

    def test_interactions_selectable(self):
        Ip2 = interactions_form_po(self.driver)
        self.scroll_vertical(400)
        Ip2.click_selectable_menu()
        Ip2.click_all_list()
        self.driver.get_screenshot_as_file(".\\Screenshots\\interactions_selectable_list.png")
        Ip2.click_selectable_grid()
        Ip2.grid_click_all()
        self.driver.get_screenshot_as_file(".\\Screenshots\\interactions_selectable_grid.png")

    def test_interactions_resizable(self):
        Ip3 = interactions_form_po(self.driver)
        self.scroll_vertical(400)
        Ip3.resizable_click()
        time.sleep(1)
        self.drag_both_axis(400, 400, Ip3.resizable_drag)
        self.drag_both_axis(-200, -200, Ip3.resizable_drag_box_drag)
        self.driver.get_screenshot_as_file(".\\Screenshots\\interactions_resizable.png")

    def test_interactions_droppable(self):
        Ip4 = interactions_form_po(self.driver)
        self.scroll_vertical(400)
        Ip4.droppabe_click()
        self.drag_both_axis(350, 0, Ip4.simple_drag_me)
        self.driver.get_screenshot_as_file(".\\Screenshots\\interactions_droppable_simple.png")
        Ip4.droppable_accept_tab()
        self.drag_both_axis(350, 0, Ip4.droppable_not_acceptable)
        self.driver.get_screenshot_as_file(".\\Screenshots\\interactions_droppable_not_accept.png")
        self.drag_vertical_with_xaxis(-350, Ip4.droppable_not_acceptable)
        self.drag_both_axis(350, 0, Ip4.droppable_acceptable)
        self.driver.get_screenshot_as_file(".\\Screenshots\\interactions_droppable_accept.png")
        Ip4.droppable_prevent_prop()
        self.drag_both_axis(350, 0, Ip4.drag_box_propaogation)
        self.drag_both_axis(0, 150, Ip4.drag_box_propaogation)
        self.driver.get_screenshot_as_file(".\\Screenshots\\interactions_droppable_inner.png")
        self.drag_both_axis(0, 200, Ip4.drag_box_propaogation)
        self.driver.get_screenshot_as_file(".\\Screenshots\\interactions_droppable_outer.png")
        Ip4.revert_draggable_click()
        self.drag_vertical_with_xaxis(350, Ip4.revert_draggable_will_revert)
        self.drag_vertical_with_xaxis(350, Ip4.revert_draggable_will_not_revert)
        self.driver.get_screenshot_as_file(".\\Screenshots\\interactions_revert_draggable.png")

    def test_interactions_dragabble(self):
        Ip5 = interactions_form_po(self.driver)
        self.scroll_vertical(400)
        Ip5.dragabble_click()
        self.drag_both_axis(300, 300, Ip5.drag_box_dragme)
        Ip5.axis_restricted_click()
        self.drag_vertical_with_xaxis(200, Ip5.restricted_x)
        self.drag_vertical_with_yaxis(200, Ip5.restricted_y)
        self.driver.get_screenshot_as_file(".\\Screenshots\\intrct_rest_axis.png")
        Ip5.container_restricted_click()
        self.drag_both_axis(200, 100, Ip5.contained_box_ele)
        self.drag_both_axis(20, 100, Ip5.contained_parant_ele)
        self.driver.get_screenshot_as_file(".\\Screenshots\\intrct_rest_click.png")
        Ip5.cursor_style_click()
        self.drag_both_axis(100, 100, Ip5.cursor_centre)
        self.drag_both_axis(200, 200, Ip5.cursor_top_left)
        self.drag_both_axis(30, 100, Ip5.cursor_bottom)
        self.driver.get_screenshot_as_file(".\\Screenshots\\intrct_cursor_placement.png")
        Ip5.expand_interactions_click()










