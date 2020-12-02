from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style='color: red'>hello I'm here!!</h1>"

@app.route('/<color>/<num>')
@app.route('/<color>')
def color(color, num=10):
    print(color)
    html_str = ""

    print(f"Variable num's type: {type(num)}")
    print("value: ", num)

    for i in range(int(num)):
        html_str += f"<h1 style='color: {color}'>hello I'm here!!</h1>"

    return html_str

if __name__ == "__main__":
    app.run(debug=True)