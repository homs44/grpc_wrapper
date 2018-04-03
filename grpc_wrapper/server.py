from grpc_wrapper.pb2 import Transfer_pb2_grpc, Transfer_pb2
import grpc
from concurrent import futures
from grpc_wrapper.utils import protobuf_to_dict, dict_to_protobuf


class TransferServer(Transfer_pb2_grpc.TransferServicer):
    def __init__(self, model):
        self.model = model

    def predict(self, request, context):
        input = protobuf_to_dict(request.input)
        output = self.model.predict(input)
        return Transfer_pb2.PredictResponse(output=dict_to_protobuf(output))


class BaseModel:

    def predict(self, input):
        pass


def create_server(model, ip="[::]", port=50051, max_workers=5):
    if type(model) == BaseModel:
        raise TypeError

    if type(port) != int:
        raise TypeError

    if type(ip) != str:
        raise TypeError

    if type(max_workers) != int:
        raise TypeError

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    Transfer_pb2_grpc.add_TransferServicer_to_server(TransferServer(model), server)
    ip_port = ip+":"+str(port)
    server.add_insecure_port(ip_port)
    return server







