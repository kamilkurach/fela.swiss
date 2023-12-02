import webbrowser
from flask import Flask, render_template, request, redirect
from threading import Timer
import subprocess

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

@app.route("/print", methods=['POST'])
def test_print():
    if request.method == 'POST':
        try:
            Timer(1, subprocess_command).start()
            return render_template("index.html")
        except Exception as e:
            print("*** Message: subprocess error ***")
            return redirect("/")
        
def subprocess_command():
    print("*** Message: run subprocess command ***")
    spo = subprocess.run(["pwd"], capture_output=True)  
    print(spo.stdout)

def open_browser():
    webbrowser.get(chrome_path).open(ip)

def main():
    Timer(1, open_browser).start()
    app.run(port=5000)
    
if __name__== "__main__":
    main()
