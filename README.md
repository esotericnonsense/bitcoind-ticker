# bitcoind-ticker

A very basic demo of the zmqpubhashtx functionality in bitcoind.

## NOTE - this repository is no longer maintained.

## Example output

```
Connecting to bitcoind RPC...
Connected. Requesting 'getinfo'...
Success.

2016-05-09T15:14:06.223603 1CGu2NZGTBHwomAync9YUM2ANyahastwDt received 0.02178459BTC
2016-05-09T15:14:06.223754 18Z1CMiFoSJzvhZmzVgn1A7s8jaoWLowcK received 0.30555483BTC

2016-05-09T15:14:06.310399 1PM3eEmr9LNhoWbxnf5FW9ivQczpWehvF1 received 0.00410816BTC
2016-05-09T15:14:06.310494 14HhBm1H2y7k2KdBLS788fF8YFPSJJ9txE received 0.01501444BTC

2016-05-09T15:14:06.849056 15SzeSV6viKgKY2fHrqSXeZS9qdmNu5997 received 3.47252400BTC
2016-05-09T15:14:06.849267 13JeugdTt4SvmSNPRiNdRsM9Zkk1QDVZy5 received 0.10932927BTC

[live stream continues]
```

## Dependencies

* Developed with python 2.7.11, Bitcoin Core 0.12.1
* jgarzik's python-bitcoinrpc library (https://github.com/jgarzik/python-bitcoinrpc)
* python2-pyzmq, ZeroMQ 4.1.4
* python2-gevent 1.1.1

## Installation

```
$ git clone https://github.com/esotericnonsense/bitcoind-ticker
$ git clone https://github.com/jgarzik/python-bitcoinrpc
$ mv python-bitcoinrpc/bitcoinrpc bitcoind-ticker/
```

## Usage
```
$ cp ~/.bitcoin/bitcoin.conf bitcoind-ticker/
$ cd bitcoind-ticker
$ ./bitcoind -zmqpubhashtx=tcp://127.0.0.1:10000
$ main.py
```

Frog Food
---------

If you have found bitcoind-ticker useful, please consider donating.
The funds will be used for creating future Bitcoin development projects.

![ScreenShot](/screenshots/donation-qr.png)

**bitcoin 3BYFucUnVNhZjUDf6tZweuZ5r9PPjPEcRv**
