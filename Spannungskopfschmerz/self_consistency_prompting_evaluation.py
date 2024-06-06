from collections import Counter

# lists of medications
benchmark_medications = ["capsicum", "acetaminophen", "calfactant", "poractant alfa", "dinoprost",
                         "peppermint oil", "almitrine", "lasmiditan", "colfosceril palmitate",
                         "acetazolamide", "atogepant", "dihydrocodeine", "guaifenesin", "promethazine",
                         "tripelennamine", "mirtazapine", "hypochlorite", "hydromorphone", "margetuximab", "tofacitinib"]

llm_generated_medications_1 = ["Acetaminophen", "Aspirin", "Butalbital", "Caffeine", "Carisoprodol", "Chlorzoxazone",
               "Clonidine", "Cyclobenzaprine", "Dexibuprofen", "Flurbiprofen", "Gabapentin", "Hydrocodone",
               "Ibuprofen", "Ketorolac", "Metoclopramide", "Naproxen", "Oxycodone", "Propoxyphene",
               "Tricyclic antidepressants", "Voltaren"]

llm_generated_medications_2 = ["Acetaminophen", "Aspirin", "Butalbital", "Caffeine", "Codeine", "Clonazepam",
               "Dexibuprofen", "Diclofenac", "Flunitrazepam", "Gabapentin", "Imitrex", "Ketorolac",
               "Loratadine", "Meclizine", "Naproxen", "Ondansetron", "Pregabalin", "Propranolol",
               "Quetiapine", "Risperidone", "Tramadol", "Valerian", "Venlafaxine", "Xanax"]

llm_generated_medications_3 = ["Acetaminophen", "ibuprofen", "naproxen sodium", "Nortriptyline", "desipramine",
               "protriptyline", "mirtazapine", "amitriptyline", "venlafaxine", "Diclofenac potassium",
               "Volatern", "ketorolac tromethamine", "indomethacin", "meloxicam", "celecoxib",
               "rofecoxib"]

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