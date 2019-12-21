import device
import application
import threading

all_devices = []
all_applications = []
lock = threading.Lock()



def main_loop():
    while True:
        a = 1


def run():
    thread = threading.Thread(target=main_loop)
	thread.daemon = True
	thread.start()
    


