#!/usr/bin/python

# Edit the script and put in your name, email address and file extension of your songs
# Copy this script to the folder that contains your songs
# From a terminal/CLI, change directory to the aforementioned folder
# Run the script by typing: python strip.py
# 
# It will look for all files with the given file extension
# Then, it will open each file and replace all occurences of your name and email with spaces

# NOTE: PLEASE BACK UP YOUR SONGS BEFORE RUNNING THE SCRIPT IN CASE SOMETHING GOES WRONG

import os

# Set your name and email address accordingly
name = "Firstname Lastname"
email = "foo@bar.com"
space = " " # You can set a character here to replace each character in your info
file_extension = ".m4a" #Set the correct file extension for your songs


cwd = os.getcwd()
files = os.listdir(cwd)

for curfile in files:
	if curfile.find(file_extension) != -1:
		songfile = file(curfile,"r+b")
		song = songfile.read()
		
		
		song = song.replace(name,space*len(name))
		song = song.replace(email,space*len(email))
		
		songfile.seek(0)
		songfile.write(song)
		songfile.close()