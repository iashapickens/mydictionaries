"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $60,000



"""

import json
import pandas as pd

with open("school_data.json", "r") as file:
    data = json.load(file)

df = pd.json_normalize(data)

conference_codes = [372, 108, 107, 130]

#Report 1
report1 = df[
    (df["NCAA.NAIA conference number football (IC2020)"].isin(conference_codes)) &
    (df["Graduation rate  women (DRVGR2020)"] > 75)
]
print("=== Universities with Graduation Rate for Women > 75% ===")
print(report1[["instnm", "Graduation rate  women (DRVGR2020)"]])

#Report 2
report2 = df[
    (df["NCAA.NAIA conference number football (IC2020)"].isin(conference_codes)) &
    (df["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 60000)
]
print("\n=== Universities with Total In-State Price (Off Campus, Not with Family) > $60,000 ===")
print(report2[["instnm", "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]])

