import pandas as pd

def preprocess_data(file_path):
    # Load raw data
    data = pd.read_csv(file_path)
    
    # Perform any necessary preprocessing steps, e.g., filtering, normalization
    data['muscle_voltage'] = data['muscle_voltage'] / data['muscle_voltage'].max()
    
    # Save processed data
    processed_file_path = file_path.replace('raw', 'processed')
    data.to_csv(processed_file_path, index=False)
    
    return processed_file_path

if __name__ == "__main__":
    preprocess_data('../data/raw/muscle_data_raw.csv')
