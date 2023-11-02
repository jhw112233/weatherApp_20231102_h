import requests
from bs4 import BeautifulSoup
#area=("한남동") #지역변경#날씨변경
area = input("날씨를 입력하세요:")

weather_html = requests.get(f'https://search.naver.com/search.naver?&query={area}날씨')

#print(weather_html.text)

weather_soup = BeautifulSoup(weather_html.text,'html.parser')


#<h2 class="title">용산구 한남동</h2>
#지역 테그

area_text = weather_soup.find('h2',{'class':'title'}).text
#현재 날씨가 보여지고 있는 텍스트
print(f"-----------{area_text} 날씨-----------")




# <div class="temperature_text"> <strong><span class="blind">현재 온도
# </span>23.3<span class="celsius">°</span></strong></div>
#현재온도 출력하는 텍스트

today_temperature = weather_soup.find('div',{'class':'temperature_text'}).text
today_temperature= today_temperature[6:11]

print(f"현재온도 : {today_temperature}")



#<span class="weather before_slash">맑음</span>

weat_tx=weather_soup.find('span',{'class':"weather before_slash"}).text
print(f"오늘날씨:{weat_tx}")


yesterday_tx=weather_soup.find('p',{'class':'summary'}).text#어제와 현재 온도 비교
yesterday_tx = yesterday_tx[:13].strip()
#총 13글자를 가져온 후, strip으로 양쪽 공백을 제거
print(yesterday_tx)
#<div class="sort"> <dt class="term">체감</dt> <dd class="desc">24.5°</dd> </div>

sense_tx= weather_soup.find('div',{'class':'sort'}).text
print(sense_tx)

#div class="sort"

sense_tx2= weather_soup.select('div.sort>dd')
#dl태그 중에서 class가 summary 리스트인 태그를 찾은 후, 그 안의 dd태그를 모두 리스트로 반환
sense_tx2 = sense_tx2[0].text
print(sense_tx2)


sense_temperature = weather_soup.find('div',{'class':'weather_info'}).find('dl',{'class':'summary_list'}).find('dd',{'class':'desc'}).text
# <div> 태그 중 클래스가 weather_info 인 div 태그 안에 있는 dl 태그 중 클래스가 summary_list인 dl을 찾음
# dl 태그 안에 있는 dd 태그 중 클래스가 desc 인 태그를 찾아 텍스트 값을 반환
print(f"* 체감온도 : {sense_temperature}")



dust_in = weather_soup.select('ul.today_chart_list>li')
print(dust_in)

dust_in2=dust_in[0].find('span',{'class':'txt'}).text
print(dust_in2)#미세먼지 정보

dust_in3=dust_in[1].find('span',{'class':'txt'}).text
print(dust_in3)#초미세먼지 정보