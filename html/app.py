from flask import Flask
from flask import render_template
app = Flask(__name__)

#传递参数con
#html界面用{{con}}表示
def release():
    con=1
    return con

@app.route('/')

def index():
    return render_template('index.html',re=release)

if __name__ == "__main__":
    app.run()

