from grpc_wrapper.pb2 import Transfer_pb2_grpc, Transfer_pb2
import grpc
from concurrent import futures
from grpc_wrapper.utils import protobuf_to_dict, dict_to_protobuf


class TransferServer(Transfer_pb2_grpc.TransferServicer):
    def __init__(self, model):
        self.model = model

    def send(self, request, context):
        temp = []
        for item in request.inputs:
                item_wrapper = protobuf_to_dict(item.input)
                if item_wrapper is not None:
                    temp.append(item_wrapper)

        input = None

        if len(request.inputs) == 1:
            input = temp[0]
        else:
            input = temp

        result = self.model.send(input)
        output_wrappers = []
        try:
            if type(result) == dict:
                output_wrappers.append(Transfer_pb2.Response(output=dict_to_protobuf(result)))
            elif type(result) == list:
                output_wrappers = []
                for item in result:
                    print("%%%%"+str(item))
                    item_wrapper = dict_to_protobuf(item)
                    if item_wrapper is not None:
                        output_wrappers.append(Transfer_pb2.Response(output=item_wrapper))
        except Exception:
            output_wrappers = []
            print(str(Exception))

        return Transfer_pb2.ArrayResponse(outputs=output_wrappers)


class BaseModel:

    def send(self, input):
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







