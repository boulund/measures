# Measures

Cloned from `ragrawal/measures`.

Added a small script, `compare_lists.py`, that implements the `RBO` and
`AverageOverlap` algorithms. The script prints simple comparisons between
lists.

## Example output
Here's what it could look like, comparing two dissimilar taxonomic composition
estimates from two mock metagenomes:

```
Comparing 'mg2_1_pe.kaiju.family' with 'mg1_1_pe.kaiju.family'               
--------------------                                                         
  1 | Prevotellaceae                 | Methanosaetaceae                      
  2 | Ruminococcaceae                | Syntrophomonadaceae                   
  3 | Rikenellaceae                  | Spirochaetaceae                       
  4 | Odoribacteraceae               | Peptococcaceae                        
  5 | Oscillospiraceae               | Ruminococcaceae                       
  6 | Porphyromonadaceae             | Moraxellaceae                         
  7 | Lachnospiraceae                | Methanospirillaceae                   
  8 | Clostridiaceae                 | =                                     
  9 | Paenibacillaceae               | Streptomycetaceae                     
 10 | Peptococcaceae                 | Sphingomonadaceae                     
 11 | Lactobacillaceae               | Flavobacteriaceae                     
 12 | Streptococcaceae               | Rhodocyclaceae                        
 13 | Desulfovibrionaceae            | Mycobacteriaceae                      
 14 | Veillonellaceae                | Porphyromonadaceae                    
 15 | Listeriaceae                   | Comamonadaceae                        
 16 | Akkermansiaceae                | Hyphomicrobiaceae                     
 17 | Bacillaceae                    | Rikenellaceae                         
 18 | Thermoanaerobacterales Family III. Incertae Sedis | Desulfovibrionaceae
 19 | Enterobacteriaceae             | Synergistaceae                        
 20 | Thermoanaerobacterales Family IV. Incertae Sedis | Paenibacillaceae    
 21 | Selenomonadaceae               | Streptococcaceae                      
 22 | Bacteroidaceae                 | Thermoanaerobacteraceae               
 23 | Thermoanaerobacteraceae        | Listeriaceae                          
 24 | Flavobacteriaceae              | Xanthomonadaceae                      
 25 | Alcanivoracaceae               | Geobacteraceae                        
Average Overlap score (only 25 first entries):  0.24834274513270338          
Rank Biased Overlap score (entire list):        0.39854413004654143          
--------------------                                                         
```
The two lists are different in most positions.

Here's another example, comparing two similar taxonomic composition estimates
from two mock metagenomes:

```
Comparing 'mock_1_1.kaiju.genus' with 'mock_1_2.kaiju.genus'
--------------------
  1 | Propionibacterium              | =
  2 | Actinomyces                    | =
  3 | Bacteroides                    | =
  4 | Deinococcus                    | =
  5 | Clostridium                    | =
  6 | Bacillus                       | =
  7 | Lactobacillus                  | =
  8 | Listeria                       | =
  9 | Staphylococcus                 | =
 10 | Enterococcus                   | =
 11 | Streptococcus                  | =
 12 | Streptomyces                   | =
 13 | Sanguibacter                   | =
 14 | Chlamydia                      | =
 15 | Parabacteroides                | =
 16 | Xylanimonas                    | =
 17 | Bifidobacterium                | =
 18 | Rhodococcus                    | =
 19 | Mycobacterium                  | =
 20 | Corynebacterium                | =
 21 | Catenibacterium                | =
 22 | Rhodobacter                    | =
 23 | Bradyrhizobium                 | =
 24 | Rothia                         | =
 25 | Micromonospora                 | =
Average Overlap score (only 25 first entries):  1.0
Rank Biased Overlap score (entire list):        0.9853397172523548
--------------------
```

Here you can see the two ranked lists are very similar. The differ only in
positions somewhere below #25.
