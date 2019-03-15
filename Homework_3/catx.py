#!/usr/bin/python3

## Catx Interface API

scripts = { P2PKH: "OP_DUP OP_HASH160 <Public-Key-Hash> OP_EQUALVERIFY OP_CHECKSIG",
            P2PT: "Pay to Post UC Tribute <shortened -url>",
            P2UCS: "Pay to UC Scholar <Public-Key-Hash>",
            P2HS: "Pay to Hashed Script <Hashed-Address>",
            OTHER: "Another Script" }

def encodeCatx(script, *args, **kwargs): return code
