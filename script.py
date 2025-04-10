from preswald import text, plotly, connect, get_df, table
import pandas as pd
import plotly.express as px

text("# Welcome to Preswald!")
text("This is your first app. 🎉")


# Load the CSV
connect() # load in all sources, which by default is the sample_csv
dataset_name="sugar_consumption_dataset_csv"
df = get_df(dataset_name)

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

