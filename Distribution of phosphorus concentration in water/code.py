import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('covstack.csv', encoding='gbk')
# Extract the phosphorus concentration column
phosphorus = data['PH']
# Create a histogram
plt.hist(phosphorus, bins=10, edgecolor='black')

# Add labels and title
plt.xlabel('Phosphorus Concentration')
plt.ylabel('Frequency')
plt.title('Distribution of Phosphorus Concentrations in Great Barrier Reef Water')

# Display the graph
plt.show()
