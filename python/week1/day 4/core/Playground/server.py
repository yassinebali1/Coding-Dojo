from  flask import Flask , render_template

app= Flask(__name__)

@app.route('/play')
def dispay_play():
    return render_template('index.html',x=3)


@app.route('/play/<int:x>')
def display_playy(x):
    return render_template('index.html',x=x)

@app.route('/play/<int:x>/<color>')
def display_color(x,color):
    return render_template('index.html',x=x , color=color)




if __name__=="__main__":
    app.run(debug=True)
