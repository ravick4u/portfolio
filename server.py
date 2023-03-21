from flask import Flask,render_template,url_for,request,redirect
import csv

app = Flask(__name__)
print(__name__)

''' hello world'''
@app.route('/')
def default():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/thankyou.html')
def thankyou():
    return render_template('thankyou.html')

def writetofile(data):

    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    with open('./database.txt','a') as databasefile:
        databasefile.writelines(f"{email},{subject},{message}")

def writetocvs(data):

    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    with open('./database.csv',mode='a',newline='') as databasefile:
        csv_writer = csv.writer(databasefile, delimiter=",",quotechar='"', quoting=csv.QUOTE_MINIMAL)

        fieldnames = ['email', 'subject','message']
        csv_writer = csv.DictWriter(databasefile, fieldnames=fieldnames)

        #csv_writer.writeheader()
        csv_writer.writerow({'email':email, 'subject':subject,'message': message})

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        try:
            print(request.form.to_dict())
            #return f"email have been sent to {request.form['email']} subject: '{request.form['subject']}'; message: '{request.form['message']}'"
            writetocvs(request.form.to_dict())
            return redirect('/thankyou.html')
        except:
            return 'something went wrong'
    else:
        return 'invalid method'
    