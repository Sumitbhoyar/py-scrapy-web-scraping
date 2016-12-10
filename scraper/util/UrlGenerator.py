import httplib
import urllib

url="https://www.compareraja.in/filter/controlls/commonfinderext.aspx?page=%s&&Price=&Brand=&UserRatings=&DoorType=&Capacity=&StarRating=&FreezerType=&RefrigeratorType=&minPrice=5000&maxPrice=260000&sort=Popularity&categoryId=10&CategoryNameInURLs=refrigerators&p_csv_Filter_01_Ids=&p_csv_Filter_02_Ids=&p_csv_Filter_03_Ids=&p_csv_Filter_04_Ids=&p_csv_Filter_05_Ids=&p_csv_Filter_06_Ids=&p_csv_Filter_07_Ids=&p_csv_Filter_08_Ids=&catid=10&catname=refrigerators&searchparam="
isAvailable = 1;
counter=1

while isAvailable == 1:
    newUrl=url % (str(counter))
    responseCode = urllib.urlopen(newUrl).getcode()
    if responseCode == 200:
        print "'"+newUrl+"',\n"
        counter= counter+1
    else:
        isAvailable=0
