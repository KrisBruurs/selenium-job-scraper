import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
# Set the page title, icon, and layout for a professional look
st.set_page_config(
    page_title="Remote Jobs Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- DATA LOADING ---
# Use Streamlit's caching to load the data once and improve performance
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/cleaned_data.csv')
        # Basic cleaning of 'Category' column for consistency
        df['Category'] = df['Category'].str.strip()
        return df
    except FileNotFoundError:
        st.error("Error: 'cleaned_data.csv' not found. Please make sure the file is in the correct directory.")
        return None

df = load_data()

# Stop the app if data fails to load
if df is None:
    st.stop()

# --- MAIN TITLE ---
st.title("📊 Trending Remote Jobs Dashboard")
st.markdown("An overview of the top 150 trending remote job postings on WeWorkRemotely.")

# --- KEY METRICS ---
# Display some high-level numbers at the top
total_jobs = len(df)
unique_companies = df['Company'].nunique()
unique_skills = df.dropna(subset=['Skills'])['Skills'].str.split(', ').explode().nunique()

metric1, metric2, metric3 = st.columns(3)
metric1.metric(label="Total Job Postings", value=total_jobs)
metric2.metric(label="Unique Companies", value=unique_companies)
metric3.metric(label="Unique Skills Mentioned", value=unique_skills)

st.markdown("---")


# --- LAYOUT WITH TWO COLUMNS ---
col1, col2 = st.columns(2, gap="large")


# --- COLUMN 1 ---
with col1:
    st.header("🏢 Company & Role Insights")

    # --- Top 5 Companies List ---
    st.subheader("Top 5 Most Active Companies")
    top_5_companies = df['Company'].value_counts().head(5)
    for rank, (company, jobs) in enumerate(top_5_companies.items(), 1):
        st.markdown(f"**{rank}.** {company} | **{jobs}** jobs")

    # --- Job Type Donut Chart ---
    st.subheader("Job Type Distribution")
    job_type_counts = df['Job Type'].value_counts()
    fig_job_types = px.pie(
        job_type_counts,
        values=job_type_counts.values,
        names=job_type_counts.index,
        title="Full-Time vs. Contract Roles",
        hole=.4  # This creates the donut chart effect
    )
    fig_job_types.update_traces(textinfo='percent+label', hovertemplate='<b>%{label}</b><br>%{value} jobs<extra></extra>')
    st.plotly_chart(fig_job_types, use_container_width=True)

    # --- Region Table ---
    st.subheader("Job Counts by Region")
    region_counts = df['Region'].value_counts().reset_index()
    region_counts.columns = ['Region', 'Number of Jobs']
    st.table(region_counts)


# --- COLUMN 2 ---
with col2:
    st.header("🛠️ Skills & Category Focus")

    # --- Top Skills Bar Chart ---
    st.subheader("Top 15 Most In-Demand Skills")
    df_skills = df.dropna(subset=['Skills']).copy()
    individual_skills = df_skills['Skills'].str.split(', ').explode()
    skill_counts = individual_skills.value_counts().head(15)
    
    # Convert to DataFrame for more robust plotting
    skill_df = skill_counts.reset_index()
    skill_df.columns = ['Skill', 'Count']

    # Create the chart
    fig_skills = px.bar(
        skill_df,
        x='Count',
        y='Skill',
        orientation='h',
        title='Top 15 Skills',
        color='Skill',  # This correctly colors each bar differently
        labels={'Count': 'Number of Job Postings', 'Skill': 'Skill'}
    )
    fig_skills.update_layout(
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'} # Sorts bars from smallest to largest
    )
    fig_skills.update_traces(hovertemplate='<b>%{x}</b> jobs<extra></extra>') # Correctly use %{x} for horizontal bar chart
    st.plotly_chart(fig_skills, use_container_width=True)

    # --- Category Bar Chart ---
    st.subheader("Top Job Categories")
    filtered_category = df[df['Category'] != 'All Other Remote']
    top_categories = filtered_category['Category'].value_counts().head(7)
    
    fig_categories = px.bar(
        top_categories,
        x=top_categories.index,
        y=top_categories.values,
        title="Top 7 Job Categories",
        labels={'x': 'Category', 'y': 'Number of Jobs'},
        color_discrete_sequence=['coral']
    )
    fig_categories.update_traces(hovertemplate='<b>%{y}</b> jobs<extra></extra>')
    st.plotly_chart(fig_categories, use_container_width=True)

        # --- NEW: AVERAGE SALARY BY CATEGORY ---
    st.subheader("Average Salary by Category")
    # Group by category and calculate the mean salary, then sort
    avg_salary_by_cat = df.groupby('Category')['average_salary'].mean().dropna().sort_values(ascending=False).head(10)
    
    fig_cat_salary = px.bar(
        avg_salary_by_cat,
        x=avg_salary_by_cat.values,
        y=avg_salary_by_cat.index,
        orientation='h',
        title='Top 10 Highest Paying Categories',
        labels={'x': 'Average Salary (USD)', 'y': 'Category'}
    )
    fig_cat_salary.update_layout(yaxis={'categoryorder': 'total ascending'})
    fig_cat_salary.update_traces(hovertemplate='$%{x:,.0f}<extra></extra>')
    st.plotly_chart(fig_cat_salary, use_container_width=True)