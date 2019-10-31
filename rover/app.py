"""
CONSOLE COMMANDS:
> activate dashboard
> cd C:\Users\alokj\Desktop\Rover
> python app.py  [Keep deleting __pycache__ before every run]
"""

# Importing external libraries:
from flask import Flask, render_template, request, url_for, redirect, flash, session, abort
from pyfladesk import init_gui

# Importing internal dependencies:
from configurations import config, BaseConfig

# Initiating our primary Flask application:
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(BaseConfig)

from routes import *

# Run Application:
if __name__ == "__main__":
    print(u"[INFO] Launching Data Rover desktop application...")
    init_gui(app, port=5000,  width=800, height=600, window_title=" Data Rover", icon="appicon.png", argv=None)
