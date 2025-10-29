with open("Vm_list_25th_Aug_Prod.txt") as f:
    lines = [line.strip() + ";" for line in f if line.strip()]
for line in lines:
    print(line)
