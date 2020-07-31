import pytest

from pages.application import Application


@pytest.fixture(scope='session')
def app():
    base_url = 'https://idemo.bspb.ru/'
    fixture = Application(base_url)
    fixture.wd.implicitly_wait(10)  # неявное ожидание, по умолчанию 10 секунд
    fixture.wd.maximize_window()
    yield fixture
    fixture.wd.quit()
