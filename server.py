import grpc
from concurrent import futures
import time

# import the generated classes
import inverter_pb2
import inverter_pb2_grpc

# import the original inverter.py
import inverter

# create a class to define the server functions, derived from
# inverter_pb2_grpc.inverterServicer
class InverterServicer(inverter_pb2_grpc.InverterServicer):

    # inverter.invert is exposed here
    # the request and response are of the data type
    # inverter_pb2.String
    def Invert(self, request, context):
        response = inverter_pb2.String()
        response.value = inverter.invert(request.value)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_inverterServicer_to_server`
# to add the defined class to the server
inverter_pb2_grpc.add_InverterServicer_to_server(
        InverterServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)