from com_functions import mongo_writer, csv_writer
from datetime import datetime
import traceback, sys

def item_parsing(item, fh, coll, fhl):
    def prices_func(item):
        try:
            price = item['productBaseInfoV1']['flipkartSellingPrice']['amount']
            offer_price = item['productBaseInfoV1']['flipkartSpecialPrice']['amount']
        except:
            price = item['productBaseInfoV1']['maximumRetailPrice']['amount']
            offer_price = item['productBaseInfoV1']['maximumRetailPrice']['amount']
        return price, offer_price

    def offers_func(item):
        try:
            offers = ', '.join(item['productBaseInfoV1']['offers']).strip(',')+'.'
        except:
            offers = ''
        return offers
    
    def shipping_func(item):
        try:
            shipping = item['productShippingInfoV1']['shippingCharges']['amount']
        except:
            shipping = ''
        return shipping

    try:
        price, offer_price = prices_func(item)
        d = {}
        d['id'] = ''
        d['name'] = item['productBaseInfoV1']['title']
        d['permalink'] = '' 
        d['create_date'] = ''
        d['mrp'] = ''
        d['price'] = price
        d['offer_price'] = offer_price 
        d['discount'] = item['productBaseInfoV1']['discountPercentage']
        d['store_id'] = ''
        d['category_id'] = item['productBaseInfoV1']['categoryPath'] 
        d['data_source'] = 'flipkart.com'
        d['ref_id'] = item['productBaseInfoV1']['productId']
        d['url'] = item['productBaseInfoV1']['productUrl']
        d['image_url'] = ''#item[]
        d['description'] = item['productBaseInfoV1']['productDescription']
        d['deal_notes'] = ''
        d['meta_title'] = d['name']
        d['meta_key'] = ''
        d['meta_des'] = ''
        d['brand'] = item['productBaseInfoV1']['productBrand']
        d['size'] = item['productBaseInfoV1']['attributes']['size']
        d['size_unit'] = item['productBaseInfoV1']['attributes']['sizeUnit']
        d['key_features'] = ', '.join(item['categorySpecificInfoV1']['keySpecs']).strip(',')+'.'
        d['features'] = item['categorySpecificInfoV1']['specificationList']
        d['color'] = item['productBaseInfoV1']['attributes']['color']
        d['specifications'] = item['categorySpecificInfoV1']['specificationList']
        d['offers'] = offers_func(item)
        d['in_stock'] = item['productBaseInfoV1']['inStock']
        d['free_shipping'] = ''
        d['shippingCharge'] = shipping_func(item)
        d['mm_average_rating'] = ''
        d['is_deal'] = ''
        d['is_coupon'] = ''
        d['start_date'] = ''
        d['end_date'] = ''
        d['coupon_code'] = ''
        d['special_deal'] = ''
        d['upcoming_deal'] = ''
        d['show_as_banner'] = ''
        d['local_store_deal'] = ''
        d['localstore_deal_enabled'] = ''
        d['featured'] = ''
        d['enabled'] = ''
        d['no_cashback'] = ''
        d['base_product'] = ''
        d['match_set'] = ''
        d['match_attempt'] = ''
        d['store_count'] = ''
        d['display_order'] = ''
        d['last_update'] = ''
        d['deleted'] = ''
        d['_id'] = {'item_url': d['url'], 'date': str(datetime.now().date())}
        mongo_writer(coll, d)
        csv_writer(fh, d['id'],d['name'],d['permalink'],d['create_date'],d['mrp'],d['price'],d['offer_price'],d['discount'],\
               d['store_id'],d['category_id'],d['data_source'],d['ref_id'],d['url'],d['image_url'],d['description'],d['deal_notes'],\
               d['meta_title'],d['meta_key'],d['meta_des'],d['brand'],d['size'],d['size_unit'],d['color'],d['key_features'],\
               d['features'],d['specifications'],d['offers'],d['in_stock'],d['free_shipping'],d['shippingCharge'],\
               d['mm_average_rating'],d['is_deal'],d['is_coupon'],d['start_date'],d['end_date'],d['coupon_code'],\
               d['special_deal'],d['upcoming_deal'],d['show_as_banner'],d['local_store_deal'],d['localstore_deal_enabled'],\
               d['featured'],d['enabled'],d['no_cashback'],d['base_product'],d['match_set'],d['match_attempt'],d['store_count'],\
               d['display_order'],d['last_update'],d['deleted'])

    except:
        traceback.print_exc(file=fhl)
        fhl.write('#'*50+'\n')
        traceback.print_exc(file=sys.stdout)
        
