from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,name,message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('index.html')
        except:
            return 'failed to send message :('
    else:
        return 'something went wrong'
