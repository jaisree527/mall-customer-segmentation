import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("Mall_Customers.csv")
# Print first 5 rows
print(df.head())
# Scatter plot
plt.scatter(
    df['Annual Income (k$)'],
    df['Spending Score (1-100)']
)
# Labels
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
# Title
plt.title("Mall Customer Segmentation")
# Show graph
plt.show()
