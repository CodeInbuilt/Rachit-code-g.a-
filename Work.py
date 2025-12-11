import pandas as pd
import numpy as np

# Fetch dataset from CMU repository
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

# Reconstruct data and target
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

# Feature names
columns = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", 
    "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
]

# Build DataFrame
df = pd.DataFrame(data, columns=columns)
df["PRICE"] = target

# Show top 50 rows
df.head(50)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import math

# --- Load Boston Housing dataset ---
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

columns = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", 
    "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
]

df = pd.DataFrame(data, columns=columns)
df["PRICE"] = target

# --- Train/Test Split ---
X = df.drop("PRICE", axis=1)
y = df["PRICE"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Train Linear Regression ---
model = LinearRegression()
model.fit(X_train, y_train)

# --- Evaluate ---
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = math.sqrt(mean_squared_error(y_test, y_pred))

print(f"Model Performance:\nR² = {r2:.4f}\nRMSE = {rmse:.4f}")

# --- Prediction Function ---
def predict_price():
    print("\nEnter values for the 13 features to predict house price:\n")
    user_input = {}
    for col in columns:
        val = float(input(f"Enter {col}: "))
        user_input[col] = val
    
    input_df = pd.DataFrame([user_input])
    pred_price = model.predict(input_df)[0]
    print(f"\n🏠 Predicted House Price: ${pred_price*1000:,.2f} ")

# Example usage (uncomment to run interactively in Colab)
# predict_price()


