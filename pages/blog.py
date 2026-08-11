class blog:
    def __init__(self,page):
        self.page=page
        self.blog_header = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        self.sub1_blog = page.locator('//div[@class="cat-grid-box"]/li[1]')
        self.sub2_blog = page.locator('//div[@class="cat-grid-box"]/li[2]')
        self.sub3_blog = page.locator('//div[@class="cat-grid-box"]/li[3]')
        self.sub4_blog = page.locator('//div[@class="cat-grid-box"]/li[4]')
        self.sub5_blog = page.locator('//div[@class="cat-grid-box"]/li[5]')
        self.sub6_blog = page.locator('//div[@class="cat-grid-box"]/li[6]')
        self.sub7_blog = page.locator('//div[@class="cat-grid-box"]/li[7]')
        self.sub8_blog = page.locator('//div[@class="cat-grid-box"]/li[8]')
        self.sub9_blog = page.locator('//div[@class="cat-grid-box"]/li[9]')
        self.sub10_blog = page.locator('//div[@class="cat-grid-box"]/li[10]')
        self.sub11_blog = page.locator('//div[@class="cat-grid-box"]/li[11]')
        self.sub12_blog = page.locator('//div[@class="cat-grid-box"]/li[12]')
        self.blog_list = [self.sub1_blog, self.sub2_blog, self.sub3_blog, self.sub4_blog, self.sub5_blog, self.sub6_blog, self.sub7_blog, self.sub8_blog, self.sub9_blog,
                     self.sub10_blog, self.sub11_blog, self.sub12_blog]

    def blog_click(self):
        for i in self.blog_list:
            self.blog_header.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
