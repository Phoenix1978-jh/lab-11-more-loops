userinput = int(input("Gimme a number please that is greater than 100..."))

while userinput <= 100:  #first condition should capture an input that isnt true,then a message back to user to try again)
    print(str(userinput) + " is less than 100, try again..")
    
    userinput = int(input("Nope, not what i asked for...Gimme a number please that is greater than 100..."))
    
# imagine that the condition has been satisfied...exited the loop..
print(str(userinput) + "is greater than 100 - Good Job!!")