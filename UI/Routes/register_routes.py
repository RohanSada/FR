from flask import Flask, render_template, Response, request, redirect, url_for, session, Blueprint
import cv2
import os


user_name = ''

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

Register = Blueprint('Register', __name__, url_prefix='/Register/')

@Register.route('/Display_Video_Feed')
# This is present in the register.html file to diaplay the video feed for clicking pictures. 
def Display_Video_Feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@Register.route('/RegisterFace', methods=['POST'])
# This is present in the register.html page. When this is clicked, the picture is taken and asked to confirm (Opens the confirm.html page)
def Register_Face():
    global user_name
    if user_name == '':
        return render_template('register.html', name='Please Enter Name')
    else:
        camera = cv2.VideoCapture(0)
        success, frame = camera.read()
        cv2.imwrite('../CapturedImages/Img_'+str(user_name)+'.jpg', frame)
        return render_template('confirm.html', saved_text=user_name)

@Register.route('/Enter_Name', methods=['GET', 'POST'])
def add_name():
    global user_name
    if request.method == 'POST':
        # Retrieve the text from the form submission
        text = request.form['text']
        if not text:
            return "Please Enter Name"
        else:
            user_name = text
            return render_template('register.html', name='Name Entered: '+str(user_name))

@Register.route('/Back', methods=['POST'])
def go_back():
   return render_template('home_page.html')

@Register.route('/Quit', methods=['POST'])
def Quit():
    os._exit(0)