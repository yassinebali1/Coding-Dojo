from flask import Flask, render_template,redirect,request,session
from usermodel import Users
app=Flask(__name__)
app.secret_key="password123"


@app.route('/users')
def get():
    return render_template('usernew.html',users=Users.get_all())

@app.route('/users/new')
def users_new():
    return render_template('users.html')

@app.route('/create/new',methods=["POST"])
def newusers():
    new_users={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
        }
    Users.create_users(new_users)
    return redirect("/users")
if __name__ == "__main__":
    app.run( debug = True)