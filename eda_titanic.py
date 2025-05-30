# eda_titanic.py
# Task 1: EDA and Visualization of Titanic Dataset

# ─────────────────────────────
# Step 1: Load the Dataset
# ─────────────────────────────
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Load CSV
df = pd.read_csv("./Titanic_Dataset.csv")

# Show first few rows
print("First 5 rows:\n", df.head())

# Show info and stats
print("\nDataset Info:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe(include='all'))

# ─────────────────────────────
# Step 2: Data Cleaning
# ─────────────────────────────

# Missing Values
print("\nMissing Values Before Cleaning:\n", df.isnull().sum())

# Fill 'Age' with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill 'Embarked' with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop 'Cabin' due to too many nulls
df.drop(columns=['Cabin'], inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Outlier detection (Fare column)
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Fare'] < Q1 - 1.5 * IQR) | (df['Fare'] > Q3 + 1.5 * IQR)]
print(f"\nNumber of Outliers in Fare: {len(outliers)}")

# ─────────────────────────────
# Step 3: Visualizations
# ─────────────────────────────

# Bar Charts for Categorical Variables
categorical_cols = ['Sex', 'Pclass', 'Embarked', 'Survived']
for col in categorical_cols:
    plt.figure()
    sns.countplot(x=col, data=df)
    plt.title(f"{col} Count")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# Histograms for Numerical Variables
numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']
for col in numeric_cols:
    plt.figure()
    plt.hist(df[col], bins=20, edgecolor='black')
    plt.title(f"{col} Distribution")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# Correlation Heatmap (Only numeric features)
plt.figure(figsize=(10, 6))
corr_matrix = df.select_dtypes(include=['float64', 'int64']).corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# ─────────────────────────────
# Step 4: Summary of Insights
# ─────────────────────────────
print("\n🧠 Summary of Key Insights:")
print("- Majority of passengers were male.")
print("- Most passengers were in 3rd class.")
print("- Survival rate appears higher for females.")
print("- Age is right-skewed, with many younger passengers.")
print("- Fare values contain outliers with some very high prices.")
print("- Strong positive correlation between Parch and SibSp (family aboard).")
