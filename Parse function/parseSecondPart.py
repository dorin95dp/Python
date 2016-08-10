highOrderedOperators = ["*","/"]
lowOrderedOperators = ["+","-"]
def grabOperands(array, index):
    operand1 = array[index-1]
    operand2 = array[index+1]

    return (operand1, operand2)

def extractOperation(array, index):
    operands = grabOperands(array,index)
    operator = array[index]
    
    return (operands[0],operator,operands[1])

def removeOperandsAndOperator(array, index):
    for i in range(3):
        del array[index-1]
    
    return array

def doOperation(operation):
    operator = operation[1]
    operand1 = float(operation[0])
    operand2 = float(operation[2])
    if operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    else:
        raise ValueError("Error")

def operationToResult(array, index):
    operation = extractOperation(array, index)
    resultOperation = doOperation(operation)
    array = removeOperandsAndOperator(array, index)
    array.insert(index-1, str(resultOperation))

    return array

def parseOperators(array, operatorsType):
    index = 0
    while index < len(array):
        for operator in operatorsType:
            if array[index] == operator:
                array = operationToResult(array, index)
                index = 0
                
        index += 1
        
    return array

def parse(array):
    arrayParsedHighOrder = parseOperators(array, highOrderedOperators)
    arrayFinal = parseOperators(arrayParsedHighOrder, lowOrderedOperators)
    
    return float(arrayFinal[0]) 

array = ["12","+","3","*","4","*","3.5","+","2","/","5"]
number = parse(array)
print(number)



