#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
from PIL import Image
import base64
import cStringIO
import PIL.Image
# 打开数据库连接
db = MySQLdb.connect("mysql.cc.puv.fi","e1600553","rjg7bjYbWbMy","e1600553_Project" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT image FROM `en` WHERE number=4969"

try:
   # 执行SQL语句
   print "1"
   db.commit()
   cursor.execute(sql)
   print "2"
   # 获取所有记录列表
   numrows = int(cursor.rowcount)
   print "3"
   for i in range(numrows):
       cursor.execute(sql)
       data = cursor.fetchall()
       # print type(data[0][0])
       data1 = base64.b64decode(data[0][0])
       file_like = cStringIO.StringIO(data[0][0])
       img = PIL.Image.open(file_like)
       img.show()
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()