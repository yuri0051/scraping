import sys, time
sys.path.append('/home/john/Scripts/upwork_projects/scraping/functions')
from functions import csv_writer 
from selenium import webdriver
from functions import selenium_spider

def cats_parsing(driver):
    pass

def main():
    url = 'https://www.snapdeal.com'
    driver = selenium_spider(url)
    time.sleep(20)
    driver.quit()

def snapdeal_item_parser(response, fh):
    def prices(response):
        try:
            price = response.xpath('.//div[contains(@class, "pdpCutPrice")]/text()').extract()[0].strip()
            offer_price = response.xpath('.//span[@class="pdp-final-price"]/span/text()').extract()[0].strip()
            discount = response.xpath('.//span[contains(@class, "pdpDiscount")]/span/text()').extract()[0].strip() + '%'
        except:
            try:
                price = response.xpath('.//span[@itemprop="price"]/text()').extract()[0].strip()
                offer_price = price
                discount = ''
            except:
                price = ''
                offer_price = ''
                discount = ''
        return price, offer_price, discount

    def description_func(response):
        x = response.xpath('.//div[@class="tab-container"]/div/div[contains(@class, "spec-section expanded")]')

        specs = x[1].xpath('./div')[1].xpath('./div/table/tr')
        meta_specifications = {}
        specifications = ''
        for spec in specs:
            for sp in spec.xpath('./td/table/tr'):
                sp = sp.xpath('./td')
                if len(sp) < 2: continue
                xx = sp.xpath('./text()').extract()[0].strip()
                yy = sp.xpath('./text()').extract()[1].strip()
                meta_specifications[xx] = yy 
                specifications += xx +': ' + yy + ', '
        specifications = specifications.strip().strip(',') + '.'

        descr_h = x[2].xpath('./div')[1].xpath('./div/div/p/strong/text()').extract()
        descr_b = x[2].xpath('./div')[1].xpath('./div/div/p/text()').extract()
        descr_b = [d.strip() for d in descr_b if len(d.strip()) != 0]
        descr = ' '.join(descr_b)

        highlights = x[0].xpath('./div')[1].xpath('./ul/li/span/text()').extract()
        highlights = ', '.join(highlights) + '.'
        return descr, specifications, meta_specifications, highlights 

    def color_func(meta_specs):
        try:
            color = meta_specs['Colour']
        except:
            color = ''
        return color

    def brand_func(meta_specs):
        try:
            brand = meta_specs['Brand']
        except:
            brand = ''
        return brand

    def group_func(response):
        try:
            group = response.xpath('.//div[@id="breadCrumbWrapper2"]/div/a/span/text()').extract()
            group = ', '.join(group)
        except:
            group = ''
        return group

    def offer_func(response):
        try:
            offer = response.xpath('.//div[contains(@class, "offer-content")]/div/div/text()').extract()
            offer = [o.strip() for o in offer if len(o.strip())!= 0]
            offer = ', '.join(offer) + '.'
        except:
            offer = ''
        return offer

    def instock_func(response):
        try: 
            response.xpath('.//div[@class="sold-out-err"]/text()')[0]
            in_stock = 0
        except:
            in_stock =1
        return in_stock

    price, offer_price, discount = prices(response)
    descr, specs, meta_specs, highlights = description_func(response)

    id = ''
    name = response.xpath('.//h1[@itemprop="name"]/text()').extract()[0].strip()
    permalink = '' 
    create_date = ''
    mrp = ''
    price = price
    offer_price = offer_price
    discount = discount
    store_id = ''
    category_id = group_func(response)
    data_source = 'snapdeal.com'
    ref_id = ''
    url = response.url
    deal_notes = ''
    meta_title = name
    meta_key = ''
    meta_des = meta_specs
    size = ''
    size_unit = ''
    features = highlights
    description = descr
    key_features = highlights
    color = color_func(meta_specs)
    brand = brand_func(meta_specs)
    specifications = specs
    offers = offer_func(response)
    in_stock = instock_func(response)
    free_shipping = 0
    shippingCharge = ''
    mm_average_rating = ''
    is_deal = ''
    is_coupon = ''
    start_date = ''
    end_date = ''
    coupon_code = ''
    special_deal = ''
    upcoming_deal = ''
    show_as_banner = ''
    local_store_deal = ''
    localstore_deal_enabled = ''
    featured = ''
    enabled = ''
    no_cashback = ''
    base_product = ''
    match_set = ''
    match_attempt = ''
    store_count = ''
    display_order = ''
    last_update = ''
    deleted = ''
    csv_writer(fh, id,name,permalink,create_date,mrp,price,offer_price,discount,store_id,category_id,\
               data_source,ref_id,url,description,deal_notes,meta_title,meta_key,meta_des,brand,\
               size,size_unit,color,key_features,features,specifications,offers,in_stock,free_shipping,\
               shippingCharge,mm_average_rating,is_deal,is_coupon,start_date,end_date,coupon_code,\
               special_deal,upcoming_deal,show_as_banner,local_store_deal,localstore_deal_enabled,\
               featured,enabled,no_cashback,base_product,match_set,match_attempt,store_count,\
               display_order,last_update,deleted)