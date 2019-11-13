# Importing required external libraries:
import os
import json
import pandas as pd
from werkzeug import secure_filename
from datetime import datetime, timedelta
from flask import Flask, render_template, request, url_for, redirect, flash, session, abort
from app import app

# Importing internal dependencies:
from forms import *
from extensions import *
from analysis import *


# Landing Page for Dataset Upload:
@app.route("/", methods=["GET", "POST"])
def index():
    print(u"[INFO] Launching dataset upload page...")
    form = DatasetUploadForm()
    if form.validate_on_submit():
        data_file = secure_filename(form.new_dataset.data.filename)
        if allowed_file(data_file):
            # Check previously uploaded dataset file & delete them, if exists:
            if find_local_file(("new_dataset.csv"), "data/datasets/") != []:
                for item in (find_local_file(("new_dataset.csv"), "data/datasets/")):
                    os.remove(item)
            # Save newly uploaded dataset:
            form.new_dataset.data.save("data/datasets/" + "new_dataset" + ".csv")
            # Generate success prompt & redirecting to overview page:
            return redirect(url_for("analysis_dash"))
        else:
            flash(u"Kindly re-attempt as per guidelines!")
    return render_template("index.html", form=form)


# Primary Data Analysis Dashboard:
@app.route("/analysis_dash", methods=["GET", "POST"])
def analysis_dash():
    print(u"[INFO] Launching dataset preview page...")
    preview = dataset_preview()
    col_list = preview.columns
    pivot_data = request.get_json()
    if pivot_data is not None:
        pFilters = pivot_data["filterArray"]
        pCols = pivot_data["colArray"]
        pRows = pivot_data["rowArray"]
        pVals = pivot_data["valArray"]
        # Generating pivot table:
        preview = pd.pivot_table(preview, index=pRows, columns=pCols, values=pVals)
    preview = preview.to_html(classes="table table-striped", na_rep="NULL", table_id="data_pivot")
    return render_template("analysis_dash.html", data=preview, col_list=col_list)
