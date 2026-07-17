from data_cleaning import clean_data
from visualization import create_charts

def main():

    print("=" * 50)
    print("DATA CLEANING & VISUALIZATION PROJECT")
    print("=" * 50)

    # Clean the dataset
    df = clean_data()

    # Create visualizations
    create_charts(df)

    print("\nProject Completed Successfully!")

if __name__ == "__main__":
    main()