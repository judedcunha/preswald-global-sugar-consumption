from preswald import text, plotly, connect, get_df, table, slider
import pandas as pd
import plotly.express as px

text("# Welcome!")
text("Basic table")


# Load the CSV
connect() # load in all sources, which by default is the sample_csv
dataset_name="sugar_consumption_dataset_csv"
df = get_df(dataset_name)

# Filter the DataFrame to include only necessary columns
df = df[['Country', 'Year', 'Continent', 'Region', 'Avg_Daily_Sugar_Intake']]


text("Scatter Plot")

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

text("Slider with Sugar Intake Values")


#Slider 
threshold_value_column="Avg_Daily_Sugar_Intake"
threshold = slider("Threshold", min_val=0, max_val=200, default=50)
table(df[df[threshold_value_column] > threshold], title="Daily Sugar Intake")


