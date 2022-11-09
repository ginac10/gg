Improvements:
* No need to increment i's to continuously check `nums[i] + 1 == nums[i+1]`. Instead, you can just check the next i, then increment ans and i.