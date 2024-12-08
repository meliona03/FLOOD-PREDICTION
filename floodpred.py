import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")


flood_counts = df.groupby(['STATE', 'DISTRICT'])['FLOOD'].sum()
print(flood_counts)
flood_counts.to_csv('flood_counts_by_state_and_district.csv', index=True)

flood_status_counts = df['FLOOD'].value_counts()  # Count of flood vs no flood

# Plot the bar chart
plt.figure(figsize=(8, 6))
flood_status_counts.plot(kind='bar', color=['g', 'r'], label='Flood Status')
plt.title('Flood vs No Flood Counts', fontsize=16)
plt.xlabel('Flood Status (0 = No Flood, 1 = Flood)', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=0)
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()

yearly_rainfall = df.groupby('YEAR')['ANNUAL RAINFALL'].sum().reset_index()
plt.figure (figsize= (10,6))
plt.plot(yearly_rainfall["YEAR"], yearly_rainfall["ANNUAL RAINFALL"], marker='o', linestyle='-', color='b', label='Total Annual Rainfall')

plt.title('Annual Rainfall vs Year', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Annual Rainfall (mm)', fontsize=14)

plt.grid(True)

plt.show()

#hello
