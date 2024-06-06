from collections import Counter

# lists of medications
benchmark_medications = ["ibuprofen", "atogepant", "eptinezumab", "lasmiditan", "acetaminophen", "frovatriptan",
                         "timolol", "tibolone", "ubidecarenone", "diltiazem", "atenolol", "indomethacin",
                         "metoclopramide", "tramadol", "acetylsalicylic acid", "caffeine", "galcanezumab",
                         "erenumab", "rimegepant", "ubrogepant"]

llm_generated_medications_1 = ["acetaminophen", "acetaminophen", "dipyrone", "dipyrone", "dimenhydrinate", "metamizol",
                               "diclofenac", "sodium", "Diclofenac", "ibuprofen", "hydrocodone", "bitartrate", "hydrocodone",
                               "protolazine", "promectin", "meperidine", "caffeine", "decarbazine", "dipivaloate", "protolazone",
                               "dextropropoxyphene", "Flumazenil", "dihydrocodeine", "didrophonium", "chloride", "oxcarbazepine",
                               "oxcarbazepine", "clonazepam", "Diamcinonide", "hydrocodone", "hydrochloride", "oxycodone", "hydrochloride",
                               "oxycodone", "hydrochloride", "propoxyphene", "dihydrochloride", "droperidol", "hydromorphone", "oxycodone",
                               "hydrochloride", "oxycodone", "hydrochloride", "hydrocodone", "bitartrate", "acetaminophen", "oxycodone", "acetaminophen",
                               "hydrocodone", "tartrate", "oxycodone", "acetaminophen", "oxybutynin", "succinate", "oxybutynin", "oxiloilofrine",
                               "guanabenz", "levoproxyphene", "hydrochloride", "oxybutynin", "tartrate", "diphenhydramine", "maleate",
                               "dimenhydrinate", "dichloride", "triptans", "dolasetron", "codeine", "phosphate", "codeine", "sulfate", "morphine",
                               "phosphate", "codeine", "hydromorphone", "morphine", "sulfate", "oxitropium", "bromide", "scopolamine",
                               "hydrobromide", "sumatriptan", "serotonin", "receptor", "agonist", "dihydroergotamine", "maleate",
                               "sumatriptan", "hemihydrate", "butyrophenone", "citrate", "oxybemiphene", "citrate", "tramadol",
                               "hydrochloride", "tramadol", "hydrochloride", "ibuprofen", "codeine", "phosphate", "codeine", "phosphate",
                               "codeine", "phosphate", "codeine", "sulfate", "ibuprofen", "aspirin", "acetylsalicylic acid", "acetaminophen",
                               "aspirin plus acetaminophen", "aspirin", "acetaminophen", "triptans", "antiepileptics", "ergots",
                               "antidepressants", "calcium antagonists", "tricyclic antidepressants", "lithium", "calcium channel blockers",
                               "anticonvulsants", "potassium channel blockers", "benzodiazepines", "phenothiazines", "monoamine oxidase inhibitors",
                               "lithium", "nonsteroidal anti-inflammatory drugs", "neuroleptics", "local anaesthetics", "topical anaesthetics",
                               "tricyclic antidepressants", "lithium", "beta blockers", "NSAIDs", "oral contraceptives", "acetaminophen", "paracetamol",
                               "aspirin", "butalbital", "butorphanol tartrate", "chlorpheniramine maleate", "metoclopramide", "dihydroergotamine tartrate",
                               "droperidol", "prochlorperazine hydrochloride", "phenformin tartrate", "dextropropoxyphene", "promethazine hydrochloride",
                               "phenelzine hydrochloride", "lorazepam", "midazolam", "diphenhydramine", "hydroxyzine sodium", "amitriptyline hydrochloride"]

llm_generated_medications_2 =  ["Acetaminophen", "Aspirin", "Naproxen", "Imitrex", "Maxalt", "Fioricet", "Butalbital-APAP",
               "Propranolol", "Indomethacin", "Topamax", "Gabapentin", "Mecobalamine", "Methysergide",
               "Verapamil", "Prednisone", "Triptans", "DexibuProfen", "Pizotifen", "Caffeine"]

llm_generated_medications_3 =  ["Amitriptyline", "Divalproex sodium", "Topiramate", "Sumatriptan", "Alprazolam",
               "Metoprolol tartrate", "Propranolol", "Naproxen", "Ketorolac tromethamine",
               "Diclofenac potassium", "Acetaminophen", "Butalbital-APAP", "Sertraline HCl", "Fluoxetine hydrochloride",
               "Venlafaxine hydrochloride", "Meclizine HCl", "Ondansetron", "Diphenhydramine HCl", "Aspirin"]

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