# SHA Assistant

## Easy SHA1, SHA256, SHA384, and SHA512 HTTPS domain fingerprinting.

## Syntax

`python3 sha-assist -d google.com -p 443`

Usage: sha-assist.py [OPTIONS]

| Options                   | Description                                                        |
| ------------------------- | ------------------------------------------------------------------ |
| -d or --domain [required] | [Text] Domain URL to be fingerprinted (eg. https://www.github.com) |
| -p, --port [optional]     | [Integer] Port to establish connection on. Defaults to 443         |

**URL must be prefixed with https://**
