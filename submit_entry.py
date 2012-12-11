#This file conatains routine involving the addition of a song/album/artist to database

import _mysql
import string

def add_entry(*args, **entry_type):
    
    #DiscID: The only argument provided is the DiscID
    #This will use the DiscID to lookup all tracks on disc and add each artist, song and album to the respective DBS
    if options.get("type")  == "DiscID":
        #Query the Net to find the Album name/Artists/song names relating to discid
        
        DiscID=args[0]
        #Some Crazy TCP shit I'll do later
        tracks=1
        song_name="IMASONG"
        album_name="IMAALBUM"
        artist_name="IMAARTIST"
        for index in xrange(tracks):
            #Insert 
            sql_insert_string="INSERT INTO Songs VALUES("+artist_name+","+album_name+","+song_name+","+DiscID
            try:
                musicDB.execute(sql_insert_string)
            except _mysql.Error, e:
                print "You fucked up"
            
            sql_insert_string="INSERT INTO Artists VALUES("+artist_name+","+album_name+","+song_name+","+DiscID
            try:
                musicDB.execute(sql_insert_string)
             except _mysql.Error, e:
                 print "You fucked up"
            
            sql_insert_string="INSERT INTO Albums VALUES("+artist_name+","+album_name+","+song_name+","+DiscID
            try:
                musicDB.execute(sql_insert_string)
             except _mysql.Error, e:
                 print "You fucked up"
    else:
        #Uh... I'll do this later too.
    