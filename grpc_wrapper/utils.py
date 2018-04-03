from grpc_wrapper.pb2 import Transfer_pb2


def protobuf_to_dict(obj):
    result = {}
    for i in obj.keys():
        result[i] = get_dict(obj[i])
    return result


def get_dict(value):
    if value.type == 2:
        return value.int_val
    elif value.type == 3:
        return value.int64_val
    elif value.type == 4:
        return value.float_val
    elif value.type == 5:
        return value.double_val
    elif value.type == 6:
        return value.string_val
    elif value.type == 7:
        return value.bool_val
    elif value.type == 8:
        return value.byte_val
    elif value.type == 9:
        return value.uint32_val
    elif value.type == 10:
        return value.uint64_val
    else:
        return None


def dict_to_protobuf(dic):
    result = {}
    for i in dic.keys():
        value = get_proto(dic[i])
        if type(value) is not None:
            result[i] = value

    return result


def get_proto(value):
    if type(value) == str:
        return Transfer_pb2.Data__pb2.Data(type=6, string_val=value)
    elif type(value) == int:
        return Transfer_pb2.Data__pb2.Data(type=2, int_val=value)
    elif type(value) == float:
        return Transfer_pb2.Data__pb2.Data(type=5, double_val=value)
    elif type(value) == float:
        return Transfer_pb2.Data__pb2.Data(type=5, double_val=value)
    elif type(value) == bool:
        return Transfer_pb2.Data__pb2.Data(type=7, bool_val=value)
    elif type(value) == bytes:
        return Transfer_pb2.Data__pb2.Data(type=8, byte_val=value)
    else:
        return None
