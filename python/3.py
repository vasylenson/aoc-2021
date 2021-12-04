'''
Copyrigth Marko Vasylenko 2021 to present

I mean look at this horrendous mess...
'''

from typing import List


with open('input/3.in', 'r') as in_file:
    inputs = list(map(str.strip, in_file.readlines()))

INPUT_WIDTH = len(inputs[0])

def gamma_and_epsilon(nums: list[str]) -> tuple[str, str]:
    gamma = [0] * len(nums[0])
    for num in nums:
        for ind, symbol in enumerate(num):
            if symbol == '1':
                gamma[ind] += 1
            elif symbol == '0':
                gamma[ind] -= 1
            else:
                print(f'opppsie, {symbol}')
    gammastr = ''.join('1' if val >= 0 else '0' for val in gamma)
    epsilstr = ''.join('0' if val >= 0 else '1' for val in gamma)

    gammanum = int(gammastr, 2)
    epsilnum = int(epsilstr, 2)
    return gammanum,epsilnum


def get_oxygen(nums: list[str]) -> str:
    nums = nums[:]  # get nums by copy to avoid in place mutation
    INPUT_WIDTH = len(nums[0])

    for bit in range(INPUT_WIDTH):
        if len(nums) == 1:
            return nums[0]
        bit_set = [val for val in nums if val[bit] == '1']
        bit_unset = [val for val in nums if val[bit] == '0']
        nums = bit_set if len(bit_set) >= len(bit_unset) else bit_unset

    return nums[0]


def get_oxygen(nums: list[str]) -> str:
    nums = nums[:]  # get nums by copy to avoid in place mutation
    INPUT_WIDTH = len(nums[0])

    for bit in range(INPUT_WIDTH):
        if len(nums) == 1:
            return nums[0]
        bit_set = [val for val in nums if val[bit] == '1']
        bit_unset = [val for val in nums if val[bit] == '0']
        nums = bit_set if len(bit_set) >= len(bit_unset) else bit_unset

    return nums[0]


oxygen = get_oxygen(inputs)

bit = 0
carbonnums = inputs[:]
while len(carbonnums) > 1:
    bit_set = []
    bit_unset = []
    for num in carbonnums:
        if num[bit] == '1':
            bit_set.append(num)
        elif num[bit] == '0':
            bit_unset.append(num)
    carbonnums = bit_unset if len(bit_set) >= len(bit_unset) else bit_set
    bit += 1

gamma, epsil = gamma_and_epsilon(inputs)
print(f'Part 1: {gamma * epsil}')

oxigennum = int(oxygen, 2)
carbonnum = int(carbonnums, 2)

print(oxigennum * carbonnum)