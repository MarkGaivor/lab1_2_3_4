txt=input('введите текс: ')
txt=txt.lower()
dlin=len(txt)
vsego=0
list1=[]
def count_letters(txt,vsego):
    for n in range(0,dlin):
        if txt[n].isalpha():
            list1.append(txt[n])
            vsego+=1
    return vsego,list1
count_letters(txt,vsego)
list2=list(set(list1))

def calculate_frequency(list1,list2):
    localcount=0
    dict1={}
    for i in range(0,len(list2)):
        for j in range(0,len(list1)):
            if list2[i] is list1[j]:
                num=list2[i]
                localcount+=1
        dict1[num]=round(localcount/len(list1),2)
    print(dict1)
calculate_frequency(list1,list2)








