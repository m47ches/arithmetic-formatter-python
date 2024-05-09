def arithmetic_arranger(problems, show_answers=False):
    
    
    #cuando hay más de 5 items en la lista
    if len(problems)>5:
        return 'Error: Too many problems.'
    
    
    
    #ciclo for de la lista
    for problema in problems:
        operacion = problema.split(' ')
        
        #error que no sean números
        try:
            primero = int(operacion[0])
            segundo = int(operacion[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        #error operacion distinta de suma o resta
        if operacion[1] not in '+-':
            return "Error: Operator must be '+' or '-'."
        print(operacion)

        #error que el número sea muy largo
        if (len(operacion[0])>4) or (len(operacion[2])>4):
            return "Error: Numbers cannot be more than four digits."

    return problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')