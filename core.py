import device
import application
import threading
import resource
import linke_vision_server

lock = threading.Lock()

class BackendCore:
    def __init__(self):
        # self.devices = []
        # self.applications = []
        pass
    
    def start(self):
        grpc_server = threading.Thread(target=linke_vision_server.serve)
        grpc_server.daemon = True
        grpc_server.start()

        self.load_devices()

    def main_loop(self):
        while True:
            print(resource.devices)

    def load_devices(self):
        pass

def run():
    core = BackendCore()
    core.start()

    thread = threading.Thread(target=core.main_loop)
    thread.daemon = True
    thread.start()
    


