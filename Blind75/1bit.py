def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1   # check last bit
        n >>= 1          # shift right
    return count