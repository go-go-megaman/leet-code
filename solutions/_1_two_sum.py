class Solution:
    def main(self, numbers: [int], target: int) -> [int]:
        numbers_dict = {}
        for index, number in enumerate(numbers):
            paired_number = target - number
            if paired_number in numbers_dict.keys():
                return [numbers_dict[paired_number], index]
            numbers_dict[number] = index

        raise ValueError("There is no pair their sum equals to target.")
