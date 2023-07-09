import datetime 
import time 
from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

TargetTime = "2023-04-16 16:39:00.00000000"  # 设置抢购时间
WebDriver = webdriver.Chrome()
WebDriver.get("https://show.bilibili.com/platform/detail.html?id=71212&from=pc_ticketlist")  # 输入目标购买页面
time.sleep(1)
print("进入购票页面成功")
WebDriver.find_element(By.CLASS_NAME, "nav-header-register").click()
print("请在10s内登录")
time.sleep(10)

# if(WebDriver.find_element(By.CLASS_NAME, "product-buy")):
#     print("确认此页面为预购页面")
#     time.sleep(3)
# elif(WebDriver.find_element(By.CLASS_NAME, "product-buy.enable")):
#     print("确认此页面为直接购买页面")
#     time.sleep(3)
# else:
#     print("此页面未发现预购按钮")
#     time.sleep(3)

# while True:
#     try:
#         WebDriver.find_element(By.CLASS_NAME, "product-buy.enable")
#         print("找到购买按钮")
#         break
#     except:
#         print("无购买按钮")

#刷新页面部分

while True:
    try:
        wait = WebDriverWait(WebDriver, 10)
        product_buy_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-buy.enable")))
        if len(product_buy_buttons) > 0:
            print("找到购买按钮")
            product_buy_buttons[0].click()  # 点击第一个购买按钮
            print("进入购买页面成功")
            break
        else:
            print("无购买按钮")
    except:
        print("无法点击购买")
        time.sleep(1)

try:
    wait = WebDriverWait(WebDriver, 10)
    confirm_paybtn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "confirm-paybtn.active")))
    confirm_paybtn.click()
    print("订单创建完成，请在一分钟内付款")
    # time.sleep(60)
except:
    print("无法点击创建订单")