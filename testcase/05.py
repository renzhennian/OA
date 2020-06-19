from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.select import Select
class Test_OA_3(unittest.TestCase):
    def setUp(self):
        self.wb=webdriver.Firefox()
        self.wb.get('http://192.168.0.122:808')
        time.sleep(5)
    #登录
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
    # 新建费用报销单
    def test_2(self):
        self.wb.find_element_by_css_selector(
            '.tabmenu_content > div:nth-child(1) > ul:nth-child(6) > li:nth-child(1)').click()
        time.sleep(3)
        self.wb.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(3)
        self.wb.switch_to.frame(2)
        # Select(self.wb.find_element_by_id('kind')).select_by_value('009')
        self.wb.find_element_by_id('kind').click()
        # time.sleep(3)
        self.wb.find_element_by_xpath("/html/body/form/ul/li[1]/select/option[1]").click()
        time.sleep(3)
        self.wb.find_element_by_xpath('//*[@id="subject"]').send_keys('ren出差费用')
        time.sleep(3)
        self.wb.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('002020-06-05')
        time.sleep(5)
        self.wb.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys("1")
        time.sleep(3)
        self.wb.find_element_by_xpath("/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input").send_keys('住宿')
        time.sleep(3)
        self.wb.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('260')
        time.sleep(3)
        self.wb.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[3]/td[2]/input').send_keys('飞机票')
        time.sleep(3)
        self.wb.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[3]/td[3]/input').send_keys('660')
        time.sleep(3)
        self.wb.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[4]/td[2]/input').send_keys('伙食费')
        time.sleep(3)
        self.wb.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[4]/td[3]/input').send_keys('800')
        time.sleep(3)
        self.wb.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1720')
        time.sleep(3)
        self.wb.find_element_by_xpath('//*[@id="save"]').click()
        a = self.wb.switch_to.alert
        b = self.a.text
        self.assertEqual(b, '成功：当前事务创建成功！', msg='成功：当前事务创建成功！')
        time.sleep(3)
        a.accept()
    #查看新建报销单
    def test_3(self):
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
    #部门领导办理（不同意）
    def test_4(self):
        self.wb.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[3]').click()
        time.sleep(2)
        self.wb.switch_to.frame(2)
        self.wb.find_element_by_xpath('//*[@id="GridView1_ctl02_lbt_Operation"]').click()
        self.wb.switch_to.default_content()
        time.sleep(3)
        self.wb.switch_to.frame('AffairWork10_ifm')
        self.wb.find_element_by_xpath("/html/body/form/dl[3]/dt[2]/label[2]/input").click()
        time.sleep(3)
        self.wb.find_element_by_xpath('//*[@id="opinion"]').send_keys('太贵了')
        time.sleep(2)
        self.wb.find_element_by_xpath('//*[@id="save"]').click()
        self.wb.switch_to.default_content()
        a=self.wb.switch_to.alert
        b=a.text
        print('b',b)
        self.assertEqual(b ,'成功：当前事务办理成功！',msg='办理失败')
        a.accept()
    #删除报销单
    def test_5(self):
        self.wb.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[2]').click()
        self.wb.switch_to.frame('tab_OaAffairList_ifm')
        self.wb.find_element_by_xpath('//*[@id="GridView1_ctl02_cbxCheck"]').click()
        time.sleep(2)
        self.wb.find_element_by_xpath('//*[@id="GridView1_ctl23_lbtDeleteAll"]').click()
        self.wb.switch_to.default_content()
        a = self.wb.switch_to.alert
        b = a.text
        print('b', b)
        self.assertEqual(b, '成功：当前事务办理成功！', msg='办理失败')
        a.accept()
    def tearDown(self):
        self.wb.quit()
        # self.wb.close()
if __name__ == '__main__':
    unittest.main()