import click
import validators

@click.command()
@click.option("-d", "--domain", "domain_var", required=True, help="Domain to be fingerprinted (eg. https://www.github.com)")
@click.option("-p", "--port", "port_var", default=443, help="HTTPS port (Defaults to 443)")

def process(domain_var, port_var):
  validateURL(domain_var)
  click.echo(f"Domain - {domain_var}, port - {port_var}")

def validateURL(domain_var):
  if not validators.url(domain_var):
    raise click.BadArgumentUsage("Invalid domain URL provided")

if __name__ == "__main__":
  process()