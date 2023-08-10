

print("Pwoje sa ka fe tab miltiplikasyon de 1 a 10")
while True:
    nonb_rantre = int(input("Antre yon chif: "))
    
    while nonb_rantre < 1 or nonb_rantre > 10:
        print("Chif ou rantre a pa valide. Chif dwe ant 1 ak 10.")
        nonb_rantre = int(input("Antre yon chif: "))
    for n in range(1, 11):
        print(nonb_rantre, "*", n, "=", n * nonb_rantre)
    
    kontinye = input("Ou vle kontinye? (w/n): ")
    if kontinye.lower() != "w":
        print("Mesi paske ou itilize pwogram nou a pouw travay!!!.")
        break