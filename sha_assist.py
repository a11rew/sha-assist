#!/usr/bin/env python3

import click
import ssl
import urllib.request
import sys
import hashlib

from utils.validate import url

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
  if not url(domain_var):
    raise click.BadArgumentUsage("Invalid HTT URL provided")

def fingerprint_checking_SSLSocket():
    class SSLSocket(ssl.SSLSocket):
        def do_handshake(self, *args, **kw):
            res = super().do_handshake(*args, **kw)
            bcert = self.getpeercert(binary_form=True)

            sha1 = hashlib.sha1(bcert).hexdigest()
            sha256 = hashlib.sha256(bcert).hexdigest()
            sha384 = hashlib.sha384(bcert).hexdigest()
            sha512 = hashlib.sha512(bcert).hexdigest()
            md5 = hashlib.md5(bcert).hexdigest()

            stdEcho(sha1, sha256, sha384, sha512, md5)

    return SSLSocket

def stdEcho(sha1, sha256, sha384, sha512, md5 ):
  # click.echo(f"""
  #    SHA-1 : {sha1}                                          
  #    SHA-256 : {sha256}                                      
  #    SHA-384 : {sha384}                                      
  #    SHA-512 : {sha512}                                      
  #    MD5 : {md5}                                             
  # """
  # )

  click.echo(click.style("        SHA-1 : ", fg="green") + click.style(f"{sha1}", fg="yellow"))
  click.echo(click.style("        SHA-256 : ", fg="green") + click.style(f"{sha256}", fg="yellow"))
  click.echo(click.style("        SHA-384 : ", fg="green") + click.style(f"{sha384}", fg="yellow"))
  click.echo(click.style("        SHA-512 : ", fg="green") + click.style(f"{sha512}", fg="yellow"))
  click.echo(click.style("        MD5 : ", fg="green") + click.style(f"{md5}", fg="yellow"))


if __name__ == "__main__":
  process()
  exit()
