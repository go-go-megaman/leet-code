class Solution:
    def main(
            self,
            nums1: [int],
            nums2: [int]) -> float:
        indexOfNums1 = indexOfNums2 = 0
        marged: [int] = []
        totalLength = len(nums1) + len(nums2)
        while indexOfNums1 <= len(nums1) and indexOfNums2 <= len(nums2):
            if len(marged) > (totalLength / 2):
                return marged[len(marged) - 1] if totalLength % 2 == 1 else (
                    (marged[len(marged) - 1] + marged[len(marged) - 2]) / 2)
            target1 = nums1[indexOfNums1]
            target2 = nums2[indexOfNums2]
            if target1 >= target2:
                marged.append(target2)
                indexOfNums2 += 1
            else:
                marged.append(target1)
                indexOfNums1 += 1
