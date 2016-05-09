# bitcoind-ticker

A very basic demo of the zmqpubhashtx functionality in bitcoind.

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
