def to_rna(dna_strand):
    # The translation table 
    trans_table = str.maketrans("GCTA", "CGAU")

    return dna_strand.translate(trans_table).upper()
