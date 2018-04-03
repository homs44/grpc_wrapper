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

    def predict(self,input):

        # get data from input like below
        value = input[key]

        output = {}
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
Your model should inherit BaseModel and implement predict function

Client Example
-------------
```
from grpc_wrapper.client import create_client

def run():
    client = create_client(ip="localhost", port=50051)
    input = {
        "input_a": 1,
        "input_b": 0.3,
        "input_c": "value_c",
    }
    result = client.predict(input)
```
