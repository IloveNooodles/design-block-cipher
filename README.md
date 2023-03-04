# design-block-cipher

IES is a block cipher that created based on AES and DES and feistel network. It uses the Sbox from AES and Feistel network from DES.

## How does IES work

Generally IES have 5 components

1. Sbox
2. Pbox
3. Expansion Matrix
4. Round function
5. Key Generation

## Requirements

1. Python 3.10
2. virtualenv

## How to install

1. Make sure you have all the [requirements](#requirements) installed.
2. Create virtualenv by using `virtualenv venv`
3. Use the virtualenv by using
   1. Windows: `./venv/Scripts/activate`
   2. UNIX: `source ./venv/bin/activate`
4. Install all the requirements using `pip3 install -r requirements.txt`
