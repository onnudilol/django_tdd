from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item.  She hits Enter on on the empty input box.

        # The home page refreshes, and there is an error saying
        # that list items cannot be blank.

        # She tries again with some text for the item, which now works.

        # Perversely, she now decides to submit a second blank item.

        # She receives a similar warning on the list page.

        # And she can correct it by filling in some text.
        self.fail('write me')
