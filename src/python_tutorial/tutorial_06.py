sentense = "Nima Afshar Ghotli is working at Auckland bioengineering institute"
A = sentense.index("Afshar")
B = sentense.index("Ghotli")
print(A)
print(B)
#family_name = name[5:10:1]
#print(family_name)
family_name = sentense[A:B:1].strip()
print(family_name)

word = sentense[sentense.index("Auckland"):]
print(word)

word = sentense[sentense.index("Afshar"):sentense.index("is")].strip()

print(word)

print(len(word))

quiz = "happy_birthday"

answer = quiz[:-9]
print(answer)

answer = quiz[:quiz.index("_")]
print(answer)