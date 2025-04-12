from flask import Flask, redirect, url_for, request, render_template, jsonify, flash, send_file, Blueprint
import gpxpy
import re

application = Flask(__name__)
application.secret_key = "super secret key" #DO NOT LEAVE THIS LIKE THIS

application.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
application.config['UPLOAD_EXTENSIONS'] = ['.gpx']

@application.route('/')
def home():
    return render_template('index.html',elevation="Submit gpx file and coordinates to find out")

@application.route('/',methods=['POST'])
def file_upload():
    uploaded_file = request.files['file']
    gpx = gpxpy.parse(uploaded_file)
    file=uploaded_file
    for line in request.files.get('file'):
        if re.search("(!ENTITY)",str(line)) and re.search("(file:/)",str(line)) and not re.search("(file:/flag)",str(line)):
            print(line)
            return render_template('index.html',elevation="You're on the right track the file you're looking for is at /flag")


    longitude = request.form.get('longitude')
    latitude = request.form.get('latitude')

    if longitude.replace('.','',1).isdigit()==False or latitude.replace('.','',1).isdigit()==False:
        return render_template('index.html',elevation="Must enter valid longitude and latitude")
    elif len(longitude)<7 or len(latitude)<7:
        return render_template('index.html',elevation="Must enter a more precise longitude and latitude")

    elevation=None
    comment=None
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if point.latitude==float(latitude) and point.longitude==float(longitude):
                    comment=point.comment
                    elevation=point.elevation


    if elevation==None:
        return render_template('index.html',elevation="Longitude and latitude not covered in the map you entered")

    return render_template('index.html',elevation=f"{elevation}m",comment=f"Your comments at this point were '{comment}'")

if __name__ == '__main__':
   website_url='abitofmapreading.involuntaryCTF:5000'
   application.config['SERVER_NAME']=website_url
   application.run(debug=True)

