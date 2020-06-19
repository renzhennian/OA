#查阅事务
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.select import Select
class Test_OA_3(unittest.TestCase):
    def setUp(self):
        self.wb=webdriver.Firefox()
        self.wb.get('http://192.168.0.122:808')
        time.sleep(5)
        self.wb.find_element_by_xpath('//*[@id="tbx_UserName"]').send_keys('adm')
        time.sleep(3)
        self.wb.find_element_by_xpath('//*[@id="tbx_Password"]').send_keys('adm')
        time.sleep(3)
        self.wb.find_element_by_id('ibtLogin').click()
        time.sleep(5)
        a = self.wb.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/ul/li/div[1]').text
        print('sjdf',a)
        self.assertEqual(a, '我的桌面', msg='登录失败')
    def test_1(self):
        self.wb.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[5]').click()
        time.sleep(2)
        self.wb.switch_to.frame('tab_OaAffairFind_ifm')
        self.wb.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[1]/th[1]/a').click()
        time.sleep(2)
        self.wb.find_element_by_xpath('//*[@id="GridView1_ctl02_lbtSubject"]').click()
        time.sleep(3)
        self.wb.switch_to.default_content()
        self.wb.switch_to.frame('AffairView1_ifm')
        self.wb.find_element_by_xpath('/html/body/form/div/a').click()
        time.sleep(3)
        a=self.wb.switch_to.alert
        a.dismiss()
        self.wb.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/ul/li[3]/div[2]').click()


    def tearDown(self):
        self.wb.quit()
        # self.wb.close()
if __name__ == '__main__':
    unittest.main()