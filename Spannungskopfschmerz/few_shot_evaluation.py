# lists of medications
benchmark_medications = ["capsicum", "acetaminophen", "calfactant", "poractant alfa", "dinoprost",
                         "peppermint oil", "almitrine", "lasmiditan", "colfosceril palmitate",
                         "acetazolamide", "atogepant", "dihydrocodeine", "guaifenesin", "promethazine",
                         "tripelennamine", "mirtazapine", "hypochlorite", "hydromorphone", "margetuximab", "tofacitinib"]

llm_generated_medications =  ["Acetaminophen", "Tylenol", "Nonsteroidal", "anti-inflammatory", "chats doctores", "NSAIDs", "ibuprofen",
                              "Advil", "naproxen", "Aleve", "ketorolac", "Toradol", "diclofenac", "Voltaren", "Opioids", "oxycodone",
                              "OxyContin", "hydrocodone", "Vicodin", "codeine", "carisoprodol", "Soma", "cyclobenzaprine", "Flexeril",
                             "amitriptyline", "Elavil", "nortriptyline", "Pamelor", "Anticonvulsants", "gabapentin", "Neurontin",
                             "pregabalin", "Lyrica"
]

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