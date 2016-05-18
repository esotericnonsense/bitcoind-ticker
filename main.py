import gevent.monkey as monkey
monkey.patch_all()

import gevent
import gevent.queue

import sys

import zmq.green as zmq

import binascii
import datetime

import config
import bitcoinrpc.authproxy

class termcolors:
    yellow = '\033[33m'
    cyan = '\033[36m'
    reset = '\033[0m'

def zmqpoller(hash_queue):
    while True:
        msg = socket.recv_multipart()
        topic = str(msg[0])
        body = msg[1]
        hash_queue.put(binascii.hexlify(body))

def rpcrequester(hash_queue, cfg):
    rpcurl = "{}://{}:{}@{}:{}".format(
        cfg["protocol"],
        cfg["rpcuser"],
        cfg["rpcpassword"],
        cfg["rpcip"],
        cfg["rpcport"],
    )
    print "Connecting to bitcoind RPC..."
    handle = bitcoinrpc.authproxy.AuthServiceProxy(rpcurl, None, 500)
    print "Connected. Requesting 'getinfo'..."

    # Check that it's working...
    getinfo = handle.getinfo()
    print "Success."
    print

    total = 0
    start_time = datetime.datetime.utcnow()

    for txhash in hash_queue:
        sys.stdout.write("\r")
        tx = handle.getrawtransaction(txhash, 1)
        try:
            outs = [(vout["scriptPubKey"]["addresses"][0], vout["value"]) for vout in tx["vout"]] 
            for out in outs:
                print "{}{}{} {} received {}{}BTC{}".format(
                    termcolors.yellow, datetime.datetime.utcnow().isoformat(), termcolors.reset,
                    out[0],
                    termcolors.cyan, out[1], termcolors.reset
                )
                total += out[1]
        except KeyError:
            print "odd tx"
            print tx

        total_time = datetime.datetime.utcnow() - start_time
        print
        sys.stdout.write("Total transferred: {}{}BTC{} in {}s".format(
            termcolors.cyan, total, termcolors.reset,
            total_time.total_seconds()))
        sys.stdout.flush()

def process_config(cfg):
    assert "rpcuser" in cfg
    assert "rpcpassword" in cfg

    if "rpcip" not in cfg:
        cfg["rpcip"] = "localhost"

    if "rpcport" not in cfg:
        if "testnet" in cfg:
            cfg["rpcport"] = 18332
        else:
            cfg["rpcport"] = 8332

    if "protocol" not in cfg:
        cfg["protocol"] = "http"

    return cfg

if __name__ == "__main__":
    cfg = config.read_file("bitcoin.conf")
    cfg = process_config(cfg)

    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt(zmq.SUBSCRIBE, "hashtx")
    socket.connect("tcp://127.0.0.1:10000")

    hash_queue = gevent.queue.Queue()
    zmq_process = gevent.spawn(zmqpoller, hash_queue)

    try:
        rpcrequester(hash_queue, cfg)
    finally:
        socket.close()
        context.term()
