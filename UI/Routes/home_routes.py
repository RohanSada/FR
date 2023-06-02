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

home = Blueprint('home', __name__, url_prefix='/')

@home.route('/')
def index():
    return render_template('home_page.html')

@home.route('/Start',  methods=['POST'])
# When start is clicked, the FR runs and the output is displayed on the webpage 
def Start():
    return render_template('start.html')

@home.route('/Register', methods=['POST'])
# This button is present in the home_page. When this is clicked register tab should be opened. 
def Register():
    return render_template('register.html')

@home.route('/Quit', methods=['POST'])
def Quit():
    os._exit(0)