#!/usr/bin/python3
from common import cli_parser
from digital_signature import digital_signature
from datetime import datetime
start_time = datetime.now()



def main(args=None):
    args = cli_parser.parse_args()

    ds = digital_signature.DigitalSignature(args)

    ds.generateKeys()
    secret, public = ds.secret, ds.public
    ds.sign()
    is_verified = ds.verify()

    # Timing and output
    end_time = datetime.now()
    print("Overall execution took:", end_time - start_time, "time")
    print("Given message:", ds.message)
    print("Signature is verified:", is_verified, end="\n")
    return

main()
