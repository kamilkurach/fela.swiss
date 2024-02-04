from flask import Flask, render_template, request, redirect
from threading import Timer
import subprocess
import sys
import re 
import os
import socket
import time

app = Flask(__name__)

# params
command = []
info_command = []
ip_command = []
try:
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            command.append(sys.argv[i])
    else:
        command = ["/home/root/gebe-imx/print.sh"]
        info_command = ["/home/root/skrypty/render.sh"]
        ip_command = ["/home/root/skrypty/ip.sh"] 
except IndexError:
    command = ["/home/root/gebe-imx/print.sh"]
    info_command = ["/home/root/skrypty/render.sh"]
    ip_command = ["/home/root/skrypty/ip.sh"] 

@app.route("/")
def fela_screen():
    return render_template("index.html")

@app.route("/render", methods=['POST'])
def info_screen():
    if request.method == 'POST':
        try:
            Timer(1, subprocess_info_command).start()
            return redirect("/")
        except Exception as e:
            print(e)
            return redirect("/")

@app.route("/tickets", methods=['POST'])
def test_tickets():
    if request.method == 'POST':
        try:
            Timer(1, subprocess_command).start()
            return render_template("anim.html")
        except Exception as e:
            print("*** Message: subprocess error. Redirecting.. ***")
            return redirect("/")

@app.route("/info", methods=['POST'])
def info():
    ip = get_ip()
    print("test", ip)
    if request.method == 'POST':
        return render_template("info.html", value=ip)

@app.route("/ip")
def get_ip():
    try:
        spo = subprocess.run(ip_command, capture_output=True)
        # print(spo.stdout.decode())
        return str(spo.stdout.decode())
    except Exception as e:
        print(e)


def subprocess_info_command():
    print("*** Message: run subprocess command ***")
    try:
        spo = subprocess.run(info_command, capture_output=True)  
        print(spo.stdout)
    except Exception as e:
        print(e)
        
def subprocess_command():
    print("*** Message: run subprocess command ***")
    try:
        spo = subprocess.run(command, capture_output=True)
        print(spo.stdout)
    except Exception as e:
        print(e)

@app.route("/anim")
def animation():
    return render_template("anim.html")

def open_browser():
    # set default page to http://127.0.0.1:5000/
    # exit kiosk alt+F4
    try:
        subprocess.run(["chromium", "0.0.0.0:5000"]) 
    except Exception as e:
        print(e) 

def main():
    Timer(1, open_browser).start()
    app.run(host='0.0.0.0', port=5000)
    
if __name__== "__main__":
    main()
