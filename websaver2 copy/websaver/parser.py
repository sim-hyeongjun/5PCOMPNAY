# parser.py
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
import django
django.setup()
# BlogData를 import해옵니다
from parsed_data.models import BlogData

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
                news_link.append("https://land.naver.com/" + dt_photo[0].find("a")["href"])
                img_link.append('https://img.freepik.com/free-photo/downtown-cityscape-at-night-in-seoul-south-korea_335224-272.jpg?w=1380&t=st=1670381883~exp=1670382483~hmac=1d49d4fa660f16b4c9df642e674945229f6f799592e8fc4d0ad118523b78bdd3')
            elif len(dt_photo) == 2:
                title.append(dt_photo[1].find("a").text)
                news_link.append("https://land.naver.com/" + dt_photo[1].find("a")["href"])
                img_link.append(dt_photo[0].find("img")["src"])

    return title,news_link,img_link
    
def get_dict_title_data():
    blog_data_dict = get_news_data()
    title={}
    for i in range(len(blog_data_dict[0])):
        title[str(i)] = blog_data_dict[0][i]
    return title
def get_dict_link_data():
    blog_data_dict = get_news_data()
    link={}
    for i in range(len(blog_data_dict[0])):
        link[str(i)]= blog_data_dict[1][i]
    return link
        
def get_dict_img_data():
    blog_data_dict = get_news_data()
    img={}
    for i in range(len(blog_data_dict[0])):
        img[str(i)] = blog_data_dict[2][i]
    print(img)
    return img
    
        
if  __name__ == '__main__':
    blog_data_dict = get_dict_title_data()
    blog_link_dict = get_dict_link_data()
    blog_img_dict = get_dict_img_data()
    for i in range(len(blog_link_dict)):
        BlogData(title =blog_data_dict[str(i)],
        link =blog_link_dict[str(i)],
        img = blog_img_dict[str(i)]).save()







'''
if  __name__ == '__main__':
    blog_data_dict = get_dict_title_data()
    blog_link_dict = get_dict_link_data()
    blog_img_dict = get_dict_img_data()
    for i in range(len(blog_link_dict)):
        BlogData(title =blog_data_dict[str(i)],
        link =blog_link_dict[str(i)],
        img = blog_img_dict[str(i)]).save

    for i,j,k in blog_data_dict.values():
        BlogData(title = i).save()
    for j in blog_link_dict.values():
        BlogData(link = j).save()
    for k in blog_img_dict.values():
        BlogData(img = k).save()
        

if __name__=='__main__':
    blog_data_dict = parse_blog()
for t, l in blog_data_dict.items():
    BlogData(title=t, link=l).save()
'''







