from concurrent import futures
import time
import math
import logging
import os

import grpc

import linke_vision_pb2
import linke_vision_pb2_grpc

import resource

count = 0

def display(DO4image):
    global count
    image = DO4image.image
    ext = image.extension  #".jpg"
    size = image.size
    image_bytes = image.bytes
    
    # add processing to here
    with open("./image/" + str(count) + ext, "wb") as f:
        f.write(image_bytes)
        f.flush()
    count += 1


class LinkeVisionServicer(linke_vision_pb2_grpc.LinkeVisionServicer):
    """Provides methods that implement functionality of linke vision server."""
    
    def __init__(self):
        pass
        #add global variables to here

    def ObjectDetection(self, request, context):
        start_time = time.time()
        display(request)
        print("server delay: ", time.time() - start_time)
        return linke_vision_pb2.Result(status=1)

    def ObjectDetectionStream(self, request_iterator, context):
        for request in request_iterator:
            display(request)
            yield linke_vision_pb2.Result(status=1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    linke_vision_pb2_grpc.add_LinkeVisionServicer_to_server(
        LinkeVisionServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

# class ObjectDetectionMessager:

if __name__ == '__main__':
    logging.basicConfig()
    serve()

    # construct the argument parser and parse command line arguments
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--ip", type=str, default="0.0.0.0",
    #     help="ip address of the device")
    # ap.add_argument("-o", "--port", type=int, default=18000,
    #     help="ephemeral port number of the server (1024 to 65535)")

    # args = vars(ap.parse_args())
    
    # tt = threading.Thread(target=get_video)
    # tt.daemon = True
    # tt.start()
    # time.sleep(3.0)
    # t = threading.Thread(target=detect, args=(model,))
    # t.daemon = True
    # t.start()
    
    # # start the flask app
    # app.run(host=args["ip"], port=args["port"], debug=True,
    #     threaded=True, use_reloader=False)
