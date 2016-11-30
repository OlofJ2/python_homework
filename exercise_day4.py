#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Exercise 4 by Olof Jönsson


import os
import pandas as pd
import warnings
import webbrowser

class Song(object):
    '''Describes musical songs'''
    def __init__(self,title,artist,duration): #constructor
        def duration_check(self,duration):
            '''Tests if duration is a positive number that can be converterted to int. 
            Sets the duration to 0 if not a number, rasies excpetion if negative. 
            '''
            try: 
                int(duration)
            except ValueError:
                warnings.warn("Duration is not a number, is now set to 0")
                return 0
            else:
                duration=int(duration)          
            if duration<0:
                raise Exception("Negative_Number")
            return duration        
        self.title=title
        self.artist=artist
        self.duration=duration_check(self,duration)
    def play(self):
        '''Opens the default webrowser and searches youtube for the artist and title
        '''
        webbrowser.open("https://www.youtube.com/results?search_query={0} {1}".format(self.title,self.artist))
        print 'playing "{0}" by "{1}"'.format(self.title,self.artist)
    def pretty_duration(self):
        '''Returns a pretty string formated as "x h: y min: z s" with z as hours, y as minutes, z as seconds
        '''
        m, s = divmod(self.duration, 60)
        h, m = divmod(m, 60)
        return '{0} h: {1} min {2} s'.format(h,m,s)
    def print_all_info(self):
        '''Prints all attributes and their values
        '''
        print ',\t'.join("%s: %s" % item for item in self.__dict__.items()) #use the __dict__ command to print all attributes

in_path='{0}/lulu_mix_16.csv'.format(os.environ['HOME'])
if not os.path.exists(in_path): #test if the file exixts
    raise Exception('No file called {0}.'.format(in_path))

song_frame=pd.read_csv(in_path,header=0,infer_datetime_format=False)
songs=[]
for index,row in song_frame.iterrows():
    print row['Name'],row['Artist'],row['Duration']
    try : #tries to add the song
        songs.append(Song(row['Name'],row['Artist'],row['Duration']))
    except Exception:
        print "{0} is a negative number, can't add {1} by {2}".format(row['Duration'],row['Name'],row['Artist'])

"""
Python course EBC 2016
Day 4 - Exercise instructions
Lucas Sinclair <lucas.sinclair@me.com>

* Write a program in a file called "exercise_day4.py"
* You have until the start of the next course at 13h00 tomorrow to finish it.
* Once the program is done, upload it in your github repository "python_homework" in a directory named "day4".

The program should read the file named "lulu_mix_16.csv". This file should be placed in your "home" directory. Your program should use the OS environment variable "$HOME" to find the file.
This file is a comma separated values format. It contains information about different music tracks.

For each line in the file (excluding the header) the program should produce a new "Song" instance. It should place all the Song instances created in a list called "songs".

### Each Song object should have these attributes:

* title
The title of the song as a string.

* artist
The artist of the song as a string.

* duration
The title of the song as an integer in seconds.

When creating new Song instances:

-> If the duration of a song is not a number, set it to 0, but issue a warning.
-> If the duration of a song is negative, raise an Exception and stop the program.

### Each Song object should have these methods:

* pretty_duration(self)
Returns a nice string describing the duration. For instance if the duration is 3611, this methods takes no input and returns "01 hours 00 minutes 11 seconds" as a string.

* play(self)
Automatically opens a webpage on your computer with a youtube search for the title.

Once your program is ready the following four lines of code should run without errors. (After you have removed the negative duration song!).
"""

for s in songs: print s.artist
for s in songs: print s.pretty_duration()
print sum(s.duration for s in songs), "seconds in total"
songs[6].play()