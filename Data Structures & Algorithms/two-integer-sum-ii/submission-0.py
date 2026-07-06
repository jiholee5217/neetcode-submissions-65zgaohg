class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        result = []


        while left < right:
            twoSum = numbers[left] + numbers[right]
            if twoSum < target:
                left += 1
            elif twoSum > target:
                right -= 1
            else:
                break

        result.append(left + 1)
        result.append(right + 1)
        return result