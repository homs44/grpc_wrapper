#gRPC Wrapper
Simple lib for gRPC Server and Client

Installing
```
pip install grpc_wrapper
```

Server Example
```
from grpc_wrapper.server import create_server, BaseModel

class YourModel(BaseModel):
    def __init__(self):
        #initialize for your model

    def predict(self,input):

        # get data from input like below
        value = input[key]

        output = {}
        return output

```

Installing
```
pip install grpc_wrapper
```

