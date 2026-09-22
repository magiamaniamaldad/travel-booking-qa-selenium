from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class BookingPage(BasePage):
    """Page Object for the travel booking search flow."""

    ORIGIN = (By.ID, "origin")
    DESTINATION = (By.ID, "destination")
    DEPARTURE_DATE = (By.ID, "departure-date")
    PASSENGERS = (By.ID, "passengers")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    RESULTS = (By.CSS_SELECTOR, "[data-testid='search-results']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-testid='booking-error']")

    def select_origin(self, origin):
        Select(self.find(self.ORIGIN)).select_by_visible_text(origin)

    def select_destination(self, destination):
        Select(self.find(self.DESTINATION)).select_by_visible_text(destination)

    def enter_departure_date(self, date):
        self.type_text(self.DEPARTURE_DATE, date)

    def select_passengers(self, passengers):
        Select(self.find(self.PASSENGERS)).select_by_value(str(passengers))

    def search_trip(self, origin, destination, date, passengers=1):
        self.select_origin(origin)
        self.select_destination(destination)
        self.enter_departure_date(date)
        self.select_passengers(passengers)
        self.click(self.SEARCH_BUTTON)

    def results_are_displayed(self):
        return self.is_visible(self.RESULTS)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
