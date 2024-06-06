from collections import Counter

# lists of medications
benchmark_medications = ["capsicum", "acetaminophen", "dinoprost", "lasmiditan", "atogepant", "dihydrocodeine",
                         "tripelennamine", "ritlecitinib", "margetuximab", "peppermint oil", "tofacitinib",
                         "metyrosine", "fomepizole", "guaifenesin", "triprolidine", "lumefantrine",
                         "teplizumab", "esomeprazole", "isoetharine", "penciclovir"]

llm_generated_medications_1 = ["Verapamil", "calcium channel blocker", "Methysergide", "5HT1 agonist", "Imitrex",
               "sumatriptan", "Lidocaine", "Propranolol", "beta blocker", "Pizotifen", "Oxygen therapy"]

llm_generated_medications_2 = ["Acyclovir", "Amitriptyline", "Atomoxetine", "Azithromycin", "Benzoic Acid", "Beta Blockers",
               "Bupropion", "Calcium Carbimide", "Camphene", "Cyclobenzaprine", "Dexamethasone",
               "Dihydroergotamine", "Dopamine Agonists", "Flunarizine", "Gabapentin", "Imipramine",
               "Isometheptene Mast Cell Stabilizers", "Magnesium Sulfate", "Nalbuphine", "Narcotics",
               "Naproxen", "Niacin", "Opioids", "Pregabalin", "Propranolol", "Quinine", "Sertraline",
               "Sodium Valproate", "Sumatriptan", "Topiramate", "Tranylcypromine", "Verapamil",
               "Venlafaxine", "Zolmitriptan"]

llm_generated_medications_3 = ["Acetaminophen", "Alprazolam", "Amitriptyline", "Brompheniramine", "Carbinoxamine",
               "Celecoxib", "Clonazepam", "Cyclobenzaprine", "Desipramine", "Dihydroergotamine",
               "Dicyclomine", "Erythromycin", "Gabapentin"]

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