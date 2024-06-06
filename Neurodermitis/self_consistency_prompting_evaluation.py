from collections import Counter

# lists of medications
benchmark_medications = ["borage oil", "beclomethasone", "dipropionate"]

llm_generated_medications_1 = ["Topical steroids", "mometasone furoate cream", "clobetasol propionate cream",
               "topical calcineurin inhibitors", "pimecrolimus cream", "tacrolimus ointment",
               "oral antihistamines", "cetirizine", "levocetirizine", "oral corticosteroids",
               "prednisolone", "dexamethasone"]

llm_generated_medications_2 = ["Methotrexate", "Tacrolimus", "Pimecrolimus", "Topical steroid", "Oral steroid",
               "Cyclosporine", "Calcitriol", "Antibiotics", "Antihistamines", "Immunomodulators",
               "Trigger point injections", "Phototherapy", "Probiotic", "Antifungals", "Antidepressants",
               "Systemic corticosteroids", "Oral immunomodulators"]

llm_generated_medications_3 = ["Topical steroids", "mometasone", "fluticasone cream", "Topical calcineurin inhibitors",
               "pimecrolimus", "tacrolimus ointment", "Oral antihistamines", "cetirizine", "fexofenadine",
               "Topical immunomodulators", "tacrolimus", "pimecrolimus ointments", "Oral antibiotics",
               "azithromycin", "clarithromycin", "Anti-inflammatory painkillers", "ibuprofen", "diclofenac",
               "Topical moisturizers", "Antifungals", "fluconazole", "ketoconazole", "Corticosteroids"]

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