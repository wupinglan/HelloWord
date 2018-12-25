from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
class AdminTest(LiveServerTestCase):
    # load fixtures
    fixtures = ['admin.json'] 
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_login(self):  
        # user opens web browser, navigates to admin page
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        print("body:")
        print(body.text)
        print("body结束")
        self.assertIn('Django 管理\n用户名:\n密码:\n', body.text)
    # def test_admin_site(self): 

    #     # user opens web browser, navigates to admin page
    #     self.browser.get(self.live_server_url + '/admin/')
    #     body = self.browser.find_element_by_tag_name('body')
    #     self.assertIn('Django 管理\n用户名:\n密码:\n', body.text)
    #     # users types in username and passwords and presses enter
    #     username_field = self.browser.find_element_by_name('username')
    #     username_field.send_keys('admin')
    #     password_field = self.browser.find_element_by_name('password')
    #     password_field.send_keys('wupinglan')
    #     password_field.send_keys(Keys.RETURN)
    #     # login credentials are correct, and the user is redirected to the main admin page
    #     body = self.browser.find_element_by_tag_name('body')
    #     self.assertIn('Django 管理\n用户名:\n密码:\n', body.text)
        