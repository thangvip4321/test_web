import os
from flask import Flask, flash, request, redirect, url_for ,g, send_file
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from mtcnn import MTCNN
UPLOAD_FOLDER = 'damn_son'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_mapping(SECRET_KEY="dev")
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def apply_detection(img,detection):
    box = detection['box']
    img = cv2.rectangle(img,(box[0],box[1]),(box[0]+box[2],box[1]+box[3]),thickness=5,color=(0,0,255))
    keypoints = detection['keypoints']
    for i,j in keypoints.items():
        img = cv2.circle(img,(j[0],j[1]),radius=3,thickness=-1,color=(0,0,255))
    return img
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(request.files)
        print(file.filename)

        data= file.read()
        x = np.fromstring(data,dtype= 'uint8')
        img = cv2.imdecode(x,cv2.IMREAD_COLOR)
        detector= MTCNN()
        detections = detector.detect_faces(img)
        for detection in detections:
            img = apply_detection(img,detection)
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print("name is ",filename)
            file.close()
            file_path =os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print("name path is ",file_path)
            cv2.imwrite(file_path,img)

            response = send_file(file_path,mimetype='image/jpeg',cache_timeout=0) #set time_out to renew every reload :)
            print("response is",response.headers)
            #os.remove(file_path)
            return response 
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file >
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run()
