import pytest

from pages.portfolio import portfolio


@pytest.mark.smoke
def test_portfolio(page):
    port=portfolio(page)
    port.portfolioclick()
