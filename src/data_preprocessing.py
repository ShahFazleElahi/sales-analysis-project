import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """Preprocess data (e.g., calculate target achievement)."""
    df['Target_Met'] = df['Products_Sold'] >= df['Target_Sales']
    return df
