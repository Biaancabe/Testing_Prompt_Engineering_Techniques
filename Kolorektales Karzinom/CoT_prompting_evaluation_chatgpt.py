# lists of medications
benchmark_medications = ["trametinib", "sotorasib", "irinotecan", "oxaliplatin",
                         "human papillomavirus type 31 L1 capsid protein antigen",
                         "human papillomavirus type 45 L1 capsid protein antigen",
                         "human papillomavirus type 52 L1 capsid protein antigen", "sipuleucel-T",
                         "human papillomavirus type 18 L1 capsid protein antigen", "polydatin",
                         "tibolone", "panitumumab", "leucovorin", "vinflunine", "temsirolimus",
                         "efbemalenograstim alfa", "asciminib", "titanium dioxide", "paclitaxel", "mesalazine"]

llm_generated_medications = []

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