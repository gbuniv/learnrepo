import sys
from hello import HelloService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloService.Client(protocol)
    transport.open()

    print "client - say"
    msg = client.test("Hello!(test)")
    print "server - " + msg

    transport.close()

except Thrift.TException, ex:
    print "%s" % (ex.message)
