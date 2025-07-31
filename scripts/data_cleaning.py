import pandas as pd
import numpy as np

df = pd.read_csv('data/top_trending_jobs.csv')

df['Company'] = df['Company'].str.replace('\n', ' ', regex=False).str.strip()

salary_extracted = df['Salary'].str.extract(r'\$(\d{1,3}(?:,\d{3})*)\s*(?:-\s*\$(\d{1,3}(?:,\d{3})*))?.*')

salary_extracted.columns = ['min_salary', 'max_salary']

for col in salary_extracted.columns:
    salary_extracted[col] = salary_extracted[col].str.replace(',', '', regex=False)
    salary_extracted[col] = pd.to_numeric(salary_extracted[col], errors='coerce')

salary_extracted['max_salary'] = salary_extracted['max_salary'].fillna(salary_extracted['min_salary'])

df = pd.concat([df, salary_extracted], axis=1)

df['average_salary'] = df[['min_salary', 'max_salary']].mean(axis=1)

df.to_csv('data/cleaned_data.csv', index=False)