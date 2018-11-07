
'''
Formula Used
P(wk|+)=(nk+1)/(npos + vocabulary)
P(wk|-)=(nk+1)/(nneg + vocabulary)
'''

#DATA SET
data=[
      ["I", "loved", "the", "movie","+"],
      ["I", "hated", "the", "movie","-"],
      ["good", "movie","+"],
      ["poor","acting","-"],
      ["good", "acting","+"]
]


def countWord(w,data): #occurences of word w per data instance
    l=[]
    for d in data:
        c=0
        for i in d:
            if i==w:
                c+=1
        l.append(c)
    return l


#TEXT ATTRIBUTES
unique = [] #text attribrutes
for d in data:
    for i in d:
        if not i in unique:
            if((i!="+") and (i!="-")):
                unique.append(i)
                
print("\nVocabulary:\n",unique,"\n\n\n\n")

vocabulary=len(unique) #total number of unique words

                
print("Feature Sets, Words of Vocabulary are attributes and values are number of occurences\n")
diction={}
for i in unique:
    diction[i]=countWord(i,data) #list

#extractiong class labels from data
    
diction["class"]=[] #list of class labels
for d in data:
    diction["class"].append(d[len(d)-1])
    
    #adding class to dictionary
print(diction,"\n\n\n")

Ppos=(diction['class'].count('+'))/len(data) #P(+)

Pneg=(diction['class'].count('-'))/len(data) #P(-)


#INITIALIZING
#n(+)
npos=0
#n(-)
nneg=0
#nk(+)
nk_pos={}
for u in unique:
    nk_pos[u]=0
#nk(-)
nk_neg={}
for u in unique:
    nk_neg[u]=0
    

#calculating 'n' for '+' and '-'
for u in unique:
    for i in range(0,len(diction["class"])):
        if(diction["class"][i]=="+"):
            nk_pos[u]+=diction[u][i]#caculating nk for '+' e.g total "I" with class '+'
            npos+=diction[u][i]#caculating n for '+'
            

for u in unique:
    for i in range(0,len(data)):
        if(diction["class"][i]=="-"):
            nk_neg[u]+=diction[u][i] #caculating nk for '-'
            nneg+=diction[u][i] #caculating n for '-'
            
print("n(+)=",npos,"\nn(-)=",nneg)
print("nk(+)=",nk_pos,"\nnk(-)",nk_neg)





#probability calculation
print("\n\nProbabilities:\n")

Pk_pos={}#P(wk|+)
for u in unique:
    Pk_pos[u]=0 
    
for u in unique:
    Pk_pos[u]=(nk_pos[u]+1)/(npos+vocabulary)


Pk_neg={}#P(wk|-)
for u in unique:
    Pk_neg[u]=0 
    
for u in unique:
    Pk_neg[u]=(nk_neg[u]+1)/(nneg+vocabulary)


print("P(wk|+)=",Pk_pos,"\n\nP(wk|-)=",Pk_neg)

print("\n********************************************\n\n")

s=input("Enter text for classification:\n\n")

a=s.split(" ")#list



print("\nFor Class + :\n")
plus=Ppos #P(+)
for i in a:
    print("P(",i,"|+)=",Pk_pos[i])
    plus=plus*Pk_pos[i] #P(wk|+)*P(+)
print("P(+)=",Ppos)



print("\nFor Class - :\n")
minus=Pneg #P(-)
for i in a:
    print("P(",i,"|-)=",Pk_neg[i])
    minus=minus*Pk_neg[i] #P(wk|-)*P(-)
print("P(-)=",Pneg)

print("********************************************\nargmax(",plus,",",minus,")\n")
if(plus>minus):
    print("class -> (+)")
else:
    print("class -> (-)")