v="aeiou"
def number(string):
  i=0
  for leter in string:
    if leter in v:
      i +=1
  return i
