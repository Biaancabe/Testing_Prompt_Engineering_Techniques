# lists of medications
benchmark_medications = ["neratinib", "phenoxymethylpenicillin", "betula pendula tar oil"]

llm_generated_medications = ["Intravenous penicillin G", "intravenous cephalosporins", "Oral antibiotics",
             "Amoxicillin", "Cefuroxime", "Cephalexin"]

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