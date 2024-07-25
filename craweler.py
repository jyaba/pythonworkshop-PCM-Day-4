import json
import os
import re
import logging
import time
import random
import datetime
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

import requests
from parsel import Selector


MAX_RETRY = 5
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d')
logging.getLogger("requests").setLevel(logging.DEBUG)



class MillerDECrawler:
    def __init__(self):
        self.start_process()
    


    def start_process(self):
        response = requests.get('https://www.meiller.com/de/karriere/stellenangebote/#tabber-215611')
        page = Selector(response.text)
        page_links = list(set(page.xpath('//table/tbody/tr/td/a/@href').extract()))
        for page_link in page_links:
            url = f'https://www.meiller.com{page_link}'
            response = requests.get(url)
            page = Selector(text=response.text)
            title = page.xpath("//h1").extract_first()
            #TODO Add the afugaben section
            profile = self.get_profile(page)
            task = self.get_task(page)
            benefits = self.get_benefits(page)
            breakpoint()
    
    
    def get_profile(self, page):
        keynames = ['Ihr Profil']
        profile_details = self.get_sections(keynames)
        return profile_details
        

    def get_task(self, task):
        keynames = ['Ihre Aufgaben:']
        task_details = self.get_sections(keynames)
        return task_details

    def get_benefits(self, page):
        keynames = ['Warum wir:']
        benefits_details = self.get_sections(page=page, keynames)
        return benefits_details
    

    def get_sections(self, page, keynames):
        for key_name in keynames:
            section_html = page.xpath(f"//p[strong[contains(text(),'{key_name}')]]/following-sibling::ul[1]/li").extract()
            section_text = page.xpath(f"//p[strong[contains(text(),'{key_name}')]]/following-sibling::ul[1]/li/text()").extract()

            return {
                'html': section_html,
                'text': section_text
            }

    def make_requests(self, url):
        '''Making requests of the request
        '''
        pass

def main():
    pass

if __name__ == '__main__':
    crawler = MillerDECrawler()
    crawler.start_process()
