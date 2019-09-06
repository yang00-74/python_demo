#coding=utf-8

import urllib
import json #simplejson
from bs4 import BeautifulSoup

def get_content_from_keyword(keyword='鞋子',page=1):
    """
    根据页数和keywords采集内容
    """

    params = {'keyword':keyword,'page':page,'area':1,'enc':'utf-8'}
    data = urllib.urlencode(params)
    opener =  urllib.urlopen('https://search.jd.com/Search?'+ data)
    response = opener.read()
    opener.close()
    return response


def get_price_from_ids(*ids):
    '''
    [123,42,5,678,9123123]
    https://p.3.cn/prices/mgets?callback=jQuery2495381
    &type=1&area=1_72_2799_0
    &skuIds=J_11801816314%2CJ_27669502843%2CJ_6799637%2CJ_366783%2CJ_27857353950%2CJ_
    3538187%2CJ_13542096645%2CJ_28107443131%2CJ_10931189474%2CJ_27528515156%2CJ_
    12101502951%2CJ_11396098697%2CJ_27528638686%2CJ_25617396844%2CJ_13047144982%2CJ_
    21990821714&pdbp=0&pdtk=&pdpin=&pduid=1522075425247497983644&source=search_pc
    &_=1528101293565
    根据id采集到价格
    '''
    st = ''.join(['J_%s%s'%(id,'%2C') for id in ids])
    # print st
    params = 'skuIds=%s&type=1'%st
    opener = urllib.urlopen('http://p.3.cn/prices/mgets?'+params)
    response = opener.read()
    opener.close()
    return json.loads(response)


if __name__ == "__main__":

    '''
    分析数据，生成干净的数据 res
    '''

    content = get_content_from_keyword(keyword="鞋子",page=4)
    soup = BeautifulSoup(content,"lxml")
    mids = soup.find_all(attrs={"data-sku":True})
    ids = [mid['data-sku'] for mid in mids]
    prices = get_price_from_ids(*ids)

    res = []
    for id in mids:
        data = {}
        data['id'] = id['data-sku']
        data['img'] = id.find(class_='p-img').find('a')
        aobj = id.find(class_='p-name').find('a')
        data['url'] = aobj['href']
        data['title'] = aobj.text.strip()
        data['price'] = filter(lambda price:price['id'] == 'J_%s'%data['id'] ,prices)[0]['p']
        res.append(data)

    print res
