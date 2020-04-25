# to get flask app to work, make sure you are in web_server folder
# type in bash: export FLASK_APP=server.py. A blank line should appear after the line with you hit enter
# type in flask run
# you should get a warning in red saying do not use in development
# a website will pop up. http://127.0.0.1:5000. Do not ctrl+c this link, you will close the connection
# insead hit ctrl and click on the link. It will open your website with you function
# everytime you make changes, you have to cancel the connection (ctrl+c) and rerun flask app
# or instead of export FLASK_APP=server.py, run export FLASK_ENV=development. This will turn the debugger mode off
# so you can make changes without rerunning


from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again!'
