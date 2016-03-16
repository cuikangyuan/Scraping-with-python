__author__ = 'Tim.Cui'

import urllib2
import requests
import re
from bs4 import BeautifulSoup
from sqlutils import basesqlutil

#爬取 chiphell 买菜车栏目 信息
class VegetableCarSpider(object):

    def getVegetableCarData(self):
        current_page = 1
        img_url_prefix = 'http://www.chiphell.com/'
        pre_url = 'http://www.chiphell.com/portal.php?mod=list&catid=58&page='+str(current_page)
        source_code = requests.get(pre_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')

        labels = soup.findAll('input', {'name' : 'custompage'})
        for labelItem in labels:
            page_title = labelItem.parent.find('span').get('title')
            page_title = page_title.encode("utf-8")
            max_page = filter(str.isdigit, page_title)
            max_page = int(max_page)
            
    
        while current_page <= max_page:
            url = 'http://www.chiphell.com/portal.php?mod=list&catid=58&page='+str(current_page)
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, 'lxml')


            
            for link_outer in soup.findAll('dl', {'class' : 'bbda cl'}):

               article_date =  link_outer.find('span', {'class' : 'xg1'})
               #article date
               date_plain = article_date.string

               link = link_outer.find('dt', {'class' : 'xs2'})
               
               href = link.find('a', {'class' : 'xi2'})
               #article link
               link_plain = href.get('href')
               #article title
               title_plain = href.string
               title_plain = title_plain.replace('\'','')
               title_plain = title_plain.replace('\"','')
               #article desc
               desc_plain = link_outer.find('dd', {'class' : 'xs2 cl'}).text
               desc_plain = desc_plain.replace('\'','')
               #img url
               img_url_code = link_outer.find('img', {'class' : 'tn'})
  
               img_url_plain = img_url_prefix + img_url_code.get('src')

               #link_id_part1 = link_plain[32:35]
               #link_id_part2 = link_plain[36:37]
               link_id = re.sub(r'\D', "", link_plain)
               #basesqlutil.vegetable_car_insert_sql(link_id,title_plain,desc_plain,link_plain,img_url_plain,date_plain,current_page,max_page)
               
            current_page += 1
            
            
            
            
            



        
