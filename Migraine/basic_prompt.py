# lists of medications
benchmark_medications = ["ibuprofen", "atogepant", "eptinezumab", "lasmiditan", "acetaminophen", "frovatriptan",
                         "timolol", "tibolone", "ubidecarenone", "diltiazem", "atenolol", "indomethacin",
                         "metoclopramide", "tramadol", "acetylsalicylic acid", "caffeine", "galcanezumab",
                         "erenumab", "rimegepant", "ubrogepant"]

llm_generated_medications = ["Propranolol", "Amitriptyline", "Gabapentin", "Topiramate", "Valproic acid", "Metoprolol",
             "Clonazepam", "Divalproex sodium" ,"Timolol", "Diclofenac sodium", "Flunarizine",
             "Acetaminophen", "Tricyclic antidepressants", "Serotonin receptor agonists", "Ondansetron",
             "Pizotifen", "Verapamil", "Alprazolam", "Nortriptyline"]

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