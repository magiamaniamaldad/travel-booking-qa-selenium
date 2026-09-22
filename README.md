# Travel Booking QA Automation

End-to-end QA automation project for a travel booking platform, built with **Selenium WebDriver, Python and Pytest**.

The project demonstrates a maintainable UI automation framework using the **Page Object Model (POM)**, reusable browser interactions, positive and negative test scenarios, data-driven testing, business-rule validation and automated CI execution with **GitHub Actions**.

## Project Overview

The system under test is **TripFlow**, a small travel booking application included in this repository specifically for QA automation.

Users can:

- Select an origin and destination
- Choose a departure date
- Select the number of passengers
- Search for available trips
- View the selected route
- View the calculated total price
- Receive validation errors for invalid booking scenarios

The application provides a controlled environment where automated tests can validate both UI behavior and business rules.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- HTML / JavaScript
- GitHub Actions
- Headless Chrome

## Test Coverage

The automated suite currently validates:

### Positive scenarios

- Successful travel search
- Correct origin and destination displayed
- Correct total price calculation
- Multiple passenger quantities
- Multiple route combinations

### Negative scenarios

- Same origin and destination
- Invalid booking combinations
- Validation error messages

### Data-driven testing

Pytest parametrization is used to execute multiple booking scenarios with different:

- Origins
- Destinations
- Passenger quantities
- Expected prices

## Project Structure

```text
travel-booking-qa-selenium/
│
├── app/
│   └── index.html
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── booking_page.py
│
├── tests/
│   └── test_booking.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── requirements.txt
└── README.md
```

## Automation Architecture

The framework follows the **Page Object Model** pattern.

`BasePage` contains reusable Selenium interactions such as:

- Explicit waits
- Element lookup
- Click actions
- Text input
- Text retrieval
- Visibility checks

`BookingPage` represents the booking interface and exposes higher-level actions such as:

- Selecting an origin
- Selecting a destination
- Entering a departure date
- Selecting passengers
- Searching for a trip
- Reading route and price information
- Reading validation errors

This separation keeps test logic readable while reducing duplicated Selenium code.

## Example Test Scenario

```python
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
```

## Continuous Integration

The repository includes a **GitHub Actions CI workflow**.

On every push or pull request to `main`, GitHub automatically:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Configures the project import path
5. Executes the Selenium test suite in headless Chrome

This ensures automated regression tests are continuously validated.

## Running the Tests Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the complete suite:

```bash
python -m pytest tests/ -v
```

Generate an HTML report:

```bash
python -m pytest tests/ -v --html=report.html --self-contained-html
```

## QA Skills Demonstrated

This project demonstrates practical experience with:

- UI test automation
- Selenium WebDriver
- Python test development
- Pytest fixtures
- Data-driven testing
- Page Object Model
- Explicit waits
- Positive and negative testing
- Business-rule validation
- Regression testing
- Test framework architecture
- CI/CD test execution
- GitHub Actions

## Purpose

This project was created as part of my **QA Engineering portfolio** to demonstrate how I design automated test scenarios, structure maintainable test code, validate business rules and integrate automated testing into a CI workflow.
