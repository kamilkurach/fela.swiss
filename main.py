import webbrowser
from flask import Flask, render_template
from threading import Timer

app = Flask(__name__)

# params
command = None
ip = 'http://127.0.0.1:5000/'
chrome_path = '/usr/bin/chromium-browser'

@app.route("/")
def fela_screen():
    return render_template("index.html")

@app.route("/update")
def update_params():
    pass

def open_browser():
    webbrowser.get(chrome_path).open(ip)
    
def main():
    Timer(1, open_browser).start()
    app.run(port=5000)
    
if __name__== "__main__":
    main()
