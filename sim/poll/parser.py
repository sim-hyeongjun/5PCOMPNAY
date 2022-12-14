
import requests
from bs4 import BeautifulSoup  
import json 
from collections import OrderedDict
# 아래 4줄을 추가해 줍니다.
import os
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
from poll.models import News
django.setup()



        # 여기부터 내가 한거
def get_news_data():
    ## 네이버 기사 크롤링
    import urllib.request
    from bs4 import BeautifulSoup
    url = 'https://land.naver.com/news/issueView.naver?'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')

    len_photo = soup.select('ul > li')

    title =[]
    news_link=[]
    img_link=[]
    for i in len_photo:
        dl_photo = i.select('li > dl')
        for j in range(len(dl_photo)):
            dt_photo = dl_photo[j].select('dl > dt')
            if len(dt_photo) == 1:
                title.append(dt_photo[0].find("a").text)
                news_link.append(dt_photo[0].find("a")["href"])
                img_link.append('https://img.freepik.com/free-photo/downtown-cityscape-at-night-in-seoul-south-korea_335224-272.jpg?w=1380&t=st=1670381883~exp=1670382483~hmac=1d49d4fa660f16b4c9df642e674945229f6f799592e8fc4d0ad118523b78bdd3')
            elif len(dt_photo) == 2:
                title.append(dt_photo[1].find("a").text)
                news_link.append(dt_photo[1].find("a")["href"])
                img_link.append(dt_photo[0].find("img")["src"])


    products = OrderedDict()
    for  k in len(title):
        products = {'News': {

        {'title': title[k],
        'link': news_link[k],
        'img': img_link[k],        
            }
        }
    }  
      
    with open("C:\VENV\sim\polldata.json", "w") as f:
        json.dump(products, f)
    
    with open('data.json') as f:
        json.load(f)
    
    
    post = []
    
    for i in range(len(title)):
        post.append({
            'name': f['News'][i]['title'],
            'link': f['News'][i]['link'],
            'img': f['News'][i]['img'],

        })
    return post
    


if __name__ == '__main__':
    post = get_news_data()

    for i in range(len(post)):
        News(
            title = post[i]['name'],
            description =post[i]['link'],
            content = post[i]['img'],


        ).save()
    






'''
if __name__=='__main__':
    blog_data_dict = get_news_data()
    for i in range(len(blog_data_dict[0])):
        News(title=blog_data_dict[0][i]).save() #기사제목
        News(description=blog_data_dict[1][i]).save() # 기사링크
        News(content=blog_data_dict[2][i]).save() # 이미지링크
'''