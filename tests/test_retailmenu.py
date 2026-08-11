import pytest

from pages.vertical import vertical

@pytest.mark.smoke
def test_retail(page):
    vert=vertical(page)
    vert.retailecom_click()