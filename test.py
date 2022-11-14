def containsDuplicate(nums: list) -> bool:
    hmap = {}
    for i in range(len(nums)):
        if nums[i] in hmap:
            print(nums[i])
            return True
        else:
            hmap[nums[i]] = 1
    print([nums[i]])
    print(hmap)
    return False

print(containsDuplicate([3,3]))