class Solution:
    def main(self, numbers: [int], target: int) -> [int]:
        numbers_dict = {}
        for number in numbers:
            paired_number = target - number
            exists = paired_number in numbers_dict.keys()
            if exists:
                return [paired_number, number]
            numbers_dict[number] = True

        raise ValueError("There is no pair their sum equals to target.")
