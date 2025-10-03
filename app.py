from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from werkzeug.utils import secure_filename
import ffmpeg
import os
import json
from datetime import datetime

app = Flask(__name__)



@app.route('/')
def index():
    # return "Hello"
    return render_template('index.html')

@app.route('/user/<username>')
def show_user(username):
    return f"User: {username}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)