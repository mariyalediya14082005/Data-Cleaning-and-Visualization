import pandas as pd
import os

def clean_data():

    # Create output folder if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Load dataset
    df = pd.read_csv("dataset/Superstore.csv", encoding="latin1")

    print("=" * 50)
    print("DATASET LOADED SUCCESSFULLY")
    print("=" * 50)

    # Display first 5 rows
    print(df.head())

    # Dataset information
    print("\nDataset Information")
    print(df.info())

    # Missing values
    print("\nMissing Values")
    print(df.isnull().sum())

    # Fill missing numeric values with mean
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    # Fill missing text values with mode
    text_cols = df.select_dtypes(include="object").columns
    for col in text_cols:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])

    # Remove duplicate rows
    duplicate_count = df.duplicated().sum()
    print(f"\nDuplicate Rows Found: {duplicate_count}")

    df = df.drop_duplicates()

    # Remove outliers using IQR
    for col in numeric_cols:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        df = df[(df[col] >= lower) & (df[col] <= upper)]

    # Save cleaned dataset
    df.to_csv("output/cleaned_data.csv", index=False)

    print("\nCleaned dataset saved successfully.")

    return df