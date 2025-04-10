from preswald import text, plotly, connect, get_df, table, slider, query, text_input, separator, selectbox
import pandas as pd
import plotly.express as px

text("# Welcome!")
separator()

text("### Basic table")


# Load the CSV
connect() # load in all sources, which by default is the sample_csv
dataset_name="sugar_consumption_dataset_csv"
df = get_df(dataset_name)

# Filter the DataFrame to include only necessary columns
df = df[['Country', 'Year', 'Continent', 'Region', 'Avg_Daily_Sugar_Intake']]
table(df, title="Global Sugar Data")
separator()
text("### Basic Scatter Plot")

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
separator()



text("### Detailed Scatter Plot")

# Create a scatter plot

fig = px.scatter(
    df,
    x="Country",                     # X-axis: Country
    y="Avg_Daily_Sugar_Intake",      # Y-axis: Average Daily Sugar Intake
    title="Sugar Intake by Country",
    color="Continent",               # Color points by Continent
    size="Avg_Daily_Sugar_Intake",   # Size points by sugar intake
    hover_name="Country",            # Show country name on hover
    hover_data=["Year", "Region"],   # Additional hover data
)
# Show the plot
plotly(fig)

separator()
text("### Bar Chart")

# Create a bar chart

fig = px.bar(df, x="Country", y="Avg_Daily_Sugar_Intake", title="Sugar Intake of all countries")

plotly(fig)

separator()
text("### Pie chart")

fig = px.pie(df,values="Avg_Daily_Sugar_Intake", names="Continent" , title="Sugar Intake of various continents")
# Show the plot
plotly(fig)

separator()

text("### Slider with Sugar Intake Values")


#Slider 
threshold_value_column="Avg_Daily_Sugar_Intake"
threshold = slider("Threshold", min_val=0, max_val=200, default=50)
table(df[df[threshold_value_column] > threshold], title="Daily Sugar Intake")

separator()
# SQL Time

# Basic table retrieval
 
sql = "SELECT Country, Year, Avg_Daily_Sugar_Intake  FROM sugar_consumption_dataset_csv"
filtered_df = query(sql, "sugar_consumption_dataset_csv")
text("# Just Country, Year and Sugar Intake using SQL")
table(filtered_df, title="Filtered Data")



separator()
separator()

# Enter the Country and get it's details
# Basic text input
name = text_input(label="Enter a country", placeholder="India")
sql = f"SELECT Country, Year, Avg_Daily_Sugar_Intake  FROM sugar_consumption_dataset_csv WHERE Country='{name}'"
filtered_df = query(sql, "sugar_consumption_dataset_csv")
text("# Specific Country")
table(filtered_df, title="Filtered Data")



separator()
# Use SQL to filter the table based on Region

# region= df["Region"].unique()

text("### Specific Region")
# Select a Region and get it's details
# Create a dropdown menu to select a data subset
region_name = selectbox(
    label="Choose Region",
    #options=region
    options = ["Western Europe","Australia & New Zealand","Sub-Saharan Africa","South Asia","Central America","Eastern Europe","Northern America","East Asia","Southeast Asia"]
)
text(" ")
sql = f"SELECT Country, Continent, Year, Avg_Daily_Sugar_Intake, Region  FROM sugar_consumption_dataset_csv WHERE Region='{region_name}'"
filtered_df = query(sql, "sugar_consumption_dataset_csv")
table(filtered_df, title="Filtered Data")











