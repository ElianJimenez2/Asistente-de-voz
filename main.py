import subprocess

resultado = subprocess.run(["echo", "hola"], capture_output=True, text=True)

print(resultado.stdout)