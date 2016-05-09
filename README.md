# bitcoind-ticker

A very basic demo of the zmqpubhashtx functionality in bitcoind.

## Dependencies

* Developed with python 2.7.11, Bitcoin Core 0.12.1
* jgarzik's python-bitcoinrpc library (https://github.com/jgarzik/python-bitcoinrpc)

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

**1FrogqMmKWtp1AQSyHNbPUm53NnoGBHaBo**
