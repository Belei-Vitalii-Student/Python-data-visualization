import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('GoogleApps.csv')
    app_size_frequency(df)
    installs_to_rating(df)
    columns_to_apps_count(df)


def app_size_frequency(df):
    plt.figure(figsize=(10, 6))
    df['Size'].hist(bins=30)
    plt.xlabel('App Size (Mb)')
    plt.ylabel('Frequency')
    plt.title('Distribution of App Sizes')
    plt.show()

def installs_to_rating(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Installs'], df['Rating'])
    plt.xlabel('Installs')
    plt.ylabel('Rating')
    plt.title('Installs vs Rating')
    plt.show()

def columns_to_apps_count(df):
    plt.figure(figsize=(12, 6))
    df['Category'].value_counts().plot(kind='pie')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Number of Apps per Category')
    plt.xticks(rotation=90)
    plt.show()

main()