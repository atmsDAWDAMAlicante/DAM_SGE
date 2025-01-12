edad_input = input("Introduce tu edad: ")
salario_input = input("Introduce el salario que percibes: ")
edad_int = int(edad_input)
salario_float = float(salario_input)
if ((edad_int > 17) and (salario_float >= 1200.00)):
    print("Tienes que presentar la declaración de la renta")
elif ((edad_int > 17) and (salario_float < 1200.00)):
    print("No tienes que realizar la renta porque percibes un salario inferior al límite")
else:
    print("No tienes obligación de realizar la renta porque eres menor de edad")