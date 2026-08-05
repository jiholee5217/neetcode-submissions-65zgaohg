class TimeMap:

    def __init__(self):
        # create a hashmap called store to store key and value 
        # key will just be the key given
        # value will be a [value, timestamp]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key is not in the hashmap, just set the value to an empty list
        if key not in self.store:
            self.store[key] = []

        # append the list of value and timestamp to the value stored at key 
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = "" # create a empty string called res
        values = self.store.get(key, []) # retrieve the value for key or return an empty string if no value exist

        # set l to 0 and r to the last index of the list that is values
        l, r = 0, len(values) - 1 
        while l <= r:
            m = (l + r) // 2 # get the middle of the list 
            if values[m][1] <= timestamp: # if the timestamp of the middle of the list is <= timestamp 
                res = values[m][0] # result is equal to values[mid index][value]. returnt he value
                l = m + 1   
            else:
                r = m - 1
        return res

    # hashmap
    # key : [value, timestamp]

