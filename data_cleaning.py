import pandas
import pandas as pd
import sklearn
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Load the dataset
df = pd.read_csv("Data_Cleaning/books_raw.csv")

# Display dataset information
print(df.info())

# Display the first five rows
print(df.head())

# Display column names
print(df.columns)


# Check for missing values
print(df.isnull().sum())


# Check for duplicate rows
duplicate_count = df.duplicated().sum()
print("Number of duplicate rows:", duplicate_count)
duplicates = df[df.duplicated()]
print(duplicates)


# Remove duplicate rows 
df = df.drop_duplicates()
print("Dataset shape after removing duplicates:", df.shape)

# Display current data types
print("\nCurrent Data Types:")
print(df.dtypes)



# Keep only digits and decimal points
df["Price"] = df["Price"].str.replace(r"[^0-9.]", "", regex=True)

# Convert to float
df["Price"] = pd.to_numeric(df["Price"])
print(df["Price"].head())
print(df.dtypes)



# Convert ratings to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

print("\nUpdated Rating Column:")
print(df["Rating"].head())

print("\nUpdated Data Types:")
print(df.dtypes)



#checking unique value availability
print("\nUnique values in Availability:")
print(df["Availability"].unique())


# encoding the availabity to 1 or 0
df["Availability"] = df["Availability"].map({
    "In stock": 1,
    "Out of stock": 0
})

print("\nUpdated Availability Column:")
print(df["Availability"].head())
print("\nUpdated Data Types:")
print(df.dtypes)

#statistics Summary
print("\nSummary Statistics:")
print(df["Price"].describe())

#Q1 and Q3 calculation
Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

#IQR calculation
IQR = Q3 - Q1
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

# Lower and upper limits
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

# Finding outliers
outliers = df[
    (df["Price"] < lower_bound) |
    (df["Price"] > upper_bound)
]

print("\nNumber of outliers:", len(outliers))
print(outliers)

# dataset dimensions
print(df.shape)

# Normalizing the Price column
scaler = MinMaxScaler()
df["Price_Normalized"] = scaler.fit_transform(df[["Price"]])
print("\nNormalized Price:")
print(df[["Price", "Price_Normalized"]].head())

# Save the cleaned dataset
df.to_csv("books_cleaned.csv", index=False)


