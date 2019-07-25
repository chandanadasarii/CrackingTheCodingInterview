def sortStack(stack):
    tempStack = list()

    while(len(stack)):
        elm = stack.pop()
        
        while(len(tempStack) and elm < tempStack[-1]):
            stack.append(tempStack.pop())

        tempStack.append(elm)
    
    return tempStack


print(sortStack([3,8,1,5,3,0,2]))
