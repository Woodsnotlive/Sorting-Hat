q1 = int(input('Do you like Dawn [1] or Dusk [2]? '))

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

if q1 == 1:
  Gryffindor = (Gryffindor + 1)
  Ravenclaw = (Ravenclaw + 1)
elif q1 == 2:
  Hufflepuff = (Hufflepuff + 1)
  Slytherin = (Slytherin + 1)

q2 = int(input('When I am dead I want to be remembered as, The good [1], The Great [2], The Wise [3], The Bold [4] '))

if q2 == 1:
 Hufflepuff = (Hufflepuff + 2)
elif q2 == 2:
  Slytherin = (Slytherin + 2)
elif q2 == 3:
  Ravenclaw = (Ravenclaw + 2 )
elif q2 == 4:
  Gryffindor = (Gryffindor + 2)

q3 = int(input('I like listening to, The Violin [1], The Trumpet [2], The Piano [3], The Drum [4]'))

if q3 == 1:
  Slytherin = (Slytherin + 4)
elif q3 == 2:
  Ravenclaw = (Ravenclaw + 4)
elif q3 == 3:
  Ravenclaw = (Ravenclaw + 4)
elif q3 == 4:
  Gryffindor = (Gryffindor + 4)

  print('Gryffindor: ' + Gryffindor)
  print(Slytherin)
  print(Ravenclaw)
  print(Hufflepuff)