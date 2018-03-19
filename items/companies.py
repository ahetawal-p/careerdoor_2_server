from toapi import Item, XPath


class Companies(Item):
    __base_url__ = 'https://www.careercup.com/categories'

    qUrl = XPath('//a/@href')
    qLogo = XPath('//a/@href')
    companyName = XPath('//a/text()')
    qCount = XPath('translate(normalize-space(//text()[2]), "()", "")')

    class Meta:
        source = XPath("//div[@id='mainpagebody']"
                       "//div[@class='box'][1]"
                       "//div[@class='boxBody']"
                       "//div[not(@class='clearance')]")
        route = {'/companies': ''}

    def clean_qUrl(self, qUrl):
        pidLocationIdx = qUrl.find("pid=")
        endpoint = qUrl[pidLocationIdx+4:]
        return endpoint

    def clean_qLogo(self, qLogo):
        pidLocationIdx = qLogo.find("pid=")
        logoURI = qLogo[pidLocationIdx+4:] + ".png"
        return 'https://www.careercup.com/attributeimages/%s' % logoURI
