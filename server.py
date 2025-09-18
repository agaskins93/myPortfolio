import os
from flask import Flask, render_template, request, redirect, send_from_directory
import csv
app = Flask(__name__)

# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)


@app.route("/")
def my_world():
    return render_template('index.html')

@app.route("/<string:page_name>")
def show_about(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            save_user_info_csv(data)
            return redirect('thankyou.html')
        except:
            return'something went wrong'
    else:
        return ('form not submitted')

def save_user_info(data):
    with open('database.txt' , mode='a') as my_file:
        my_file.write(f'\nEmail: {data["email"]}, Subject: {data["subject"]}, Message: {data["message"]}')
        return 'Database saved'

def save_user_info_csv(data):
    with open('database.csv' , mode='a', newline="") as my_file:
        csv.writer(my_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL).writerow([data['email'], data['subject'], data['message']])
        return 'Database saved'
