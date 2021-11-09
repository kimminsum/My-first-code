# from tkinter import *

# class Window(Frame):

#     def __init__(self, master=None):
#         Frame.__init__(self, master)        
#         self.master = master

#         # widget can take all window
#         self.pack(fill=BOTH, expand=1)

#         # create button, link it to clickExitButton()
#         exitButton = Button(self, text="Exit", command=self.clickExitButton)

#         # place button at (0,0)
#         exitButton.place(x=80, y=80)

#     def clickExitButton(self):
#         exit()
        
# root = Tk()
# app = Window(root)
# root.wm_title("Game Over")
# root.geometry("200x200")
# root.mainloop()

from pygame import mixer
  
# Starting the mixer
mixer.init()
  
# Loading the song
mixer.music.load("alice.mp3")
  
# Setting the volume
mixer.music.set_volume(0.7)
  
# Start playing the song
mixer.music.play()
  
# infinite loop
while True:
      
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")
      
    if query == 'p':
  
        # Pausing the music
        mixer.music.pause()     
    elif query == 'r':
  
        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':
  
        # Stop the mixer
        mixer.music.stop()
        break