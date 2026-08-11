import pytest

from pages.vertical import vertical

@pytest.mark.smoke
def test_trading(page):
    vert=vertical(page)
    vert.trading_click()
