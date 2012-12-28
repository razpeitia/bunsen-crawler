from lxml import etree

url = "http://www.heroeslocales.com/bunsen/comics/"

parser = etree.HTMLParser()
tree = etree.parse(url, parser)

links = [url + i for i in tree.xpath('//a[starts-with(@href, "20")]/@href')]

with open("bunsen.txt", "wb") as f:
    for link in links:
        f.write(link)
        f.write("\n")
