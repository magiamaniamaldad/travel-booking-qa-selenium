from pathlib import Path

import pytest
from selenium import webdriver

from pages.booking_page import BookingPage


@pytest.fixture
def driver():
    """Launch a headless Chrome browser for each test."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def booking_page(driver):
    """Open the local TripFlow booking application."""
    page = BookingPage(driver)

    app_path = Path(__file__).resolve().parents[1] / "app" / "index.html"
    page.open(app_path.as_uri())

    return page


def test_valid_booking_displays_correct_route_and_price(booking_page):
    booking_page.search_trip(
        origin="Buenos Aires",
        destination="Mar del Plata",
        date="2026-11-10",
        passengers=2,
    )

    assert booking_page.results_are_displayed()
    assert booking_page.get_route() == "Buenos Aires → Mar del Plata"
    assert booking_page.get_price() == "Total: ARS 64000"


def test_same_origin_and_destination_is_rejected(booking_page):
    booking_page.search_trip(
        origin="Buenos Aires",
        destination="Buenos Aires",
        date="2026-11-10",
        passengers=1,
    )

    assert (
        booking_page.get_error_message()
        == "Origin and destination must be different."
    )


@pytest.mark.parametrize(
    "origin,destination,passengers,expected_price",
    [
        ("Buenos Aires", "Mar del Plata", 1, "Total: ARS 32000"),
        ("Buenos Aires", "Rosario", 2, "Total: ARS 64000"),
        ("Cordoba", "Mar del Plata", 4, "Total: ARS 128000"),
    ],
)
def test_multiple_booking_scenarios(
    booking_page,
    origin,
    destination,
    passengers,
    expected_price,
):
    booking_page.search_trip(
        origin=origin,
        destination=destination,
        date="2026-11-10",
        passengers=passengers,
    )

    assert booking_page.results_are_displayed()
    assert booking_page.get_route() == f"{origin} → {destination}"
    assert booking_page.get_price() == expected_price
