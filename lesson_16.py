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

