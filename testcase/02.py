from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.select import Select
class Test_OA_2(unittest.TestCase):
    def setUp(self):
        self.wb=webdriver.Firefox()
        self.wb.get('http://192.168.0.121:808')
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
        self.wb.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[2]').click()
        time.sleep(3)
        self.wb.switch_to.frame(2)
        self.wb.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[1]/th[1]/a').click()
        time.sleep(2)
        self.wb.find_element_by_xpath('//*[@id="GridView1_ctl07_lbtTitle"]').click()
        a=self.wb.find_element_by_xpath('/html/body/div[3]/div/div[2]/span/table[1]/tbody/tr[2]/td[2]').text
        print("a:",a)
        self.assertEqual(a,'费用报销单',msg='查看失败')
        time.sleep(2)
        self.wb.find_element_by_xpath('/html/body/div[3]/div/div[1]/img').click()

    def tearDown(self):
        self.wb.quit()
        # self.wb.close()

if __name__ == '__main__':
    unittest.main()
