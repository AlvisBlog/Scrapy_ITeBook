# -*- coding: utf-8 -*-


import os
import re
import time

import requests
import pymysql

class Download_ITeBooks:

    def __init__(self):

        self.down_url = []

        self.un_down_url = []

        self.user_url=[]


    def user_select_url(self):

        self.page=input("请选择页数不大于多少:")

        self.size=input("请选择文件不大于多少:")

        self.category=input("请选择语言类型:")

        self.format=input("请选择文件格式(rar or pdf):")


        if 'rar' in self.format:

            self.format='PDF+Code'

        else:

            self.format='PDF'

        print("你选择的下载条件为:页数不大于%s页,文件大小不大于%sMB,文件类型为:%s,文件格式为:%s"%(self.page,self.size,self.category,self.format))

        print("正在连接数据库")

        time.sleep(5)


        try:

            db = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='',
                charset='utf8',
                db='itebooks'
            )

            print("数据库连接成功,进行筛选可下载的URL")

            cursor = db.cursor()

            sql="SELECT book_down_link FROM itebooks.book_info WHERE book_page<=%s AND book_size<=%s AND book_format='%s' AND book_category LIKE '%%%%%s%%%%'"


            sql=sql%(self.page,self.size,self.format,self.category)

            cursor.execute(sql,())

            result=cursor.fetchall()

            print("以下是为你筛选的结果")

            for url in result:

                print(url[0])

                self.user_url.append(url[0])


            print("正在为你自动筛选可供下载的链接")

            for link in result:

                if '.pdf' not in link[0] and '.rar' not in link[0] :

                    self.un_down_url.append(link[0])

                else:

                    self.down_url.append(link[0])

            print("筛选成功,一共有{}条链接可进行下载,{}条不可进行下载".format(len(self.down_url),len(self.un_down_url)))



        except Exception as connect_error:

            print("数据库连接错误:{}".format(connect_error))

        return self.down_url


    def start_download(self):

        download_chooice=input("是否进行下载:")

        if download_chooice=='y':

            print("创建文件夹")

            try:

                os.mkdir("DownloadPDF")

            except Exception as exist:

                print("文件夹存在:%s"%exist)

            for url in self.down_url:

                try:

                    response = requests.get(url, stream=True)

                    print("正在下载文件:")

                    filename = re.findall('http://file.allitebooks.com/.*?/(.*?).pdf', url, re.S)[0].replace('%20', ' ')

                    print(filename)

                    with open('DownloadPDF/%s.pdf' % filename, 'wb') as pdf:

                        for chunk in response.iter_content(chunk_size=1024):

                            if chunk:

                                pdf.write(chunk)

                        print("%s.pdf下载成功"%filename)

                except Exception as response_error:

                    print("下载失败:%s"%response_error)

                    with open("downloadfail.txt",'a') as f:

                        f.write(time.strftime("%Y-%m-%d %H:%M:%S  ")+"下载失败的链接:{}  ".format(url)+"原因:{}".format(response_error)+"\n")
        else:

            print("退出下载")


Spider=Download_ITeBooks()

Spider.user_select_url()

Spider.start_download()