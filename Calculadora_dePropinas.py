historial = []

while True:
    print("Calcular propina:")

    print("Monto total de la cuenta - Escribe solo el número")
    i = float(input())  
    print("$", i)

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
            print("Usa el formato correcto: =10%, =15% o =20%")

    print(f"Propina: ${propina}")

    print("Personas a pagar")
    pe = float(input())
    
    tot = (i+propina) / pe

    historial.append(tot)

    print(f"Total equivalente por persona: ${tot}")
    print(f"Historial de totales equivalentes: {historial}")
    for tot in historial:
        print(tot)
    
    print("¿Quieres calcular otra propina? Responde s/n:")
    while True:
        salir = input()
        if salir == "s":
            print("Historial final de totales equivalentes:", historial)
            break
        elif salir == "n":
            print("Muchas gracias por usar la calculadora de propinas")
        else:
            print("¿Si o No?")