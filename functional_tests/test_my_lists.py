from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class MyListsTest(FunctionalTest):

    def test_logged_in_users_are_saved_as_my_lists(self):
        email = 'edith@example.com'

        self.browser.get(self.server_url)
        self.wait_to_be_logged_out(email)

        # Edith is a logged-in user
        self.create_pre_authenticated_session(email)

        self.browser.get(self.server_url)
        self.wait_to_be_logged_in(email)

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith is a logged in user
        self.create_pre_authenticated_session('edith@example.com')

        # She goes to the home page and starts a list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Reticulate splines\n')
        self.get_item_input_box().send_keys('Immanentize eschaton\n')
        first_list_url = self.browser.current_url

        # She notices a 'My lists' link for the first time
        self.browser.find_element_by_partial_link_text('My lists').send_keys(Keys.RETURN)

        # She sees her list is there, named according to its first list item
        self.browser.find_element_by_partial_link_text('Reticulate splines').send_keys(Keys.RETURN)
        self.wait_for(lambda: self.assertEqual(self.browser.current_url, first_list_url))

        # She decides to start another list, just to see
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Click cows\n')
        second_list_url = self.browser.current_url

        # Under My Lists, her new list appears
        self.browser.find_element_by_partial_link_text('My lists').send_keys(Keys.RETURN)
        self.browser.find_element_by_partial_link_text('Click cows').send_keys(Keys.RETURN)
        self.assertEqual(self.browser.current_url, second_list_url)

        # She logs out.  The 'My lists' option disappears
        self.browser.find_element_by_id('id_logout').send_keys(Keys.RETURN)
        self.assertEqual(self.browser.find_elements_by_partial_link_text('My lists'), [])
