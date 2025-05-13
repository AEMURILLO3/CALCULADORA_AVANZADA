def advanced_calculator():
    print("Bienvenido a la calculadora avanzada.")
    print("Ingrese los valores separados por espacios:")
    values = list(map(float, input().split()))
    
    print("Seleccione la operación que desea realizar:")
    print("1. Suma (+)")
    print("2. Resta (–)")
    print("3. Multiplicación (×)")
    print("4. División (÷)")
    
    operation = input("Ingrese el número de la operación: ")
    
    if operation == '1':
        result = sum(values)
        print(f"El resultado de la suma es: {result}")
    elif operation == '2':
        result = values[0]
        for value in values[1:]:
            result -= value
        print(f"El resultado de la resta es: {result}")
    elif operation == '3':
        result = 1
        for value in values:
            result *= value
        print(f"El resultado de la multiplicación es: {result}")
    elif operation == '4':
        result = values[0]
        for value in values[1:]:
            if value != 0:
                result /= value
            else:
                print("Error: División por cero.")
                return
        print(f"El resultado de la división es: {result}")
    else:
        print("Operación no válida.")

# Ejecutar la calculadora avanzada
advanced_calculator()
