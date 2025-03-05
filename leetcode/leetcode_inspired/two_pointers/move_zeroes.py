class Soluton:
    def move_zeroes(self, nums: list[int]) -> None:
        # slow-fast pointer style
        left = 0
        for right in range(len(nums)):
            # if a non-zero value appears in the iteration send it back to the left index position
            if nums[right] != 0:
                # give right index's value to left's index position
                nums[left] = nums[right]
                # this is needed because IF left's index position isnt at the same position as right then 
                # left's index will be holding a 0 and will need to give that zero to right's index
                # aka moving that zero along to the back in this case
                if left != right:
                    # give left's index element's value to right
                    nums[right] = 0
                # move left's index position up by one because its current position has been filled with a non-zero value
                left += 1
        return nums
    
# alternative explanation of same code (more clarity)
class Solution:
    def move_zeroes(self, nums: list[int]) -> None:
        # Two pointers: left tracks next position for a non-zero, right scans the array
        left = 0
        for right in range(len(nums)):
            # If a non-zero is found, move it to the next available slot at 'left'
            if nums[right] != 0:
                # Place the non-zero at the 'left' position
                nums[left] = nums[right]
                # If the non-zero came from a different index, clear the old position (move the zero back)
                if left != right:
                    nums[right] = 0
                # Advance 'left' since that slot has been filled
                left += 1


solution = Soluton()
test_cases = [
    # [0, 1, 0, 3, 12],
    [1, 0, 2, 0, 3]
]
for i in test_cases:
    print(solution.move_zeroes(i))