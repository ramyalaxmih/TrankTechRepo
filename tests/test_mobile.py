import pytest

from pages.technologies import technologies


@pytest.mark.smoke
def test_mobile(page):
    tech=technologies(page)
    tech.mobile_click()