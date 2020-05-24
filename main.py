from flask import Flask
import sys
import cv2
import numpy as np
from flask import jsonify
from flask import request
import face_recognition.api as fr
from PIL import Image
import io
import os
#import magic
import urllib.request
import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def add_star():
  name = request.files['image1']
  print(type(name))
  print(name)
  #if name and allowed_file(name.filename):
  name = secure_filename(name.filename)
  print(name)
   #name.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
   #flash('File successfully uploaded')
  #return redirect('/')
  #else:
   #flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
   #return redirect(request.url)
  name1 = request.files['image2']

  #if name1 and allowed_file(name1.filename):
  #filename = secure_filename(name1.filename)
   #name1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
   #flash('File successfully uploaded')
   #return redirect('/')

  #else:
   #flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
  



        
  
  print('Amirrrrr')
  print(name)
  #print(name2)
    
  file_name1 = name    
  file_name2 = name1

  #file_name1 = receiveImage(name)
  #file_name2 = receiveImage(name1)
  #image_data = name
  #image = Image.open(io.BytesIO(image_data))
  #image.show()



  #file_name1 = raw_input("Enter name of the first image file:")
  #file_name2 = raw_input("Enter name of the second image file:")
  
  

  image1 = fr.load_image_file(file_name1)
  image2 = fr.load_image_file(file_name2)

  print('After File Load Image function')
  image1_encoding = fr.face_encodings(image1)[0]
  image2_encoding = fr.face_encodings(image2)[0]
  
  results = fr.compare_faces([image1_encoding], image2_encoding)
  
  if results[0] == True:
    return "Match"
  else:
   return "No Match"



@app.route("/p")

 

def main():
 
  args = sys.argv[1:]
  
  file_name1 = args[0]
  file_name2 = args[0]
 
  #file_name1 = raw_input("Enter name of the first image file:")
  #file_name2 = raw_input("Enter name of the second image file:")
  
  image1 = fr.load_image_file(file_name1)
  image2 = fr.load_image_file(file_name2)
  
  image1_encoding = fr.face_encodings(image1)[0]
  image2_encoding = fr.face_encodings(image2)[0]
  
  results = fr.compare_faces([image1_encoding], image2_encoding)
  
  if results[0] == True:
    return "Match"
  else:
   return "No Match"
 
 
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
  app.run(debug=True)
  app.run(host='0.0.0.0', port=80)
  
