from flask import Flask, render_template

app = Flask(__name__)

# This route will render the index.html file when the app is accessed at the root URL '/'
@app.route('/')
def index():
    return render_template('index.html')  # Automatically displays index.h

# Additional routes for other pages
@app.route('/prev')
def prev():
    return render_template('prev.html')  # Render prev.html when accessed at /prev

if __name__ == '__main__':
    app.run(debug=True)
