from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='text-align: center;'>Hello World!</h1> \
        <p>This is a paragraph</p>"


def make_bold(function):

    def wrapper():
       return f"<b>{function()}</b>"
    return wrapper

def underline(function):

    def  wrapper():
        return f"<u>{function()}</u>"
    return wrapper

def emphasis(function):

    def  wrapper():
        return f"<em>{function()}</em>"
    return wrapper



@app.route("/bye")
@emphasis
@underline
@make_bold
def bye():
    return "Bye!"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
