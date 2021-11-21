def isLetter(character):
  if character.lower() in 'aáàãbcçdeéèfghiíìjklmnoóòõpqrstuvxywz':
    return True
  else:
    return False

s = input()
words = []
indexes = [-1]

for i in range(len(s)):
  if not isLetter(s[i]):
    indexes.append(i) # pegar os indexes dos caracteres não letras e fazer um split nesses indexes

if isLetter(s[-1]):
  indexes.append(len(s))

for i in range(len(indexes)-1):
  words.append(s[indexes[i]+1 : indexes[i+1]])

for x in words:
  print(x)
  

