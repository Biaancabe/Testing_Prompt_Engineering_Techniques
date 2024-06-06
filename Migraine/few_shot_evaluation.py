# lists of medications
benchmark_medications = ["ibuprofen", "atogepant", "eptinezumab", "lasmiditan", "acetaminophen", "frovatriptan",
                         "timolol", "tibolone", "ubidecarenone", "diltiazem", "atenolol", "indomethacin",
                         "metoclopramide", "tramadol", "acetylsalicylic acid", "caffeine", "galcanezumab",
                         "erenumab", "rimegepant", "ubrogepant"]

llm_generated_medications = ["Acetaminophen", "Tylenol", "DHE", "Imitrex", "sumatriptan", "Maxalt", "rizatriptan", "Zomig",
                             "zolmitriptan", "Verapamil",  "calcium channel blocker", "Naproxen", "Aleve", "Fioricet",
                             "butalbital", "acetaminophen", "caffeine", "Midrin", "aspirin", "butalbital", "caffeine",
                             "Inderal", "propranolol", "Propranolol", "Inderal LA", "Depakote", "valproate", "Topamax", "topiramate",
                             "Acetaminophen", "Tylenol", "Aspirin", "Naproxen", "Imitrex", "Maxalt", "Fioricet", "Butalbital-APAP",
                             "Propranolol", "Indomethacin", "Topamax", "Gabapentin", "Mecobalamine", "Methysergide", "Verapamil",
                             "Prednisone", "Triptans", "DexibuProfen", "Pizotifen", "Caffeine", "Amitriptyline", "Elavil",
                             "Divalproex sodium", "Depakote", "Topiramate", "Topamax", "Sumatriptan", "Imitrex", "Alprazolam",
                             "Xanax", "Metoprolol tartrate", "Lopressor", "Propranolol", "Inderal", "Naproxen", "Naprosyn",
                             "Ketorolac tromethamine", "Toradol", "Diclofenac potassium", "Cataflam", "Acetaminophen", "Tylenol",
                             "Butalbital-APAP", "Fioricet", "Sertraline HCl", "Zoloft", "Fluoxetine hydrochloride", "Prozac",
                             "Venlafaxine hydrochloride", "Effexor", "Meclizine HCl", "Antivert", "Ondansetron", "Zofran",
                             "Diphenhydramine HCl", "Benadryl", "Aspirin", "Bayer"
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