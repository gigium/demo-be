import os
from flask import Flask
from flask import render_template
import socket
import random

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "pink": "#be2edd",
    "yellow": "#ffff00",
    "white": "#ffffff",
    "purple": "#7d3c98"
}




color = random.choice(list(color_codes.keys()))


@app.route("/")
def main():
    #return 'Hello'
    print(color)
    return (color_codes[color])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
