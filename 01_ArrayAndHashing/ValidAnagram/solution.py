def isAnagram(s1, s2):
    # 両方の文字列をソートして比較
    return sorted(s1) == sorted(s2)