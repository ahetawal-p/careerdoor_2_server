import os
from colorama import Fore
from toapi import Item, XPath, logger
from shutil import rmtree

class DailyCron(Item):
    __base_url__ = 'https://www.google.com'
    qUrl = XPath('input')

    class Meta:
        source = XPath("//form")
        route = {'/cron': ''}

    def clean_qUrl(self, qUrl):
        # print(qUrl)
        # localStorage = os.getcwd() + "/.html"
        # logger.info(Fore.RED, 'CLEANUP', 'Clean up ' + localStorage)
        # rmtree(localStorage)
        return 'clean'
