

# -*- coding: utf-8 -*-
import scrapy

#see comment in spider 6a 
class Nairabotpg1Spider(scrapy.Spider):
    name = 'nairabot_thread6b' 
    #allowed_domains = ['www.nairaland.com/1279130/canadian-federal-skilled-worker-program-timelines']
    allowed_domains = ['www.nairaland.com/']
    #start_urls = ['https://www.nairaland.com/1279130/canadian-federal-skilled-worker-program-timelines/']
    #page0 = 'https://www.nairaland.com/4843199/canadian-express-entry-federal-skilled/' #first page, the url carries no page number
    #list of pages'urls
    start_urls = ['https://www.nairaland.com/4843199/canadian-express-entry-federal-skilled/{page_num}'.format(page_num=page_num)
                  for page_num in range(280, 511)]

    def parse(self, response):
        #extracting the comment posts and creat a library with it
        scraped_comment = response.css(".narrow , .pd::text").extract()
        #time of posting comments
        time = response.css(".pu b:nth-child(1)::text").extract()
        #date of posting comments
        date = response.css(".pu b:nth-child(2)::text").extract()
        #year of posting comments
        year = response.css(".pu b:nth-child(3)::text").extract() 
        #poster's moniker
        poster = response.css(".user::text").extract() # i cant use thus bit as there post with no user tags.

        #create a dictionary to store the scraped info
        for item in zip(scraped_comment, time, date):

        	yield {
                'scraped_comment' : item[0],
                'time' : item[1],
                'date' : item[2],
                }

















	    







