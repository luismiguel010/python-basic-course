euros = input("¿Cuántos euros tienes?: ")
euros = float(euros)
valor_dolar = 0.85
dolares = euros / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares.")