def lunchchild(list1, list2):
  list3 = []
  if len(list1) >= len(list2):
    for i in range(len(list1)):
      if list1[i] in list2:
        list3.append(list1[i])
  if len(list1) <= len(list2):
    for i in range(len(list12)):
      if list2[i] in list1:
        list3.append(list2[i])
  return list3 
