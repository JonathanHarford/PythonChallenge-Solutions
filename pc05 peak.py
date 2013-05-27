# http://www.pythonchallenge.com/pc/def/peak.php
import pickle
with open("pc05 banner.p") as f: p = pickle.load(f)
for row in p:
    print("".join([n*ch for ch, n in row]))
    
