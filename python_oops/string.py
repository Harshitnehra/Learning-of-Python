# Q20. Why are sets unordered?
# Internally
# Hash Table.
# Position depends on hash.
# Not insertion order logic.

# Q21. Why are duplicates removed?
# Each object has
# Hash value

# If same hash + same value
# Ignored.

# Q22. How does membership become O(1)?
# Hash table.
# Instead of scanning
# 1
# 2
# 3
# 4

# Python jumps directly.

# Q23. Difference between remove() and discard()?
# s={1,2}

# s.remove(5)

# Error

# s.discard(5)

# No error.

# Q24. Why can't set contain list?
# List mutable.
# Not hashable.
# {[1,2]}

# Error.

# Q25. Can set contain tuple?
# Yes
# {(1,2)}

# Works.

# Q26. Frozen Set?
# Immutable set.
# fs=frozenset([1,2])

# Can be dictionary key.

# Q27. Difference between set and frozenset?
# Set
# FrozenSet
# Mutable
# Immutable
# Can't be key
# Can be key
# add()
# No add()


# Q28. Can set contain another set?
# No.
# Because mutable.
# Use
# frozenset()


# Q29. Why pop() removes random element?
# Set has no indexing.
# Python removes an arbitrary element based on internal hash table state.

# Q30. How collision handled in hash table?
# Python
# Open Addressing
# Probe next location.

# PART 4 : DICTIONARY

# Q31. How dictionary works internally?
# Dictionary uses
# Hash Table
