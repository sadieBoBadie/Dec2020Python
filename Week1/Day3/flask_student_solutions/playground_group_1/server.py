### Group who worked together ###
# Spencer	Huyck
# Joseph	Lee
# Michael	Shin
# Victor	Gargurevich
# Michael	Towson
# Rebeca	Gonzalez

from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/play')
def play():
    return render_template("index.html", number=3)

@app.route('/play/<int:number>')
def playNum(number):
    return render_template("index.html", number=number)

@app.route('/play/<int:number>/<color>')
def playNumColor(number,color):
    return render_template("index.html", number=number,color=color)

if __name__=="__main__":  
    app.run(debug=True)