# from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import threading
import argparse
import datetime
# import imutils
import time
# from cv2 import cv2
import core

core.run()

app = Flask(__name__)
bootstrap = Bootstrap(app)
 
time.sleep(2.0)

@app.route("/")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--ip", type=str, default="0.0.0.0",
		help="ip address of the device")
	ap.add_argument("-o", "--port", type=int, default=18000,
		help="ephemeral port number of the server (1024 to 65535)")

	args = vars(ap.parse_args())

	app.run(host=args["ip"], port=args["port"], debug=True,
		threaded=True, use_reloader=False)
