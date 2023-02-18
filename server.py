from flask_app import app
from flask import render_template, session, request, redirect
from flask_app.models.model_user import User

@app.route('/')
def index():
    return redirect("user")

@app.route('/user')
def users():
    return render_template("index.html", users=User.get_all())            

@app.route('/user/new')
def to_add_page():
    return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def add_user():
    print(request.form) 
    User.save(request.form)

    return redirect('/user')
    


if __name__ == "__main__":
    app.run(debug=True)
