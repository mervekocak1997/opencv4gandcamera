import numpy as np
import cv2
import imageio

from utils import CFEVideoConf, image_resize
from matplotlib import pyplot as plt
import cv2 as cv

import tkinter as tk
from PIL import Image

root = tk.Tk()
file="images/logo/cfe.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))

def stop_animation():
    root.after_cancel(anim)

gif_label = tk.Label(root,image="")
gif_label.pack()

start = tk.Button(root,text="start",command=lambda :animation(count))
start.pack()

stop = tk.Button(root,text="stop",command=stop_animation)
stop.pack()

root.mainloop()

def make_480p():
    cap.set(3, 640)
    cap.set(4, 600)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)


def rescale_frame(frame, percent=50):
    scale_percent = 50
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

cap = cv2.VideoCapture(0)



frames_per_seconds = 24


img_path = 'images/logo/cfe-coffee.png'


logo = cv2.imread(img_path, -1)
watermark = image_resize(logo, height=50 ,width=100)
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)

logo = cv2.imread(img_path, -1)
watermark = image_resize(logo, height=50 ,width=100)
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)


while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = rescale_frame(frame, percent=30)

    frame2 = rescale_frame(frame, percent=500)




    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    frame_h, frame_w, frame_c = frame.shape
    # overlay with 4 channels BGR and Alpha
    overlay = np.zeros((frame_h, frame_w, 4), dtype='uint8')
    watermark_h, watermark_w, watermark_c = watermark.shape
    # replace overlay pixels with watermark pixel values
    for i in range(0, watermark_h):
        for j in range(0, watermark_w):

                offset = 10
                h_offset = frame_h - watermark_h - offset
                w_offset = frame_w - watermark_w - offset
                overlay[ i, offset+ j] = watermark[i,j]




    cv2.addWeighted(overlay, 0.25, frame, 1.0, 0, frame)
    cv2.line(frame, (0, 100), (800, 100), (100, 0, 255), 2)
    cv2.rectangle(frame, (10, 450), (200, 300), (100, 0, 255), 1)
    # cv2.rectangle(frame, (630, 450), (400, 300), (100, 0, 255), 3)
    cv2.putText(frame, "1.TEST", (50, 380), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame, "2.TEST", (50, 430), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame, "MERVE", (500, 430), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame, "TEST", (500, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)



    cv2.line(frame2, (0, 100), (800, 100), (100, 0, 255), 2)
    cv2.rectangle(frame2, (10, 450), (200, 300), (100, 0, 255), 1)
    # cv2.rectangle(frame, (630, 450), (400, 300), (100, 0, 255), 3)
    cv2.putText(frame2, "1.TEST", (50, 380), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame2, "2.TEST", (50, 430), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame2, "MERVE", (500, 430), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame2, "TEST", (500, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGRA2BGR)


    # Display the resulting frame

    cv2.imshow('frame', frame)
    cv2.imshow('frame2', frame2)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.waitKey(0)

cv2.destroyAllWindows()