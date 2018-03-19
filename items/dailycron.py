import os
from colorama import Fore
from toapi import Item, XPath, logger
from shutil import rmtree

class DailyCron(Item):
    __base_url__ = 'https://www.careercup.com/categories'
    qUrl = XPath('div[@id="mainpagebody"]')

    class Meta:
        source = XPath("//div[@id='main']")
        route = {'/cron': ''}

    def clean_qUrl(self, qUrl):
        localStorage = os.getcwd() + "/.html"
        logger.info(Fore.RED, 'CLEANUP', 'Clean up ' + localStorage)
        rmtree(localStorage)
        return 'clean'
