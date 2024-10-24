from flask import Flask, rendertemplate
app = Flask(name) 


@app.route('/')

def hello():
    return "Hello world!"

@app.route('/dojo')

def dojo():
    return "Dojo!"

@app.route('/say/<name>')

def hi(name):
    return "Hi "+name

@app.route('/repeat/<int:numb>/<word>')

def repeat(numb,word):
    return (word +" " )*numb




if name=="_main":
    app.run(debug=True)