from selenium import webdriver
import time
import unittest
class Test_OA_0(unittest.TestCase):
    def setUp(self):
        self.wb=webdriver.Firefox()
        self.wb.get('http://192.168.0.117:808')
        time.sleep(5)
    def test_1(self):
        self.wb.find_element_by_xpath('//*[@id="tbx_UserName"]').send_keys('adm')
        time.sleep(3)
        self.wb.find_element_by_xpath('//*[@id="tbx_Password"]').send_keys('adm')
        time.sleep(3)
        self.wb.find_element_by_id('ibtLogin').click()
        time.sleep(5)
        a = self.wb.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/ul/li/div[1]').text
        print('sjdf',a)
        self.assertEqual(a, '我的桌面', msg='登录失败')
    def test_2(self):
        self.wb.find_element_by_id('tbx_UserName').send_keys('amd')
        time.sleep(3)
        self.wb.find_element_by_id('tbx_Password').send_keys('cmd')
        time.sleep(3)
        self.wb.find_element_by_id('ibtLogin').click()
        time.sleep(3)
        a = self.wb.switch_to.alert
        b=a.text
        print("这是",b)
        self.assertEqual(b,'失败：用户账号或密码错误！',msg='用户账号或密码错误')
        time.sleep(3)
        a.accept()
    def test_3(self):
        self.wb.find_element_by_id('tbx_UserName').send_keys('')
        time.sleep(5)
        self.wb.find_element_by_id('tbx_Password').send_keys('adm')
        time.sleep(5)
        self.wb.find_element_by_id('ibtLogin').click()
        time.sleep(5)
    def test_4(self):
        self.wb.find_element_by_id('tbx_UserName').send_keys('adm')
        time.sleep(5)
        self.wb.find_element_by_id('tbx_Password').send_keys('')
        time.sleep(5)
        self.wb.find_element_by_id('ibtLogin').click()
        time.sleep(5)
    def tearDown(self):
        self.wb.quit()
        self.wb.close()
if __name__ == '__main__':
    unittest.main()