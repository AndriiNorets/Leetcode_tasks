class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine_list = list(magazine)
        for item in ransomNote:
            if item not in magazine_list:
                return False
            magazine_list.remove(item)

        return True
        