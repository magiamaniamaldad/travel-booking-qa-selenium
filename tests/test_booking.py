from pathlib import Path

import pytest
from selenium import webdriver

from pages.booking_page import BookingPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def booking_page(driver):
    page = BookingPage(driver)

    app_path = Path(__file__).resolve().parents[1] / "app" / "index.html"
    page.open(app_path.as_uri())

    return page


def test_search_valid_trip(booking_page):
    booking_page.search_trip(
        origin="Buenos Aires",
        destination="Mar del Plata",
        date="10-11-2026",
        passengers=1,
    )

    assert booking_page.results_are_displayed()


def test_same_origin_and_destination_is_rejected(booking_page):
    booking_page.search_trip(
        origin="Buenos Aires",
        destination="Buenos Aires",
        date="10-11-2026",
        passengers=1,
    )

    assert (
        booking_page.get_error_message()
        == "Origin and destination must be different."
    )


@pytest.mark.parametrize(
    "origin,destination,passengers",
    [
        ("Buenos Aires", "Mar del Plata", 1),
        ("Buenos Aires", "Rosario", 2),
        ("Cordoba", "Mar del Plata", 4),
    ],
)
def test_multiple_valid_booking_scenarios(
    booking_page,
    origin,
    destination,
    passengers,
):
    booking_page.search_trip(
        origin=origin,
        destination=destination,
        date="10-11-2026",
        passengers=passengers,
    )

    assert booking_page.results_are_displayed()
