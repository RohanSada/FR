from flask import Flask, render_template, Response, request, redirect, url_for, session, Blueprint
import cv2
import os


def display_image():
    img_name = os.listdir('../CapturedImages/')
    frame = cv2.imread('../CapturedImages/'+str(img_name[0]))
    ret, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

Confirm = Blueprint('Confirm', __name__, url_prefix='/Confirm/')

@Confirm.route('/Show_Capture')
# This is present in the comfirm.html page. This shows the captured image and asked the user to confirm or delete.
def Show_Capture():
    global user_name
    return Response(display_image(), mimetype='multipart/x-mixed-replace; boundary=frame')

@Confirm.route('/Confirm_Capture', methods=['POST'])
# This is present in the confirm page which askes the user to confirm the image taken.
def confirm_capture():
    img_name = os.listdir('../CapturedImages/')
    frame = cv2.imread('../CapturedImages/'+str(img_name[0]))
    cv2.imwrite('../ConfirmedImages/'+str(img_name[0]), frame)
    os.remove('../CapturedImages/'+str(img_name[0]))
    return render_template('home_page.html')

@Confirm.route('/Retake_Capture', methods=['POST'])
def retake():
    img_name = os.listdir('../CapturedImages/')
    os.remove('../CapturedImages/'+str(img_name[0]))
    return render_template('register.html')

@Confirm.route('/Quit', methods=['POST'])
def Quit():
    os._exit(0)
