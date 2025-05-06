import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# In this script I have used a sample sales dataset from kaggle

try:
    # Task 1: Loading & exploring the dataset
    # Loading the dataset
    file_path = 'Sample - Superstore.csv'
    df = pd.read_csv(file_path, encoding='ISO-8859-1') # reading the csv file

    # Display the first few rows
    print("First 5 rows:")
    print(df.head())

    # Check data types and missing values
    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    # Drop rows with missing values (if any)
    df.dropna(inplace=True)

    # Convert date columns
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])


    # Task 2: Basic statistics
    print("\nDescriptive statistics:")
    print(df[['Sales', 'Quantity', 'Discount', 'Profit']].describe())

    # Group by Region and Category
    region_group = df.groupby('Region')['Sales'].mean()
    category_group = df.groupby('Category')['Sales'].mean()

    print("\nAverage sales by Region:")
    print(region_group)

    print("\nAverage sales by Category:")
    print(category_group)


    # Task 3: Data Visualization
    sns.set(style="whitegrid")

    # 1. Line Chart – Sales over Time
    df_daily = df.groupby('Order Date')['Sales'].sum().reset_index()
    plt.figure(figsize=(10, 5))
    plt.plot(df_daily['Order Date'], df_daily['Sales'], color='blue')
    plt.title('Daily Sales Over Time')
    plt.xlabel('Order Date')
    plt.ylabel('Total Sales')
    plt.tight_layout()
    plt.show()

    # 2. Bar Chart – Average Sales per Category
    plt.figure(figsize=(6, 4))
    sns.barplot(x=category_group.index, y=category_group.values, palette='Set2')
    plt.title('Average Sales per Category')
    plt.xlabel('Category')
    plt.ylabel('Average Sales')
    plt.tight_layout()
    plt.show()

    # 3. Histogram – Sales Distribution
    plt.figure(figsize=(6, 4))
    sns.histplot(df['Sales'], bins=50, kde=True, color='orange')
    plt.title('Distribution of Sales')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    # 4. Scatter Plot – Sales vs. Profit
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='Sales', y='Profit', hue='Category', data=df, alpha=0.6)
    plt.title('Sales vs. Profit by Category')
    plt.xlabel('Sales')
    plt.ylabel('Profit')
    plt.legend(title='Category')
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
