import grpc

import random
import string

# import the generated classes
import inverter_pb2
import inverter_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = inverter_pb2_grpc.InverterStub(channel)

# create a valid request message
string = inverter_pb2.String(value=''.join(
    random.choice(string.ascii_letters) for i in range(random.randint(2, 20))))

# make the call
response = stub.Invert(string)

# et voilà
print(response.value)