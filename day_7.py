'''
Read a file called "lulu_mix_16.csv", writes contents as three columns in an SQL database called "playlist.db
'''

#Built in modules
import csv
import sqlite3
import sys

filename="lulu_mix_16.csv"
playlistdb=sqlite3.connect('playlist.db')
c=playlistdb.cursor()


with open(filename, 'r' ) as csvfile:
    playlistreader = csv.reader(csvfile)
    for row_index,row_content in enumerate(playlistreader):
        if row_index==0:
            print "Header is {0}".format(row_content)
            c.execute('''CREATE TABLE playlist (Name text, Artist text, Duration text)''')
        else:
            print "A normal line is:\t {0}".format(row_content)
            row_content=(row_content,)
            print type(row_content)
            try:
                c.executemany('INSERT INTO playlist VALUES (?,?,?)', row_content)
            except:
                print "Unexpected error:", sys.exc_info()[0]
            else:
                continue

                

                
playlistdb.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
playlistdb.close()


con = sqlite3.connect('playlist.db')
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
x=cursor.fetchall()
print x #prints that we have saved a new table called playlist in playlist.db