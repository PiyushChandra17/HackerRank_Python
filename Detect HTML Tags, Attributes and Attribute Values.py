from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr))for attr in attrs]

parser = MyHtmlParser()

parser.feed('\n'.join([input() for _ in range(int(input()))]))

parser.close()
