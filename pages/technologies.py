class technologies:
    def __init__(self,page):
        self.page=page
        self.tech_header=page.locator('(//a[text()="Technologies"])[1]')

        #menu1
        self.menu1=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/ecomm-mob.png"]')
        self.sub1_ecom=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.sub2_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.sub3_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.sub4_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.sub5_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.sub6_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.sub7_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.sub8_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.sub9_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.sub10_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.sub11_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.sub12_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.sub13_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.sub14_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.sub15_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.sub16_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.sub17_ecom = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.ecom_list=[self.sub1_ecom,self.sub2_ecom,self.sub3_ecom,self.sub4_ecom,self.sub5_ecom,self.sub6_ecom,self.sub7_ecom,self.sub8_ecom,self.sub9_ecom,self.sub10_ecom,self.sub11_ecom,self.sub12_ecom,self.sub13_ecom,self.sub14_ecom,self.sub15_ecom,self.sub16_ecom,self.sub17_ecom]

        #menu2
        self.menu2 = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/mobileapp-mob.png"]')
        self.sub1_mobileapp = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.sub2_mobileapp = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.sub3_mobileapp = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.sub4_mobileapp = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.sub5_mobileapp = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.sub6_mobileapp = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.sub7_mobileapp = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.sub8_mobileapp = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mobileapp_list=[self.sub1_mobileapp,self.sub2_mobileapp,self.sub3_mobileapp,self.sub4_mobileapp,self.sub5_mobileapp,self.sub6_mobileapp,self.sub7_mobileapp,self.sub8_mobileapp]

    def ecom_click(self):
            for i in self.ecom_list:
                self.tech_header.hover()
                self.menu1.hover()
                i.click()
                self.page.wait_for_load_state("load")
                self.page.go_back()

    def mobile_click(self):
        for i in self.mobileapp_list:
            self.tech_header.hover()
            self.menu2.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
