s = input() 
FAVORAVEL = 7
TIMAO = "0"
TRICOLOR = "1"


if FAVORAVEL*TIMAO in s and FAVORAVEL*TRICOLOR not in s:
  print("VAI TIMAO")
elif FAVORAVEL*TRICOLOR in s and FAVORAVEL*TIMAO not in s:
  print("VAMO TRICOLOR")
else: 
  print("BORA UM VIRTUAL NO CODEFORCES")