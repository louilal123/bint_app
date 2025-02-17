@app.route('/profile')
def profile():
    user_info = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "location": "Somewhere, Earth"
    }
    return render_template('profile.html', user=user_info)
