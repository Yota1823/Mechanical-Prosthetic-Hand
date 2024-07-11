import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load the data
data = pd.read_csv('../data/processed/muscle_data.csv')

# Feature extraction
X = data[['muscle_voltage']]
y = data[['servo_position']]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, '../models/servo_model.pkl')

# Evaluate the model
score = model.score(X_test, y_test)
print(f"Model Score: {score}")
