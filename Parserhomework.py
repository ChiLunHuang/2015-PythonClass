# -*- coding: utf-8 -*-  
import urllib.request, urllib.parse, urllib.error
# 令一變數起始IDFirst
global IDFirst
IDFirst=942599
# 令一變數結束IDLast
global IDLast
IDLast=942700
# 令一變數myURL，為URL
global myURL
myURL="http://udn.com/news/story/6928/"
# 令一變數storage，為儲存位置
global storage

# 令一變數match，跟東吳有關的
global match
match=False

# 使用HTMLParser
import html.parser  
  
# 解析器，繼承自HTMLParser  
class HTMLParserExample(html.parser.HTMLParser):    
    # 用來抓標籤的資料
    def handle_data(self, data):
      

        if ('故宮' in data):
                global match
                match = True
                #print(data+str(match))
                

        

print ("The program is for parser of full movie information")
print ("Copyright  2014 Soochow University, CHI-LUN HUANG. All rights reserved.")    
print ("processing start... ")
print(("Goal:"+str(IDFirst)+" to "+str(IDLast)))

for i in range(IDFirst,IDLast):
  
    print(("up to :"+str(i)))
    storage= "D:\YahooInfo\Data" +str(i)+".txt" 
    url =(myURL+str(i))
    ExampleWeb = urllib.request.urlopen(url)  
    webContent = ExampleWeb.read().decode('utf_8')  
    ExampleWeb.close()

    #try:
        # 開啟檔案在尾端加入東西
    fout = open (storage, "w",encoding=("utf-8"))
    fout.writelines('%s ' % str(i))
    fout.writelines('\n')

    Parser = HTMLParserExample()  

    try:  
        # 將網頁內容拆成一行一行餵給Parser  
        for line in webContent.splitlines():  
            Parser.feed(line)  
    except (html.parser.HTMLParseError, data):  
        print(("# Parser error : " + data.msg  ))

    Parser.close()
    
    if match==True:
        match=False
        fout.writelines('%s ' % url)
        fout.writelines('\n')
        
    fout.close()

print ("processing End... ")
