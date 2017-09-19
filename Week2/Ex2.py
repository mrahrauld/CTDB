def text_to_words(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()

def Ex2():
    with open('pizza-train.json') as pizzafile:
        pizza_train = json.load(pizzafile)
    Dictionary ={} #dictionary of all the words in all the texts
    ListDict = [] #list of dictionaries, one for each text
    
    # Loop over the requests
    for request in pizza_train:
        # transform the string in a list of words, without punctuation and capitalization
        words = text_to_words(request['request_text'])
        dico ={}
        
        # Loop over the words in a request
        for w in words: 
            if w in dico.keys():
                dico[w]+=1 # Incrementation
            else:
                dico[w]=1 # Addition
            Dictionary[w]=1 # the value doesn't matter 
                     
        ListDict.append(dico)
        
    N = len(pizza_train)
    M = len(Dictionary)
    Result = [[0 for x in range(M)] for y in range(N)] 
      
    # loop over the texts  
    i=0 
    for dico in ListDict:
        
        #loop over the words in the Dictionary
        j=0
        for word in Dictionary.keys():
            if word in dico:
                Result[i][j] = dico[word]
            j+=1
        i+=1  
    return Result

