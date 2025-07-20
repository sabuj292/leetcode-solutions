
def mergeAlternately(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """

    len1 = len(word1)
    len2 = len(word2)
    merged = ""
    i = 0
    j = 0

    #merge untill one of the strings end
    while i < len1 and j < len2 :
        merged += word1[i] + word2[j]
        i += 1
        j += 1
    
    #if word1 is longer
    if i < len1:
        merged += word1[j:]

    #if word2 is longer
    if j < len2:
        merged += word2[i:]

    return merged

