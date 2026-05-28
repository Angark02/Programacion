places = ["China", "Korea", "New York", "Japan", "Australia"]
print(places)

sorted_places = sorted(places)
print(sorted_places)# Alphabetically sorted
print(places) # The original one has not get changed

unsorted_places = sorted(places, reverse=True)
print(sorted_places)
print(places)

places.reverse() # Reverse the list
print(places)
places.reverse() # Reverse it again to its original order
print(places)

places.sort()
print(places)
places.sort(reverse=True)
print(places)