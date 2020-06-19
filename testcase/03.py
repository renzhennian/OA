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
    #部门办理
    def test_1(self):
        self.wb.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[3]').click()
        time.sleep(2)
        self.wb.switch_to.frame(2)
        self.wb.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[1]/th[1]/a').click()
        time.sleep(2)
        self.wb.find_element_by_xpath('//*[@id="GridView1_ctl02_lbt_Operation"]').click()
        self.wb.switch_to.default_content()
        time.sleep(3)
        self.wb.switch_to.frame('AffairWork10_ifm')
        self.wb.find_element_by_xpath("/html/body/form/dl[3]/dt[2]/label[2]/input").click()
        time.sleep(3)
        self.wb.find_element_by_xpath("/html/body/form/dl[3]/dt[2]/label[1]/input").click()
        time.sleep(5)
        self.wb.find_element_by_xpath('//*[@id="selectClerk"]').click()
        time.sleep(2)
        self.wb.switch_to.frame(1)
        self.wb.find_element_by_xpath('//*[@id="TreeView1n3CheckBox"]').click()
        time.sleep(2)
        self.wb.find_element_by_xpath('//*[@id="btn_Ok"]').click()
        time.sleep(3)
        self.wb.switch_to.default_content()
        self.wb.switch_to.frame('AffairWork10_ifm')
        self.wb.find_element_by_xpath('//*[@id="save"]').click()
        self.wb.switch_to.default_content()
        a=self.wb.switch_to.alert
        b=a.text
        print('b',b)
        self.assertEqual(b ,'成功：当前事务办理成功！',msg='办理失败')
        a.accept()
    #主管领导办理
    def test_2(self):
        self.wb.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[3]').click()
        time.sleep(2)
        self.wb.switch_to.frame(2)
        self.wb.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[1]/th[1]/a').click()
        time.sleep(2)
        self.wb.find_element_by_xpath('//*[@id="GridView1_ctl02_lbt_Operation"]').click()
        self.wb.switch_to.default_content()
        time.sleep(3)
        self.wb.switch_to.frame('AffairWork10_ifm')
        self.wb.find_element_by_xpath("/html/body/form/dl[3]/dt[2]/label[2]/input").click()
        time.sleep(3)
        self.wb.find_element_by_xpath("/html/body/form/dl[3]/dt[2]/label[1]/input").click()
        self.wb.find_element_by_xpath('//*[@id="save"]').click()
        self.wb.switch_to.default_content()
        a = self.wb.switch_to.alert
        b=a.text
        print('b', b)
        self.assertEqual(b , '成功：当前事务办理成功！', msg='办理失败')
        a.accept()
    #总经理办理
    def test_3(self):
        self.wb.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[3]').click()
        time.sleep(2)
        self.wb.switch_to.frame(2)
        self.wb.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[1]/th[1]/a').click()
        time.sleep(2)
        self.wb.find_element_by_xpath('//*[@id="GridView1_ctl02_lbt_Operation"]').click()
        self.wb.switch_to.default_content()
        time.sleep(3)
        self.wb.switch_to.frame('AffairWork10_ifm')
        self.wb.find_element_by_xpath("/html/body/form/dl[3]/dt[2]/label[2]/input").click()
        time.sleep(3)
        self.wb.find_element_by_xpath("/html/body/form/dl[3]/dt[2]/label[1]/input").click()
        time.sleep(5)
        self.wb.find_element_by_xpath('//*[@id="selectClerk"]').click()
        time.sleep(2)
        self.wb.switch_to.frame(1)
        self.wb.find_element_by_xpath('//*[@id="TreeView1n3CheckBox"]').click()
        time.sleep(2)
        self.wb.find_element_by_xpath('//*[@id="btn_Ok"]').click()
        time.sleep(3)
        self.wb.switch_to.default_content()
        self.wb.switch_to.frame('AffairWork10_ifm')
        self.wb.find_element_by_xpath('//*[@id="save"]').click()
        self.wb.switch_to.default_content()
        a= self.wb.switch_to.alert
        b=a.text
        print('a', b)
        self.assertEqual(b, '成功：当前事务办理成功！', msg='办理失败')
        a.accept()
    #财务部门办理
    def test_4(self):
        self.wb.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[3]').click()
        time.sleep(2)
        self.wb.switch_to.frame(2)
        self.wb.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[1]/th[1]/a').click()
        time.sleep(2)
        self.wb.find_element_by_xpath('//*[@id="GridView1_ctl02_lbt_Operation"]').click()
        self.wb.switch_to.default_content()
        time.sleep(3)
        self.wb.switch_to.frame('AffairWork10_ifm')
        self.wb.find_element_by_xpath("/html/body/form/dl[3]/dt[2]/label[2]/input").click()
        time.sleep(3)
        self.wb.find_element_by_xpath("/html/body/form/dl[3]/dt[2]/label[1]/input").click()
        self.wb.find_element_by_xpath('//*[@id="save"]').click()
        self.wb.switch_to.default_content()
        a = self.wb.switch_to.alert
        b=a.text
        print('b', b)
        self.assertEqual(b , '成功：当前事务办理成功！', msg='办理失败')
        a.accept()
    def tearDown(self):
        self.wb.quit()
        # self.wb.close()
if __name__ == '__main__':
    unittest.main()
