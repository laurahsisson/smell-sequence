import recommendation
import time
import json

# seq = []
# for gen in range(12):
#   s = time.perf_counter()
#   res = json.loads(json.dumps(recommendation.get(3,seq)))
#   print(f"Gen = {gen} in {time.perf_counter()-s:.2}")
#   for i,r in enumerate(res):
#     print(i,r)
#   print()
#   print()
#   seq.append(res[0])

recommendation.get(3,[])