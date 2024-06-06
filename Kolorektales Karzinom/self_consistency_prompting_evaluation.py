from collections import Counter

# lists of medications
benchmark_medications = ["trametinib", "sotorasib", "irinotecan", "oxaliplatin",
                         "human papillomavirus type 31 L1 capsid protein antigen",
                         "human papillomavirus type 45 L1 capsid protein antigen",
                         "human papillomavirus type 52 L1 capsid protein antigen", "sipuleucel-T",
                         "human papillomavirus type 18 L1 capsid protein antigen", "polydatin",
                         "tibolone", "panitumumab", "leucovorin", "vinflunine", "temsirolimus",
                         "efbemalenograstim alfa", "asciminib", "titanium dioxide", "paclitaxel", "mesalazine"]

llm_generated_medications_1 = ["Adriamycin", "Taxol", "FOLFOX", "XELOX", "CAP", "Cetuximab", "Panitumumab", "Bevacizumab"]

llm_generated_medications_2 = ["5-Fluorouracil", "Oxaliplatin", "Irinotecan", "Cetuximab", "Leucovorin", "Fluorouracil",
               "Irinotecan", "Leucovorin", "Fluorouracil", "Oxaliplatin", "Bevacizumab(AVAC)", "Panitumumab",
               "Etoposide", "Cisplatin", "Sunitinib", "Temsirolimus", "Erlotinib", "Bortezomib",
               "Vemurafenib", "Sorafenib", "Pemetrexed", "Docetaxel", "Capecitabine",
               "Carboplatin / paclitaxel", "Everolimus", "Trametinib", "RAD001"]

llm_generated_medications_3 = ["Metronidazole", "Ciprofloxacin", "Amoxicillin", "Cephalosporins", "Clindamycin",
               "Trimethoprim-Sulfamethoxazole", "Nitrofurantoin", "Aminoglycosides", "Vancomycin",
               "Enzymes", "Levofloxacin", "Tetracycline", "Minocycline", "Erythromycin", "Penicillin",
               "Azithromycin", "Augmenting", "Beta-lactams", "Dexamethasone", "Minoxidil", "Probiotics",
               "Antibiotics", "Antihistamines", "Corticosteroids", "Immunotherapy", "Radiation therapy",
               "Surgery", "Chemotherapy", "Antimetabolites", "Tocopherol", "Fusidic acid"]

# combine all drugs and convert them to lower
llm_medications_all = llm_generated_medications_1 + llm_generated_medications_2 + llm_generated_medications_3
llm_medications_all_lower = [med.lower() for med in llm_medications_all]

# Count the frequency of each medication
med_counter = Counter(llm_medications_all_lower)

# Choose the 20 most common medications
most_common_medications = [med for med, count in med_counter.most_common(20)]

# convert the list to set
benchmark_set = set(med.lower() for med in benchmark_medications)
llm_set = set(most_common_medications)

#find matching medication
common_medications = benchmark_set.intersection(llm_set)

#numbers of matching medication
number_common_medications = len(common_medications)

#Output
print(most_common_medications)
print(f"{number_common_medications} out of {len(benchmark_medications)} Medications agree.")
print(f"Common Medications: {', '.join(common_medications)}")