from typing import List


class Solution:

    def duplicate_zeros(self, arr: List[int]):
        zeroAcum = 0
        last = 0
        arrayLen = len(arr) - 1 # 0

        for idx, value in enumerate(arr):
            if value == 0 and idx + zeroAcum < arrayLen:
                zeroAcum += 1 #0
                last = idx #4

        for _ in arr:
            if arrayLen is not 0:
                arr[arrayLen] = arr[arrayLen - zeroAcum]
                if arr[arrayLen] == 0 and zeroAcum > 0 and arrayLen - zeroAcum <= last:
                    arr[arrayLen - 1] = 0
                    zeroAcum -= 1
                    arrayLen -= 1
                arrayLen -= 1
