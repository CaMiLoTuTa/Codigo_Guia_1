#Usaremos la base decimal como primer numero (m)
#Pasaremos el numero m a octal (n)
def m_a_octal(m):
    n = ""
    while m > 0:
        residuo = (m % 8)
        n = str(residuo) + n
        m = int(m / 8)
    return n
#Pedimos a "m" por teclado
m = int(input("Ingresa un número decimal (No mayor a 6 dijitos): "))
n = m_a_octal(m)
print(f"El decimal (m) {m} es (n) 0o{n} en octal")

#Pasamos n a binario
print(f"El octal {n} en binario es", bin(m))

#Pasamos el numero binario a codigo ascii
print("El carácter en ascii de m es", chr(m))

#para pedir dijito por dijito en codigo ascii
q = int(input("Ingresa un número decimal (no mayor a 3 dijitos): "))
w = int(input("Ingresa un número decimal (no mayor a 3 dijitos): "))
e = int(input("Ingresa un número decimal (no mayor a 3 dijitos): "))
r = int(input("Ingresa un número decimal (no mayor a 3 dijitos): "))

ascii_q = chr(q)
ascii_w = chr(w)
ascii_e = chr(e)
ascii_r = chr(r)

print("El carácter en ascii es "+ ascii_q + ascii_w + ascii_e + ascii_r)