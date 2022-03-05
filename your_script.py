import streamlit as st
import numpy as np
import pandas as pd

st.header('This is a header')
st.subheader('This is a subheader')

code = '''def hello():
    print("Hello, Streamlit!")'''

st.code(code, language='python')

st.text('This is some text')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

df = pd.DataFrame(
	np.random.randn(10, 4),
	columns=('col %d' % i for i in range(4))
)

st.table(df)

st.line_chart(df)