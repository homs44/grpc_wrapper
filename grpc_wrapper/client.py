from grpc_wrapper.pb2 import Transfer_pb2_grpc, Transfer_pb2
import grpc
from grpc_wrapper.utils import protobuf_to_dict, dict_to_protobuf


class TransferClient:
    def __init__(self, ip="localhost", port=50051):
        channel = grpc.insecure_channel(ip+":"+str(port))
        self.stub = Transfer_pb2_grpc.TransferStub(channel)

    def predict(self, input):
        input_wrapper = dict_to_protobuf(input)
        result = self.stub.predict(Transfer_pb2.PredictRequest(input=input_wrapper))
        return protobuf_to_dict(result.output)


def create_client(ip="localhost", port=50051):
    return TransferClient(ip, port)

