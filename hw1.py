"""
• La repository-ul creat săptămâna trecută adăugați un script Python care îndeplinește următoarele funcții:
○ declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
○ afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
○ afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
○ afișarea numerelor cu indici pari din listă (folosind DOAR slice, altă metodă va fi considerată
invalidă)
○ afișarea numerelor cu indici impari din listă (folosind DOAR slice, altă metodă va fi considerată
invalidă)
○ afișarea elementelor multipli ai lui 3.
"""



# declare a list
list1=[7,8,9,2,3,1,4,10,5,6]

# sort the list, keeping the initial list unchanged
sorted_ascending_list1=sorted(list1)
print(list1, " in ascending order is ", sorted_ascending_list1)

# descending order
sorted_descending_list1=sorted(list1, reverse=True)
print(list1, " in descending order is ", sorted_descending_list1)

# start from the beginning
even_indices = list1[::2]
print("even indices from the list ", even_indices)

odd_indices = list1[1::2]
print("odd indices from the list ", odd_indices)

multiples_of_3 = [nr for nr in list1 if nr % 3 == 0]
print("multiples of 3: ", multiples_of_3)

