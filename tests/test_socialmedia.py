import pytest

from pages.socialmedia import socialmedia


@pytest.mark.smoke
def test_socialmedia(page):
    social=socialmedia(page)
    social.socialmediapageclick()