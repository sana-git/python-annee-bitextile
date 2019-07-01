annee = input("Veuillez taper une année")
annee = int(annee)

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
	print("bissextile")
else:
	print("non bissextile")