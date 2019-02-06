

from lxml import html
import requests

linkpage = requests.get('http://www.ibdbeauty.com/Products/Just-Gel-Polish/Polish/index.html')
imgpage = requests.get('http://www.ibdbeauty.com/Products/Just-Gel-Polish/Polish/product_351.html')

linktree = html.fromstring(linkpage.content)
imgtree = html.fromstring(imgpage.content)


link = linktree.xpath('//div[@id="product_thumb"]/a/@href')

imgdesc = imgtree.xpath('//b/following-sibling::text() | //div[contains(@class,"lash")]/img/@src | (//div[contains(@class,"textarea")]/text())[1]')



#replace the junk
imgdescclean = [w.replace('\n','') for w in imgdesc]
imgdescclean2 = [w.replace('\t','') for w in imgdescclean]
#remove blanks
filteredimgdesc = list(filter(None,imgdescclean2)) #have to convert back into list from the filter

print('Link: ', link)
print('Image: ', filteredimgdesc)