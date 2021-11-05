import random as r
heads = 0
tails = 0
heads_tails = 0
while heads + tails != 100:
    heads_tails = r.choice(["Tail", "Head"])
    if heads_tails == "Tail":
        tails += 1
    if heads_tails == "Head":
        heads += 1

print(f"Tails: {tails} Heads: {heads}")
