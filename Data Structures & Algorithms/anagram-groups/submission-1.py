class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this instantiates a hashmap which is represented as a dictionary
        # in Python called result and its default value when a key is not
        # present is a empty list for that key 
        result = defaultdict(list) 

        # this will loop through all the strings given in our list of strings
        # and store each string's characters in a count array
        for s in strs:
            # this creates an empty array of size 26 to represent lower case
            # alphabet by index and the stored value is the frequency of that
            # letter present in the string
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord('a')] += 1

            # this converts the count array to a tuple so it can be used
            # as a key in the dictionary and appends it the value which
            # is a list of strings for that key
            result[tuple(count)].append(s)

        # this converts the all the values stored as lists into a list so
        # you return a list of sublists 
        return list(result.values())
