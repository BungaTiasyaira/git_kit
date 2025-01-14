def inverse(seq):
    return seq[::-1]

def to_rna(seq):
    out = ""
    for nt in seq:
        if nt == 'T':
            out += 'U'
        else:
            out += nt
    
    return out

def from_rna(seq):
    out = ""
    for nt in seq:
        if nt == 'U':
            out += 'T'
        else:
            out += nt

def complement(seq):
    mapping = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
    out = str()

    for nt in seq:
        out += mapping[nt]
    
    return out