"""
  Problem 22
  Names scores
"""
# Open text file
name_ul = open('p022_names.txt')
# Split names
name_ol = name_ul.read().split(',')
# close the text file
name_ul.close()
# sort the list of names
name_ol.sort()

# init score
score = 0
#loop through the names and calculate their worth
for i in range(0, len(name_ol)):
    worth = sum([(ord(ch) - 34)%30 for ch in name_ol[i]])
    index = i + 1
    score += (worth * index)
  
#Output  
print ("p022 Ans: ", score)
