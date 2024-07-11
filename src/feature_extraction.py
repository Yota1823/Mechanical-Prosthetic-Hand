#Code to extract features from data.
import pandas as pd

def extract_features(file_path):
    # Load preprocessed data
    data = pd.read_csv(file_path)
    
    # Extract features (in this case, just the muscle voltage)
    X = data[['muscle_voltage']]
    
    # Define target (servo positions)
    y = data[['servo_position']]
    
    return X, y

if __name__ == "__main__":
    X, y = extract_features('../data/processed/muscle_data.csv')
    print(X.head(), y.head())
