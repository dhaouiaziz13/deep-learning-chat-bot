
from flask import Flask, render_template, request
# from chatbot import get_response
import chatbot

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.res(userText))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
