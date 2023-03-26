# design-block-cipher

IES is a block cipher that created based on AES and DES and feistel network. It uses the Sbox from AES and Feistel network from DES.

|   NIM    |              Name              |
| :------: | :----------------------------: |
| 13520029 | Muhammad Garebaldhie ER Rahman |
| 13520163 |     Frederik Imanuel Louis     |
| 13520166 |       Raden Rifqi Rahman       |

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

## How to run
```
usage: encrypt.py/decrypt [-h] [-M MODE] [-iv initial-vector-file] [-o output-vector-file] filepath key-file-or-phrase

positional arguments:
  filepath
  key-file-or-phrase

optional arguments:
  -h, --help            show this help message and exit
  -M MODE, --mode MODE
  -iv initial-vector-file
  -o initial-vector-file, --outfile initial-vector-file
```

1. `-M mode` is consisting of `ECB, CBC, CFB, OFB, CTR` other than that it will fails
2. `-iv path` is filepath consisting of the iv the program want to use. The file might be anything `.txt`, `.in` or no exstention. The files is consisting bytes or text. `iv` options will be used for all modes except `ECB`

This is example of `iv` file
```md
akusukamakaniyayayaya
```

3. `-o output` is the filename that you want to output, the default is it will append `encrypted-` to the filename so if the filename is `a.txt` the result will be `encrypted-a.txt`
4. `filepath` file you want to `encrypt` or `decrpyt`
5. `key-file-or-phrase` the key that will be used for the process, might be phrase or from file

Example:
1. Encrypt file named `requirements.txt` using `ECB` mode with `key` from stdin

```bash
python .\src\encrypt.py  -M ecb .\requirements.txt akusukakripto
```

2. Encrypt file named `requirements.txt` using `CBC` mode and `iv` file with `key` from stdin
```bash
python .\src\encrypt.py -M cbc -iv .\iv .\requirements.txt akusukakripto
```

3. Decrypt file named `requirements.txt` using `CBC` mode and `iv` file with `key` from `a` file
```bash
python .\src\decrypt.py -M cbc -iv .\iv .\encrypted-requirements.txt .\a
```

4. Decrypt file named `requirements.txt` using `CBC` mode and `iv` file with `key` from `a` file with file name `gare`
```bash
python .\src\decrypt.py -M cbc -iv .\iv -o .\gare .\encrypted-requirements.txt .\a
```