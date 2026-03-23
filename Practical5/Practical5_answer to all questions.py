import matplotlib.pyplot as plt

# -----------------------------
# TASK 1: Gene Expression Analysis
# -----------------------------

# Step 1: Create initial dictionary
gene_expression = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}

print("Initial gene dictionary:")
print(gene_expression)

# Step 2: Add MYC gene
gene_expression["MYC"] = 11.6

print("\nUpdated gene dictionary:")
print(gene_expression)

# Step 3: Query a gene
selected_gene = "TP53"  # 可以改成你想查询的

if selected_gene in gene_expression:
    print(f"\nThe expression value of {selected_gene} is {gene_expression[selected_gene]}.")
else:
    print(f"\nError: {selected_gene} is not in the dataset.")

# Step 4: Calculate average
average_expression = sum(gene_expression.values()) / len(gene_expression)
print(f"\nThe average gene expression level is {average_expression:.2f}.")

# Step 5: Bar chart
plt.figure(figsize=(8, 5))
plt.bar(gene_expression.keys(), gene_expression.values())
plt.title("Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.show()


# -----------------------------
# TASK 2: Heart Rate Analysis
# -----------------------------

heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# Step 1: Count patients and average
num_patients = len(heart_rates)
mean_heart_rate = sum(heart_rates) / num_patients

print(f"\nThere are {num_patients} patients in the dataset, and the mean heart rate is {mean_heart_rate:.2f} bpm.")

# Step 2: Categorize heart rates
low = 0
normal = 0
high = 0

for rate in heart_rates:
    if rate < 60:
        low += 1
    elif 60 <= rate <= 120:
        normal += 1
    else:
        high += 1

print(f"Low heart rate: {low}")
print(f"Normal heart rate: {normal}")
print(f"High heart rate: {high}")

# Step 3: Find largest category
categories = {
    "Low": low,
    "Normal": normal,
    "High": high
}

largest_category = max(categories, key=categories.get)
print(f"The largest category is {largest_category}.")

# Step 4: Pie chart
plt.figure(figsize=(6, 6))
plt.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
plt.title("Distribution of Heart Rate Categories")
plt.show()


# -----------------------------
# TASK 3: Population Growth Analysis
# -----------------------------

population_data = {
    "UK": (66.7, 69.2),
    "China": (1426, 1410),
    "Italy": (59.4, 58.9),
    "Brazil": (208.6, 212.0),
    "USA": (331.6, 340.1)
}

# Step 1: Calculate percentage change
population_change = {}

for country, (pop2020, pop2024) in population_data.items():
    change = ((pop2024 - pop2020) / pop2020) * 100
    population_change[country] = change

print("\nPopulation percentage changes:")
for country, change in population_change.items():
    print(f"{country}: {change:.2f}%")

# Step 2: Sort from largest increase to largest decrease
sorted_population_change = dict(
    sorted(population_change.items(), key=lambda item: item[1], reverse=True)
)

print("\nPopulation changes from largest increase to largest decrease:")
for country, change in sorted_population_change.items():
    print(f"{country}: {change:.2f}%")

# Step 3: Identify largest increase and decrease
countries = list(sorted_population_change.keys())

largest_increase = countries[0]
largest_decrease = countries[-1]

print(f"\nThe country with the largest increase is {largest_increase}.")
print(f"The country with the largest decrease is {largest_decrease}.")

# Step 4: Bar chart
plt.figure(figsize=(8, 5))
plt.bar(sorted_population_change.keys(), sorted_population_change.values())
plt.title("Population Change by Country")
plt.xlabel("Country")
plt.ylabel("Population Change (%)")
plt.show()