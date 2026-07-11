# MercadoLibre Seller Profitability & Margin Analytics Tool 📊

An interactive, data-driven financial simulator designed for MercadoLibre e-commerce sellers to uncover hidden operation costs, calculate precise product margins, and simulate profitability KPIs in real-time.

Built entirely in Python using **Streamlit** for dynamic UI rendering and **Pandas** for historical session state tracking and data exporting features.

---

## 🎯 The Business Problem Solved
E-commerce sellers on platforms like MercadoLibre often struggle to identify their true net profit due to complex, multi-layered fee structures (listing types, fixed costs, shipping subsidies, and local taxes like VAT or withholding taxes). 

This tool serves as a **Financial Intelligence Pipeline** that ingests basic raw inputs (listing price, supplier costs, shipping expenses) and instantly applies platform-specific business logic to prevent pricing errors and optimize profit margins before committing to inventory.

## 🚀 Key Features & Architecture
- **Dynamic Fee Engine:** Instantly evaluates fees based on listing tiers (Clásica vs. Premium).
- **Tax & Logistics Breakdown:** Automates deductions for variable shipping rates and country-specific tax withholding simulations.
- **Session-State Persistence:** Implements a localized transactional history buffer using `st.session_state` to let sellers compare multiple product configurations side-by-side without database overhead.
- **Data Export Pipeline:** Compiles analytical outputs into clean, structured datasets ready for download in CSV format for legacy ERP or Excel integration.

---

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Frontend/Dashboard:** Streamlit (Dynamic layout, interactive inputs, and native data visualization tables)
- **Data Manipulation:** Pandas (Session serialization and CSV compilation)

---

## 📊 Core Financial Logic & KPIs Formula
The system processes data through the following engineering metrics:

1. **Gross Revenue (Payout):**
   $$\text{Payout} = \text{Selling Price} - \text{Meli Fee} - \text{Shipping Cost}$$
2. **Total Cost of Goods Sold (COGS):**
   $$\text{Total Cost} = \text{Supplier Cost} + \text{Packaging/Extra Costs}$$
3. **Net Profit:**
   $$\text{Net Profit} = \text{Payout} - \text{Total Cost}$$
4. **Return on Investment (ROI):**
   $$\text{ROI (\%)} = \left( \frac{\text{Net Profit}}{\text{Total Cost}} \right) \times 100$$

---

## 💻 Installation & Local Deployment

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/CamiloMondragon93/meli-profitability-analytics.git](https://github.com/CamiloMondragon93/meli-profitability-analytics.git)
   cd meli-profitability-analytics

1.Install Dependecies:

   pip install -r requirements.txt

2.Run the Streamlit application:

  streamlit run app.py


📂 Project Structure
├── app.py                 # Main Streamlit application and financial logic
├── requirements.txt       # Project dependencies (Streamlit, Pandas)
└── README.md              # Software and business documentation

Future Data Engineering Roadmap
To scale this local analytics engine into an enterprise-level data platform, the next structural increments will include:

[ ] DuckDB Integration: Migrate st.session_state to a permanent, serverless local OLAP database (.db file) to store persistent historical simulations using SQL.

[ ] API Ingestion: Connect directly to the official MercadoLibre API to automatically pull live marketplace category fees and real-time shipping cost grids.

[ ] Advanced Visualization Layer: Embed native Plotly charts to track margin distribution and detect high-risk underperforming products.




