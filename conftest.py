import pytest

from pages.application import Application


@pytest.fixture(scope="session")
def app():
    base_url = "https://idemo.bspb.ru/"
    # headless = request.config.getoption("--headless")
    # fixture = Application(base_url, headless)
    fixture = Application(base_url)
    fixture.wd.implicitly_wait(10)
    fixture.wd.maximize_window()
    yield fixture
    fixture.wd.quit()
