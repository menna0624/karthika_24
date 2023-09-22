def linear_search_product(productList,targetProduct):
  indices =[]

  for index,product in enumerate(productList):
    if product==targetProduct:
      indices.append(index)

  return indices

product=["pencil","scale","inkpen","scale","Blackpen","scale"]
target="scale"
target2='gelpen'
result=linear_search_product(product,target)
result2=linear_search_product(product,target2)

print(result)
print(result2)



  