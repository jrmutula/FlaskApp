from flask import Flask, render_template
from Bat import app

@app.route("/")
def main():
    return render_template("index.html")
