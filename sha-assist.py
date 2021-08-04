import click
import validators
import ssl
import urllib.request
import sys
import base64
import hashlib

@click.command()
@click.option("-d", "--domain", "domain_var", required=True, help="Domain to be fingerprinted (eg. https://www.github.com)")
@click.option("-p", "--port", "port_var", default=443, help="HTTPS port (Defaults to 443)")

def process(domain_var, port_var):
  validateURL(domain_var)
  url = "{domain_var}:{port_var}".format(domain_var=domain_var, port_var=port_var)

  if sys.version_info >= (3, 7):
    ssl.SSLContext.sslsocket_class = fingerprint_checking_SSLSocket()
  else:
    ssl.SSLSocket = fingerprint_checking_SSLSocket()

  ssl._create_default_https_context = ssl._create_unverified_context 

  r = urllib.request.Request(url)
  urllib.request.urlopen(r)
  
def validateURL(domain_var):
  if not validators.url(domain_var):
    raise click.BadArgumentUsage("Invalid HTT URL provided")

def fingerprint_checking_SSLSocket():
    class SSLSocket(ssl.SSLSocket):
        def do_handshake(self, *args, **kw):
            res = super().do_handshake(*args, **kw)
            bcert = self.getpeercert(binary_form=True)

            sha1 = hashlib.sha1(bcert).hexdigest()
            sha256 = hashlib.sha256(bcert).hexdigest()
            sha384 = hashlib.sha384(bcert).hexdigest()

            print(sha1)
            print(sha256)
           

    return SSLSocket

if __name__ == "__main__":
  process()