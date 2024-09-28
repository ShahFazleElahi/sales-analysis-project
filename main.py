from src.data_preprocessing import load_data, preprocess_data
from src.analysis import calculate_statistics, target_summary
from src.visualization import plot_products_sold, plot_revenue, plot_target_summary

def main():
    # Load data
    df = load_data('data/sales_data.csv')
    
    # Preprocess data
    df = preprocess_data(df)
    
    # Calculate statistics
    average_revenue, std_deviation_revenue = calculate_statistics(df)
    print(f'Average Revenue: {average_revenue}')
    print(f'Standard Deviation of Revenue: {std_deviation_revenue}')
    
    # Target achievement summary
    target_count = target_summary(df)
    print(target_count)
    
    # Visualize results
    plot_products_sold(df)
    plot_revenue(df)
    plot_target_summary(target_count)

if __name__ == '__main__':
    main()
