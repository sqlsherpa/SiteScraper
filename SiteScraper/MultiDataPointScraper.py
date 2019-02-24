from lxml import html
import pandas as pd
import requests
import datetime
import timeit
import os
import math

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


def clear():
    os.system('cls')


def getLinkList(myPage):
    page = requests.get(myPage)
    tree = html.fromstring(page.content)

    # color = tree.xpath('//div[@class="image box"]//a/@href')
    # color = tree.xpath('//div[@class="image box"]/following-sibling::text()')
    # color = tree.xpath('//div[@id="product_thumb"]/a/following-sibling::text()') #closest I could get
    link = tree.xpath('//div[@id="product_thumb"]/a/@href')

    # replace the junk
    linkclean = [w.replace('\n', '') for w in link]
    linkclean2 = [w.replace('\t', '') for w in linkclean]
    # remove blanks
    filteredlinks = list(filter(None, linkclean2))  # have to convert back into list from the filter

    # this is called a list comprehension
    appendedLinkList = ["http://www.chinaglaze.com" + s for s in filteredlinks]

    return appendedLinkList


def addToLinkListOutput(lList, myList):
    linkList = lList + myList
    return linkList


def getDetailSku(myPage):
    page = requests.get(myPage)
    tree = html.fromstring(page.content)

    color = tree.xpath('//div[@id="detail_sku"]/text() | //div[@id="detail_dot"]/img/@src')

    # replace the junk
    colorclean = [w.replace('\n', '') for w in color]
    colorclean2 = [w.replace('\t', '') for w in colorclean]
    # remove blanks
    filteredColors = list(filter(None, colorclean2))  # have to convert back into list from the filter

    return filteredColors


pageList = ['http://www.chinaglaze.com/China-Glaze/index.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_1.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_2.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_3.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_4.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_5.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_6.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_7.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_8.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_9.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_10.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_11.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_12.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_13.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_14.html'
    , 'http://www.chinaglaze.com/China-Glaze/pageNum_15.html'
            ]

linkIterationList = []
skuIterationList = []

nameSkuList = []
linkList = []

# Iterate over the pages
for x in pageList:
    linkIterationList = getLinkList(x)
    linkList = addToLinkListOutput(linkList, linkIterationList)

# print(linkList)
# print(finalList[0])
start = timeit.default_timer()
count = 0

# now visit each of these links and pull the detail sku
for x in linkList:

    skuIterationList = getDetailSku(x)
    nameSkuList.append(skuIterationList)
    count += 1
    stop = timeit.default_timer()

    if (count / len(linkList) * 100) < 5:
        expected_time = "Calculating..."

    else:
        time_perc = timeit.default_timer()
        expected_time = ((time_perc - start) / (count / len(linkList))) / 60

    clear()
    print("Item:", count, " of ", len(linkList))
    cpro = str(round(count / len(linkList) * 100))
    crt = str(round(((stop - start) / 60), 2))
    if expected_time == 'Calculating...':
        ert = expected_time
    else:
        ert = round(float(expected_time))

    print("Current progress:", cpro, "%")
    print("Current run time:", crt, "minutes")
    print("Expected Run Time", ert, "minutes")

# print(nameSkuList)


# convert list to pandas dataframe single dimension
# df = pd.DataFrame({'col':nameSkuList})

# convert list to pandas dataframe multi dimension
df = pd.DataFrame(nameSkuList, columns=['ColorImgLink', 'Name', 'SKU'])

# create dot column ( I could write a one liner for this whole thing but it is nice to be able to have the raw data in the columns to work with)
dfc = df.assign(
    ImageLinker="http://chinaglaze.com" + df.ColorImgLink + "," + "http://chinaglaze.com" + df.ColorImgLink.str.replace(
        'dots', 'bottle') + ",,,,,,")
# dfd = df.assign(DotsColumn = "http://chinaglaze.com" + df.ColorImgLink)
##create bottle column
# dfdb = dfd.assign(BottleColumn = "http://chinaglaze.com" + df.ColorImgLink)
##replace dots with bottle
# dfdb = dfdb['BottleColumn'].str.replace('dots','bottle')

##put it all together


dfc.to_excel(writer, 'Sheet1')

writer.save()
