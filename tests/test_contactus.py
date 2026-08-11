import pytest

from pages.contactus import contactus


@pytest.mark.smoke
def test_mobile(page):
    cont=contactus(page)
    cont.contact_click()