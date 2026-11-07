import subprocess

resultado = subprocess.run(["ls", "-l"], capture_output=True, text=True)

print(resultado.stdout)      # lo que imprimió el comando
print(resultado.stderr)      # los errores, si hubo
print(resultado.returncode)  # 0 = éxito, otro número = error