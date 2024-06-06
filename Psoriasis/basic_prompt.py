# lists of medications
benchmark_medications = ["wormwood", "coal tar", "salicylic acid", "colloidal oatmeal", "spesolimab",
                         "deucravacitinib", "brodalumab", "acitretin", "desoximetasone", "clobetasol", "alefacept",
                         "methoxsalen", "octasulfur", "tazarotene", "clobetasone", "flumethasone", "halcinonide",
                         "clobetasol propionate", "alitretinoin", "difluocortolone"]

llm_generated_medications = ["Methotrexate", "Cyclosporine A", "Acitretin", "Anthralin cream",
             "Salicylic acid", "Coal tar", "Tacrolimus ointment", "UVB phototherapy", "etanercept",
             "adalimumab", "infliximab"]

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