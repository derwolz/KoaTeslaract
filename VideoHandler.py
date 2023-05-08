import os, cv2, asyncio, random

async def playVideo(video, ttl):
    cap = cv2.VideoCapture(video)
    print(ttl)
    #resets the video so there isn't overlap
    await setToBG()
    await asyncio.sleep(.1)
    await setToFG()
    size = [1920, 1080]

    while True:
        ret, frame = cap.read()

        if ret:
            resized_frame = cv2.resize(frame, size)
            cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('frame', resized_frame)
        if not ret:
            if video == bg[1]:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            else:
                 await setToBG()   
        if not isShow or ttl < 0.0 or (cv2.waitKey(1) and 0xFF == ord('q')):
            await setToBG()
            break
        await asyncio.sleep(1/30.0)
        ttl -= 1/30.0
        print(ttl)

async def showBG():
    size = [1920, 1080]
    while True:
        img = cv2.imread(bg[0])
        resized_frame = cv2.resize(img, size)
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("frame", resized_frame)
        if isShow or (cv2.waitKey(1) and 0xFF == ord('q')):
            break
        await asyncio.sleep(1/30.0)

async def setToFG():
    print('setToFG')
    global isShow
    isShow = True
async def setToBG():
    print('setToBG')
    global isShow
    isShow = False
    loop.create_task(showBG())

async def insertGoodVideo():
    await setToFG()
    selection = random.randrange(0,len(good_videos))
    await playVideo(good_videos[selection], ttl)

async def insertBadVideo():
    await setToFG()
    selection = random.randrange(0,len(bad_videos))
    await playVideo(bad_videos[selection], ttl)

async def main_loop():
    ttl = 3
    global bg, playing, isPartyTime
    loop.create_task(setToBG())
    while True:
        await readResult()
        await asyncio.sleep(1/30.0)

async def readResult():
    
    lines = []
    with open("./Qresult") as file:
        lines = file.readlines()
    with open("./Qresult", 'w') as file:
        file.write("")
    if lines:
        if lines[0] == "true":
            loop.create_task(insertGoodVideo())
        if lines[0] == "false":
            loop.create_task(insertBadVideo())
        if lines[0] == "PartyTime":
            loop.create_task(changeBGVideo())

async def changeBGVideo():
    if not isShow:
        await setToFG()
        loop.create_task(playVideo(bg[1],-1))
    else:
        await setToBG()
    
def start():
    loop.run_until_complete(main_loop())
if __name__ == "__main__":
    #global Variables within the Video Handler
    current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data\\goodVid\\")
    
    good_videos = [os.path.join(current_dir,f) for f in os.listdir(current_dir)]
    current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data\\badVid\\")
    bad_videos = [os.path.join(current_dir,f) for f in os.listdir(current_dir)]
    bg = [os.path.join(os.path.dirname(os.path.abspath(__file__)),"data\\bg.png"), os.path.join(os.path.dirname(os.path.abspath(__file__)),"data\\bg2.mp4")]
    playing = []
    ttl = 4
    isShow=True
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start()