from flask import Flask, render_template, request
import webbrowser


app = Flask(__name__)

# Hi sunny
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:2000/')
    app.run(debug=True, port=2000)
