##### 1. list (mutable) ########
## .append()
## .extend() -- can be list, set, tuple
## .index() -- find the position of an item in a list
## .pop() --remove item
## sorted(listname)

# create list of babynames
baby_names = list(["Ximena","Aliza","Ayden","Calvin"])

# Extend baby_names with 'Rowen' and 'Sandeep'
baby_names.extend(["Rowen","Sandeep"])
# Print baby_names
print(baby_names)

# Find the position of 'Aliza': position
position = baby_names.index("Aliza")

# Remove 'Aliza' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)

# Create the empty list: baby_names
baby_names = list()

# Loop over records
for name in records:
    # Add the name to the list
    baby_names.append(name[3])

# Sort the names in alphabetical order
for i in sorted(baby_names):
    # Print each name
    print(i)

####### 2. Tuples (immutable) ########
## zip() -- pair up multiple arrays of data
## enumerate()  -- return the index of the list time and the item

# Pair up the boy and girl names: pairs
pairs = zip(girl_names,boy_names)

# Iterate over pairs
for idx,pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name,boy_name))

###### 3. set() ##########
## .union()
## .intersection()
## .difference()
## .add()

# Find the union: all_names
all_names = baby_names_2011.union(baby_names_2014)

# Print the count of names in all_names
print(len(all_names))

# Find the intersection: overlapping_names
overlapping_names = baby_names_2011.intersection(baby_names_2014)

# Print the count of names in overlapping_names
print(len(overlapping_names))

# Create the empty set: baby_names_2011
baby_names_2011 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Check if the first column is '2011'
    if row[0]== '2011':
        # Add the fourth column to the set
        baby_names_2011.add(row[3])

# Find the difference between 2011 and 2014: differences
differences = baby_names_2011.difference(baby_names_2014)

# Print the differences
print(differences)


###### 4. Dictionaries #######
## sorted(reverse = True) -- sort keys of dictionary
## .get()  -- safely find the key and return a velue
## .get(key, default value if not found)
## .keys()
## .update()
## .pop(key, default emplty dictionary{}) -- safely remove
## del dictionary[index]
## .items() -- iterate over items of a dictionary
## x in dict -- check if index in a dictionary
## x in dictionary.values() -- check if value in dictionary

# Create an empty dictionary: names
names = {}

# Loop over the girl names
for name, rank in female_baby_names_2012:
    # Add each name to the names dictionary using rank as the key
    names[rank]=name

# Sort the names list by rank in descending order and slice the first 10 items
for i in sorted(names,reverse = True)[:10]:
    # Print each item
    print(names[i])

# Safely print rank 7 from the names dictionary
print(names.get(7))

# Safely print the type of rank 100 from the names dictionary
print(type(names.get(100)))

# Safely print rank 105 from the names dictionary or 'Not Found'
print (names.get(105,"Not Found") )

#### Deal with nested data ######
# Print a list of keys from the boy_names dictionary
print(boy_names.keys())

# Print a list of keys from the boy_names dictionary for the year 2013
print(boy_names[2013].keys())

# Loop over the dictionary
for year in boy_names:
    # Safely print the year and the third ranked name or 'Unknown'
    print(year, boy_names[year].get(3, "Unknown"))

##### update a dictionary
# Assign the names_2011 dictionary as the value to the 2011 key of boy_names
boy_names[2011] = names_2011

# Update the 2012 key in the boy_names dictionary
boy_names[2012].update([(1, 'Casey'), (2, 'Aiden')])

# Loop over the boy_names dictionary
for year in boy_names:
    # Loop over and sort the data for each year by descending rank
    for rank in sorted(boy_names[year], reverse=True)[:1]:
        # Check that you have a rank
        if not rank:
            print(year, 'No Data Available')
        # Safely print the year and the least popular name or 'Not Available'
        print(year, boy_names[year].get(rank,"Not Available"))

#### remove & delete
# Remove 2011 and store it: female_names_2011
female_names_2011 = female_names.pop(2011)

# Safely remove 2015 with an empty dictionary as the default: female_names_2015
female_names_2015 = female_names.pop(2015,{})

# Delete 2012
del female_names[2012]

# Print female_names
print(female_names)

####### 5. CSV #######
## .reader()  -- loop through each line
## open('file','r'/'w')
## csv.DictReader(csvfile)  -- read header as dict index 

# Import the python CSV module
import csv
# Create a python file object in read mode for the baby_names.csv file: csvfile
csvfile = open("baby_names.csv",'r')

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    # Print each row
    print(row)
    # Add the rank and name to the dictionary
    baby_names[row[5]] = row[3]

# Print the dictionary keys
print(baby_names.keys())

####### create dictionary from file
# Import the python CSV module
import csv
# Create a python file object in read mode for the `baby_names.csv` file: csvfile
csvfile = open('baby_names.csv','r')

# Loop over a DictReader on the file
for row in csv.DictReader(csvfile):
    # Print each row
    print(row)
    # Add the rank and name to the dictionary: baby_names
    baby_names[row['RANK']] = row["NAME"]

# Print the dictionary
print(baby_names.keys())
