#!/usr/bin/env python3

import requests
import json

apikey = "labserver"
tsigname = "musiclab.signer"
tsigkey = "xK/kp3MoSbuoPKgDVcLMJctmBicHc4Sl9cWiLgtPFWF6dgPqrklft7ffqPgQxSUoJh8y4EZRT6QCBrmJLbo9tw=="
tsigalg = "hmac-sha256"

uri = "http://127.0.0.1:8181/api/v1/servers/localhost/zones"
headers = {"X-API-Key": apikey}

payload_catch22 = {
    "kind": "native",
    "masters": [],
    "name": "msat2.catch22.se.",
    "edited_serial": 101,
    "nameservers": ["signer1.catch22.se."],
    "rrsets": [
        {
            "name": "msat2.catch22.se.",
            "type": "SOA",
            "ttl": 300,
            "records": [
                {
                    "content": "signer1.catch22.se. hostmaster.msat2.catch22.se. 1 300 300 86400 300",
                },
            ],
        },
        {
            "name": "msat2.catch22.se.",
            "type": "TXT",
            "ttl": 300,
            "records": [
                {
                    "content": '"v=spf1 -all"',
                },
            ],
        },
        {
            "name": "msat2.catch22.se.",
            "type": "MX",
            "ttl": 300,
            "records": [
                {
                    "content": "0 .",
                },
            ],
        },
    ],
}

r = requests.post(uri, data=json.dumps(payload_catch22), headers=headers)
print(r.text)

uri = (
    "http://127.0.0.1:8181/api/v1/servers/localhost/zones/msat2.catch22.se./cryptokeys"
)
headers = {"X-API-Key": apikey}

payload_zsk = {
    "active": True,
    "algotrihm": "ecdsa256",
    "bits": 256,
    "keytype": "ksk",
    "type": "Cryptokey",
}

payload_ksk = {
    "active": True,
    "algotrihm": "ecdsa256",
    "bits": 256,
    "keytype": "zsk",
    "type": "Cryptokey",
}

r = requests.post(uri, data=json.dumps(payload_zsk), headers=headers)
print(r.text)
r = requests.post(uri, data=json.dumps(payload_ksk), headers=headers)
print(r.text)

uri = (
    "http://127.0.0.1:8181/api/v1/servers/localhost/tsigkeys"
)
headers = {"X-API-Key": apikey}

payload_tsig = {
        "name": tsigname,
        "id": "1",
        "algorithm": tsigalg,
        "key": tsigkey,
        "type": "TSIGKey"
}


r = requests.post(uri, data=json.dumps(payload_tsig), headers=headers)
print(r.text)

uri = (
    "http://127.0.0.1:8181/api/v1/servers/localhost/zones/msat2.catch22.se./metadata"
)
headers = {"X-API-Key": apikey}

payload_update_from = {
        "kind": "ALLOW-DNSUPDATE-FROM",
        "metadata": ["0.0.0.0/0"],
        "type": "Metadata",
}

payload_tsig_allow = {
        "kind": "TSIG-ALLOW-DNSUPDATE",
        "metadata": [tsigname],
        "type": "Metadata",
        }


r = requests.post(uri, data=json.dumps(payload_update_from), headers=headers)
print(r.text)
r = requests.post(uri, data=json.dumps(payload_tsig_allow), headers=headers)
print(r.text)

### Signer 2 after this

uri = "http://127.0.0.1:8281/api/v1/servers/localhost/zones"
headers = {"X-API-Key": apikey}

payload_catch22 = {
    "kind": "native",
    "masters": [],
    "name": "msat2.catch22.se.",
    "edited_serial": 101,
    "nameservers": ["signer2.catch22.se."],
    "rrsets": [
        {
            "name": "msat2.catch22.se.",
            "type": "SOA",
            "ttl": 300,
            "records": [
                {
                    "content": "signer2.catch22.se. hostmaster.msat2.catch22.se. 1 300 300 86400 300",
                },
            ],
        },
        {
            "name": "msat2.catch22.se.",
            "type": "TXT",
            "ttl": 300,
            "records": [
                {
                    "content": '"v=spf1 -all"',
                },
            ],
        },
        {
            "name": "msat2.catch22.se.",
            "type": "MX",
            "ttl": 300,
            "records": [
                {
                    "content": "0 .",
                },
            ],
        },
    ],
}

r = requests.post(uri, data=json.dumps(payload_catch22), headers=headers)
print(r.text)



uri = (
    "http://127.0.0.1:8281/api/v1/servers/localhost/zones/msat2.catch22.se./cryptokeys"
)
headers = {"X-API-Key": apikey}

payload_zsk = {
    "active": True,
    "algotrihm": "ecdsa256",
    "bits": 256,
    "keytype": "ksk",
    "type": "Cryptokey",
}

payload_ksk = {
    "active": True,
    "algotrihm": "ecdsa256",
    "bits": 256,
    "keytype": "zsk",
    "type": "Cryptokey",
}

r = requests.post(uri, data=json.dumps(payload_zsk), headers=headers)
print(r.text)
r = requests.post(uri, data=json.dumps(payload_ksk), headers=headers)
print(r.text)

uri = (
    "http://127.0.0.1:8281/api/v1/servers/localhost/tsigkeys"
)
headers = {"X-API-Key": apikey}

payload_tsig = {
        "name": tsigname,
        "id": "1",
        "algorithm": tsigalg,
        "key": tsigkey,
        "type": "TSIGKey"
}


r = requests.post(uri, data=json.dumps(payload_tsig), headers=headers)
print(r.text)


uri = (
    "http://127.0.0.1:8281/api/v1/servers/localhost/zones/msat2.catch22.se./metadata"
)
headers = {"X-API-Key": apikey}

payload_update_from = {
        "kind": "ALLOW-DNSUPDATE-FROM",
        "metadata": ["0.0.0.0/0"],
        "type": "Metadata",
}

payload_tsig_allow = {
        "kind": "TSIG-ALLOW-DNSUPDATE",
        "metadata": [tsigname],
        "type": "Metadata",
        }


r = requests.post(uri, data=json.dumps(payload_update_from), headers=headers)
print(r.text)
r = requests.post(uri, data=json.dumps(payload_tsig_allow), headers=headers)
print(r.text)
