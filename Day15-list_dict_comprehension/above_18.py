a=[12,34,31,19,44,3,18]
b=[f"Eligibe-{i}" if i>=18 else f"Not Eligible-{i}" for i in a]
print(b)
