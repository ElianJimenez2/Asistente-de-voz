import subprocess

resultado = subprocess.run(["ipconfig"], capture_output=True, text=True)
print(resultado.stdout)