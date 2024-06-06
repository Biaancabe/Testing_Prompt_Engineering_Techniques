from collections import Counter

# lists of medications
benchmark_medications = ["wormwood", "coal tar", "salicylic acid", "colloidal oatmeal", "spesolimab",
                         "deucravacitinib", "brodalumab", "acitretin", "desoximetasone", "clobetasol", "alefacept",
                         "methoxsalen", "octasulfur", "tazarotene", "clobetasone", "flumethasone", "halcinonide",
                         "clobetasol propionate", "alitretinoin", "difluocortolone"]

llm_generated_medications_1 = ["Methotrexate", "cyclosporine", "retinoids", "salicylic acid", "coal tar", "phototherapy",
               "methylprednisolone pulses", "Biologics", "etanercept", "adalimumab", "infliximab",
               "acitretin", "ustekinumab", "Calcitriol", "etretinate", "acitretin", "methoxsalen",
               "anthralin", "calcipotriene"]

llm_generated_medications_2 = ["Methotrexate", "Cyclosporine", "Acitretin", "Biologic agents", "etanercept", "infliximab",
               "Topical steroids", "calcitriol", "salicylic acid", "anthralin cream", "Retinoids",
               "tazarotene", "acitretin", "Phototherapy", "PUVA", "NBUVB", "Oral immunosuppressants",
               "mycophenolate mofetil", "cyclophosphamide"]

llm_generated_medications_3 = ["Methotrexate", "Cyclosporine", "Biologics", "etanercept", "adalimumab", "infliximab"]


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