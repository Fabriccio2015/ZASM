import sys
import time
if len(sys.argv) < 2:
    print("Uso: python interprete.py [archivo.zasm]")
    codigo_sin_separar = "// Esto no hace nada"
else:
    with open(sys.argv[1], "r") as f:
        codigo_sin_separar = f.read()
codigo_lineas_separadas = codigo_sin_separar.split("\n")
codigo = []
for i in codigo_lineas_separadas:
    codigo.append(i.split(" "))

variables = {"ZERO":0, "ONE":1}
comando = ""
pc = -1
ejecutando = True
while pc < len(codigo) - 1 and ejecutando:
    pc = pc + 1
    i = codigo[pc]
    argumentos_comando = []
    for j, valor in enumerate(i):
        if j == 0:
            comando = valor.strip()
        else:
            argumentos_comando.append(valor)
    if comando == "//":
        pass
    elif comando == "SLEEP":
        time.sleep(variables[argumentos_comando[0]])
    elif comando == "JMP":
        if variables[argumentos_comando[0]]:
            pc = int(variables[argumentos_comando[1]] - 1)
    elif comando == "NOR":
        variables[argumentos_comando[2]] = float(not (variables[argumentos_comando[0]] or variables[argumentos_comando[1]]))
    elif comando == "A<B":
        variables[argumentos_comando[2]] = float(variables[argumentos_comando[0]] < variables[argumentos_comando[1]])
    elif comando == "A>B":
        variables[argumentos_comando[2]] = float(variables[argumentos_comando[0]] > variables[argumentos_comando[1]])
    elif comando == "A=B":
        variables[argumentos_comando[2]] = float(variables[argumentos_comando[0]] == variables[argumentos_comando[1]])
    elif comando == "VAR":
        variables[argumentos_comando[0]] = 0
    elif comando == "PC-GET":
        variables[argumentos_comando[0]] = float(pc)
    elif comando == "ADD-IM":
        variables[argumentos_comando[0]] = variables[argumentos_comando[0]] + float(argumentos_comando[1])
    elif comando == "ADD":
        variables[argumentos_comando[0]] = variables[argumentos_comando[0]] + float(variables[argumentos_comando[1]])
    elif comando == "PRINT-NUM":
        if variables[argumentos_comando[0]] == int(variables[argumentos_comando[0]]):
            print(int(variables[argumentos_comando[0]]))
        else:
            print(variables[argumentos_comando[0]])
    elif comando == "ROUND":
        variables[argumentos_comando[0]] = round(variables[argumentos_comando[0]], int(argumentos_comando[1]))
    elif comando == "":
        pass
    else:
        print("ERROR: Comando no encontrado (", end="")
        print(comando, end="")
        print(")")
        ejecutando = False
