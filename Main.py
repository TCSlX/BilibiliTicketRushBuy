import datetime 
import time 
from selenium.webdriver.common.by import By 
from selenium import webdriver

# 设置抢购时间
TargetTime = "2023-04-16 16:39:00.00000000"    

WebDriver = webdriver.Chrome()
WebDriver.get("https://show.bilibili.com/platform/detail.html?id=71212&from=pc_ticketlist")   
time.sleep(1)

# 登录         
WebDriver.find_element(By.CLASS_NAME, "nav-header-register").click()    
print("请在10s内登录")     
time.sleep(10)

# 获取所有场次       
scenes = WebDriver.find_elements(By.CLASS_NAME, "select-text")
scene_dict = {scene.text:scene for scene in scenes}

scene = input("请输入想要抢购的场次关键词:")
selected_scene = scene_dict[scene]

while True:        
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')        
    if now >= TargetTime:
        # 刷新页面     
        WebDriver.refresh()           
        selected_scene.click()              
        break

# 点击购买按钮         
WebDriver.find_element(By.CLASS_NAME,"product-buy.enable").click()
# 提交订单      
WebDriver.find_element(By.CLASS_NAME,"confirm-paybtn.active").click()
time.sleep(60)