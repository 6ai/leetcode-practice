# 551. Student Attendance Record I

class Solution:
    def checkRecord(self, s: str) -> bool:
        hadAbsent = False
        for index in range(len(s)):
            if s[index] == 'A':
                if hadAbsent:
                    return False
                else:
                    hadAbsent = True
            elif index > 1 and s[index - 2: index + 1] == 'LLL':
                return False
        return True
        