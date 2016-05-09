import gevent.monkey as monkey
monkey.patch_all()

import gevent
import gevent.queue

import zmq.green as zmq

import binascii
import datetime

import bitcoinrpc.authproxy

def zmqpoller(hash_queue):
    while True:
        msg = socket.recv_multipart()
        topic = str(msg[0])
        body = msg[1]
        hash_queue.put(binascii.hexlify(body))

def rpcrequester(hash_queue):
    with open("bitcoin.conf", "r") as f:
        rpcuser = f.readline().strip("\n")
        rpcpassword = f.readline().strip("\n")

    rpcurl = "http://{}:{}@127.0.0.1:8332".format(rpcuser, rpcpassword)
    handle = bitcoinrpc.authproxy.AuthServiceProxy(rpcurl, None, 500)

    # Check that it's working...
    getinfo = handle.getinfo()

    for txhash in hash_queue:
        tx = handle.getrawtransaction(txhash, 1)
        try:
            outs = [(vout["scriptPubKey"]["addresses"][0], vout["value"]) for vout in tx["vout"]] 
            for out in outs:
                print "{} {} received {}BTC".format(datetime.datetime.utcnow().isoformat(), out[0], out[1])
        except KeyError:
            print "odd tx"
            print tx

        print

if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt(zmq.SUBSCRIBE, "hashtx")
    socket.connect("tcp://127.0.0.1:10000")

    hash_queue = gevent.queue.Queue()
    zmq_process = gevent.spawn(zmqpoller, hash_queue)

    try:
        rpcrequester(hash_queue)
    finally:
        socket.close()
        context.term()
