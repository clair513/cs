import os
import json
from werkzeug import secure_filename
from datetime import datetime, timedelta
from flask import Flask, render_template, request, url_for, redirect, flash, session, abort
from app import app

@app.route('/')
def index():
    return render_template('index.html')
