import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
df = sns.load_dataset("titanic")

# Explore dataset
print("First 5 rows:\n", df.head())
print("\nSummary statistics:\n", df.describe(include="all"))
print("\nMissing values:\n", df.isnull().sum())

# Visualization
sns.countplot(x="survived", data=df)
plt.title("Survival Count")
plt.show()

sns.histplot(data=df, x="age", kde=True, bins=30)
plt.title("Age Distribution")
plt.show()

# ------------------- Preprocessing -------------------

# Drop missing values (create explicit copy to avoid warning)
df = df.dropna(subset=["age", "embarked"]).copy()

# Encode categorical values
le_sex = LabelEncoder()
le_embarked = LabelEncoder()

df["sex"] = le_sex.fit_transform(df["sex"])
df["embarked"] = le_embarked.fit_transform(df["embarked"])

# Scale numerical features
scaler = StandardScaler()
df[["age", "fare"]] = scaler.fit_transform(df[["age", "fare"]])

print("\nPreprocessed Data:\n", df.head())
