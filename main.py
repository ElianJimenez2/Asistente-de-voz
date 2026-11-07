import subprocess

# Recomendado: lista, sin shell
subprocess.run(["ping", "-c", "1", "google.com"])

# Con shell: un string, interpretado por la terminal
subprocess.run("ping -c 1 google.com | grep time", shell=True)