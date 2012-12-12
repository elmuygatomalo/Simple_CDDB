#db_query
# This module will contain functions that allow the user 
# to query the databases for relevent information... or something
import sys
import _mysql
import string


#Finds all entries relating to specified args in the Songs DB
def find_song(**args):
	artist_name=None
	album_name=None
	song_name=None
	disc_id=None

	for index,value in args.iteritems():
		if args.get("album") != None:
			album_name=args.get("album")
		elif args.get("artist") != None:
			song_name=args.get("song")
		elif args.get("discid") != None:
			disc_id=agrs.get("discid")
		else:
			raise Exception("What are you doing!?")

	#now I need to form queries based on the available data.
	mysql_Songs_query="SELECT Artist FROM Songs"

	if song_name != None:
		mysql_Songs_query=mysql_Songs_query+"WHERE Song="+'"'+song_name+'"'
	if album_name != None:
		mysql_Songs_query=mysql_Songs_query+"WHERE Artist="+'"'+artist_name+'"'
	if artist_name != None:
		mysql_Songs_query=mysql_Songs_query+"WHERE Album="+'"'+album_name+'"'
	if disc_id != None:
		mysql_Songs_query=mysql_Songs_query+"WHERE DiscID="+'"'+disc_id+'"'

	results=musicDB.execute(mysql_Songs_query)

	return results



#Finds all entries relating to specified args in the Artists DB
def find_song(**args):
	artist_name=None
	album_name=None
	song_name=None
	disc_id=None

	for index,value in args.iteritems():
		if args.get("album") != None:
			album_name=args.get("album")
		elif args.get("artist") != None:
			song_name=args.get("song")
		elif args.get("discid") != None:
			disc_id=agrs.get("discid")
		else:
			raise Exception("What are you doing!?")
	#now I need to form queries based on the available data.
	mysql_Artists_query="SELECT Artist FROM Artists"

	if song_name != None:
		mysql_Artists_query=mysql_Artists_query+"WHERE Song="+'"'+song_name+'"'
	if album_name != None:
		mysql_Artists_query=mysql_Artists_query+"WHERE Artist="+'"'+artist_name+'"'
	if artist_name != None:
		mysql_Artists_query=mysql_Artists_query+"WHERE Album="+'"'+album_name+'"'
	if disc_id != None:
		mysql_Artists_query=mysql_Artists_query+"WHERE DiscID="+'"'+disc_id+'"'

	results=musicDB.execute(mysql_Artists_query)

	return results

#Finds all entries relating to specified args in the Albums DB
def find_song(**args):
	artist_name=None
	album_name=None
	song_name=None
	disc_id=None

	for index,value in args.iteritems():
		if args.get("album") != None:
			album_name=args.get("album")
		elif args.get("artist") != None:
			song_name=args.get("song")
		elif args.get("discid") != None:
			disc_id=agrs.get("discid")
		else:
			raise Exception("What are you doing!?")
	#now I need to form queries based on the available data.
	mysql_Albums_query="SELECT Artist FROM Albums"

	if song_name != None:
		mysql_Albums_query=mysql_Albums_query+"WHERE Song="+'"'+song_name+'"'
	if album_name != None:
		mysql_Albums_query=mysql_Albums_query+"WHERE Artist="+'"'+artist_name+'"'
	if artist_name != None:
		mysql_Albums_query=mysql_Albums_query+"WHERE Album="+'"'+album_name+'"'
	if disc_id != None:
		mysql_Albums_query=mysql_Albums_query+"WHERE DiscID="+'"'+disc_id+'"'


#Finds all entries relating to specified args in all DBs
def find_song(**args):
	artist_name=None
	album_name=None
	song_name=None
	disc_id=None

	for index,value in args.iteritems():
		if args.get("album") != None:
			album_name=args.get("album")
		elif args.get("artist") != None:
			song_name=args.get("song")
		elif args.get("discid") != None:
			disc_id=agrs.get("discid")
		else:
			raise Exception("What are you doing!?")
	#now I need to form queries based on the available data.
	mysql_Songs_query="SELECT * FROM Artists"
	mysql_Artists_query="SELECT * FROM Artists"
	mysql_Albums_query="SELECT * FROM Artists"
 
	if song_name != None:
		mysql_Songs_query=mysql_Songs_query+"WHERE Song="+'"'+song_name+'"'
		mysql_Artists_query=mysql_Artists_query+"WHERE Song="+'"'+song_name+'"'
		mysql_Albums_query=mysql_Albums_query+"WHERE Song="+'"'+song_name+'"'
	if album_name != None:
		mysql_Songs_query=mysql_Songs_query+"WHERE Artist="+'"'+artist_name+'"'
		mysql_Artists_query=mysql_Artists_query+"WHERE Artist="+'"'+artist_name+'"'
		mysql_Albums_query=mysql_Albums_query+"WHERE Artist="+'"'+artist_name+'"'
	if artist_name != None:
		mysql_Songs_query=mysql_Songs_query+"WHERE Album="+'"'+album_name+'"'
		mysql_Artists_query=mysql_Artists_query+"WHERE Album="+'"'+album_name+'"'
		mysql_Albums_query=mysql_Albums_query+"WHERE Album="+'"'+album_name+'"'
	if disc_id != None:
		mysql_Songs_query=mysql_Songs_query+"WHERE DiscID="+'"'+disc_id+'"'
		mysql_Artists_query=mysql_Artists_query+"WHERE DiscID="+'"'+disc_id+'"'
		mysql_Albums_query=mysql_Albums_query+"WHERE DiscID="+'"'+disc_id+'"'

	complete_query='('+mysql_Albums_query+')'+"UNION"+'('+mysql_Artists_query\
	+')'+"UNION"+'('+mysql_Albums_query+')'

	results=musicDB.execute(complete_query)

	return result
