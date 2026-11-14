import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="IS 445 HW6 - BFRO Bigfoot Reports Analysis", layout="wide")

st.title("HW6.1: Interactive Data Storytelling with Streamlit")
st.markdown("**Student Name:** Harshal Panda | **Course:** IS 445 (UIUC)")

data = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/bfro_reports_fall2022.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(data)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year
    return df

df = load_data()

st.header("Dataset Overview")
st.write("This application explores Bigfoot field encounter reports (BFRO dataset), analyzing report classifications, seasonal distributions, and geographic patterns.")

st.subheader("Visualization 1: Distribution of BFRO Report Classifications")

class_counts = df['classification'].value_counts().reset_index()
class_counts.columns = ['classification', 'count']

viz1_chart = alt.Chart(class_counts).mark_bar().encode(
    x=alt.X('classification:N', title='Classification Type'),
    y=alt.Y('count:Q', title='Number of Reports'),
    color=alt.Color('classification:N', scale=alt.Scale(scheme='tableau10'), legend=None),
    tooltip=['classification', 'count']
).properties(
    width=600,
    height=400,
    title="BFRO Sighting Reports by Classification"
)

st.altair_chart(viz1_chart, use_container_width=True)

# Write-up Paragraph 1
st.markdown("""
**Visualization 1 Write-up:** 
This bar chart highlights the frequency of different BFRO report classifications within the dataset, providing insight into the reliability and corroboration level associated with various encounters. For design choices, I utilized vertical bar marks with distinct category labels on the x-axis to clearly separate Class A and Class B reports, mapping quantitative count values to the y-axis. I selected the 'tableau10' color scheme to differentiate the classification categories clearly while maintaining a clean aesthetic. If I had more time, I would incorporate a dropdown filter allowing users to subset the classifications by specific geographic regions or states. This visualization uses an entirely different dataset and set of plots compared to Homework #5, meaning there is no overlap in data or analysis.
""")

st.subheader("Visualization 2: Encounter Distribution by Season and State with Interactive Brush")

df_clean = df.dropna(subset=['season', 'state', 'temperature_high']).copy()

brush = alt.selection_interval(encodings=['x'])

timeline = alt.Chart(df_clean).mark_bar().encode(
    x=alt.X('season:N', title='Season', sort=['Spring', 'Summer', 'Fall', 'Winter']),
    y=alt.Y('count():Q', title='Report Count'),
    color=alt.Color('season:N', legend=None)
).properties(
    width=700,
    height=100
).add_params(
    brush
)

scatter = alt.Chart(df_clean).mark_circle(size=30, opacity=0.7).encode(
    x=alt.X('temperature_high:Q', title='High Temperature (°F)'),
    y=alt.Y('humidity:Q', title='Humidity'),
    color=alt.Color('state:N', title='State', scale=alt.Scale(scheme='category10')),
    tooltip=['title', 'state', 'season', 'temperature_high', 'humidity']
).properties(
    width=700,
    height=350
).transform_filter(
    brush
)

viz2_chart = alt.vconcat(scatter, timeline)

st.altair_chart(viz2_chart, use_container_width=True)

st.markdown("""
**Visualization 2 Write-up:**
This linked visualization pairs an interactive seasonal bar chart with an upper scatter plot examining high temperatures versus humidity levels during reported encounters, categorized by state. To handle environmental variables effectively, I mapped meteorological metrics to quantitative axes and used a categorical color scheme ('category10') to distinguish states. The primary interactive feature incorporates an interval brush on the lower seasonal chart, enabling users to highlight specific seasons to dynamically filter the environmental scatter plot above. If I had more time, I would add multi-select state dropdown filters to let users isolate specific states without relying solely on the color legend. This visualization uses an entirely different dataset and set of plots compared to Homework #5, meaning there is no overlap in data or analysis.
""")

st.markdown("---")
st.subheader("Resources & Code")
st.markdown("[The Data Source](https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/bfro_reports_fall2022.csv)")
st.markdown("[GitHub Repository](https://github.com/hp0525/)", unsafe_allow_html=True)

#personal dataset explorations
#df
#df['classification']
#df['classification'].value_counts()

#display viz
#viz1_chart.display()

#viz2_chart.display()