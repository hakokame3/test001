import os
import csv

aa=[["トップガン","Risky Business","Minority Report"], ["タイタニック","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

with open("C:\\data\\test096_01.csv","w",encoding="shift_jis",newline="") as f:
    w=csv.writer(f,delimiter=",")
    for m in aa:
          w.writerow(m)

