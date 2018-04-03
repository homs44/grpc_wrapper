from grpc_wrapper.client import create_client

def test():
    client = create_client(ip="localhost", port=50051)
    input = {
        "input_1": 1,
        "input_2": 0.3,
        "input_3": 3,
    }
    inputs = [input, input]

    print("input" + str(input))
    result = client.send(inputs)
    print("output" + str(result))


if __name__ == "__main__":
    test()
