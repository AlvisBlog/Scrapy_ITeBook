# -*- coding: utf-8 -*-

import re

import scrapy


from SpiderITeBooks.items import Spider_itebooks_Item

class Spiderman001Spider(scrapy.Spider):

    name = 'spiderman001'

    start_urls = ['http://www.allitebooks.com/']


    def start_requests(self):

        first_url='http://www.allitebooks.com/'

        yield scrapy.Request(url=first_url,callback=self.parse_first_page)



    def parse_first_page(self, response):

        html=response.text

        max_page = re.findall('<span class="pages">1 /(.*?)Pages', html,re.S)[0].strip()

        print("当前需要爬取%s页"%max_page)

        for page in range(1,int(max_page)+1):

            visitUrl='http://www.allitebooks.com/page/{}/'.format(page)

            yield scrapy.Request(url=visitUrl,callback=self.parse_page_books)



    def parse_page_books(self,response):

            html=response.text

            page=re.findall('http://www.allitebooks.com/page/(.*?)/',response.url,re.S)[0]

            print("开始获取第%s页的书籍信息"%page)

            book_list=re.findall('<article(.*?)</article>',html,re.S)

            for book in book_list:

                book_link=re.findall('<h2 class="entry-title"><a href="(.*?)"',book,re.S)[0]

                yield scrapy.Request(url=book_link,callback=self.parse_book_info)



    def parse_book_info(self,response):



         html=response.text

         book_name=re.findall('http://www.allitebooks.com/(.*?)/',response.url,re.S)[0]

         print("开始获取书籍:---%s---的信息"%book_name)


         book_detail=re.findall('<div class="book-detail">(.*?)</div>',html,re.S)[0]

         author_list=re.findall('<a href="http://www.allitebooks.com/author/.*?rel="tag">(.*?)</a>',book_detail,re.S)

         category_data=re.findall('<dt>Category:</dt><dd>(.*?)</dd>',html,re.S)[0]

         category_list=re.findall('<a href.*?category" >(.*?)<',category_data,re.S)



         item=Spider_itebooks_Item()


         #书籍ID
         item['book_id']=re.findall('<article class="post-(.*?)post',html,re.S)[0].strip()

         # 书籍的国际标准编号
         item['book_isbn'] = re.findall('<dt>ISBN-10:</dt><dd>(.*?)</dd>', book_detail, re.S)[0].strip()

         #书籍的详情地址
         item['book_detail_link'] = response.url

         # 书籍的作者
         item['book_author'] = str(author_list).replace("'", "").replace("[", "").replace("]", "").replace(r"\u200e",'')

         #书籍的名称
         item['book_name'] = re.findall('<h1 class="single-title">(.*?)</h1>', html, re.S)[0]

         # 书籍的页数
         item['book_page'] = re.findall('<dt>Pages:</dt><dd>(.*?)</dd>', book_detail, re.S)[0].strip()

         #书籍的发布年份
         item['book_pub_year']=re.findall('<dt>Year:</dt><dd>(.*?)</dd>',book_detail,re.S)[0].strip()

         #书籍编写的语言
         item['book_language']=re.findall('<dt>Language:</dt><dd>(.*?)</dd>',book_detail,re.S)[0].strip()

         #书籍的大小
         item['book_size']=re.findall('<dt>File size:</dt><dd>(.*?)</dd>',book_detail,re.S)[0].strip()

         #书籍文件格式
         item['book_format']=re.findall('<dt>File format:</dt><dd>(.*?)</dd>',book_detail,re.S)[0].strip()

         #书籍的分类
         item['book_category'] = str(category_list).replace("'", "").replace("[", "").replace("]", "").replace("&amp;", '&')

         #书籍描述
         item['book_description']=re.findall('<div class="entry-content">(.*?)</div>',html,re.S)[0].replace('<p>','').replace('</p>','').strip()

         #书籍图片
         item['book_img_url']=re.findall('<main id="main-content">.*?<img.*?src="(.*?)"',html,re.S)[0]

         #书籍下载链接
         item['book_down_link']=re.findall('<span class="download-links">.*?<a href="(.*?)"',html,re.S)[0].replace(" ","%20")

         print("书籍:---%s---的信息获取成功"%item['book_name'])

         yield item









