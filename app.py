from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/profile')
def profile():
    return render_template('dashboard.html')  

if __name__ == '__main__':
    app.run(debug=True)
