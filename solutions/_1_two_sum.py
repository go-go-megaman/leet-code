class Solution:
    def main(self, numbers: [int], target: int) -> [int]:
        numbers_dict = {number: True for number in numbers}

        for number in numbers:
            paired_number = target - number
            exists = paired_number in numbers_dict.keys()
            if exists:
                return [number, paired_number]

        raise ValueError("There is no pair their sum equals to target.")
