#!/usr/bin/env python3

from click.testing import CliRunner
import sha_assist


#TODO - Obtain reliable evergreen digests fro testing

def test_process():
  runner = CliRunner()
  result = runner.invoke(sha_assist.process, ['-d https://www.tesla.com'])
  result_1 = runner.invoke(sha_assist.process, ['-d https://www.google.com'])
  result_2 = runner.invoke(sha_assist.process, ['-d https://www.facebook.com'])


  assert result.exit_code == 0
  assert result_1.exit_code == 0
  assert result_2.exit_code == 0

  # assert result.output == ("""
  #       SHA-1 : 89927fc6dc030effa089cd09f627703bd5ea615c
  #       SHA-256 : a8838b4d9af555956e3c01c2737c497fa178424c78a811c8b7e8e5c51590a431
  #       SHA-384 : 7245e1d3b86ee3804e6b812ba2f7d6f4ff32b6512744a0ac1776c3f35325c84e7ecdad48e0e53b33ed0f081d4cba8074
  #       SHA-512 : adfe4bfc45fa49f4e2897cfe7e621f83fafcd2bb84814dbae2050940043920db8d1381b69e4b2baeba8ff6948b03a06f805505de466e1041728e8467ce19d338
  #       MD5 : a717c486cdbc8493d837741e04072884
  # """)
