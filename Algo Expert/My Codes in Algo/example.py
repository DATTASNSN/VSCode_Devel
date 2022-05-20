def getCost(parcles,k):
  minimum_cost = 0
  parcles_length = len(parcles)
  for parcle in range(1,max(parcles)):
    if parcle not in parcles and parcles_length < k:
      minimum_cost += parcle
      parcles_length+=1
  return minimum_cost

parcles = [2,3,6,10,11]
k=9

print(getCost(parcles,k))
