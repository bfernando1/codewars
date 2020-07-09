#! python3

def countBits(n):
    """Count the bits in the binary string

    Args: 
         non-negative base-10 number 

    Returns: 
        total number of bits 

    Examples:
        >>> countBits(7)
            3
    """
    return bin(n).count('1') 
