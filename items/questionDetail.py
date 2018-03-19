from toapi import Item, XPath, Css
from bs4 import BeautifulSoup


class QuestionDetail(Item):
    __base_url__ = 'https://www.careercup.com'

    ansText = Css("div.commentBody", attr='html')
    netVote = XPath("//div[@class='votesNet']/text()")
    totalVote = XPath("//div[@class='votesCount']/span/text()")
    ansDate = XPath("//span[@class='author']/abbr/text()")

    class Meta:
        source = XPath("//div[@id='mainpagebody']"
                       "//div[@class='comment']")
        route = {'/question?id=:id': '/question?id=:id'}
        # route = {'/test': ''}

    def clean_ansText(self, ansText):
        qTextStr = []
        if ansText:
            from lxml.html import tostring
            html = tostring(ansText[0])\
                .replace(b'\r', b'\n')\
                .replace(b'\n\n', b'\n')\
                .replace(b'<br>', b'\n')
            # print(html)
            soup = BeautifulSoup(html, 'html.parser')
            for child in soup.div.contents:
                if child.name:
                    if child.name == 'span' and child['class'][0] == 'author':
                        continue
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
