from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/prev]')
def profile():
    return render_template('prev.html')  

if __name__ == '__main__':
    app.run(debug=True)
