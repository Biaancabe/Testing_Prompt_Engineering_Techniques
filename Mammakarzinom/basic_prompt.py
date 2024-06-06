# lists of medications
benchmark_medications = ["efbemalenograstim alfa", "fluoroestradiol", "pertuzumab", "fluoroestradiol f-18",
                         "asciminib", "tibolone", "palbociclib", "fulvestrant", "toremifene", "paclitaxel",
                         "capivasertib", "gemcitabine", "trastuzumab", "thiotepa", "vinblastine", "trabectedin",
                         "anastrozole", "neratinib", "norethisterone", "eribulin"]

llm_generated_medications = ["Tamoxifen", "Paget's disease", "Trastuzumab", "Cyclophosphamide", "Doxorubicin", "Docetaxe",
              "Epirubicin", "Fluorouracil", "Methotrexate", "Etoposide", "Cisplatin", "Carboplatin",
              "Vinblastine", "Vincristine", "Mitomycin", "Melphalan", "Leuprolide", "Interferon",
              "Taxol"]
#llm_generated_medications = ["tamoxifen", "5-fluorouracil", "adriamycin", "melphalan"]

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