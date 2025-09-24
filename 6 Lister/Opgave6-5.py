liste = ["Ged", "ko", "Får"]

print("Før ko bliver fjernet:")
for i in liste:
    print("-", i)

liste.remove("Ko")

print("\nEfter ko er blevet fjernet:") # \n betyder new-line, det gør at der er et mellemrum før denne liste
for i in liste:
    print("-", i)