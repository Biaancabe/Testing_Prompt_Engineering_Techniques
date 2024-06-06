# lists of medications
benchmark_medications = ["neratinib", "phenoxymethylpenicillin", "betula pendula tar oil"]

llm_generated_medications = ["neomycin sulfate", "bacitracin neomycin", "penicillin G", "erythromycin base", "fusidic acid", "chloramphenicol",
                             "minocycline", "clindamycin", "cephalexin", "metronidazole", "lincomycin", "bacitracin", "ciprofloxacin",
                             "ciprofloxacin citrate", "clindamycin phosphate", "trimethoprim", "erythromycin base", "doxycycline",
                             "chloramphenicol phosphate", "tetracycline hydrochloride", "doxycycline tetracycline monohydrate", "rifampicin",
                             "oxytetracycline", "Amoxicillin", "Citrate Citrate", "Probiotics", "Bacitracin", "Calcium Carborate", "Magnesium Carborrhoea Malate",
                             "Ceftriaxone", "Sulfinpyrazone", "Ceftizoxam", "Cephalexin", "Cephradine Penicillin sodium", "Cefuroxime", "Sulfamethoxazole-trimethoprim",
                             "Ceftriaxone sodium", "Vancomycin", "Metronidazole", "Amoxicillin-Gentamicin", "Amoxicillin", "clavulanic Acid", "Ceftolozane",
                             "Sulbactam-Metronidazole", "neomycin", "tetracycline", "trimethoprim", "sulfamethoxazole", "gentamicin", "clotrimazole",
                             "minocycline", "doxycyline", "diphenoxylate", "novocaine", "diphenoxylate", "metoclopramide", "clorsultine",
                             "phenotiazine", "penicillin G", "ampicillin", "erythromycin", "penicillin V", "doxycycline", "doxycycline hyclate", "azithromycin",
                             "vancomycin"]
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