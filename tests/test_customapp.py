import pytest

from pages.vertical import vertical


@pytest.mark.smoke
def test_custom(page):
    vert=vertical(page)
    vert.custom_click()