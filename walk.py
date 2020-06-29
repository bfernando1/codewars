#! python3

def is_valid_walk(walk):
    """Determines if a person returns back from
       their 10 minute walking route" 

    Args: 
        List contaning n, s, e, w

    Returns:
        Boolean

    Usage: 
        >>> python3 is_valid_walk(['n', 's', 'n'])
            False 
    """
    time = {
            'n':  1,
            's': -1,
            'e':  1,
            'w': -1
            }
    count = {}

    for w in walk:
            count.setdefault(w, 0)
            count[w] = count[w] + 1

    if len(walk) is not 10:
        return False
    elif count.get('n', 0) != count.get('s', 0)  or \
         count.get('e', 0) != count.get('w', 0):
        return False
    return True if sum([time[w] for w in walk]) is 0 else False 
