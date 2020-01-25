from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from fake_useragent import UserAgent
from selenium.common.exceptions import * #Handle different exceptions for selenium 
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree, html
import requests, bs4

class bot():
    def __init__(self):
        self.user = 'savage_sperm'
        self.password = 'avikp@33'
        self.url = 'https://www.instagram.com/'
        
        
        # self.mobile_emulation = {
        #     "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

        #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

        #for requests 
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        self.header = {'User-Agent': self.user_agent}

        #for chrome options 
        #self.options.add_experimental_option("mobileEmulation", self.mobile_emulation)
        self.options = Options()
        self.options.add_argument('--user-agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"')
        self.options.add_argument("user-data-dir=/Users/xxxx/Desktop/pythonpr/pythonpr/Default") #login from previous saved user data
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.options) #install and manage chromedriver automatically 
        self.driver.get(self.url)
        self.page = None 
        self.names = []
        self.user_details = {}
        self.user_index = {}
        time.sleep(2)
        self.lis = []
        self.target_acc = None
    def login(self):

        #go to login
        try: 
            #pc
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()
        except NoSuchElementException:
            #phone
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button').click()
        else: 
            time.sleep(3)

        #self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[4]/div/label/input').send_keys(self.user)

        #enter username
        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.user)
            time.sleep(2)
        except:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[4]/div/label/input').send_keys(self.user)
            time.sleep(2)
        else: 
            time.sleep(5)


        #enter password 
        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password, Keys.ENTER)
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[5]/div/label/input').send_keys(self.password, Keys.ENTER)
        else: 
            time.sleep(3)
        #login 
        # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        # time.sleep(3)
        
        #self.driver.close()
    def profile(self):
        #not Now 
        print('to profile')
        try: 
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]').click()
        except NoSuchElementException: 
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
        except:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/button').click()
        
        else: 
            time.sleep(2)
        time.sleep(3)
    def scroll(self, no_of_times):
        for i in range(no_of_times):
            try:
                self.driver.execute_script('var element = document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP"); element.scrollTop = element.scrollHeight; ')
            except JavascriptException:
                 self.driver.execute_script("window.scrollBy(0, 550)")
            #self.driver.find_element_by_tag_name('li').send_keys(Keys.DOWN)
            time.sleep(2)
    def unfollow(self):
        #self.login()
        print('out of profile')
        time.sleep(2)
        try:
            uf_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        except NoSuchElementException:
            uf_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        uf_button.click()
        time.sleep(3)

        # try:
        #     box = self.driver.find_element_by_xpath('//div[@class="PZuss"]')
        # # except NoSuchElementException:
        # #     box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[1]')
        # else: 
        #     time.sleep(1)
        # hover = ActionChains(self.driver).move_to_element(box)
        # hover.perform()
        
        # box.click()
        self.page = self.driver.page_source
    # def usernames(self):
        
    #     dom = html.fromstring(self.page)
    #     for i in range(1,6):
    #         name = dom.xpath('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/a/text()'.format(i))
    #         name = self.toStr(name)
    #         self.names.append(name)
    #     print(self.names)
    #     for name in self.names:
    #         print(name)
    #         response = self.driver.get(self.url + name)
    #         # print(response.content)
    #         self.page = self.driver.page_source
    #         time.sleep(2)

    #         dom = html.fromstring(self.page)
    #         ullist = dom.xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span/text()')
    #         time.sleep(2)
    #         user_followers = dom.xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span/text()')
    #         print(ullist)
    #         time.sleep(2)
    #         self.lis.append(self.toStr(user_followers))
    #         # for lista in ullist:
    #         #     info_post = lista.xpath('li[1]/span/span/')
    #         #     print(info_post.text_content())
    #         #     time.sleep(2)
    #         # user_posts  = dom.xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span/text()')
    #         # print(self.toStr(user_posts))
    #         time.sleep(2)
    #     print(self.lis)
    #     # for i in range(1,11):
    #     #     name = dom.xpath('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/a/text()'.format(i))
    #     #     name = self.toStr(name)
    #     #     follow_status = dom.xpath('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[2]/button/text()'.format(i))
    #     # #    re = requests.get(self.url+name, headers = self.header)
    #     #     self.driver.get(self.url+name)
    #     #     self.page  = self.driver.page_source
    #     #     user_dom = html.fromstring(self.page) #response to string format
    #     #     time.sleep(2)
                    
    #     #     user_posts  = user_dom.xpath('/html/body/div[1]/section/main/div/header/section/div[2]/h1/text()')
    #     #     time.sleep(2)
    #     #     title = user_dom.xpath('//title')[0]
            
    #     #     print(user_posts)
    #     #     user_followers = user_dom.xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span/text()')
    #     #     user_followings = user_dom.xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span/text()')
    #     #     self.user_details['Username'] = name
    #     #     self.user_details['Follow Status']= self.toStr(follow_status)
    #     #     self.user_details['Followers'] = self.toStr(user_followers)
    #     #     self.user_details['Followings'] = self.toStr(user_followings)
    #     #     self.user_details['Posts'] = self.toStr(user_posts)
    #     #     self.user_index[name] = self.user_details
    #     #     print('Appended {}. {}'.format(i, name))
    #     #     time.sleep(2)
    #     # print(self.user_index)
        
    def follow_user(self):
        self.target_acc = 'shitheadsteve'
        self.driver.get(self.url+ self.target_acc )
        self.page = self.driver.page_source
        dom = html.fromstring(self.page)
        #post containers 1 container contains 3 posts
        for i in range(1,2):
            post_container = dom.xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[{}]'.format(i))
            #for 3 posts
            for j in range(1,4):
                post = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[{}]/div[1]/a/div/div[2]'.format(j)).click()
                likes_button = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button').click()
                self.scroll(3)
                for i in range(1,11):
                    dom_page = self.driver.page_source
                    domm = html.fromstring(dom_page)
                    name = domm.xpath('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/a/text()'.format(i))
                    name = self.toStr(name)
                    follow_status = domm.xpath('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[2]/button/text()'.format(i))
                    self.user_details['Username'] = name
                    self.user_details['Follow Status']= self.toStr(follow_status)
                    
        print(self.user_details)
    def toStr(self, string):
        return ''.join(map(str, string))
    def like_post(self):
        #like by hashtag
        tag = 'memes'
        tag_url = self.url + 'explore/tags/' + tag
        self.driver.get(tag_url)
        self.scroll(2)
        self.page = self.driver.page_source
        dom = html.fromstring(self.page)
        
    
            # post_xpath = dom.xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[{}]/div[{}]/a/@href'.format(i, j))
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]').click()
        time.sleep(2)
        
        # like_button = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/svg' ).get_attribute('aria-label')
        for i in range(10):
            like_button = self.driver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg')
            
            if like_button.get_attribute('aria-label') == 'Like':
                like_button.click()
                time.sleep(2)
                i +=1
                print('Liked {} post'.format(i))
                
                self.next()
            else:
                print('already liked')
                self.next()
                time.sleep(2)
                
    def next(self):
        self.driver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.EfHg9 > div > div > a.HBoOv.coreSpriteRightPaginationArrow').click()

        
        time.sleep(2)


sample = bot()
sample.like_post()