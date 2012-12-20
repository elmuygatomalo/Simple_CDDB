#This file conatains routine involving the addition of a song/album/artist to database

import _mysql
import string

def add_entry(database,*args, **entry_type):
	#DiscID: The only argument provided is the Disc
	#This will use the DiscID to lookup all tracks on disc and add each artist, song and album to the respective DBS
	
	database.execute("select * from Songs;")
	rows=database.fetchall()
	for row in rows:
		print row
	
	if entry_type.get("type")  == "DiscID":
		#Query the Net to find the Album name/Artists/song names relating to discid
		DiscID=args[0]
		#Some Crazy TCP shit I'll do later
		tracks=1
		song_name="Ias123412dfasdf"
		album_name="IsdfB12341234UMasdf"
		artist_name="IMsdIS12341234Tasdf"
		result=""
		for index in xrange(tracks):
			#Insert track into Songs database
			sql_insert_string="insert into Songs (Artist,Album,Song,DiscID) values('"+artist_name+"','"+album_name+"','"+song_name+"','"+DiscID+"');"
			print(sql_insert_string)
			try:
				print(database.execute(sql_insert_string))
			except _mysql.Error, e:
				print "You fucked up\n"
				print e
			#Insert track into Albums database
			sql_insert_string="insert into Albums (Song,Artist,Album,DiscID) values('"+artist_name+"','"+album_name+"','"+song_name+"','"+DiscID+"');"
			try:
				print(database.execute(sql_insert_string))
			except _mysql.Error, e:
				print "You fucked up"
			#Insert track into Artists database
			sql_insert_string="insert into Artists (Song,Artist,Album,DiscID) values('"+artist_name+"','"+album_name+"','"+song_name+"','"+DiscID+"');"
			try:
				print(database.execute(sql_insert_string))
			except _mysql.Error, e:
				print "You fucked up"
		return
	else:
		#Uh... I'll do this later too.
		return




