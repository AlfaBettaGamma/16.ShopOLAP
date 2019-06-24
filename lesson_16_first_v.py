def DivisionItemsText(items):
  n =[]
  item = []
  l = list(items[0])
  for i in range(len(items)):
    l = list(items[i])
    for j in range(len(l)):
      if l[j] == ' ':
        item.append(l[0:j])
  return item

def DivisionItemsNumb(items):
  n =[]
  item = []
  l = list(items[0])
  for i in range(len(items)):
    l = list(items[i])
    for j in range(len(l)):
      if l[j] == ' ':
        n.append(l[j+1:len(l)])
  return n

def ListConversion(n):
  nn = []
  for i in range(len(n)):
    f = int(''.join(map(str, n[i])))
    nn.append(f)
    f = 0
  return nn

def SumItem(item,n):
  newitem = []
  numb = []
  for i in range(len(item)):
    for j in range(len(item) -  1):
      if item[i] == item[j] and i != j and i < j:
        numb.append(j)
  for i in range(len(item)):
    if i != j-1:
      newitem.append(item[i])
  return newitem

def SumNumb(item,n):
  newn = []
  numb = []
  f = 0
  d = []
  ij = []
  nb = []
  for i in range(len(item)):
    for j in range(len(item) -  1):
      if item[i] == item[j] and i != j and i < j:
        numb.append(j)
        ij.append(i)
        d.append(j)
        f = n[i]+n[j]
        nb.append(f)
  for i in range(len(item)):
    for j in range(len(ij)): 
      if i == ij[j]:
        newn.append(nb[i])
      elif i != d[j]:
        newn.append(n[i])
  return newn


def AssociationItemText(item,nn,N):
  f = 0
  for i in range(N):
    for j in range(len(item) - 1):
      if item[i] == item[j] and i != j:
        f = nn[i] + nn[j]
        item.pop([j])
  return item

def AssociationItemNumb(item,n,N):
  f = 0
  for i in range(N):
    for j in range(len(item) - 1):
      if item[i] == item[j] and i != j:
        f = n[i] + n[j]
        n.pop([j])
        n.insert(i, f)
        n.pop([i + 1])
  return n

def SortItem(n,item):
  result = []
  k = 0
  l = 1
  st = ''
  numb = []
  for i in range(0,len(n)-1):
    for j in range(0,len(n)-i-1):
      if n[j] < n[j+1]:
        n[j],n[j + 1] = n[j + 1], n[j]
        item[j],item[j + 1] = item[j + 1], item[j]
  for i in range(len(n)*2):
    if i == 0:
      numb.append(item[i])
    elif i == 1 :
      numb[k].append(' ')
      numb[k].append(n[k])
      k += 1
    elif i%2 == 0 :
      numb.append(item[l])
      l += 1
    else:
      numb[k].append(' ')
      numb[k].append(n[k])
      k += 1
  for i in range(len(numb)):
    st = ' '.join(str(x) for x in numb[i])
    result.append(st)
    st = ''
  return result

def ShopOLAP(N, items):
  n = DivisionItemsNumb(items)
  print('1 - ',n)
  item = DivisionItemsText(items)
  print('2 - ',item)
  n = ListConversion(n)
  print('3 - ',n)
  n = SumNumb(item,n)
  print('4 - ', n)
  item = SumItem(item,n)
  print('5 - ', item)
  result = SortItem(n,item)
  print('res - ',result)

ShopOLAP(5,['платье1 52', 'сумка32 2','платье1 1','сумка23 3','сумка128 4'])