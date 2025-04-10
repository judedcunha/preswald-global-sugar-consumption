from preswald import text, plotly, connect, get_df, table, slider, query, text_input
import pandas as pd
import plotly.express as px

text("# Welcome!")
text("### Basic table")


# Load the CSV
connect() # load in all sources, which by default is the sample_csv
dataset_name="sugar_consumption_dataset_csv"
df = get_df(dataset_name)

# Filter the DataFrame to include only necessary columns
df = df[['Country', 'Year', 'Continent', 'Region', 'Avg_Daily_Sugar_Intake']]


text("### Scatter Plot")

table(df, title="Global Sugar Data")

# Create a scatter plot
fig = px.scatter(df, 
                x='Year', 
                y='Avg_Daily_Sugar_Intake',
                labels={
                    'Year': 'Year', 
                    'Avg_Daily_Sugar_Intake': 'Average Daily Sugar Intake (g)'
                })
# Show the plot
plotly(fig)
text("There don't seem to be any outliers present in this data, however if they were present they could be imputed through various methods using numpy")


text("### Slider with Sugar Intake Values")


#Slider 
threshold_value_column="Avg_Daily_Sugar_Intake"
threshold = slider("Threshold", min_val=0, max_val=200, default=50)
table(df[df[threshold_value_column] > threshold], title="Daily Sugar Intake")


# SQL Time

# Basic table retrieval
 
sql = "SELECT Country, Year, Avg_Daily_Sugar_Intake  FROM sugar_consumption_dataset_csv"
filtered_df = query(sql, "sugar_consumption_dataset_csv")
text("# Just Country, Year and Sugar Intake filtered using SQL")
table(filtered_df, title="Filtered Data")




# Enter the Country and get it's details

# Basic text input
name = text_input(label="Enter a country", placeholder="India")
name="India"
sql = f"SELECT Country, Year, Avg_Daily_Sugar_Intake  FROM sugar_consumption_dataset_csv WHERE Country='{name}'"
filtered_df = query(sql, "sugar_consumption_dataset_csv")
text("# Specific Country")
table(filtered_df, title="Filtered Data")
