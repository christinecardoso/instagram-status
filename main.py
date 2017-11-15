from flask import Flask, render_template, request
from insta_login import InstaLogin
from sys import exit

username = ''
password = ''

if username and password:
    insta = InstaLogin(username, password)
else:
    print('Please set username/password first!')
    exit(1)

app = Flask("instastatus")


@app.route("/")
def main():
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


app.run(debug=True)
