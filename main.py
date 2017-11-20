from flask import Flask, render_template, request
from insta_login import InstaLogin

app = Flask('instastatus')
insta = False


@app.route('/', methods=['GET', 'POST'])
def login():
    global insta
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        if request.form['username']:
            username = request.form['username']
            password = request.form['password']
            try:
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
                return("Username or password is wrong!")


@app.route('/unf', methods=['POST'])
def unf():
    unf = request.form['unfollow']
    insta.unfollow(unf)
    return render_template('unfollow.html', unf=unf)

app.run(debug=True)
