# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 18:31:33 2022

@author: SaadMuzammil
"""

import scrapy

class FirstSpider(scrapy.Spider):    # use FirstSpider in scrapping data using terminal instead of file name which is Firstspider
    name = "FirstSpider"
    def start_requests(self):
        urls = [
                "http://quotes.toscrape.com/page/1/",
                "http://quotes.toscrape.com/page/1/",
                "http://demo.3gensoft.com/logbook/index.php/auth/login",
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = "quotes-%s.html" % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log("Saved file %s" % filename)