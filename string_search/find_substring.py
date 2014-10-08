"""
Check if substring exists in word
"""

def simple_subsearch(word, pattern):
    """
    Check if the substring exists
    """
    n = len(word)
    m = len(pattern)
    import ipdb; ipdb.set_trace() 
    for i in range(n - m+1):
        if pattern == word[i: i + m]:
            return "Substring present: {} in {}".format(word[i: i + m], word)
    
    return "pattern does not exists"


word = "pattern"
sub = "ern"
print simple_subsearch(word=word, pattern=sub)
