from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from fake_useragent import UserAgent
from selenium.common.exceptions import * #Handle different exceptions for selenium 
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree, html
import requests
from bs4 import BeautifulSoup as bs

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
        self.follow_status = None
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
                self.driver.execute_script('var element = document.querySelector("body > div.RnEpo.Yx5HN > div > div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > div > div"); element.scrollTop = element.scrollHeight; ')
            except JavascriptException:
                 self.driver.execute_script("window.scrollBy(0, 550)")
            #self.driver.find_element_by_tag_name('li').send_keys(Keys.DOWN)
            time.sleep(2)
    
    def getLikers(self, users = ['daquan']):
        for user in users:
            self.driver.get(self.url + user)
            
            self.driver.execute_script("window.scrollBy(0, 550)")
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]').click() #photo clik
            time.sleep(2)
            self.driver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.EDfFK.ygqzn > div > div > button').click()
            # self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button').click() #likes click
            time.sleep(3)
            for i in range(5):
                users = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[{}]/div[2]/div[1]/div/a/div/div/div/text()'.format(i))
                                                            
                
                self.names.append(users)
                time.sleep(2)
            
            time.sleep(2)
            print(self.names)
    def getFollowers(self, users = 'purpleginee'):
        self.driver.get(self.url+users)
        try:
            followers_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        except NoSuchElementException:
            followers_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        followers_button.click()
        time.sleep(3)

        self.page = self.driver.page_source
        dom = html.fromstring(self.page)
        for i in range(1,6):
        
            # name = dom.xpath('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/a/text()'.format(i))
            name = dom.xpath('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/a/text()'.format(i))            
            name = self.toStr(name)
            self.names.append(name)
        print(self.names)
        self.getUserInfo(self.names)
        print(self.lis)

        # for i in range(1,11):
        #     name = dom.xpath('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/a/text()'.format(i))
        #     name = self.toStr(name)
        #     follow_status = dom.xpath('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[2]/button/text()'.format(i))
        # #    re = requests.get(self.url+name, headers = self.header)
        #     self.driver.get(self.url+name)
        #     self.page  = self.driver.page_source
        #     user_dom = html.fromstring(self.page) #response to string format
        #     time.sleep(2)
                    
        #     user_posts  = user_dom.xpath('/html/body/div[1]/section/main/div/header/section/div[2]/h1/text()')
        #     time.sleep(2)
        #     title = user_dom.xpath('//title')[0]
            
        #     print(user_posts)
        #     user_followers = user_dom.xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span/text()')
        #     user_followings = user_dom.xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span/text()')
        #     self.user_details['Username'] = name
        #     self.user_details['Follow Status']= self.toStr(follow_status)
        #     self.user_details['Followers'] = self.toStr(user_followers)
        #     self.user_details['Followings'] = self.toStr(user_followings)
        #     self.user_details['Posts'] = self.toStr(user_posts)
        #     self.user_index[name] = self.user_details
        #     print('Appended {}. {}'.format(i, name))
        #     time.sleep(2)
        # print(self.user_index)
        
    def follow_likers(self, users):
        for user in users:
            self.driver.get(self.url + user)
                    
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
    def getUserInfo(self,users):
        for user in users:
            self.driver.get(self.url + user)
            page_source = self.driver.page_source
            soup = bs(page_source, 'html.parser')
            infos = soup.find_all(attrs={'class': 'g47SY'})
            try:
                self.follow_status = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
            except NoSuchElementException:
                self.follow_status = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/button')
            no_of_post = infos[0].text
            no_of_followers = infos[1].text
            no_of_following = infos[2].text
            if self.follow_status.text == 'Follow':
                self.follow_status.click()
                print('Followed : ' + user+ ' ' +  no_of_followers )
            else:
                print(user + ' Already Folowed')
            time.sleep(2)
if __name__ == '__main__':
    sample = bot()
    sample.getFollowers()
  