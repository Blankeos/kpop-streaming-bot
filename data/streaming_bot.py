import pyautogui as pag
import time
import json
import random
import threading

random.seed(time.time())
#Opening Config JSON

class StreamingBot():
    def __init__(self):
        with open('data/config.json') as f:
            self.data = json.load(f)

        #self.browser_coord = pag.Point(int(self.data['config'][0]['browser_x']), int(self.data['config'][0]['browser_y']))
        #self.fullscreen_coord = pag.Point(int(self.data['config'][0]['fullscreen_x']), int(self.data['config'][0]['fullscreen_y']))
        self.url_coord = pag.Point(int(self.data['config'][0]['url_x']), int(self.data['config'][0]['url_y']))
        self.yt_search_coord = pag.Point(int(self.data['config'][0]['yt_x']), int(self.data['config'][0]['yt_y']))
        self.video_coord = pag.Point(int(self.data['config'][0]['video_x']), int(self.data['config'][0]['video_y']))
        self.video_name = self.data['config'][0]['videoname']
        self.video_duration = int(self.data['config'][0]['videoduration'])
        self.othervids = self.data['config'][0]['othervids']

        self.exit = threading.Event()

    def saveToJson(self):
        #self.data['config'][0]['browser_x'] = self.browser_coord.x
        #self.data['config'][0]['browser_y'] = self.browser_coord.y
        #self.data['config'][0]['fullscreen_x'] = self.fullscreen_coord.x
        #self.data['config'][0]['fullscreen_y'] = self.fullscreen_coord.y
        self.data['config'][0]['url_x'] = self.url_coord.x
        self.data['config'][0]['url_y'] = self.url_coord.y
        self.data['config'][0]['yt_x'] = self.yt_search_coord.x
        self.data['config'][0]['yt_y'] = self.yt_search_coord.y
        self.data['config'][0]['video_x'] = self.video_coord.x
        self.data['config'][0]['video_y'] = self.video_coord.y
        self.data['config'][0]['videoname'] = self.video_name
        self.data['config'][0]['videoduration'] = self.video_duration
        self.data['config'][0]['othervids'] = self.othervids

        with open('data/config.json', 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def shutdown(self):
        self.exit.set()
    
    def custom_sleep(self, seconds):
        for i in range(0, seconds):
            if (self.exit.is_set()):
                break
            time.sleep(1)

    def start(self):
        self.custom_sleep(2)
        if (self.exit.is_set()):
            return
        pag.click(self.url_coord)
        pag.typewrite('www.youtube.com', interval=0.1)
        pag.typewrite(['enter'])

        self.custom_sleep(5)
        if (self.exit.is_set()):
            return

        #loop starts here
        while(not self.exit.is_set()):
            pag.click(self.yt_search_coord)
            pag.hotkey('ctrl', 'a')
            pag.typewrite(self.video_name, interval=0.1)
            pag.typewrite(['enter'])

            self.custom_sleep(5) #CURRENTLY WAITING FOR PAGE TO LOAD (WAIT)
            if (self.exit.is_set()):
                break
            pag.click(self.video_coord)
            
            
            self.custom_sleep(self.video_duration) #CURRENTLY WATCHING VIDEO (WAIT)
            if (self.exit.is_set()):
                break

            #WATCH A DIFFERENT VID
            random.seed(time.time())
            i = random.randint(0, 2)
            prev_i = i
            pag.click(self.yt_search_coord)
            pag.hotkey('ctrl', 'a')
            pag.typewrite(self.othervids[i], interval=0.1)
            pag.typewrite(['enter'])

            self.custom_sleep(3) #CURRENTLY WAITING FOR PAGE TO LOAD (WAIT)
            if (self.exit.is_set()):
                break

            pag.click(self.video_coord)

            self.custom_sleep(60) #CURRENTLY WATCHING THE VIDEO (WAIT)
            if (self.exit.is_set()):
                break

            #WATCH A DIFFERENT VID
            while(prev_i == i):
                random.seed(time.time())
                i = random.randint(0, 2)
                
            pag.click(self.yt_search_coord)
            pag.hotkey('ctrl', 'a')
            pag.typewrite(self.othervids[i], interval=0.1)
            pag.typewrite(['enter'])

            self.custom_sleep(3) #CURRENTLY WAITING FOR PAGE TO LOAD
            if (self.exit.is_set()):
                break

            pag.click(self.video_coord)

            self.custom_sleep(60) #CURRENTLY WATCHING THE VIDEO (WAIT)
            if (self.exit.is_set()):
                break