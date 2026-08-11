class contactus:
    def __init__(self,page):
        self.page=page
        self.contact=self.page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')


    def contact_click(self):
        self.contact.click()
        self.page.locator('(//input[@placeholder="Your Name"])[2]').fill("Ramya")
        self.page.locator('(//input[@placeholder="Your Mail"])[2]').fill("test@gmail.com")
        self.page.locator('(//input[@placeholder="Enter OTP"])[2]').fill("1234")
        self.page.locator('(//input[@placeholder="Your Company"])[2]').fill("Uncodemy")
        self.page.locator('(//select[@name="service"])[2]').select_option("UI / UX Design")
        self.page.locator('(//input[@placeholder="Your Phone"])[2]').fill("789456514")
        self.page.locator('(//textarea[@placeholder="Message"])[2]').fill("This is contact US page")
        self.page.locator('(//input[@type="submit"])[2]').click()
        self.page.wait_for_timeout(2000)
        self.page.wait_for_load_state("load")
        self.page.go_back()

