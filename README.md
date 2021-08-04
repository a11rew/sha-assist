# SHA Assistant

## Easy SHA1, SHA256, SHA384, and SHA512 HTTPS domain fingerprinting.

## Syntax

`python3 sha-assist -d google.com -p 443`

Usage: sha-assist.py [OPTIONS]

Options:
-d, --domain TEXT Domain URL to be fingerprinted (eg. https://www.github.com)
[required]
**URL must be prefixed with https://**
-p, --port INTEGER HTTPS port (Defaults to 443)
