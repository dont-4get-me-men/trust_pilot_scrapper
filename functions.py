import requests
from bs4 import BeautifulSoup
from consts import *

def download_page(link: str
                 ,page_number:int
                 ,folder: str
                 ,headers: dict)-> int:
    '''
    Download page from link and save to folder as html file
    '''
    path = folder + '/page{}.html'.format(page_number)
    res = requests.get(link.format(page_number),headers=headers)
    soup = BeautifulSoup(res.content)
    with open(path,'w') as f:
        f.write(str(soup))
    if len(soup.find_all(class_ = classes['all_class']))==0:
        return page_number
    return 0

def find_class(stri: str
             ,name_class:str 
             ,span: bool = False
             ,img: bool = False
             ,split: bool = False)-> str:
    '''Find info on class in html code '''
    a = stri.find(class_ = classes[name_class])
    if a is None:
        return 'None'
    else:
        if span:
            return a.find('span').text
        elif img:
            return a.find('img').get('alt').split(' ')[1]
        elif split:
            return a.text.split(':')[1].strip()
        return a.text

def get_data_from_page(path):
    with open(path,'r') as f:
        html_info = f.read()
    soup = BeautifulSoup(html_info)
    all_classes = soup.find_all(class_ =classes['all_class'])

    # all classes is a list of comments in one page. In average it 20 comments 
    resulted_arrray = []
    for i in all_classes:
        res_dict = {
            'country':find_class(i,'country',span=True)
            ,'review':find_class(i,'review')
            ,'title':find_class(i,'title')
            ,'date':find_class(i,'date',split=True)
            ,'stars':find_class(i,'stars',img=True)
        }
        resulted_arrray.append(res_dict)
    return resulted_arrray

