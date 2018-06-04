# -*- coding: utf-8 -*-

import scrapy


class Spider_itebooks_Item(scrapy.Item):

    book_id=scrapy.Field()

    book_isbn=scrapy.Field()

    book_detail_link=scrapy.Field()

    book_author=scrapy.Field()

    book_name=scrapy.Field()

    book_page=scrapy.Field()

    book_pub_year=scrapy.Field()

    book_language=scrapy.Field()

    book_size=scrapy.Field()

    book_format=scrapy.Field()

    book_category=scrapy.Field()

    book_description=scrapy.Field()

    book_down_link=scrapy.Field()

    book_img_url=scrapy.Field()



