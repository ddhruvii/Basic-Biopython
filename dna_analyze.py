def analyze_dna(dna_sequence):
    dna_sequence = dna_sequence.upper()
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    total_bases = len(dna_sequence)    
    gc_content = ((g_count + c_count) / total_bases) * 100 if total_bases > 0 else 0
    mrna_sequence = dna_sequence.replace('T', 'U')
    print(f"Original DNA Sequence: {dna_sequence}")
    print(f"Transcribed mRNA     : {mrna_sequence}")
    print(f"Total Base Count     : {total_bases} bp")
    print(f"GC Content Percentage: {gc_content:.2f}%")
sample_dna = "ATGCGATCGATCGATCGATCGATCGATC"
analyze_dna(sample_dna)
