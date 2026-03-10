### **📌 Project Overview** 

- The Sales Intelligence Dashboard is a data analytics project designed to analyze CRM sales pipeline data and visualize key business insights through an interactive dashboard.
- The project combines SQL-based data analysis with Python visualization tools to help businesses monitor sales performance, track revenue trends, evaluate agent performance, and identify high-performing products and sectors.
- The dashboard is built using Streamlit, connected directly to a MySQL database, enabling dynamic data retrieval and real-time analysis.


### **🎯 Project Objectives**

- The primary objectives of this project are:
   - Store and manage sales data in a MySQL database
   - Perform business analysis using SQL queries
   - Build an interactive analytics dashboard
   - Track important sales KPIs
   - Provide insights into revenue, products, agents, and industries
 

### **🛠️ Tech Stack**
| Technology    | Purpose                    |
| ------------- | -------------------------- |
| **MySQL**     | Database storage           |
| **SQL**       | Data analysis and querying |
| **Python**    | Backend processing         |
| **Streamlit** | Dashboard development      |


### **📊 Business Analysis Queries**

1️⃣ **Overall Sales Performance**

<img width="626" height="178" alt="Screenshot 2026-03-10 115716" src="https://github.com/user-attachments/assets/81b280a8-1166-4f28-bc23-311995057d4b" />

- This query calculates the overall health of the sales pipeline by measuring the total number of opportunities, total revenue generated, and the number of successful deals.
- Insight from Dashboard:
  - The conversion rate between opportunities and won deals helps evaluate sales team effectiveness.
  - A low conversion rate indicates that many deals are getting stuck or lost in the pipeline.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
2️⃣ **Monthly Revenue Trend**

<img width="537" height="197" alt="image" src="https://github.com/user-attachments/assets/5839245f-409c-4760-80fa-59befba27bd4" />

- This query analyzes revenue growth over time.
- Insight from Dashboard:
  - The line chart shows how revenue fluctuates month by month.
  - Certain months generate higher revenue, indicating seasonal trends or successful sales campaigns.
  - Sales managers can use this insight to forecast future revenue and plan strategies.
---
3️⃣ **Deal Stage Distribution**

<img width="511" height="130" alt="image" src="https://github.com/user-attachments/assets/c9ef76e2-16b9-4dcd-8313-57e3a88323de" />

- This query shows the distribution of deals across different pipeline stages.
- Insight from Dashboard:
  - The funnel chart highlights where deals are dropping off in the pipeline.
  - If many deals remain stuck in early stages, it indicates inefficient lead conversion.
  - Helps identify stages that require process improvement.
---
4️⃣ **Revenue by Product**

<img width="561" height="153" alt="image" src="https://github.com/user-attachments/assets/69d27f17-c8ee-4ba3-8ce6-4fc4ba230425" />

- This query identifies top-performing products.
- Insight from Dashboard:
  - Some products contribute significantly higher revenue than others.
  - Businesses can focus marketing and sales efforts on high-performing products.
  - Low-performing products may require pricing adjustments or promotion strategies.
--- 
5️⃣ **Top Performing Sales Agents**

<img width="601" height="182" alt="image" src="https://github.com/user-attachments/assets/41aaa41e-a212-4b78-938c-bd2216ba42b7" />

- This query identifies the top revenue-generating sales agents.
- Insight from Dashboard:
  - Top agents consistently generate higher revenue.
  - Managers can analyze their strategies and replicate successful sales practices across the team.
  - It also helps identify agents who may need training or performance improvement.
---
6️⃣ **Revenue by Industry Sector**

<img width="553" height="180" alt="image" src="https://github.com/user-attachments/assets/fc3484a0-eba4-4417-aae1-11389b3b06b5" />

- This query analyzes which industry sectors generate the highest revenue.
- Insight from Dashboard:
  - Certain sectors contribute a larger share of revenue.
  - Sales teams can prioritize high-value industries to maximize revenue.
  - It also helps businesses identify new market opportunities.
---
7️⃣ **Top Customers**

<img width="557" height="213" alt="image" src="https://github.com/user-attachments/assets/7c6b213b-ef96-4e53-aae9-feddd2a7bd1b" />

- This query identifies the most valuable customers.
- Insight from Dashboard:
  - A small number of customers contribute a large portion of total revenue.
  - These customers should be treated as strategic accounts.
  - Maintaining strong relationships with them can ensure long-term business growth.
