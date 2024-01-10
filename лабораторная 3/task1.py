list=input("Введите список товаров: ").split()
list1=input("Введите товар: ")
def searcher():
     good=list
     nado=good
     print('ваш список товаров:', nado)
     num=list1
     if num in nado:
          vot=nado.index(num)
          print('товар найден',vot)
     else:
          print('товар не найден')
searcher()
