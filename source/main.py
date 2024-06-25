from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def index():
    page_title = "Интернет магазин"
    return render_template("index.html", page_title=page_title)


@app.route('/<name>')
def new_1(name):
    page_title = 'Новая страница'
    return render_template('new_1.html', page_title=name, r=1234)

        

if __name__ == "__main__":
    app.run(debug=True)
