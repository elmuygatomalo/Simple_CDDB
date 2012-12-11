#Wrapper File for a simple CDDB will implement user interface allowing:
#adding entries
#removing entries
#querying entries
import _mysql
import submit_entry
import db_query



musicDB_name=""
musicDB_name_query=""
musicDB=None

menu="What would you like to do? \n"
menu=menu+"1-Add Somthing?"
menu=menu+"2-Remove Somethign?"
menu=menu+"3-Search for something?"
menu=menu+"4-Get the fuck out"
#read config file to determine if any previous database was used
#check for existing config file
#check for database 

#musicDB_name=howeverifindthatout

musicDB_name_query="Would you like to use "+musicDB_name+" as your music database?: "
answer = raw_input(musicDB_name_query)
answer.lower()

if answer=="n" or answer=="no":
    musicDB_name=raw_input("Enter new database name: ")

hostname=raw_input("Please enter hostname: ")
username=raw_input("Please enter username: ")
password=raw_input("Please enter password: ")


con=None

while con==None:
 try:
    musicDB = _mysql.connect(hostname,username,password, musicDB_name)
 except _mysql.Error, e:
     print "You fucked up"

musicDB.execute("CREATE TABLE IF NOT EXISTS Artists(Artist STRING, Album VARCHAR(25), Song VARCHAR(25), DiscID VARCHAR(8))")
musicDB.execute("CREATE TABLE IF NOT EXISTS Albums(Artist STRING, Album VARCHAR(25), Song VARCHAR(25), DiscID VARCHAR(8))")
musicDB.execute("CREATE TABLE IF NOT EXISTS Songs(Artist STRING, Album VARCHAR(25), Song VARCHAR(25), DiscID VARCHAR(8))")

                
while true:
    print menu
    answer=raw_input("\n:")
    if answer=="1":
        #call adding function
        print "this is 1"
    elif anser=="2":
        #call removal funciton
        print "this is also 1"
    elif anser=="3":
        #call search function
        print "this too is 1"
    elif anser=="4":
        print "Later Motherfucker"
        break
    else:
        print "Wrong Answer"

con.close()



