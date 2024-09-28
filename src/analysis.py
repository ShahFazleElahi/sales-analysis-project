import numpy as np

def calculate_statistics(df):
    """Calculate average revenue and standard deviation."""
    average_revenue = np.mean(df['Revenue'])
    std_deviation_revenue = np.std(df['Revenue'])
    return average_revenue, std_deviation_revenue

def target_summary(df):
    """Calculate summary of target achievement."""
    target_met_count = df['Target_Met'].value_counts()
    return target_met_count
