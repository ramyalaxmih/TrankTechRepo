import pytest

from pages.blog import blog


@pytest.mark.smoke
def test_mobile(page):
    blogg=blog(page)
    blogg.blog_click()