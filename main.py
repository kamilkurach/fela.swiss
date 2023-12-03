from flask import Flask, render_template, request, redirect
from threading import Timer
import subprocess

app = Flask(__name__)

# params
command = ["pwd"]
ip = 'http://127.0.0.1:5000/'

@app.route("/")
def fela_screen():
    return render_template("index.html")

@app.route("/info", methods=['POST'])
def info_screen():
    return redirect("/")

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
            print("*** Message: subprocess error. Redirecting.. ***")
            return redirect("/")
        
def subprocess_command():
    print("*** Message: run subprocess command ***")
    spo = subprocess.run(command, capture_output=True)  
    print(spo.stdout)

def open_browser():
    # set default page to http://127.0.0.1:5000/
    # exit kiosk alt+F4
    try:
        subprocess.run(["chromium-browser", "--kiosk"]) 
    except Exception as e:
        print(e) 

def main():
    Timer(1, open_browser).start()
    app.run(port=5000)
    
if __name__== "__main__":
    main()
