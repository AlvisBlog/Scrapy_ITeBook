# -*- coding: utf-8 -*-
import time

import pymysql

from SpiderITeBooks import settings

class SpideritebooksPipeline(object):

    def __init__(self):

        '''初始化连接数据库'''

        print("正在连接数据库")

        time.sleep(5)

        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

        print("数据库连接成功")


    def process_item(self, item, spider):

        try:

            self.cursor.execute(
                "insert into itebooks.book_info (book_id,book_isbn,book_detail_link,book_author,book_name,"
                "book_page,book_pub_year,book_language,book_size,book_format,book_category,"
                "book_description,book_down_link,book_img_url) "
                "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                [item['book_id'], item['book_isbn'], item['book_detail_link'], item['book_author'],item['book_name'],
                 item['book_page'],item['book_pub_year'],item['book_language'],item['book_size'], item['book_format'],
                 item['book_category'],item['book_description'], item['book_down_link'],item['book_img_url']
                 ])

            # 提交sql语句
            self.connect.commit()

            print("书籍信息%s写入成功"%item['book_name'])


        except Exception as e:

            with open("error.log","a") as f:

                f.write(time.strftime("%Y-%m-%d %H:%M:%S   ")+"书籍信息写入失败,原因:  %s"%e+"\n"+"\n")

            self.connect.rollback()

        return item