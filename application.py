from flask import Flask, redirect, url_for, request, render_template, jsonify, flash, send_file, Blueprint
import gpxpy

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
    longitude = request.form.get('longitude')
    latitude = request.form.get('latitude')

    if longitude.replace('.','',1).isdigit()==False and latitude.replace('.','',1).isdigit()==False:
        return render_template('index.html',elevation="Must enter valid longitude and latitude")
    elif len(longitude)<7 or len(latitude)<7:
        return render_template('index.html',elevation="Must enter a more precise longitude and latitude")

    gpx = gpxpy.parse(uploaded_file)
    elevation=None
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if round(point.latitude,4)==round(float(latitude),4) and round(point.longitude,4)==round(float(longitude),4):
                    elevation=round(point.elevation,2)

    if elevation==None:
        return render_template('index.html',elevation="Longitude and latitude not covered in the map you entered")

    return render_template('index.html',elevation=f"{elevation}m")

if __name__ == '__main__':
   website_url='abitofmapreading.involuntaryCTF:5000'
   application.config['SERVER_NAME']=website_url
   application.run(debug=True)

