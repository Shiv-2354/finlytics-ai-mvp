import pandas as pd

# Define the input and output filenames
RAW_DATA_FILE = 'financials_raw.csv'
DATABASE_FILE = 'database.csv'


def process_data():
    """
    Reads raw company data, calculates revenue per worker,
    and saves it to a clean CSV file.
    """
    try:
        # Step 1: Read the raw data from the user-provided CSV
        # Assuming the CSV has columns: 'company', 'workers', 'revenue'
        df = pd.read_csv(RAW_DATA_FILE)

        # --- Data Validation ---
        # Ensure required columns exist
        required_cols = ['company', 'workers', 'revenue']
        if not all(col in df.columns for col in required_cols):
            print(f"Error: Your CSV is missing one of the required columns: {required_cols}")
            return

        # --- Analysis Engine ---
        # Calculate Revenue per Worker.
        # Handle cases where 'workers' might be zero to avoid division errors.
        df['revenue_per_worker'] = 0.0  # Initialize the column
        # Use .loc to safely perform the calculation on rows where 'workers' is not 0
        df.loc[df['workers'] != 0, 'revenue_per_worker'] = df['revenue'] / df['workers']

        # Round the result to a whole number for clarity
        df['revenue_per_worker'] = df['revenue_per_worker'].round(0).astype(int)

        # --- Save to Database ---
        # Reorder columns for the final clean database file
        output_df = df[['company', 'workers', 'revenue', 'revenue_per_worker']]
        output_df.to_csv(DATABASE_FILE, index=False)

        print(f"✅ Successfully processed data and created '{DATABASE_FILE}'")
        print("\nHere's a preview of your new database:")
        print(output_df.head())

    except FileNotFoundError:
        print(f"❌ Error: The input file '{RAW_DATA_FILE}' was not found in this directory.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# This block ensures the function runs only when the script is executed directly
if __name__ == "__main__":
    process_data()

Bash

python create_database.py
