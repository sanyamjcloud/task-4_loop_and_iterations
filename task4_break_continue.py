print("Task 4: Break and Continue example")
for i in range(1, 11):
    if i == 5:
        print("Skipping number 5")
        continue  # Skip number 5
    if i == 8:
        print("Stopping at number 8")
        break  # Stop loop at 8
    print(i)
print()
