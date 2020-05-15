def tabladeverdad():
    """"Función que permite conocer el resultado lógico dadas dos expresiones booleanas"""
    expresion = input("Ingrese una expresión lógica (por ejemplo: (p and q) o (not p or q)...etc. ): ")
    print(f"\nExpresión dada: {expresion} ")
    print(24*"=")
 
    booleans = [True, False] #Se puede omitir e iterar sobre "for p,q in True, False"

    for p in booleans:
        for q in booleans:
            print(f"{p}  =>  {q}  =  {eval(expresion)}") #función eval analiza tipo de dato para devolver resultado

try:
    tabladeverdad()
except SyntaxError:
    print("Debe ingresar una expresión lógica coherente")