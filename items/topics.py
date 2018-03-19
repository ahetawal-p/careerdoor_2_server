from toapi import Item, XPath


class Topics(Item):
    __base_url__ = 'https://www.careercup.com/categories'

    qUrl = XPath('//a/@href')
    topicName = XPath('//a/text()')
    qCount = XPath('translate(normalize-space(//text()[2]), "()", "")')

    class Meta:
        source = XPath("//div[@id='mainpagebody']"
                       "//div[@class='box'][2]"
                       "//div[@class='boxBody']"
                       "//div[not(@class='clearance')]")
        route = {'/topics': ''}

    def clean_qUrl(self, qUrl):
        pidLocationIdx = qUrl.find("pid=")
        endpoint = qUrl[pidLocationIdx+4:]
        return endpoint
