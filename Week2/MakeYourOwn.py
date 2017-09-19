
# Create a shifted dictionary for a letter
def code_dico(letter):
    shift= ord(letter) - 96
    dico = {}
    # filling the dico with the shifted letters as values
    for l in 'abcdefghijklmnopqrstuvwxyz':
        dico[l]= chr((ord(l)-97+shift)%26 +97)   
    return dico 

# Create  list of shifted dictionary for the key
def code_dictionaries(key):
    dictionaries=[]
    # creating one dico for each key
    for l in key:
        dictionaries.append(code_dico(l))
    return dictionaries   

# code a message with a certain key
def code(message,key):
    code =''
    dictionaries = code_dictionaries(key)
    i = 0
    for l in message:
        dico = dictionaries[i]
        code += dico[l]       
        i = (i+1) % len(dictionaries)
    return code 
      
print(code('bonjour','key'))
