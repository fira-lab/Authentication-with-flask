from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Add your authentication logic here
    return 'Login successful'

@app.route('/signup', methods=['POST'])
def signup():
    fullname = request.form['fullname']
    email = request.form['email']
    password = request.form['signuppassword']
    # Add your sign-up logic here
    return 'Sign-up successful'
if __name__ == '__main__':
    app.run()