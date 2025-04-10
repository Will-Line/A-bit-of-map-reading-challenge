from flask import Flask, redirect, url_for, request, render_template, jsonify, flash, send_file, Blueprint
import gpxpy

application = Flask(__name__)
application.secret_key = "super secret key" #DO NOT LEAVE THIS LIKE THIS

application.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
application.config['UPLOAD_EXTENSIONS'] = ['.gpx']

@application.route('/')
def home():
    return render_template('index.html',elevation="Submit file and coordinates to find out")

@application.route('/',methods=['POST'])
def file_upload():
    uploaded_file = request.files['file']

    elevation=0
    return render_template('index.html',elevation=elevation)

if __name__ == '__main__':
   website_url='abitofmapreading.involuntaryCTF:5000'
   application.config['SERVER_NAME']=website_url
   application.run(debug=True)

