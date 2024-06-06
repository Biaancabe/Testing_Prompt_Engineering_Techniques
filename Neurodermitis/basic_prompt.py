# lists of medications
benchmark_medications = ["borage oil", "beclomethasone", "dipropionate"]

llm_generated_medications = ["Mild steroid cream", "HY Chat Doctor", "Topical immunomodulators", "tacrolimus",
              "pimecrolimus", "Oral antihistamines", "antibiotics", "Oral corticosteroids"]

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