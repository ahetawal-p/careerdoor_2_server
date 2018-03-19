from toapi import Item, XPath, Css
from bs4 import BeautifulSoup


class Questions(Item):
    __base_url__ = 'https://www.careercup.com'

    qText = Css("span.entry", attr='html')
    qId = XPath("//span[@class='entry']/a/@href")
    ansCount = XPath("//span[@class='rating']/a/span/text()")
    qDate = XPath("//span[@class='author']/abbr/text()")
    qLocation = XPath("normalize-space(//span[@class='author']/text()[3])")
    qTags = XPath("//span[@class='tags']/a/text()")

    class Meta:
        source = XPath("//ul[@id='question_preview']"
                       "//li[@class='question']")
        route = {'/questions?pid=:url&page=:page':
                 '/page?pid=:url&n=:page'
                 }

    def clean_qText(self, qText):
        qTextStr = []
        if qText:
            from lxml.html import tostring
            html = tostring(qText[0]).replace(b'\r', b'\n').replace(b'\n\n', b'\n')
            # print(html)
            soup = BeautifulSoup(html, 'html.parser')
            for child in soup.a.contents:
                if child.select('code'):
                    if child.select('code')[0].pre['class']:
                        codeBlock = child.select('code')[0]
                        lang = codeBlock.pre['class'][0]
                        lang = "{{" + lang[9:] + "}}"
                        lang += codeBlock.pre.text
                        qTextStr.append(lang)
                else:
                    qTextStr.append(child.text)
        return qTextStr

    def clean_qTags(self, qTags):
        if isinstance(qTags, list):
            return qTags
        else:
            return [qTags]
