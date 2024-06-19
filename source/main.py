from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        page_title = "Интернет магазин"
        return render_template("index.html", page_title=page_title)
    return app

if __name__ == "__main__":
    create_app().run(debug=True)
