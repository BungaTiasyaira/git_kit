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
    
    return out