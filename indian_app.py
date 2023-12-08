import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Disable the warning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load data
file_path = r'C:\Users\Zaki\Desktop\streamlitint\company\indian-cities-dataset.csv'
data = pd.read_csv(file_path)

# Sidebar for filtering
st.sidebar.header("Filter Data")

# Calculate average distance
avg_dis = data['Distance'].mean()

# Display average distance
st.sidebar.write(f"Average Distance: {avg_dis:.2f} units")

# Calculate maximum and minimum distances
max_dis = data['Distance'].max()
min_dis = data['Distance'].min()

# Display maximum and minimum distances
st.sidebar.write(f"Maximum Distance: {max_dis} units")
st.sidebar.write(f"Minimum Distance: {min_dis} units")

# Identify city pairs with the highest and lowest distances
max_distance_row = data[data['Distance'] == max_dis]
min_distance_row = data[data['Distance'] == min_dis]

# Display city pairs with maximum and minimum distances
st.sidebar.write(f"City Pair with Maximum Distance: {max_distance_row['Origin'].values[0]} to {max_distance_row['Destination'].values[0]}")
st.sidebar.write(f"City Pair with Minimum Distance: {min_distance_row['Origin'].values[0]} to {min_distance_row['Destination'].values[0]}")

# Display the first 30 rows of the dataset
st.write("Top 30 Rows of the Dataset:")
st.write(data.head(30))

# Create a bar chart for distances
st.subheader("Distances Between Cities (Top 10)")
top_cities = data.groupby(['Origin', 'Destination']).mean().sort_values(by='Distance', ascending=False).head(10)

# Plotting bar chart using matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(top_cities.index.map(lambda x: f"{x[0]} to {x[1]}"), top_cities['Distance'])
ax.set_xticklabels(top_cities.index.map(lambda x: f"{x[0]} to {x[1]}"), rotation=45, ha='right')
ax.set_xlabel('City Pair')
ax.set_ylabel('Distance')
ax.set_title('Distances Between Cities (Top 10)')
st.pyplot(fig)

# Create a pie chart for distance distribution
st.subheader("Distance Distribution")
distance_distribution = data.groupby('Destination')['Distance'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(8, 8))
plt.pie(distance_distribution, labels=distance_distribution.index, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
st.pyplot()