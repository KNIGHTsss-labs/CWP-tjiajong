st = ""
for i in range(0, 11):
    st = f"Table de {i}:"
    for j in range(0, 11):
        st += f" {j*i}"
    print(st)