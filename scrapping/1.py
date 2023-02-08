# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:25:41 2021

@author: win10
"""

from autoscraper import AutoScraper
amazon_url = "https://www.amazon.in/s?k=iphone"

wanted_list = ["₹42,999", "Apple iPhone 11 (64GB) - White"]

scraper = AutoScraper()
result = scraper.build(amazon_url, wanted_list)

print(scraper.get_result_similar(amazon_url, grouped=True))
scraper.set_rule_aliases({'rule_vt3g': 'Price', 'rule_oan7': 'Price'})
scraper.keep_rules((['rule_vt3g', 'rule_oan7']))
scraper.save('amazon-search')

