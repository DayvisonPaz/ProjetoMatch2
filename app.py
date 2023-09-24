from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/users")
def get_users():
    return 'Hello Wonderful People!'

if __name__ == "__main__":
    app.run()
    
