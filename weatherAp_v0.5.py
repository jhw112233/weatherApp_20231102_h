#weather Application v0.5

import sys
import requests
from bs4 import BeautifulSoup

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("ui/weatherF.ui")[0]

class WeatherWin(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("오늘의 날씨")
        self.setWindowIcon(QIcon('img/icon1.png'))
        self.statusBar().showMessage("Weather Application Ver 0.5")

        self.weathr_btn.clicked.connect(self.request_weather)

    def request_weather(self):
        area = self.inputBox1.text() #입력
        weather_html = requests.get(f'https://search.naver.com/search.naver?&query={area}날씨')
        weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

        area_text = weather_soup.find('h2', {'class': 'title'}).text
        self.area_1.setText(area_text) #area레이블에 area_text를 출력
        # 오타 입력시 이상한 언어 나옴
        #에러 날경우 대비하여 예외처리를 해야한다
        #해외날씨는 소스가 다르기때문에 다르게 만들어야 함



if __name__=='__main__':
    app = QApplication(sys.argv)
    win = WeatherWin()
    win.show()
    sys.exit(app.exec_())
