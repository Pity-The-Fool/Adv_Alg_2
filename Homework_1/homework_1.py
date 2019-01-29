#!/usr/bin/python3
from common import cli_parser
from digital_signature import digital_signature



def main(args=None):
    args = parser.parse_args()

    ds = DigitalSignature(args)

    secret, public = ds.generateKeys()
    ds.sign(secret)
    isVerified = ds.verify(secret, public)
    print(isVerified, end="\n\n")
    return
    
