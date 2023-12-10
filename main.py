from flask import Flask, render_template, request, redirect
from threading import Timer
import subprocess
import sys

app = Flask(__name__)

# params
command = []
try:
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            command.append(sys.argv[i])
    else:
        command = ["pwd"]
except IndexError:
    command = ["pwd"]

@app.route("/")
def fela_screen():
    return render_template("index.html")

@app.route("/info", methods=['POST'])
def info_screen():
    return redirect("/")

@app.route("/tickets", methods=['POST'])
def test_tickets():
    if request.method == 'POST':
        try:
            Timer(1, subprocess_command).start()
            return render_template("tickets.html")
        except Exception as e:
            print("*** Message: subprocess error. Redirecting.. ***")
            return redirect("/")
        
def subprocess_command():
    print("*** Message: run subprocess command ***")
    try:
        spo = subprocess.run(command, capture_output=True)  
        print(spo.stdout)
    except Exception as e:
        print(e)

def open_browser():
    # set default page to http://127.0.0.1:5000/
    # exit kiosk alt+F4
    try:
        subprocess.run(["chromium-browser", "--kiosk", "--app=http://127.0.0.1:5000/"]) 
    except Exception as e:
        print(e) 

def main():
    Timer(1, open_browser).start()
    app.run(host='0.0.0.0', port=5000)
    
if __name__== "__main__":
    main()
