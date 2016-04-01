# -*- coding: utf-8 -*-  
import urllib.request, urllib.parse, urllib.error
# 令一變數起始IDFirst
global IDFirst
IDFirst=10
# 令一變數myURL，為URL
global myURL
myURL="http://www.imdb.com/title/tt1431045/reviews?start="
# 令一變數storage，為儲存位置
global storage
# 使用HTMLParser
import html.parser  

  
# 解析器，繼承自HTMLParser  
class HTMLParserExample(html.parser.HTMLParser):    
    # 用來抓標籤的資料
    def handle_data(self, data):
      

        fout.writelines('%s ' % data+'@@')
        fout.writelines('\n')

print ("The program is for parser full information")
print ("Copyright  2014 Soochow University, CHI-LUN HUANG. All rights reserved.")    
print ("processing start... ")
print ("Goal:"+str(IDFirst))

storage= "D:\\Data" +str(IDFirst)+".txt" 
url =(myURL+str(IDFirst))
ExampleWeb = urllib.request.urlopen(url)  
webContent = ExampleWeb.read().decode('utf_8')  
ExampleWeb.close()

#try:
    # 開啟檔案在尾端加入東西
fout = open (storage, "w",encoding=("utf-8"))
fout.writelines('%s ' % str(IDFirst))
fout.writelines('\n')

Parser = HTMLParserExample()  

try:  
    # 將網頁內容拆成一行一行餵給Parser  
    for line in webContent.splitlines():  
        Parser.feed(line)  
except (html.parser.HTMLParseError, data):  
    print(("# Parser error : " + data.msg  ))

Parser.close()
fout.close()

print ("processing End... ")
