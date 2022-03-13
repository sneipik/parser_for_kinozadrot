from numpy import number
import requests
from bs4 import BeautifulSoup
import pandas as pd 



def get_number_of_pages(): 
    url = 'http://vc.kinozadrot.cc/serial/page/1/'

    r = requests.get(url)

    soup = BeautifulSoup(r.text,'lxml')

    pages = soup.find('div',class_='navigation').findAll('a')
    numbers = [i.text for i in pages]
    
    return int(numbers[-1])



def get_datas():

    datas = []

    pages = get_number_of_pages()
    for page_num in range(0,pages):

        url = f'http://vc.kinozadrot.cc/serial/page/{page_num+1}/'
    
        soup = BeautifulSoup(requests.get(url).text,'lxml')

        serials = soup.findAll('div',class_='th-item')

        for serial in serials:

       
            s_title = serial.find('div',class_='th-title').text
            s_info = serial.findAll('div',class_='th-year')[0].text.split()  
        
            datas.append([s_title,s_info[0],s_info[1:]])
    
    return datas


def get_cvs_file(): 
    header = ['name','year','genre']
    df = pd.DataFrame(get_datas(),columns=header)
    df.to_csv('serials.csv',sep=';',encoding='utf-8')


get_cvs_file()




