from bs4 import BeautifulSoup
from urllib.request import urlopen as uo
from selenium import webdriver
import pandas as pd


class StockModel:
    def __init__(self, item):
        self.item = item
        self.url = 'https://finance.naver.com/item/sise_day.nhn?code={item}'.format(item=self.item)
        self.df = pd.DataFrame()

    def scrap(self):
        url = 'https://finance.naver.com/item/sise_day.nhn?code={item}'.format(item=self.item)
        uo(url)
        #class = tah p11
        soup = BeautifulSoup(uo(url), "html.parser")
        for i in soup.find_all(name="span", attrs=({"class":"tah"})):
            print(str(i.text))


    #페이징 처리된 부분의 주식정보 가져오기
    def selWeb(self):
        self.driver = webdriver.Chrome(executable_path='D:/pyproject/sample_project/data/chromedriver')
        self.driver.implicitly_wait(3)
        self.driver.get(self.url)

        #self.driver.find_element_by_name('id').send_keys('')
        #self.driver.find_element_by_name('pw').send_keys('')
        self.driver.implicitly_wait(3)
        # 정규식
        # *// 어떠한 값이 오는 경우에도
        # id의 속성이 []안에 있는 값일 경우
        # click 이벤트 전달
        #self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

        self.driver.find_element_by_xpath('//tbody/tr/td[@class="pgR"]/a').click()
        self.driver.implicitly_wait(3)

     #   self.driver.get('https://order.pay.naver.com/home')
        #화면에 있는 그대로의 html
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        #notices = soup.select('div.p_inr > div.p_info > a > span')
        tr = soup.select('table > tbody > tr')

        #컬럼 명
        stock_columns = ['날짜', '종가', '전일비', '시가', '고가', '저가', '거래량']

        temp = []
        num = 1
        result = soup.find("")
        #tr단위로 저장
        for b in tr:
            #print(b)
            #print(b.text)
            for i in b.find_all(name="span", attrs=({"class":"tah"})):
                #print(str(i))
                #print(str(i.text))
                #strip() -> \n \t 등 각종 개행문자 제거
                temp.append(str(i.text).strip())
                print("=========")
                #print(temp)
            print("td값 종료")
            if len(temp) > 0:
                #data = {temp[0]:temp[1:]}
                #self.df[temp[0]] = temp[1:]
                #self.df = temp[:]

                #행 추가
                #self.df.loc[num] = temp[:]

                #열 추가
                self.df[num] = temp[:]
                num = num + 1
            temp = []
        #행과 열 전치 -> transpose() or T
        #self.df.columns = stock_columns
        #컬럼 추가는 데이터프레임이 널이 아니여야 가능
        print(self.df)
        self.df = self.df.transpose()
        self.df.columns = stock_columns
        #컬럼명 추가
        #self.df.columns = stock_columns
        print(self.df)
        #csv로 저장
        self.df.to_csv('D:\Output.csv', encoding='utf-8-sig')
        #for i in notices:
        #    print(i.text.strip())