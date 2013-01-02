#Wrapper File for a simple CDDB will implement user interface allowing:
#adding entries
#removing entries
#querying entries
#<<<<<<< HEAD
import sys
import _mysql
import submit_entry
import db_query
import MySQLdb as msb


musicDB_name=""
musicDB_name_query=""
musicDB=None

menu="What would you like to do? \n"
menu=menu+"1-Add tracks by cd key \n"
menu=menu+"2-Remove Somethign \n"
menu=menu+"3-Search for something \n"
menu=menu+"4-Leave "



musicDB=None
username=None
password=None
musicDB_name="musicdb"

username=raw_input("Please Enter Username: ")
password=raw_input("Please Enter Password: ")


while musicDB==None:
	try:
		musicDB = msb.connect("localhost",username,password, musicDB_name)
	except _mysql.Error,e:
		print "Incorrect login credentials\n"
		sys.exit()

cur=musicDB.cursor()
cur.execute("show databases;")
for (database,) in cur:
	print(database)

cur.execute("use musicdb;")
for (result,) in cur:
	print(result)

cur.execute("select * from Songs;")
rows=cur.fetchall()

for row in rows:
	print row
cur.execute("CREATE TABLE IF NOT EXISTS Artists ( Id int PRIMARY KEY AUTO_INCREMENT, Artist varchar(25), Album varchar(25), Song varchar(25), DiscID varchar(8));")
cur.execute("CREATE TABLE IF NOT EXISTS Albums ( Id int PRIMARY KEY AUTO_INCREMENT, Album varchar(25), Artist varchar(25), Song varchar(25), DiscID varchar(8));")
cur.execute("CREATE TABLE IF NOT EXISTS Songs ( Id int PRIMARY KEY AUTO_INCREMENT, Song varchar(25), Artist varchar(25), Album varchar(25), DiscID varchar(8));")


while True :
	print menu
	answer=raw_input("\n:")
	if answer=="1":
		cd_key=raw_input("Enter 10 digit CD: ")
		submit_entry.add_entry(cur,cd_key,type="DiscID")
	elif answer=="2":
		#call removal funciton
		print "this is also 1"
	elif answer=="3":
		#call search function
		print "this too is 1"
	elif answer=="4":
		print "Later"
		break
	else:
		print "Wrong Answer"

musicDB.close()



#=======
#>>>>>>> 3d2463222eb5145137b5b17bf080c01579ca2fdc
