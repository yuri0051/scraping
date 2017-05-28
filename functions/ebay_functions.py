import sys, time, re
from selenium import webdriver
sys.path.append('/home/john/Scripts/upwork_projects/scraping/functions')
from functions import csv_writer

cat_list = [
#'Audio & Home Entertainment',
#'Automotive',
#'Baby & Mom',
#'Books & Magazines',
#'Cameras & Optics',
#'Charity',
#'Clothing & Accessories',
#'Coins & Notes',
#'Collectibles',
#'eBay Daily',
#'Fitness & Sports',
#'Fragrances, Beauty & Health',
#'Games, Consoles & Accessories',
#'Home & Kitchen Appliances',
#'Home & Living',
#'Jewellery & Precious Coins',
#'Kitchen & Dining',
#'Laptops & Computer Peripherals',
#'LCD, LED & Televisions',
#'Memory Cards, Pen Drives & HDD',
#'Mobile Accessories',
'Mobile Phones',
#'Motor Classifieds',
#'Movies & Music',
#'Musical Instruments',
#'Shoes',
#'Stamps',
#'Stationery & Office Supplies',
#'Tablets & Accessories',
#'Tools , Hardware & Electricals',
#'Toys, Games & School Supplies',
#'Warranty Services',
#'Watches',
#'Wearable Devices',
#'Everything Else'
]

def selenium_spider(url):
    #driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
    driver.get(url)
    return driver

def scraping_categories(url):
    
    driver = selenium_spider(url)
    time.sleep(3)
    parsed_cats = []
    li = []
    while True:
        button = driver.find_element_by_xpath('.//td[@class="gh-td"]/input[@type="submit"]')
        cats = driver.find_elements_by_xpath('.//div[@id="gh-cat-box"]/select/option')
        cats = [x for x in cats if x.text not in parsed_cats and x.text in cat_list]
        if len(cats) == 0: break
        cat = cats[0]
        cat_name = cat.text
        parsed_cats.append(cat_name)
        cat.click()
        time.sleep(1)
        button.click()
        #####
        time.sleep(5)
        first_url = driver.current_url
        l = scraping_pages(driver, first_url)
        l.append(cat_name)
        li.append(l)
        #####

    driver.quit()
    return li

def scraping_pages(driver, f_url):
    count = 0
    l = []
    while True:
        if count == 1: break
        l.append(f_url)
        #items = driver.find_elements_by_xpath('.//ul[@id="ListViewInner"]/li')
        next_page = driver.find_element_by_xpath('.//td[@class="pagn-next"]')
        #current_page = driver.find_element_by_xpath('.//td[@class="pages"]/a[@class="pg curr"]').text
        #print len(items)
        next_page.click()
        time.sleep(5)
        l.append(driver.current_url)
        count += 1

    return l

def main():
    url = 'http://www.ebay.in'
    l = scraping_categories(url)
    return l

#######################################################################################

def ebay_item_parser(response, fh, category):
    def price(response):
        try:
            price = response.xpath('.//span[@itemprop="price"]/text()').extract()[0].split(' ')[1]
            offer_price = price
            discount = ''
        except:
            try:
                price = response.xpath('.//span[@id="mm-saleOrgPrc"]/text()').extract()[0].split(' ')[1]
                offer_price = response.xpath('.//span[contains(text(), "Discounted price")]/\
                    following-sibling::span/text()').extract()[0].split(' ')[1]
                discount = response.xpath('.//div[@id="mm-saleAmtSavedPrc"]/text()').extract()[0].strip()
                discount = re.findall(r'([0-9]+%)', discount)[0]
            except:
                price = '### ERROR ###'
                offer_price = '### ERROR ###'
                discount = '### ERROR ###'
        return price, offer_price, discount

    def brand(response):
        try:
            brand = response.xpath('.//td[@class="attrLabels"][contains(text(), "Brand:")]/following-sibling\
                ::td/span/text()').extract()[0]
        except:
            brand = ''
        return brand

    def features_func(response):
        d = {}
        features = response.xpath('.//h2[contains(text(), "Item specifics")]/following-sibling::table/tr')
        d['Condition'] = features[0].xpath('./td/div/text()').extract()[0].strip().strip(':')
        try:
            d['Brand'] = features[0].xpath('./td/span/text()').extract()[0].strip()
        except:
            d['Brand'] = ''
        for feature in features[1:]:
            try:
                d[feature.xpath('./td/text()').extract()[0].strip().strip(':')] = feature.xpath('./td/span/text()')\
                    .extract()[0]
                d[feature.xpath('./td/text()').extract()[2].strip().strip(':')] = feature.xpath('./td/span/text()')\
                    .extract()[1]
            except:
                d[feature.xpath('./td/text()').extract()[0].strip().strip(':')] = feature.xpath('./td/span/text()')\
                    .extract()[0]
        return d

    def ref_number(response):
        ref_number = response.xpath('.//div[@id="descItemNumber"]/text()').extract()[0].strip()
        return ref_number

    def shipping(response):
        shipping = response.xpath('.//span[@id="shSummary"]/span/span/text()').extract()
        if 'FREE' in shipping:
            shipping = 1
        else:
            shipping = 0
        return shipping

    def color_func(features):
        try:
            color = features['Colour']
        except:
            color = ''
        return color

    def descr(features):
        s = ''
        for x, y in features.items():
            s += x + ': ' + y + ', '
        s = s.strip().strip(',') + '.'
        return s

    pr, of_pr, disc = price(response)

    id = ''
    name = response.xpath('.//h1[@id="itemTitle"]/text()').extract()[0]
    permalink = '' 
    create_date = ''
    mrp = ''
    price = pr
    offer_price = of_pr
    discount = disc
    store_id = ''
    category_id = category 
    data_source = 'ebay.in'
    ref_id = ref_number(response)
    url = response.url
    #print url, '####################################################'
    deal_notes = ''
    meta_title = name
    meta_key = ''
    meta_des = name
    size = ''
    size_unit = ''
    features = features_func(response)
    description = descr(features)
    key_features = ''
    color = color_func(features)
    brand = features['Brand']
    specifications = ''
    offers = ''
    in_stock = ''
    free_shipping = shipping(response)
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


