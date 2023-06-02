from flask import Flask, render_template, Response, request, redirect, url_for, session, Blueprint
import cv2
import os


def generate_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

StartFR = Blueprint('Start_FR', __name__, url_prefix='/Start_FR/')

@StartFR.route('/Display_FR_Data')
# This is used in the start.html page to display the fr output. (Video Feed of the FR output)
def Display_FR_Data():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@StartFR.route('/Back', methods=['POST'])
def go_back():
   return render_template('home_page.html')

@StartFR.route('/Quit', methods=['POST'])
def Quit():
    os._exit(0)