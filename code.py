import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Sales Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# MYSQL CONNECTION
# --------------------------------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kitty@123",
    database="sales_analysis"
)

# --------------------------------------------------
# CUSTOM UI STYLE
# --------------------------------------------------

st.markdown("""
<style>
            
body{
background-color:#0f172a;
}

.kpi-card{
background:linear-gradient(135deg,#1e293b,#334155);
padding:25px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0px 6px 20px rgba(0,0,0,0.3);
}

.kpi-title{
font-size:14px;
color:#cbd5f5;
}

.kpi-value{
font-size:34px;
font-weight:bold;
}

.chart-card{
background: linear-gradient(145deg,#0f172a,#020617);
padding:25px;
border-radius:18px;
border:1px solid rgba(148,163,184,0.2);
margin-bottom:25px;

box-shadow:
0 8px 25px rgba(0,0,0,0.6),
inset 0 0 0 1px rgba(255,255,255,0.05);

transition:0.3s;
}

.chart-card:hover{
transform:translateY(-5px);
box-shadow:
0 15px 35px rgba(0,0,0,0.8),
0 0 10px rgba(59,130,246,0.3);
}
            
.chart-title{
font-size:18px;
font-weight:600;
color:#e2e8f0;
margin-bottom:10px;
padding-bottom:8px;
border-bottom:1px solid rgba(148,163,184,0.2);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR (PROJECT INFO)
# --------------------------------------------------

st.sidebar.title("📊 Dashboard Info")

st.sidebar.markdown("""
### 🚀 Project Overview

This **Sales Intelligence Dashboard** helps businesses
track and analyze their sales performance.

It provides insights about:

• Revenue trends  
• Sales pipeline stages  
• Product performance  
• Agent performance  
• Industry sector revenue  
• Regional performance  

The dashboard is built using:

- **Python**
- **Streamlit**
- **MySQL**
- **Plotly**

---

### 📂 Dataset Information

The dataset contains CRM style sales pipeline data.

Tables Used:

**sales_pipeline**
- opportunity_id
- sales_agent
- product
- account
- deal_stage
- engage_date
- close_date
- close_value


**accounts**
- account
- sector
- year_established
- revenue
- employees
- office_location
- subsidiary_of


**sales_team**
- sales_agent
- manager
- regional_office


**products**
- product
- series
- sales_price


---

### 🎯 Purpose

This dashboard helps sales managers:

✔ Track revenue growth  
✔ Identify top products  
✔ Analyze winning vs losing deals  
✔ Monitor sales agent performance  

""")

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🚀 Sales Intelligence Dashboard")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

pipeline = pd.read_sql("SELECT * FROM sales_pipeline", conn)
accounts = pd.read_sql("SELECT * FROM accounts", conn)
products = pd.read_sql("SELECT * FROM products", conn)
teams = pd.read_sql("SELECT * FROM sales_team", conn)

# --------------------------------------------------
# KPI QUERY
# --------------------------------------------------

kpi_query = """
SELECT 
COUNT(opportunity_id) AS opportunities,
SUM(close_value) AS revenue,
SUM(CASE WHEN deal_stage='Won' THEN 1 ELSE 0 END) AS won
FROM sales_pipeline
"""

kpi = pd.read_sql(kpi_query, conn)

opportunities = int(kpi["opportunities"][0])
revenue = int(kpi["revenue"][0])
won = int(kpi["won"][0])

conversion = round((won/opportunities)*100,2)

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">Total Opportunities</div>
    <div class="kpi-value">{opportunities}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">Total Revenue</div>
    <div class="kpi-value">{revenue/1000000:.0f}M</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">Won Deals</div>
    <div class="kpi-value">{won}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-title">Conversion Rate</div>
    <div class="kpi-value">{conversion}%</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# MONTHLY REVENUE TREND
# --------------------------------------------------

monthly_query = """
SELECT 
DATE_FORMAT(close_date,'%Y-%m') AS month,
SUM(close_value) AS revenue
FROM sales_pipeline
GROUP BY month
ORDER BY month
"""

monthly = pd.read_sql(monthly_query, conn)

fig_trend = px.line(
    monthly,
    x="month",
    y="revenue",
    markers=True,
)

fig_trend.update_layout(
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font=dict(color="white"),
    margin=dict(l=10,r=10,t=40,b=10)
)

# --------------------------------------------------
# SALES FUNNEL
# --------------------------------------------------

stage_query = """
SELECT deal_stage, COUNT(*) AS deals
FROM sales_pipeline
GROUP BY deal_stage
"""

stage_df = pd.read_sql(stage_query, conn)

fig_funnel = px.funnel(
    stage_df,
    x="deals",
    y="deal_stage"
)

fig_funnel.update_layout(
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font=dict(color="white"),
    margin=dict(l=10,r=10,t=40,b=10)
)

# --------------------------------------------------
# PRODUCT PERFORMANCE
# --------------------------------------------------

product_query = """
SELECT product, SUM(close_value) AS revenue
FROM sales_pipeline
GROUP BY product
ORDER BY revenue DESC
"""

product_df = pd.read_sql(product_query, conn)

fig_product = px.bar(
    product_df,
    x="product",
    y="revenue"
)

fig_product.update_layout(
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font=dict(color="white"),
    margin=dict(l=10,r=10,t=40,b=10)
)

# --------------------------------------------------
# TOP AGENTS
# --------------------------------------------------

agent_query = """
SELECT sales_agent, SUM(close_value) AS revenue
FROM sales_pipeline
GROUP BY sales_agent
ORDER BY revenue DESC
LIMIT 10
"""

agent_df = pd.read_sql(agent_query, conn)

fig_agent = px.bar(
    agent_df,
    x="sales_agent",
    y="revenue"
)

fig_agent.update_layout(
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font=dict(color="white"),
    margin=dict(l=10,r=10,t=40,b=10)
)

# --------------------------------------------------
# REVENUE BY SECTOR
# --------------------------------------------------

sector_query = """
SELECT a.sector, SUM(p.close_value) AS revenue
FROM sales_pipeline p
JOIN accounts a
ON p.account = a.account
GROUP BY a.sector
"""

sector_df = pd.read_sql(sector_query, conn)

fig_sector = px.pie(
    sector_df,
    names="sector",
    values="revenue"
)

fig_sector.update_layout(
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font=dict(color="white"),
    margin=dict(l=10,r=10,t=40,b=10)
)

# --------------------------------------------------
# DASHBOARD LAYOUT WITH BORDERS
# --------------------------------------------------

col1,col2 = st.columns(2)
with col1:
    with st.container():
        st.markdown('<div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Monthly Revenue Trend</div>', unsafe_allow_html=True)
        st.plotly_chart(fig_trend, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Deal Stages Funnel</div>', unsafe_allow_html=True)
        st.plotly_chart(fig_funnel, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

col3,col4 = st.columns(2)

with col3:
    with st.container():
        st.markdown('<div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Revenue by Product</div>', unsafe_allow_html=True)
        st.plotly_chart(fig_product, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with col4:
    with st.container():
        st.markdown('<div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Top Performing Agents</div>', unsafe_allow_html=True)
        st.plotly_chart(fig_agent, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div>', unsafe_allow_html=True)
st.markdown('<div class="chart-title">Revenue by Industry Sector</div>', unsafe_allow_html=True)
st.plotly_chart(fig_sector, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# TOP CUSTOMERS
# --------------------------------------------------

st.subheader("Top Customers")

customer_query = """
SELECT account,
SUM(close_value) AS revenue
FROM sales_pipeline
GROUP BY account
ORDER BY revenue DESC
LIMIT 10
"""

customers = pd.read_sql(customer_query, conn)

st.dataframe(customers, use_container_width=True)