from collections import Counter

# lists of medications
benchmark_medications = ["calfactant", "carbon dioxide", "temsirolimus", "helium", "colfosceril palmitate",
                         "lapatinib", "sotorasib", "trilaciclib", "paclitaxel", "amivantamab", "gemcitabine",
                         "trabectedin", "human papillomavirus type 31 L1 capsid protein antigen",
                         "human papillomavirus type 45 L1 capsid protein antigen",
                         "human papillomavirus type 52 L1 capsid protein antigen", "necitumumab",
                         "sipuleucel-T", "repotrectinib", "strontium chloride Sr-89",
                         "human papillomavirus type 18 L1 capsid protein antigen"]

llm_generated_medications_1 = ["Taxotere", "Avastin", "Alimta", "Tarceva", "Xalkori", "Zykadia", "Osimertinib",
               "Opdivo", "Navelbine", "Gemcitabine", "Platinol-AQ", "Abraxane", "Erbitux",
               "Pembrolizumab"]

llm_generated_medications_2 = ["Taxotere/docetaxel", "Tarceva/erlotinib", "Navelbine/vinorelbine", "Alimta/pemetrexed",
               "Gemzar/gemcitabine", "docetaxel", "erlotinib", "vinorelbine", "pemetrexed", "gemcitabine"]

llm_generated_medications_3 = ["Camptothecins", "irinotecan", "topotecan", "Vinca alkaloids", "vincristine", "vinblastine",
               "Taxanes", "docetaxel", "paclitaxel", "Platinum agents", "cisplatin", "carboplatin",
               "Etoposide", "Immunotherapy", "interferon", "interleukin-2", "Tyrosine kinase inhibitors",
               "imatinib", "sunitinib", "Monoclonal antibodies", "bevacizumab", "cetuximab"]

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