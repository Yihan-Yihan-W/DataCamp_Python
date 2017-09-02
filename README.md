# DataCamp_Python

## DataTypes
1. list
   .append()
   .index() -- find the position of an item in a list
   .extend() -- can be list, set, tuple
   .pop() --remove item
   sorted(listname)
   
2. tuple
  zip() -- pair up multiple arrays of data
  enumerate()  -- return the index of the list time and the item

3. set
  .union()
  .intersection()
  .difference()
  .add()
  
4. dict

  sorted(reverse = True) -- sort keys of dictionary
  .get()  -- safely find the key and return a velue
  .get(key, default value if not found)
  .keys()
  .update()
  .pop(key, default emplty dictionary{}) -- safely remove
  del dictionary[index]
  .items() -- iterate over items of a dictionary
  x in dict -- check if index in a dictionary
  x in dictionary.values() -- check if value in dictionary

5. csv files
  .reader()  -- loop through each line
  open('file','r'/'w')
  csv.DictReader(csvfile)  -- read header as dict index

## Collections
1. Counter
  counter(list,set, tuple,dict)
  counter[key]=value
  countername.most_common(number)
  
2. DefaultDict

3. OrderedDict
  .popitem() method that will return items in reverse of whichthey were inserted.
  .popitem() the last=False keyword argument and go through theitems in the order of how they were added.
  
4. namedtuple
   namedtuples.attribute
