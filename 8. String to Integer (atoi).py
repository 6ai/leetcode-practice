# ls

import re

class Solution:
    INT_MAX = 2**31 - 1
    INT_MIN = (-1) * 2**31
    
    def myAtoi(self, str: str) -> int:
        regexp = r'\s*(?P<before_num>[^\d+-]*)(?P<sign>[-+]?)(?P<num>\d+)'
        m = re.match(regexp, str)
        if m:
            groupdict = m.groupdict()
            print(groupdict)
            num = int(groupdict['sign'] + groupdict['num'])
            num = min(self.INT_MAX, num) if num >= 0 else max(self.INT_MIN, num)
            before_num = groupdict['before_num']

            return num if (before_num == '') else 0
        return 0

