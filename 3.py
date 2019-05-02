print('Selamat datang, mau tahu berita apa hari ini?')
print('[1] Berita seputar teknologi \n[2] Berita seputar bisnis \n[3] Berita seputar olahraga \n[4] Berita seputar kesehatan \n[5] Berita seputar science')
a=input('Ketik pilihan anda [1/2/3/4/5] :')

import requests
dicteng={1:'technology',2:'business',3:'sports',4:'health',5:'science'}
dictindo={1:'teknologi',2:'bisnis',3:'olahraga',4:'kesehatan',5:'science'}

if a.isdigit():
    a=int(a)
    if a in range(1,len(dicteng)+1):
        apikey='7436d5b8db094e7dbfc8bd56f4c8bf42'
        url= 'https://newsapi.org/v2/top-headlines?country=id&category='+dicteng[a]+'&apiKey='+apikey
        text='\nBerikut adalah top 5 berita Indonesia bidang '+dictindo[a]+' : \n'

        if a==1:
            data=requests.get(url)
            print(text)
            for i in range(0,5):
                print((i+1),'-',data.json()['articles'][i]['title'])
                    
        elif a==2:
            data=requests.get(url)
            print(text)
            for i in range(0,5):
                print((i+1),'-',data.json()['articles'][i]['title'])

        elif a==3:
            data=requests.get(url)
            print(text)
            for i in range(0,5):
                print((i+1),'-',data.json()['articles'][i]['title'])
            
        elif a==4:
            data=requests.get(url)
            print(text)
            for i in range(0,5):
                print((i+1),'-',data.json()['articles'][i]['title'])

        else:
            data=requests.get(url)
            print(text)
            for i in range(0,5):
                print((i+1),'-',data.json()['articles'][i]['title'])
    else:
        print('Maaf pilihan yang anda input tidak tersedia')
else:
    print('Maaf pilihan yang anda input tidak tersedia')