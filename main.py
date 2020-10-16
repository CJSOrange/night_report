from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import random
today_time=str(datetime.datetime.now().year)+"/"+str(datetime.datetime.now().month)+"/"+str(datetime.datetime.now().day)
row=21

# 1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# 2.打开晚点名网页
first_url= 'https://docs.qq.com/sheet/DUmNRTWRPTnBJZHho'
print("now access %s" %(first_url))
driver.get(first_url)

# 3.登录账号用快速登入,前提已经挂着电脑qq
driver.find_element_by_id("header-login-btn").click()
time.sleep(3)
driver.switch_to.frame(driver.find_element_by_id('login_frame'))
time.sleep(3)
driver.find_element_by_class_name("img_out_focus").click()

# 4.填写是是
# 4.1定位表格
driver.switch_to.parent_frame()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="canvasContainer"]/div[1]/div[2]').click()
time.sleep(2)
# 4.2查找日期
ActionChains(driver).key_down(Keys.CONTROL).key_down('f').perform()
time.sleep(2)
driver.find_element_by_id('search-panel-input').send_keys(str(today_time))
driver.find_element_by_id('search-panel-input').send_keys(str(today_time))
driver.find_elements_by_class_name('dui-modal-close')[-1].click()
time.sleep(2)
# 4.3定位自己所在行
text=driver.find_element_by_id('alloy-simple-text-editor')
for i in range(row-1):
    text.send_keys(Keys.ENTER)
# 4.4把之后3天全填了
for i in range(6):
    text.click()
    text.clear()
    text.send_keys("是")
    text.send_keys(Keys.TAB)

driver.quit()
print('haha')