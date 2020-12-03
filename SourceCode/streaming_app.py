from tkinter import *
from data import streaming_bot
import pyautogui
import threading

#Initialize Modules
root  = Tk()
root.title('Carlo Streaming Automation App')
#root.iconbitmap(pathhere)
#root.geometry("500x200")
bot = streaming_bot.StreamingBot()

#DATA Initialization from Modules
currentMousePos = pyautogui.position()

#Functions
def save_config():
    #bot.browser_coord = pyautogui.Point(int(ba_x.get()),int(ba_y.get()))
    #bot.fullscreen_coord = pyautogui.Point(int(fs_x.get()), int(fs_y.get()))
    bot.url_coord = pyautogui.Point(int(url_x.get()),int(url_y.get()))
    bot.yt_search_coord = pyautogui.Point(int(yt_x.get()),int(yt_y.get()))
    bot.video_coord = pyautogui.Point(int(video_x.get()),int(video_y.get()))
    bot.video_name = video_name.get()
    bot.video_duration = int(video_dur.get())
    for i, vid in enumerate(other_vids):
        bot.othervids[i] = vid.get()
    
    bot.saveToJson()

def update_currentMousePos():
    currentMousePos = pyautogui.position()
    currentMousePos_label.config(text="Current Mouse Position\nX: " + str(currentMousePos.x) + " | Y: " + str(currentMousePos.y))
    currentMousePos_label.after(50, update_currentMousePos)


#Display Current Mouse Position
currentMousePos_label = Label(root, text="Current Mouse Position\nX: " + str(currentMousePos.x) + " | Y: " + str(currentMousePos.y))
currentMousePos_label.grid(row=0, column=0, columnspan=3, pady=(0,20))

update_currentMousePos()

Label(root, text="Current Parameters").grid(row=1, column=0, columnspan=3)

#Parameters Grid Starts Here:
#Label(root, text="Browser App Coordinates X | Y").grid(row=2, column=0, pady=5, padx=10)
#ba_x = Entry(root, width=10, borderwidth=2)
#ba_x.grid(row=2, column=1, padx=5)

#ba_y = Entry(root, width=10, borderwidth=2)
#ba_y.grid(row=2, column=2, padx=5)

#ba_x.insert(0, str(bot.browser_coord.x))
#ba_y.insert(0, str(bot.browser_coord.y))

#Label(root, text="Fullscreen Button Coordinates X | Y").grid(row=3, column=0, pady=5, padx=10)
#fs_x = Entry(root, width=10, borderwidth=2)
#fs_x.grid(row=3, column=1, padx=5)

#fs_y = Entry(root, width=10, borderwidth=2)
#fs_y.grid(row=3, column=2, padx=5)

#fs_x.insert(0, str(bot.fullscreen_coord.x))
#fs_y.insert(0, str(bot.fullscreen_coord.y))

Label(root, text="Address Bar Coordinates X | Y").grid(row=4, column=0, pady=5, padx=10)
url_x = Entry(root, width=10, borderwidth=2)
url_x.grid(row=4, column=1)

url_y = Entry(root, width=10, borderwidth=2)
url_y.grid(row=4, column=2)

url_x.insert(0, str(bot.url_coord.x))
url_y.insert(0, str(bot.url_coord.y))

Label(root, text="Youtube Search Coordinates X | Y").grid(row=5, column=0, pady=5, padx=10)
yt_x = Entry(root, width=10, borderwidth=2)
yt_x.grid(row=5, column=1)

yt_y = Entry(root, width=10, borderwidth=2)
yt_y.grid(row=5, column=2)

yt_x.insert(0, str(bot.yt_search_coord.x))
yt_y.insert(0, str(bot.yt_search_coord.y))

Label(root, text="Video Click Coordinates X | Y").grid(row=6, column=0, pady=5, padx=10)
video_x = Entry(root, width=10, borderwidth=2)
video_x.grid(row=6, column=1)

video_y = Entry(root, width=10, borderwidth=2)
video_y.grid(row=6, column=2)

video_x.insert(0, str(bot.video_coord.x))
video_y.insert(0, str(bot.video_coord.y))

Label(root, text="Video to Search (String)").grid(row=7, column=0, pady=5, padx=10)
video_name = Entry(root, width=20, borderwidth=2)
video_name.grid(row=7, column=1, columnspan=2)

video_name.insert(0, bot.video_name)

Label(root, text="Video Duration (Seconds)").grid(row=8, column=0, pady=5, padx=10)
video_dur = Entry(root, width=20, borderwidth=2)
video_dur.grid(row=8, column=1, columnspan=2)

video_dur.insert(0, bot.video_duration)

currentRow = 8+1
Label(root, text="Other Videos for betweens (String)").grid(row=currentRow, column=0, pady=5, padx=10)

other_vids = []
for i, vid in enumerate(bot.othervids):
    e = Entry(root, width=20, borderwidth=2)
    e.grid(row=currentRow, column=1, columnspan=2)
    e.insert(0, bot.othervids[i])
    other_vids.append(e)
    currentRow+=1

#Save Button
Button(root, text="Save", bg="blue", fg="white", padx=5, command=save_config).grid(row=currentRow, column=0, columnspan=3, pady=5)

currentRow+=1

#Start Automation
start_button = Button(root, text="Start Automation", bg="green", fg="white", padx=10, command=threading.Thread(target=bot.start).start)
start_button.grid(row=currentRow, column=0, columnspan=3, pady=20)

currentRow+=1

def exit_program():
    bot.shutdown()
    root.destroy()

    
Button(root, text="End Program", bg="red", fg="white", padx=10, command=exit_program).grid(row=currentRow, column=0, columnspan=3, pady=20)

root.mainloop()