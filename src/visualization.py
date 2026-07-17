import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_charts(df):

    os.makedirs("output", exist_ok=True)

    # Histogram
    plt.figure(figsize=(6,4))
    plt.hist(df["Sales"], bins=20)
    plt.title("Sales Distribution")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.savefig("output/histogram.png")
    plt.close()

    # Bar Chart
    plt.figure(figsize=(8,5))
    df["Category"].value_counts().plot(kind="bar")
    plt.title("Products by Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.savefig("output/bar_chart.png")
    plt.close()

    # Pie Chart
    plt.figure(figsize=(6,6))
    df["Region"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Sales by Region")
    plt.ylabel("")
    plt.savefig("output/pie_chart.png")
    plt.close()

    # Scatter Plot
    plt.figure(figsize=(6,4))
    plt.scatter(df["Sales"], df["Profit"])
    plt.title("Sales vs Profit")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.savefig("output/scatter_plot.png")
    plt.close()

    # Box Plot
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df["Sales"])
    plt.title("Sales Box Plot")
    plt.savefig("output/box_plot.png")
    plt.close()

    # Heatmap
    plt.figure(figsize=(8,6))
    sns.heatmap(df.select_dtypes(include="number").corr(),
                annot=True,
                cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("output/heatmap.png")
    plt.close()

    print("\nAll charts created successfully.")