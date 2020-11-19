"""
HogwartsAppiumCode - 当前Project名称;
basepage - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/9/2 10:53 上午
"""
import yaml
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
import logging
def get_capabilities():
    with open('../datas/capabilities.yaml') as f:
        capabilities = yaml.safe_load(f)
    return capabilities

class BasePage():
    _current_element:WebElement = None
    _current_elements = []
    driver:WebDriver = None

    logging.basicConfig(level=logging.NOTSET)  # 设置日志级别

    def __init__(self,driver:WebDriver = None):
        self.driver = driver

    def start(self):
        logging.info('启动')

        capabilities = get_capabilities()
        cap = capabilities['capabilities']
        url = capabilities['url']

        if self.driver == None:
            self.driver = webdriver.Remote(url, cap)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()

        return self

    def stop(self):
        logging.info('退出')
        self.driver.quit()

    def find(self,locator):
        logging.info('查找')
        logging.info(locator)
        self._current_element = self.driver.find_element(*locator)
        return self

    def finds(self,locator):
        logging.info('查找')
        logging.info(locator)
        self._current_elements = self.driver.find_elements(*locator)
        return self

    def click(self):
        logging.info('点击')
        self._current_element.click()
        return self

    def send_keys(self,value):
        logging.info('输入：' + value)
        self._current_element.send_keys(value)
        return self

    def back(self):
        logging.info('返回')
        self.driver.back()
        return self

    def po_run(self,po_method, **kwargs):#可以接收任意数量关键词参数的kwargs
        #po_method:yaml文件中的key
        # todo：测试步骤的数据驱动
        with open('../datas/elements.yaml') as f:
            eles = yaml.safe_load(f)
            if po_method in eles.keys():
                item = eles[po_method]
                info = item['info']
                print('步骤：' + info)
                for step in item['step']:
                    # 如果step 是字典
                    if isinstance(step,dict):
                        for key in step.keys():
                            if key == 'id':
                                locator = (MobileBy.ID,step[key])
                                self.find(locator)
                            if key == 'xpath':
                                locator = (MobileBy.XPATH,step[key])
                                print(locator)
                                self.find(locator)
                            if key == 'css':
                                locator = (MobileBy.CSS_SELECTOR,step[key])
                                print(locator)
                                self.find(locator)

                            elif key == 'click':
                                self.click()

                            elif key == 'sendkeys':
                                text = str(step[key])
                                for k,v in kwargs.items():
                                    text = text.replace('${' + k + '}',str(v))
                                self.send_keys(text)

                            elif key == 'scroll':
                                text = str(step[key])
                                self.find_by_scroll(text)
                            # todo: 更多关键词
                    else:
                        logging.info('格式错误')


            else:
                logging.info('method name error')


    def find_by_scroll(self,text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()'
                   '.scrollable(true).instance(0))'
                   '.scrollIntoView(new UiSelector()'
                   f'.text("{text}").instance(0));')
        self.find(element)
        return self

    def get_toast(self):
        element = (MobileBy.XPATH,"//*[@class='android.widget.Toast']")
        self.find(element)
        text = self._current_element.text

        return text






