array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array):
  if len(array) == 1:
    return array[0]
  else:
    pivot = array[0]
    big = 0
    small = len(array)-1
    while(True):
      while(array[big]<=pviot):
        big+=1
      while(array[small]>=pivot):
        small-=1
      if (big>=small):
        break
      array[big], array[small] = array[small], array[big]
    array[small], array[0] =array[0], array[small]
    quick(array[:small])
    quick(array[big:])

quick(array)
print(array)