import pytest

from pages.vertical import vertical


@pytest.mark.smoke
def test_fintech(page):
    vert=vertical(page)
    vert.fintech_click()