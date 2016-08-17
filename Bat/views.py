from flask import Flask
from Bat import app

@app.route("/")
def main():
    return "Welcome!"
