import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the Excel file
df = pd.read_excel("IMDbMovieRatings.xlsx")

# Set the page title
st.set_page_config(page_title="IMDb Movie Ratings")

# Set the page header
st.title("IMDb Movie Ratings")

# Bar Plot
st.header("IMDb ratings of Top 10 movies")
chart_data = df["IMDb Rating"].nlargest(10)
st.bar_chart(chart_data, use_container_width=True)
# Add Y-axis Label
st.text("")

# Histogram
st.header("Distribution of IMDb Ratings")
fig, ax = plt.subplots()
ax.hist(df["IMDb Rating"], bins=20, edgecolor="black")
ax.set_xlabel("IMDb Rating")
ax.set_ylabel("Count")
st.pyplot(fig)

# Scatter Plot
st.header("Year of Release vs IMDb Rating")
fig, ax = plt.subplots()
ax.scatter(df["Year of Release"], df["IMDb Rating"])
ax.set_xlabel("Year of Release")
ax.set_ylabel("IMDb Rating")
st.pyplot(fig)

# Box Plot
st.header("IMDb Ratings by Decade")
df["Decade"] = df["Year of Release"] // 10 * 10
fig, ax = plt.subplots()
df.boxplot(column="IMDb Rating", by="Decade", ax=ax)
ax.set_xlabel("Decade")
ax.set_ylabel("IMDb Rating")
st.pyplot(fig)


# Create a line plot of IMDb ratings by year of release
df_lineplot = df.groupby(['Year of Release']).mean()['IMDb Rating']
fig3, ax3 = plt.subplots()
sns.lineplot(x=df_lineplot.index, y=df_lineplot)
plt.xlabel('Year of Release')
plt.ylabel('IMDb Rating')
st.pyplot(fig3)



