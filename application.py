from flask import Flask, redirect, url_for, request, render_template, jsonify, flash, send_file, Blueprint


application = Flask(__name__)
application.secret_key = "super secret key" #DO NOT LEAVE THIS LIKE THIS

@application.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
   website_url='involuntaryCTF:5000'
   application.config['SERVER_NAME']=website_url
   application.run(debug=True)

