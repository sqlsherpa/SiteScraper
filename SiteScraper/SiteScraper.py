from lxml import html
import pandas as pd
import requests
import datetime

# Declare a final output object
# Define the pages to scrape
# Iterate over the pages
# getDataList()
# addToFinalOutput()
# return result

date = datetime.datetime.now().strftime("%Y-%y-%d %H%M%S")
fileName = 'pythonout'
suffix = '.xlsx'
path = 'F:\\Users\\Owner\\Desktop\\Ems Work\\'
outPath = path + fileName + date + suffix
writer = pd.ExcelWriter(outPath, engine='xlsxwriter')


def getDataList(myPage):
    page = requests.get(myPage)
    tree = html.fromstring(page.content)

    # color = tree.xpath('//div[@class="image box"]//a/@href')
    # color = tree.xpath('//div[@class="image box"]/following-sibling::text()')
    color = tree.xpath('//div[@id="product_thumb"]/a/following-sibling::text()')  # closest I could get

    # replace the junk
    colorclean = [w.replace('\n', '') for w in color]
    colorclean2 = [w.replace('\t', '') for w in colorclean]
    # remove blanks
    filteredcolors = list(filter(None, colorclean2))  # have to convert back into list from the filter

    return filteredcolors


def addToFinalOutput(fList, myList):
    finalList = fList + myList
    return finalList


pageList = ['http://www.chinaglaze.com/China-Glaze/index.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_1.html']
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_2.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_3.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_4.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_5.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_6.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_7.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_8.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_9.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_10.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_11.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_12.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_13.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_14.html'
# ,'http://www.chinaglaze.com/China-Glaze/pageNum_15.html'
# ]

finalList = []
iterationList = []

# Iterate over the pages
for x in pageList:
    iterationList = getDataList(x)
    finalList = addToFinalOutput(finalList, iterationList)

    continue

print(finalList)

# convert list to pandas dataframe
df = pd.DataFrame({'col': finalList})
df.to_excel(writer, 'Sheet1')

writer.save()
