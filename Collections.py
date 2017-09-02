######## 1.  Counter  #########
# pass an iterable(list,set, tuple, dictionary)to Counter to count
# counter[key]=value

# Import the Counter object
from collections import Counter

# Print the first ten items from the stations list
print(stations[:10])

# Create a Counter of the stations list: station_count
station_count = Counter(stations)

# Print the station_count
print(station_count)

# Find the 5 most common elements
print(station_count.most_common(5))


###### 2. defaultdict ##########
from collections import defaultdict

# Create a defaultdict with a default type of list: ridership
ridership = defaultdict(list)

# Iterate over the entries
for date,stop,riders in entries:
    # Use the stop as the key of ridership and append the riders to its value
    ridership[stop].append(riders)

# Print the first 10 items of the ridership dictionary
print(list(ridership.items())[:10])

###### 3. OrderedDict  #########
from collections import OrderedDict

# Create an OrderedDict called: ridership_date
ridership_date = OrderedDict()

# Iterate over the entries
for date, riders in entries:
    # If a key does not exist in ridership_date, set it to 0
    if not date in ridership_date:
        ridership_date[date] = 0

    # Add riders to the date key in ridership_date
    ridership_date[date] += riders

# Print the first 31 records
print(list(ridership_date.items())[:31])

#OrderedDict has a .popitem() method that will return items in reverse of which
#they were inserted.
#You can also pass .popitem() the last=False keyword argument and go through the
# items in the order of how they were added.

# Print the first key in ridership_date
print(list(ridership_date.keys())[0])

# Pop the first item from ridership_date and print it
print(ridership_date.popitem(last=False))

# Print the last key in ridership_date
print(list(ridership_date.keys())[-1])
# Pop the last item from ridership_date and print it
print(ridership_date.popitem())

######## 4. Namedtuple ###########
# Namedtuple as names for each position of the tuple
# Import namedtuple from collections
from collections import namedtuple

# Create the namedtuple: DateDetails
DateDetails = namedtuple('DateDetails', ['date', 'stop', 'riders'])

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the entries
for date, stop, riders in entries:
    # Append a new DateDetails namedtuple instance for each entry to labeled_entries
    labeled_entries.append(DateDetails(date, stop, riders))

# Print the first 5 items in labeled_entries
print (labeled_entries[:5])

#access attribute using the namedtuples.attribute
# Iterate over the first twenty items in labeled_entries
for item in labeled_entries[:20]:
    # Print each item's stop
    print(item.stop)

    # Print each item's date
    print(item.date)

    # Print each item's riders
    print(item.riders)
