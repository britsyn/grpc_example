import grpc

# import the generated classes
import inverter_pb2
import inverter_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = inverter_pb2_grpc.InverterStub(channel)

# create a valid request message
string = inverter_pb2.String(value='bethoven')

# make the call
response = stub.Invert(string)

# et voilà
print(response.value)