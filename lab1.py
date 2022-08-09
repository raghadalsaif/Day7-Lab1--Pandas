import pandas as pd


lst = ["raghad", "faras", "th-name"]
s = pd.Series(lst)

s = pd.Series(lst, index=[11, 12, 13])
print(s)

# 3: Retrieve First and second elements.
print(s[11])
print(s[12])

# 4: Add duplicate elements, then remove the duplication
s = s.append(pd.Series({14: "raghad"}))
print(s)


# 5: Create a Students DataFrame has three columns (ID, Name)
students = {'ID' : [111, 222 , 333 , 444, 555],
            'Name' : ["raghad", "faras", "hsaden", "arwa", "ather"]}
studentsd = pd.DataFrame(students, columns=['ID', 'Name'])
print(studentsd)


# 6: Read educ_figdp_1_Data.csv file

edu = pd.read_csv('https://raw.githubusercontent.com/Data-Science-July31/Lectures/main/Day%237/educ_figdp_1_Data.csv')
print(edu)


"""
7: What is the difference between loc and slicing?
loc use the index labels as references
slice use the position as references
"""



















































