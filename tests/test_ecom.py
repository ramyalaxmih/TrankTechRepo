import pytest

from pages.technologies import technologies


@pytest.mark.smoke
def test_ecom(page):
    tech=technologies(page)
    tech.ecom_click()