class portfolio:
    def __init__(self,page):
        self.page=page
        self.portfolio=page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')
        self.ics=page.locator('//a[@href="https://www.icshomework.in/"]')
        self.wing=page.locator('//a[@href="https://www.wingspharma.com/"]')
        self.arena=page.locator('//a[@href="https://arenasonipat.com/"]')
        self.home=page.locator('//a[@href="https://home360stores.com/"]')
        self.cord=page.locator('//a[@href="https://cordscable.tranktechnologies.com/"]')
        self.portfoliolist=[self.ics,self.wing,self.arena,self.home,self.cord]

    def portfolioclick(self):
        self.portfolio.click()
        self.page.wait_for_load_state(state="load")
        for portfolio_link in self.portfoliolist:
            with self.page.context.expect_page() as new_page_info:
                portfolio_link.click()
            new_tab=new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close()