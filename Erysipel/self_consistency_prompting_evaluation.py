from collections import Counter

# lists of medications
benchmark_medications = ["neratinib", "phenoxymethylpenicillin", "betula pendula tar oil"]

llm_generated_medications_1 = ["Antibiotics", "Fluoroquinolones", "Ciprofloxacin", "Tetracyclines", "Doxycycline",
               "Minocycline", "Topical antibiotic creams", "Clobetasol Propionate", "Clotrimazole",
               "Anti-inflammatory painkillers", "Naproxen", "Ibuprofen", "Corticosteroids",
               "Non-steroidal anti-inflammatory", "Diclofenac", "Antivirals", "Valacyclovir",
               "Immunosuppressants", "Cyclosporine", "Antidepressants", "Antihistamines", "HY Chat Doctor"]

llm_generated_medications_2 = ["Antibiotics", "cephalosporins", "penicillin", "Anti-inflammatory agents", "NSAIDs",
               "Corticosteroids", "Topical antibiotics", "topical anesthetics",
               "Local application of antihistamines", "Painkillers", "Skin moisturizers", "Antioxidants",
               "Antifungals", "Antivirals"]

llm_generated_medications_3 = ["Topical antibiotics", "clindamycin", "mupirocin", "Oral antibiotics", "doxycycline",
               "erythromycin", "Anti-inflammatories", "ibuprofen"]

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