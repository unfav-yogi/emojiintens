import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv(
    r"C:\Users\yoeshwar\OneDrive\Desktop\internships\emojivietualwork\Test_external_data.csv",
    engine="python",
    on_bad_lines='skip'
)

df2 = pd.read_csv(
    r"C:\Users\yoeshwar\OneDrive\Desktop\internships\emojivietualwork\Test_external_data_2.csv",
    engine="python",
    on_bad_lines='skip'
)

df3 = pd.read_csv(
    r"C:\Users\yoeshwar\OneDrive\Desktop\internships\emojivietualwork\Train_external_data.csv",
    engine="python",
    on_bad_lines='skip'
)

df4 = pd.read_csv(
    r"C:\Users\yoeshwar\OneDrive\Desktop\internships\emojivietualwork\Train_external_data_2.csv",
    engine="python",
    on_bad_lines='skip'
)

df = pd.concat([df1, df2, df3, df4], ignore_index=True)

print(df.head())

print(df.columns)

print(df.info())

print(df.isnull().sum())

df = df.dropna()

numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

print(numeric_columns)

if len(numeric_columns) > 0:

    for col in numeric_columns:

        plt.figure(figsize=(10,5))

        sns.histplot(df[col], kde=True)

        plt.title(f"{col} Distribution")

        plt.show()

    correlation = df[numeric_columns].corr()

    if not correlation.empty:

        plt.figure(figsize=(12,8))

        sns.heatmap(correlation, annot=True)

        plt.title("Correlation Heatmap")

        plt.show()

    for col in numeric_columns[:5]:

        plt.figure(figsize=(10,5))

        sns.boxplot(x=df[col])

        plt.title(f"{col} Boxplot")

        plt.show()

    if len(numeric_columns) >= 2:

        plt.figure(figsize=(10,6))

        sns.scatterplot(
            x=df[numeric_columns[0]],
            y=df[numeric_columns[1]]
        )

        plt.title(f"{numeric_columns[0]} vs {numeric_columns[1]}")

        plt.show()

else:

    print("No numeric columns found in dataset")

print("PROJECT COMPLETED SUCCESSFULLY")