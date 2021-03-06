Amazon Product Advertising API 5.0 wrapper for Python
=======================================================
A simple Python wrapper for the last version of the Amazon Product Advertising API. This module allows to get product information from Amazon using the official API in an easier way.
Like Bottlenose you can use cache reader and writer to limit the number of api calls.
<!-- 
[![PyPI](https://img.shields.io/pypi/v/amazon-paapi5)](https://pypi.org/project/amazon-paapi5/)
[![Python](https://img.shields.io/github/pipenv/locked/python-version/alefiori82/amazon-paapi5/master?label=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPL--3.0-%23e83633)](https://github.com/alefiori82/amazon-paapi5/blob/master/LICENSE)
[![Support](https://img.shields.io/badge/Support-Good-brightgreen)](https://github.com/alefiori82/amazon-paapi5/issues)
[![Amazon API](https://img.shields.io/badge/Amazon%20API-5.0-%23FD9B15)](https://webservices.amazon.com/paapi5/documentation/)
![](https://github.com/alefiori82/amazon-paapi5/workflows/Upload%20Python%20Package/badge.svg)
![](https://github.com/alefiori82/amazon-paapi5/workflows/Build%20package/badge.svg)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/amazon-paapi5)
[![Documentation Status](https://readthedocs.org/projects/amazon-paapi5/badge/?version=latest)](https://amazon-paapi5.readthedocs.io/en/latest/?badge=latest) -->


Usage guide
-----------

Search items::

    from amazon.paapi import AmazonAPI
    amazon = AmazonAPI(KEY, SECRET, TAG, COUNTRY)
    results = amazon.search_items(keywords='harry potter')
    print(results['data']['count]) # total counts
    pr
    print(product['data'][1].prices.price)

Get multiple products information::

    from amazon.paapi import AmazonAPI
    amazon = AmazonAPI(KEY, SECRET, TAG, COUNTRY)
    products = amazon.get_items(item_ids=['B01N5IB20Q','B01F9G43WU'])
    print(products['data']['B01N5IB20Q'].image_large)
    print(products['data']['B01F9G43WU'].prices.price)


Get variations::

    from amazon.paapi import AmazonAPI
    amazon = AmazonAPI(KEY, SECRET, TAG, COUNTRY)
    products = amazon.get_variations(asin=['B01N5IB20Q','B01F9G43WU'])

Get browse nodes::

    from amazon.paapi import AmazonAPI
    amazon = AmazonAPI(KEY, SECRET, TAG, COUNTRY)
    browseNodes = amazon.get_browse_nodes(browse_node_ids=['473535031'])

Use cache reader and writer::

    from amazon.paapi import AmazonAPI

    DATA = []
    
    def custom_save_function(url, data, http_info):  
        DATA.append({'url':url, 'data': data, 'http_info':http_info}) 
    
    def custom_retrieval_function(url):  
        for item in DATA:  
            if item["url"] == url: 
                return {'data':item['data'], 'http_info': item['http_info']}  
        return None
    
    amazon = AmazonAPI(KEY, SECRET, TAG, COUNTRY, CacheReader=custom_retrieval_function, CacheWriter=custom_save_function) 
    products = amazon.search_items(keywords='harry potter')

Based on fork of https://github.com/alefiori82/amazon-paapi5