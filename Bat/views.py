from flask import Flask

@app.route("/")
def main():
    return "Welcome!"
