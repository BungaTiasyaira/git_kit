def inverse(seq):
    return seq[::-1]

def complement(seq):
    mapping = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
    out = str()

    for nt in seq:
        out += mapping[nt]
    
    return out