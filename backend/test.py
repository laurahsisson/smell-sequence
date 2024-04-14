import recommendation
import time
import json

seq = []
for gen in range(12):
  s = time.perf_counter()
  res = json.loads(json.dumps(recommendation.get(3,seq,["mine"])))
  print(f"Gen = {gen} w/ dosage = {res['dosage']} in {time.perf_counter()-s:.2}")
  for i,r in enumerate(res["options"]):
    print(i,r)
  print()
  print()
  seq.append(res["options"][0])
