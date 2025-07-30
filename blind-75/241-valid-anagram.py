# definition of "Anagram":
    # two strings are anagram if:
        # They have the same characters
        # With exact same frequency
        

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
    
    
    
    
    # some theory regarding ".sort" and "sorted()"
    
    # use sorted() ---> when working with strings or when you don't want to mutate
    # use .sort() ---> only for lists, and when in-place sorting is okay
    # In-place-sorting: means sorting the elements without using extra space to store a new list- instead it modifies the original list itself
    
    
    
    # .sort() directly changes the original nums list.

    # It doesn't return anything (returns None).

    # It’s called in-place because it doesn’t allocate a new list.
    
    
    # sorted() creates a new list.

    # The original nums remains unchanged.

    # Uses extra memory, so it's not in-place.


# using .sort()

class Solution(object):
    def isAnagram(self, s, t):
        # convert strings to list as .sort doesn't work on strings
        s_list = list(s)
        t_list = list(t)
        
        # sort in-place
        s_list.sort()
        t_list.sort()
        
        return s_list == t_list
        
        
        
# Using Counter
 
        
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
    
    
    
# Theory about the Counter

#  Counter: is a dictionary subclass designed to count the "frequency" of elements in an "iterable" (like a list, string, or tuple)
# is like mapping each element


# an Example:
    # s = "rat"
    # t = "car"
    # Counter(s) → {'r': 1, 'a': 1, 't': 1}
    # Counter(t) → {'c': 1, 'a': 1, 'r': 1}
