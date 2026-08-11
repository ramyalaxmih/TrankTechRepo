class vertical:
    def __init__(self,page):
        self.page=page
        self.vertical_header=page.locator('(//a[text()="Verticals"])[1]')

        #menu1
        self.menu1 = page.locator('(//img[@alt="trading"])[1]')
        self.sub1_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.sub2_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.sub3_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.sub4_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.sub5_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.sub6_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.sub7_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        self.trading_list = [self.sub1_trading, self.sub2_trading, self.sub3_trading, self.sub4_trading, self.sub5_trading, self.sub6_trading,
                        self.sub7_trading]
        # menu2
        self.menu2 = page.locator(
            '//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/retailandecomm-mob.png"]')
        self.sub1_retail = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.sub2_retail = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retail_list = [self.sub1_retail, self.sub2_retail]
        # menu3
        self.menu3 = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/health-mob.png"]')
        self.sub1_health=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.sub2_health=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.health_list=[self.sub1_health,self.sub2_health]

        # menu4
        self.menu4=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/fintech-mob.png"]')
        self.sub1_fin=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.sub2_fin=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.fin_list=[self.sub1_fin,self.sub2_fin]

        # menu5
        self.menu5=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/custom-mob.png"]')
        self.sub1_custom=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.sub2_custom = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.sub3_custom = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.sub4_custom = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.sub5_custom = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.sub6_custom = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.sub7_custom = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.sub8_custom = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.sub9_custom = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.custom_list=[self.sub1_custom,self.sub2_custom,self.sub3_custom,self.sub4_custom,self.sub5_custom,self.sub6_custom,self.sub7_custom,self.sub8_custom,self.sub9_custom]

    def trading_click(self):
        for i in self.trading_list:
            self.vertical_header.hover()
            self.menu1.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()


    def retailecom_click(self):
        for i in self.retail_list:
            self.vertical_header.hover()
            self.menu2.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def health_click(self):
        for i in self.health_list:
            self.vertical_header.hover()
            self.menu3.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def fintech_click(self):
        for i in self.fin_list:
            self.vertical_header.hover()
            self.menu4.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def custom_click(self):
        for i in self.custom_list:
            self.vertical_header.hover()
            self.menu5.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()