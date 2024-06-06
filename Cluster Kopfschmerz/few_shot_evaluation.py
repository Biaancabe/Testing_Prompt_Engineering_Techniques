# lists of medicationsfew_shot_evaluation.py
benchmark_medications = ["capsicum", "acetaminophen", "dinoprost", "lasmiditan", "atogepant", "dihydrocodeine",
                         "tripelennamine", "ritlecitinib", "margetuximab", "peppermint oil", "tofacitinib",
                         "metyrosine", "fomepizole", "guaifenesin", "triprolidine", "lumefantrine",
                         "teplizumab", "esomeprazole", "isoetharine", "penciclovir"]

llm_generated_medications = ["Verapamil", "Isoptin", "Propranolol", "Inderal", "Methysergide Maleate", "Sergide", "Flunarizine",
                             "Floxeril", "Sodium valproate", "Depakene", "Topiramate", "Topamax", "Gabapentin", "Neurontin",
                             "Oxygen inhalation", "Lidocaine", "Xylocaine", "Paracetamol", "Tylenol", "Nortriptyline", "Pamelor",
                             "Tricyclic antidepressants", "amitriptyline", "nortriptyline", "desipramine", "Beta-blockers",
                             "metoprolol", "propranolol", "Botox injection", "Capsaicin", "Melatonin"]

# convert the list to set
benchmark_set = set(med.lower() for med in benchmark_medications)
llm_set = set(med.lower() for med in llm_generated_medications)

#find matching medication
common_medications = benchmark_set.intersection(llm_set)

#numbers of matching medication
number_common_medications = len(common_medications)

#Output
print(f"{number_common_medications} out of {len(benchmark_medications)} Medications agree.")
print(f"Common Medications: {', '.join(common_medications)}")