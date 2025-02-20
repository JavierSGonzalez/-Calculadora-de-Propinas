historial = []

while True:
    print("Calcular propina: \n")

    print("¿Que quieres hacer?")
    print("Ir a calculadora(1)  Salir(2)")
    while True:
        res = input()
        if res == "1":
            break
        elif res == "2":
            print("Muchas gracias por usar la calculadora de propinas")
            exit()
        else:
            print("Escribe una opción valida")

    print("Monto total de la cuenta - Escribe solo el número")
    i = float(input())  
    print(f"${i} \n")

    print("Porcentaje de propina que desea agregar, escriba '=' y el porcentaje")
    print("=10%")
    print("=15%")
    print("=20%")

    while True:
        pro = input()
        if pro == "=10%":
            propina = i * 0.10
            break
        elif pro == "=15%":
            propina = i * 0.15
            break
        elif pro == "=20%":
            propina = i * 0.20
            break
        else:
            print("Usa el formato correcto: =10%, =15% o =20% \n")

    propinaA = round(propina, 2)
    print(f"Propina: ${propinaA} \n")

    print("Personas a pagar")
    pe = float(input())

    tot = (i+propinaA) / pe
    totA= round(tot, 2)

    historial.append(totA)

    print(f"Total equivalente por persona: ${totA} \n")
    print(f"Historial de totales equivalentes: $ {historial}")
    for tot in historial:
        print(f"${totA}")

    print("¿Quieres calcular otra propina? Responde s/n:")
    while True:
        salir = input()
        if salir == "s":
            print("Historial final de totales equivalentes:", historial)
            break
        elif salir == "n":
            print("Muchas gracias por usar la calculadora de propinas")
            exit()
        else:
            print("¿Si o No?")