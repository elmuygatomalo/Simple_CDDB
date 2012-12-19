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
menu=menu+"4-Get the fuck out "
#read config file to determine if any previous database was used
#check for existing config file
#check for database 

#musicDB_name=howeverifindthatout
#if musicDB != None:#
#	musicDB_name_query="Would you like to use "+musicDB_name+" as your 
#music database?: "
#	answer = raw_input(musicDB_name_query)
#	answer.lower()
#	
#	if answer=="n" or answer=="no":#
#		musicDB_name=raw_input("Enter new database name: ")
#else:
#	musicDB_name=raw_input("Enter Database name: ")
#	
#	
#hostname=raw_input("Please enter hostname: ")
#username=raw_input("Please enter username: ")
#password=raw_input("Please enter password: ")


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
		print "You fucked up you login credentials, if they even exist you jerk"
		sys.exit()

cur=musicDB.cursor()
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
		print "Later Motherfucker"
		break
	else:
		print "Wrong Answer"

musicDB.close()



#=======
#>>>>>>> 3d2463222eb5145137b5b17bf080c01579ca2fdc
