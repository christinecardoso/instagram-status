from flask import Flask, render_template, request
from insta_login import InstaLogin

app = Flask('instastatus')

insta = False # variable used to indicate that user is logged-in


@app.route('/', methods=['GET', 'POST'])
def main():
    # function shows the login form if not logged in
    # and if already logged in, it will render the main screen.
    global insta
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            # checks whether user is already logged in.
            if not insta:
                insta = InstaLogin(username, password)
            flist = insta.get_followers()
            felist = insta.get_followings()
            selfpr = insta.get_self_profile()
            return render_template('index.html',
                                   flist=flist,
                                   felist=felist,
                                   length=len(flist),
                                   felength=len(felist),
                                   username=username,
                                   profiledata=selfpr)
        except:
            return render_template('login.html', error=True, text="Invalid Username or Password!")


@app.route('/unf', methods=['POST'])
def unf():
    # Handles unfollow buttens. requests will be sent using POST
    unf = request.form['unfollow']
    insta.unfollow(unf)

app.run(debug=True)
