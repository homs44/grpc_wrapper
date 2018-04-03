from grpc_wrapper.pb2 import Transfer_pb2_grpc, Transfer_pb2
import grpc
from grpc_wrapper.utils import protobuf_to_dict, dict_to_protobuf


class TransferClient:
    def __init__(self, ip="localhost", port=50051):
        channel = grpc.insecure_channel(ip+":"+str(port))
        self.stub = Transfer_pb2_grpc.TransferStub(channel)

    def send(self, input):
        input_wrappers = []
        try:
            if type(input) == dict:
                input_wrappers.append(Transfer_pb2.Request(input=dict_to_protobuf(input)))
            elif type(input) == list:
                for item in input:
                    input_wrapper = dict_to_protobuf(item)
                    if input_wrapper is not None:
                        input_wrappers.append(Transfer_pb2.Request(input=input_wrapper))
        except Exception:
            input_wrappers = []
            print(str(Exception))

        temp = self.stub.send(Transfer_pb2.ArrayRequest(inputs=input_wrappers))

        outputs = []
        for item in temp.outputs:
            item_wrapper = protobuf_to_dict(item.output)
            if item_wrapper is not None:
                outputs.append(item_wrapper)

        response = None

        if len(temp.outputs) == 1:
            response = outputs[0]
        else:
            response = outputs

        return response


def create_client(ip="localhost", port=50051):
    return TransferClient(ip, port)

