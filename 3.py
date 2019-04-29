print('Selamat datang, mau tahu berita apa hari ini?')
print('[1] Berita seputar teknologi \n[2] Berita seputar bisnis \n[3] Berita seputar olahraga \n[4] Berita seputar kesehatan \n[5] Berita seputar science')
a=int(input('Ketik pilihan anda [1/2/3/4/5] :'))

import requests

apikey='7436d5b8db094e7dbfc8bd56f4c8bf42'
if a==1:
    url='https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey='+apikey
    data=requests.get(url)
    print('\nBerikut adalah top 5 berita Indonesia bidang sports : \n')
    for i in range(0,5):
        print((i+1),'-',data.json()['articles'][i]['title'])
    
    
elif a==2:
    url2='https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey='+apikey
    data=requests.get(url2)
    print('\nBerikut adalah top 5 berita Indonesia bidang sports : \n')
    for i in range(0,5):
        print((i+1),'-',data.json()['articles'][i]['title'])

elif a==3:
    url3='https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey='+apikey
    data=requests.get(url3)
    print('\nBerikut adalah top 5 berita Indonesia bidang sports : \n')
    for i in range(0,5):
        print((i+1),'-',data.json()['articles'][i]['title'])
    
elif a==4:
    url4='https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey='+apikey
    data=requests.get(url4)
    print('\nBerikut adalah top 5 berita Indonesia bidang sports : \n')
    for i in range(0,5):
        print((i+1),'-',data.json()['articles'][i]['title'])

else:
    url5='https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey='+apikey
    data=requests.get(url5)
    print('\nBerikut adalah top 5 berita Indonesia bidang sports : \n')
    for i in range(0,5):
        print((i+1),'-',data.json()['articles'][i]['title'])