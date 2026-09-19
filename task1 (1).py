import pandas as pd
df = pd.read_excel("Delinquency_prediction_dataset (1) (1).CSV")
print(df.isnull().sum())
print("Duplicate Records:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
numeric_cols = df.select_dtypes(include=["number"]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())
# Fill categorical missing values with mode
categorical_cols = df.select_dtypes(include=["object"]).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])
df.to_csv("Cleaned_Delinquency_Dataset.csv", index=False)
print("Data cleaning completed successfully!")