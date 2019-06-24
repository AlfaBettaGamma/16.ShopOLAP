def ShopOLAP(n,items):
  result = []
  stItems = {}

  for i in range(len(items)):
    item = items[i].split()
    if stItems.get(item[0]) == None:
      stItems[item[0]] = int(item[1])
    else:
      stItems[item[0]] += int(item[1])

  srItem = sorted(stItems.items())
  srItem.sort(key=lambda numb: numb[1], reverse=True)

  for i in srItem:
    result.append(i[0] + ' ' + str(i[1]))

  return result


print(ShopOLAP(6,['платье1 52', 'сумка32 2','платье1 1','сумка23 3','сумка128 4','сумка23 8']))