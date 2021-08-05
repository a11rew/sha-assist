# SHA Assistant

## Easy SHA1, SHA256, SHA384, SHA512, MD5 HTTPS domain fingerprinting.

Quick zero dependency fingerprinting with one command. sha_assist produces algorithmic hexadecimal hashes of public keys used in TLS/SSL connections' authentication. These hashes are useful in verifying the authenticity of recieved HTTPS certificates and are essential in thwarting MiTM attacks for example.

Out of the box, sha_assist exposes 5 key digests i.e. (SHA1, SHA256, SHA384, SHA512 and MD5) but can be easily extended using `hashlib.algorithms_available`.

See [Extensibility](#Extensibility)

Credit to [dlenski](https://gist.github.com/dlenski) for [ssl.SSLSocket patching](https://gist.github.com/dlenski/fc42156c00a615f4aa18a6d19d67e208)

## Installation

`git clone https://github.com/AndrewGlago/sha-assist.git && cd sha-assist`

## Usage and Options

`python3 ./sha_assist.py -d google.com -p 443`

![git](https://user-images.githubusercontent.com/87580113/128281173-12ab0604-2711-4633-b66c-81067d876e49.png)


Usage: sha_assist.py [OPTIONS]

| Options | Description |
| ------------------------- | ------------------------------------------------------------------ |
| -d or --domain [required] | [Text] Domain URL to be fingerprinted (eg. https://www.github.com) |
| -p, --port [optional] | [Integer] Port to establish connection on. Defaults to 443 |

**NOTE: URL must be prefixed with https://**

## Extensibility

sha-assist produces algorithmic digests using hash-lib. By extension, all methods exposed by `hashlib.algorithms_available` can be used to produce required digests.
Output is by default hex but can be adapted to binary by replacing ~.digestHex().
