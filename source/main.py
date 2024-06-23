from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home_page():
    page_title = "Интернет магазин"
    return render_template("home_page.html", page_title=page_title)


@app.route("/login")
def login():
    page_title = "Авторизация"

    return render_template("login.html", page_title=page_title)


@app.route("/basket")
def basket():
    page_title = "Корзина"
    return render_template("basket.html", page_title=page_title)


if __name__ == "__main__":
    app.run(debug=True)
