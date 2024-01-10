listl=[1,2,6,4,2,8,4,8,'l',4,6,21,4,68,7]
for i in range(len(listl)):
    if not type(listl[i])==int:
       b=i
listl[b]=0
skoka=sum(listl)
vsego=len(listl)
avg=skoka/vsego
listl[b]=avg
print(listl)
