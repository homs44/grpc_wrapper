#!/bin/sh

python -m grpc_tools.protoc -I./grpc_wrapper/protos --python_out=. --grpc_python_out=. ./grpc_wrapper/protos/Transfer.proto
python -m grpc_tools.protoc -I./grpc_wrapper/protos --python_out=. --grpc_python_out=. ./grpc_wrapper/protos/Data.proto
