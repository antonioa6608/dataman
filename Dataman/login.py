#Yashua Mcdoual
#Alexander Antonio
#CTS-285-0001
#10/1/2023


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
   return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    if username == 'username' and password == 'password':
        return 'Login Successful!'
    else:
        return 'Login Failed!'

    return render_template('login.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

