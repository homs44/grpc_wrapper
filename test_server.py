from grpc_wrapper.server import create_server, BaseModel
import time


class Model(BaseModel):
    def __init__(self):
        self.version = 1

    def send(self, input):
        print("inputs" + str(input))
        return [{"aaaa" : "333"}, {"bbb" : "vvvv"}]

def test():
    model = Model()
    server = create_server(model)
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    test()
