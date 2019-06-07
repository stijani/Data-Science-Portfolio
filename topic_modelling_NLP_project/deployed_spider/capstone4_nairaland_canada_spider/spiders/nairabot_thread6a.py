

# -*- coding: utf-8 -*-
import scrapy

# for thread 6, the spider stoped returning content from page 280 because that was were 2019 started. As 2019 is the current year, year 
#was not stated in the post, hence spider stopped returning output. Solution: I will use two spiders for this thread, the first(6a) will
#return values until the end of 2018, i.e somewhere on page 280. The second(6b) will start from page 280 and will not include year at all in 
#the selection(i will manually enter it as 2019 in the CSV file). It's possible that 2018 ended somewhere in the middle of page 280,
#that will lead to repeating as few posts when merging the csv file which i will ignore (i figured out they were 8 posts based 
#on the 'nones' returned by spider 6a) 
class Nairabotpg1Spider(scrapy.Spider):
    name = 'nairabot_thread6a' 
    #allowed_domains = ['www.nairaland.com/1279130/canadian-federal-skilled-worker-program-timelines']
    allowed_domains = ['www.nairaland.com/']
    #start_urls = ['https://www.nairaland.com/1279130/canadian-federal-skilled-worker-program-timelines/']
    page0 = 'https://www.nairaland.com/4843199/canadian-express-entry-federal-skilled/' #first page, the url carries no page number
    #list of pages'urls
    start_urls = [page0] + ['https://www.nairaland.com/4843199/canadian-express-entry-federal-skilled/{page_num}'.format(page_num=page_num)
                  for page_num in range(1, 281)]

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
        for item in zip(scraped_comment, time, date, year):

        	yield {
                'scraped_comment' : item[0],
                'time' : item[1],
                'date' : item[2],
                'year' : item[3],
                }

















	    








