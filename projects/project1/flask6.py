#!/usr/bin/env python
from flask import Flask, render_template, Response
import cv2
vc = cv2.VideoCapture(0)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('stream.html')

def gen(vc):

    while True:
        frame = vc.read()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(vc),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()