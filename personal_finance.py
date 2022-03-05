from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.header('Personal Finanical Dashboard')


months = ['January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December']

# Income 
st.subheader('Income')
income = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 
            9000, 10000, 11000, 12000]

chart_data = pd.DataFrame(income, index=months, columns=['Month'])


data = pd.DataFrame({
    'Months': months,
    'Income': income
})

income_chart = alt.Chart(data).mark_bar().encode(
    x=alt.X('Months', sort=None),
    y='Income'
)

st.altair_chart(income_chart, use_container_width=True)

# https://altair-viz.github.io/gallery/area_chart_gradient.html

area_chart = alt.Chart(data).mark_area(
).encode(
    x=alt.X('Months', sort=None),
    y='Income'
)

st.altair_chart(area_chart, use_container_width=True)

# Expenses
st.subheader('Expenses')
expenses = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 
            9000, 10000, 11000, 12000]
expenses.reverse()

expense_data = pd.DataFrame({
    'Months': months,
    'Income': expenses
})

expenses_chart = alt.Chart(expense_data).mark_bar().encode(
    x=alt.X('Months', sort=None),
    y='Income'
)

st.altair_chart(expenses_chart, use_container_width=True)


# Streams of Income

st.subheader('Streams of Income')

source = pd.DataFrame({"category": ["Eminado Limited", "Onajole Ltd", "Vanguard Dami", "Vanguard Ope", "SoVivid"], "value": [4, 6, 10, 3, 7]})

source_chart = alt.Chart(source).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="category", type="nominal"),
)

st.altair_chart(source_chart, use_container_width=True)


base = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), color=alt.Color("category:N", legend=None)
)

pie = base.mark_arc(outerRadius=120)
text = base.mark_text(radius=140, size=10).encode(text="category:N")

st.altair_chart(pie + text, use_container_width=True)

# Delta Values

col1, col2, col3 = st.columns(3)
col1.metric("Income", "£700,000", "8%")
col2.metric("Expenses", "£900", "-18%")
col3.metric("Networth", "£100,000", "4%")