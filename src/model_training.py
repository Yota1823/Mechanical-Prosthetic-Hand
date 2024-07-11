#Code for training machine learning models.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def train_model(X, y):
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

if __name__ == "__main__":
    data_file = '../data/processed/muscle_data.csv'
    data = pd.read_csv(data_file)
    X, y = data[['muscle_voltage']], data[['servo_position']]
    train_model(X, y)
