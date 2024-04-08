import recommendation
import time

seq = []
for gen in range(12):
  s = time.perf_counter()
  res = recommendation.get(3,seq)
  print(f"Gen = {gen} in {time.perf_counter()-s:.2}")
  for i,r in enumerate(res):
    print(i,r)
  print()
  print()
  seq.append(res[0])