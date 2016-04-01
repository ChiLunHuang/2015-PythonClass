
import pypyodbc as pyodbc
#C:\Python34\>python.exe -m pip install pypyodbc



conn = pyodbc.connect('DRIVER={SQL Server};SERVER=yourip;DATABASE=Software;UID=test;PWD=123')
cursor = conn.cursor()
print("----------連結資料庫成功----------")


print("----------原本資料----------")
cursor.execute("select * from StudentInfo ")
rows = cursor.fetchall()
for row in rows:
    print (row)

cursor.execute ("DELETE StudentInfo  WHERE SID='%s' " % (99156222))
conn.commit()


print("----------修改資料後結果----------")
cursor.execute("select * from StudentInfo")
rows = cursor.fetchall()
for row in rows:
    print (row)


conn.close()
