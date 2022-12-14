import json
import sys,io,os
import django



sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "maping.settings")
django.setup()

from you.models import Restaurant
def parsing():

    with open('restaurants.json') as json_file:
        json_data = json.load(json_file)

    post = []
    
    for i in range(3):
        post.append({
            'name': json_data['restaurants'][i]['name'],
            'loc': json_data['restaurants'][i]['loc'],
            'lat': json_data['restaurants'][i]['lat'],
            'lon': json_data['restaurants'][i]['lon']
        })
    return post

if __name__ == '__main__':
    post = parsing()

    for i in range(len(post)):
        Restaurant(
            name = post[i]['name'],
            location =post[i]['loc'],
            latitude = post[i]['lat'],
            longitude= post[i]['lon']

        ).save()