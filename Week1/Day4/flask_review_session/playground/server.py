# imports
from flask import Flask, render_template
app = Flask(__name__)
print("file did run!")

@app.route('/')
@app.route('/play')
def index():
    print("index function!")
    return render_template("index.html")

@app.route('/play/<int:num>')
def boxes(num):
    print("boxes function!")
    print(type(num))
    return render_template("index.html", num=num)

@app.route('/play/<int:num>/<color>')
def color_boxes(num, color):
    print("***"*10)
    print(color)
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)