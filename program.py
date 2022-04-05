
weights = [0.01,0.08, 0.08]
learning_rate=0.20
with open('instances.text') as f:
        lst = []
        for ele in f:
            line = ele.replace('\n','').split(',')
            lst.append(line)
def step_function(val):
    return 1 if val >= 0 else 0
def predict(row,weights):
    activation=weights[0]
    for i in range(len(row)-2):
        activation+=weights[i+1]* int(row[i])
    return step_function(activation)

def dataset(whole_dataset,Gate):
    dataset=[]
    for sets in whole_dataset:
        if sets[3]==Gate:
            dataset.append(sets)
    return dataset
def Train(Gate,Data):
    dataset=[]
    for sets in Data:
        if sets[3]==Gate:
            dataset.append(sets)
    correct=0
    print("Initial weights",weights)
    
    epoch=0
    while True:
        print('***************************************************************************')
        epoch+=1
        print("epoch:",epoch)
        correct=0
        for row in dataset:
            print('\n')
            print('inputs:',row[0],row[1])
            print('weights:',weights)
            prediction = predict(row, weights)
            if int(row[-2])==prediction:
                strrr="Correct"
            else:
                strrr="Incorrect"
            print("y=%d, t=%d =>%s" % ( prediction,int(row[-2]),strrr))
            if int(row[-2])!=prediction:
                weights[0]=round(learning_rate*(int(row[-2])-prediction)+weights[0],3)
                weights[1]=round(learning_rate*(int(row[-2])-prediction)*int(row[0])+weights[1],3)
                weights[2]=round(learning_rate*(int(row[-2])-prediction)*int(row[1])+weights[2],3)
                # print('new weights',weights)
            else:
                correct+=1
        print('\n')
        print("total corrects:",correct)  
        if correct==4:
            
            break
    print('final weights',weights)       
        
     

Train('AND',lst)

        

        
        




