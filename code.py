from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import sys
w=Tk()
w.title('Music Player')
mixer.init()
defined_font = font.Font(family='Helvetica')
songs_list=Listbox(w,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=9)

#add many songs to the playlist of python mp3 player
def addsongs():
    tmp_song = filedialog.askopenfilename(initialdir="/", title="Choose a Song",filetypes=(("mp3 Files", "*.mp3"),))
    chain = ""
    for song in tmp_song:
        song = song.replace(f"{sys.argv[0][:-3]}/Music","")
        chain += song
        song_add = chain
    songs_list.insert(END, song_add)
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
    
    
def Play():
    song=songs_list.get(ACTIVE)
    song=f'{song}'
    mixer.music.load(song)
    mixer.music.play()

#to pause the song 
def Pause():
    mixer.music.pause()

#to stop the  song 
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#to resume the song

def Resume():
    mixer.music.unpause()

#Function to navigate from the current song
def Previous():
    #to get the selected song index
    previous_one=songs_list.curselection()
    #to get the previous song index
    previous_one=previous_one[0]-1
    #to get the previous song
    temp2=songs_list.get(previous_one)
    temp2=f'{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate new song
    songs_list.activate(previous_one)
    #set the next song
    songs_list.selection_set(previous_one)

def Next():
    #to get the selected song index
    next_one=songs_list.curselection()
    #to get the next song index
    next_one=next_one[0]+1
    #to get the next song 
    temp=songs_list.get(next_one)
    temp=f'{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate newsong
    songs_list.activate(next_one)
     #set the next song
    songs_list.selection_set(next_one)



#play button
play_button=Button(w,text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)
#pause button 
pause_button=Button(w,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)
#stop button
stop_button=Button(w,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)
#resume button
Resume_button=Button(w,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)
#previous button
previous_button=Button(w,text="Prev",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)
#nextbutton
next_button=Button(w,text="Next",width =7,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)
#menu 
my_menu=Menu(w)
w.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)
w=mainloop()
