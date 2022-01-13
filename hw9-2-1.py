# Author: CRS 01/06/22
last_initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]
rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"],
["Aiden", "Ian", "Colin", "Tim", "Cam"],
["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

for row in rows:
    for i, v in enumerate(rows):
        if i.index == v.index:
            i.append(last_initials)
        
print(rows)