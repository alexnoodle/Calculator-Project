#open questions: mostly about syntax:
#1: I'm not sure about the char at method
#2: not sure about the substring method
#3: not sure about the built in exponent method

#to do: implement multiplication and division


def loop(toCalculate):
    if '(' in toCalculate or ')' in toCalculate:
        parenthesis(toCalculate)
    
    elif '^' in  toCalculate:
        exponent(toCalculate)
    
    elif '*' in toCalculate or '/' in toCalculate:
        multiplication(toCalculate)
    
    elif '+' in toCalculate or '-' in toCalculate:
        addition(toCalculate)
    
    else:
        return toCalculate

def parenthesis(toCalculate):
    toParenthesis = ''
    stack = False
    match = False
    for i in range(len(toCalculate)):
        if toCalculate[i] == '(' and stack == False:
            stack = True
            
        elif toCalculate[i] == '(' and stack == True:
            toParenthesis = ''
            
        elif toCalculate[i] == ')':
            match = True
            toCalculate = toCalculate[:(i - len(toParenthesis)) - 1] + loop(toParenthesis) + toCalculate[i + 1:]
    
        elif stack:
            toParenthesis += toCalculate[i]
    
    if match == False and stack == True:
        toCalculate = toCalculate[: (len(toCalculate) - len(toParenthesis)) - 1] + loop(toParenthesis)
    
    if stack == False:
        for i in range(len(toCalculate)):
            if toCalculate[i] == ')':
                toCalculate = toCalculate[:i - 1] + toCalculate[i + 1:]
                i -= 1
    
    loop(toCalculate)

def exponent(toCalculate):
    index =0
    for i in range(len(toCalculate)):
        if toCalculate[i] == '^':
            index = i
            break
    toExponent = findBackward(toCacluate, index - 1)
    exponent = findForward(toCalculate, index + 1)
    toCalculate = toCalculate[:(index - len(toExponent))] + (math.exponent(float(toExponent), float(exponent))) + toCalculate[(index + len(exponent)):]
    loop(toCalculate)
    
def multiplication(toCalculate):
    index = 0
    multiplied = False
    for i in range(len(toCalculate)):
        if toCalculate[i] == '*':
            index = i
            multiplied = True
            break
            
    if multiplied:
        toMultiply = findBackward(toCalculate, index - 1)
        multiplier = findForward(toCalculate, index + 1)
        toCalculate = toCalculate[:(index - len(toMultiply))] + (float(toMultiply) * float(multiplier)) + toCalculate[(index + len(multiplier)):]
        multiplied = False
    
    else:
        for i in range(len(toCalculate)):
            if toCalculate[i] == '/':
                index = i
                multiplied = True
                break

    if multiplied:
        toMultiply = findBackward(toCalculate, index - 1)
        multiplier = findForward(toCalculate, index + 1)
        # TODO: Try format!
        print('toMultiply: ' + str(toMultiply) + ' multiplier: ' + str(multiplier))
        toCalculate = toCalculate[:(index - len(toMultiply))] + (float(toMultiply) / float(multiplier)) + toCalculate[(index + len(multiplier)):]

    loop(toCalculate)

def addition(toCalculate):
    index = 0
    added = False
    for i in range(len(toCalculate)):
        if toCalculate[i] == '+':
            index = i
            added = True
            break
            
    if added:
        toAdd = findBackward(toCalculate, index - 1)
        addition = findForward(toCalculate, index + 1)
        toCalculate = toCalculate[:(index - len(toAdd))] + (float(toAdd) + float(addition)) + toCalculate[(index + len(addition)), len(toCalculate):]
        added = False
    
    else:
        for i in range(len(toCalculate)):
            if toCalculate[i] == '-':
                index = i
                added = True
                break
    if added:
        toAdd = findBackward(toCalculate, index - 1)
        addition = findForward(toCalculate, index + 1)
        toCalculate = toCalculate[:(index - len(toAdd))] + (float(toAdd) - float(addition)) + toCalculate[(index + len(addition)), len(toCalculate):]
         
    loop(toCalculate)

def findForward(toCalculate, index):
    decimal = False
    toReturn = ''
    if toCalculate[index] == '-':
        toReturn += toCalculate[index]
        index += 1
    for i in range(len(toCalculate) - index):
        current = toCalculate[index + i]
        # TODO: Comparing a string to an integer
        if current >= 0 or current <= 9:
            toReturn += current
        
        elif current == '.' and decimal == False:
            decimal = True
            toReturn += current
            
        elif current == '.' and decimal == True:
            error()

    # TODO: Comparing a string to an integer
    if index == 0 and toCalculate[0] <= 9 and toCalculate[0] >= 0:
        toReturn = toCalculate[0]

    # TODO: Comparing a string to an integer
    elif index == len(toCalculate) and toCalculate[index] <= 9 and toCalculate[index] >= 0:
        toReturn = toCalculate[index]
        
    print('findForward toReturn: {}, type(toReturn): {}'.format(toReturn, type(toReturn)))
    return toReturn

def findBackward(toCalculate, index):
    decimal = False
    toReturnIndex = 0
    toReturn = ''
    for i in range(index):
        current = toCalculate[index - i]
        # TODO: current is a string being compared to an int
        if current >= 0 or current <= 9:
            toReturnIndex = i

        # elif current == '.' and decimal == False:
        if current == '.' and decimal == False:
            decimal = True
            toReturnIndex = i
            
        elif current == '.' and decimal == True:
            error()
            
        elif current == '-':
            toReturnIndex = i
            break
            
        else:
            print('i: ' + str(i))
            break
    
    for i in range(index - toReturnIndex):
        toReturn += toCalculate[toReturnIndex + i]

    # TODO: Comparing a string to an integer
    if index == 0 and toCalculate[0] <= 9 and toCalculate[0] >= 0:
        toReturn = toCalculate[0]

    # TODO: Comparing a string to an integer
    elif index == len(toCalculate) and toCalculate[index] <= 9 and toCalculate[index] >= 0:
        toReturn = toCalculate[index]

    print('index: ' + str(index) + ' toCalculate: ' + toCalculate)
    print('toCalculate: ' + toCalculate + ' char at 0 is: ' + toCalculate[0])

    print('backward: ' + toReturn)
    print('findBackward toReturn: {}, type(toReturn): {}'.format(toReturn, type(toReturn)))
    return toReturn

def error():
    print('something is wrong with the input you dip')


if __name__ == '__main__':
    print('please please pls print things')
    if 6 >= 0 and 6 <= 9:
        print('all is right with the world')
    toCalculate = '3+4*(6/2)+4^2'
    print('answer: ' + loop(toCalculate))
