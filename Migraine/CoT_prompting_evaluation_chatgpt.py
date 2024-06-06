# lists of medications
benchmark_medications = ["ibuprofen", "atogepant", "eptinezumab", "lasmiditan", "acetaminophen", "frovatriptan",
                         "timolol", "tibolone", "ubidecarenone", "diltiazem", "atenolol", "indomethacin",
                         "metoclopramide", "tramadol", "acetylsalicylic acid", "caffeine", "galcanezumab",
                         "erenumab", "rimegepant", "ubrogepant"]

llm_generated_medications = ["Acetaminophen", "Amitriptyline", "Aspirin", "Butalbital-Acetaminophen-Caffeine",
              "Calcium channel blockers", "Capsaicin", "Carisoprodol", "Clonazepam",
              "Combination analgesics", "Combination NSAIDs", "Combination triptans", "Dexibuprofen",
               "Dihydrocodeine", "Diclofenac", "Gabapentin", "Ibuprofen", "Naproxen", "Nortriptyline",
              "Oxygen therapy", "Triptan combination"]

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