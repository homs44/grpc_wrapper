gRPC Wrapper
=============
Simple lib for gRPC Server and Client

Installing
-------------
```
pip install grpc_wrapper
```

Server Example
-------------
```
from grpc_wrapper.server import create_server, BaseModel
import time

class YourModel(BaseModel):
    def __init__(self):
        #initialize for your model

    def send(self,input):

        # input & output can be dictionary or array

        return output
        
def run():
    model = YourModel()
    server = create_server(model, ip="localhost", port=50051, max_workders=5)
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)

```
Your model should inherit BaseModel and implement send function

Client Example
-------------
```
from grpc_wrapper.client import create_client

def run():
    client = create_client(ip="localhost", port=50051)

    # input & output can be dictionary or array
    output = client.send(input)

```
