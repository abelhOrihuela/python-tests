list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def paginate(list, page, per_page):  
  high = page * per_page

  low = high - per_page
  
  return list[low:high]


items = paginate(list, 20, 30)

print(items)
