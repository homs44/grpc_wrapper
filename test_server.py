from grpc_wrapper.server import create_server, BaseModel
import time


class Model(BaseModel):
    def __init__(self):
        self.version = 1

    def predict(self, input):
        print("input" + str(input))

        output = {
            "output_1": input["input_1"]*3,
            "output_2": input["input_2"]*3,
            "output_3": input["input_3"]*3
        }
        print("output" + str(output))
        return output


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
