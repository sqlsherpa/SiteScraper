
from lxml import html
import requests

page = requests.get('http://www.chinaglaze.com/China-Glaze/product_2.html')
tree = html.fromstring(page.content)

#color = tree.xpath('//div[@class="image box"]//a/@href')
#color = tree.xpath('//div[@class="image box"]/following-sibling::text()')
#color = tree.xpath('//div[@id="product_thumb"]/a/following-sibling::text()') #closest I could get
color = tree.xpath('//div[@id="detail_sku"]/text() | //div[@id="detail_dot"]/img/@src')
#color = tree.xpath('//div[@id="detail_dot"]/img/@src')


#replace the junk
colorclean = [w.replace('\n','') for w in color]
colorclean2 = [w.replace('\t','') for w in colorclean]
#remove blanks
filteredcolors = list(filter(None,colorclean2)) #have to convert back into list from the filter

print('Colors: ', filteredcolors)