#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("mysql.cc.puv.fi","e1600553","rjg7bjYbWbMy","e1600553_Project" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM en"

try:
   # 执行SQL语句
   print "1"
   cursor.execute(sql)
   print "2"
   # 获取所有记录列表
   numrows = int(cursor.rowcount)
   print "3"
   for i in range(numrows):
      row = cursor.fetchone()
      # 打印结果
      print row[0],row[1],row[2],row[3]
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()