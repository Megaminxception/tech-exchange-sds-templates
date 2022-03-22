# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from model import check_capitals


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/helpme', methods=["GET","POST"])
def helpme():
    if request.method == "GET":
        return redirect("/")

    answers = {"NY": request.form['New York'], "CA": request.form['California'],
               "WA": request.form['Washington'], "GA": request.form['Georgia'],
               "TX": request.form['Texas']}
    for answer in answers.keys():
        if answers[answer] == "":
            return render_template('results.html', empty=True)
    
    return render_template('results.html', results=check_capitals(answers))
