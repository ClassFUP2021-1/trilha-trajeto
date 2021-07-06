import os
import copy
import subprocess
import casosDeTeste

def command(command):
    env = copy.deepcopy(os.environ)
    proc = subprocess.Popen(command,
                shell=True, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = proc.stdout.read()
    return result

erros = 0

for key, value in casosDeTeste.casosDeTeste.items():
  entradas = key.split('-')
  comd = "python teste.py " + entradas[0]
  for i in range(1, len(entradas)):
    comd = comd + " {0}".format(entradas[i])

  ret = command(comd)
  
  if ret.decode("utf-8").replace('\n', '') != value:
    erros += 1
    print("Erro no caso: ", key, value)

if erros == 0:
  print("Passou nos testes!")
