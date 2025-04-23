from flask import Flask
hello = Flask(__name__)

@hello.route('/')
def hello_world():
    return "Hello, Abhi!"

if __name__ == "__main__":
    hello.run(host="0.0.0.0", debug=True)