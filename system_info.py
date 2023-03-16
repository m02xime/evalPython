import platform
import socket
import cpuinfo
import os
import osconf
from flask import Flask, render_template

app = Flask(__name__)

class Systeme:
    def __init__(self):
        self.os = platform.system()
        self.kernel = platform.release()
        self.hostname = socket.gethostname()
        self.cpu = cpuinfo.get_cpu_info()["brand_raw"]
        self.architecture = platform.architecture()[0]


@app.route("/")
def index():
    system = Systeme()
    return render_template("index.html", system=system)

if __name__ == "__main__":
    app.run(debug=True)
