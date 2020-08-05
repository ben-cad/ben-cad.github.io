from Bio import GenBank
from Bio import SeqIO


gbk_filename = ["JD2.gbk"]

for x in gbk_filename:
    faa_filename = x[:-4]

    input_handle  = open(x, "r")
    output_handle = open(x[:-4], "w")

    for seq_record in SeqIO.parse(input_handle, "genbank") :
        for seq_feature in seq_record.features :
            if seq_feature.type=="CDS" :
                assert len(seq_feature.qualifiers['translation'])==1
                output_handle.write(">%s from %s\n%s\n" % (
                       seq_feature.qualifiers['locus_tag'][0]  + " " + seq_feature.qualifiers['product'][0],
                       seq_record.name,
                       seq_feature.qualifiers['translation'][0]))

output_handle.close()
input_handle.close()
