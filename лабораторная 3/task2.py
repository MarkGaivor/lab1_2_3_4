group1=input('введите участников первой группы:')
group2=input('введите участников второй группы:')
def socializator (group1,group2):
     listik=group1.split(',')
     listik2=group2.split(',')
     len1=len(listik)
     len2=len(listik2)
     obshak1=[]
     for i in range(len1):
        if listik[i] not in obshak1:
          for j in range(len2):
              if listik[i]==listik2[j]:
                obshak1.append(listik[i])
                break
     if len(obshak1)==0:
         print('нету общих знакомых')
     else:
         print(obshak1)
socializator(group1,group2)

