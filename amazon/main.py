import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Amazon Review Analysis | Raj Singh", layout="wide")

# --- Custom Title ---
st.markdown("""
    <h1 style='text-align: center; font-size: 42px; color: #262730;'>
        📦 Amazon Product Review & Sentiment Analysis
    </h1>
    <h3 style='text-align: center; font-weight: 400; color: #555;'>
        Solving Quality Gaps and Smarter Discount Strategies at Scale
    </h3>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Problem Statement ---
st.markdown("## 🧩 Problem Statement", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>
In a marketplace with millions of products, not all offerings create equal value.<br> 
Products with low ratings or poor sentiment hurt customer experience, erode brand trust, and lead to higher returns.<br> 
<b>The problem:</b> How can Amazon identify product-level quality gaps, customer pain points, and ineffective discount strategies to protect growth and improve retention?
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Objective ---
st.markdown("## 🎯 Objective", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>
To help Amazon:<br>
- Detect high- and low-performing products using ratings and reviews<br>
- Understand customer sentiment by category<br>
- Evaluate whether discounts meaningfully impact customer satisfaction<br>
- Deliver business-ready insights to shape product strategy, marketing focus, and customer retention plans
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Dataset Overview ---
st.markdown("## 🗃 Dataset Overview", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>         
- ~27 million product reviews and ratings<br>
- Fields include: product ID, category, sentiment, rating, discount %, total sales<br>
- Simulated e-commerce dataset modeled on Amazon data
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Analysis Process ---
st.markdown("## 🔍 Data Analysis Process", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

# --- Data Analysis ---
with col1:
    st.markdown("""
        <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
            <div style='font-size: 36px;'>📊</div>
            <h4 style='margin-top: 10px;'>Data Analysis</h4>
            <p style='color: #555; font-size: 20px;'>
                Cleaned, formatted, and transformed raw product data into ready-for-insights structure using Python and pandas.
            </p>
        </div>
    """, unsafe_allow_html=True)
    with open("amazon/notebooks/data_cleaning&formating.ipynb", "rb") as f:
        st.download_button("See Code", f, file_name="amazon_cleaning_formating.ipynb", key="amazon_clean_download")

# --- Dashboard Creation ---
with col2:
    st.markdown("""
        <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
            <div style='font-size: 36px;'>📈</div>
            <h4 style='margin-top: 10px;'>Dashboard Creation</h4>
            <p style='color: #555; font-size: 20px;'>
                Create an intuitive Power BI dashboard enabling non-technical stakeholders to quickly understand data and take action.
            </p>
        </div>
    """, unsafe_allow_html=True)
    with open("amazon/files/data_visulization.pbix", "rb") as f:
        st.download_button("See Dashboard", f, file_name="amazon_dashboard.pbix", key="amazon_dash_download")

# --- Business Insights ---
with col3:
    st.markdown("""
        <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
            <div style='font-size: 36px;'>💡</div>
            <h4 style='margin-top: 10px;'>Business Insights</h4>
            <p style='color: #555; font-size: 20px;'>Delivered product, sentiment, and pricing insights to shape smarter product and retention strategy.</p>
        </div>
    """, unsafe_allow_html=True)
    with open("amazon/notebooks/transform_analyze_data.ipynb", "rb") as f:
        st.download_button("See Code", f, file_name="amazon_transform_analyze_.ipynb", key="amazon_analyse_download")


# --- Data Storytelling ---
with col4:
    st.markdown("""
        <div style='background-color: #ffffff; border: 1px solid #eee; border-radius: 12px; padding: 24px; text-align: center;'>
            <div style='font-size: 36px;'>🗣</div>
            <h4 style='margin-top: 10px;'>Data Storytelling</h4>
            <p style='font-size: 20px; color: #555;'>
            Developed executive presentation that help decision-makers and teams easily understand and use findings.
            </p>
        </div>
    """, unsafe_allow_html=True)
    with open("amazon/files/data analysis presentation.pptx", "rb") as f:
        st.download_button("See Presentation", f, file_name="amazon_data_analysis_presentation.pptx", key="amazon_story_download")

st.markdown("<hr>", unsafe_allow_html=True)

# --- Key Insights ---
st.markdown("## 📊 Key Insights", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>
✅ Top-rated products (4.8–5★) are consistent across key categories → promote across homepage and ads<br>
⚠ Low-rated products (<2.5★) exist in every category → these damage experience, must be reviewed or retired<br>
💬 87% of sentiment is positive → strong baseline trust, but some segments need tuning<br>
💸 Discounting doesn’t correlate with higher ratings → discounting must be strategic, not blind
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Visuals ---
st.markdown("## 📸 Dashboard Visuals", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>
Visualized in Power BI Dashboard:
</p>
<p style='font-size: 20px;'>
-Bar charts: Average rating by category<br>
-Donut chart: Sentiment distribution<br>
-Scatter plot: Discount vs Rating<br>
-Tables: Top-rated and bottom-rated product segments<br>
-KPI cards: Average rating, review count, discount, sentiment split<br>
</p>
""", unsafe_allow_html=True)

st.image("amazon/images/amazon_dashboard.jpg", caption="Amazon Review Dashboard", use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Business Recommendations ---
st.markdown("## 📌 Business Recommendations", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <p style='font-size: 25px;'>
        1. Promote high-rated products across ads, email campaigns, homepage<br>                  
        2. Flag and audit underperforming SKUs with <2.5★ ratings<br>
        3. Monitor review sentiment monthly to capture quality dips early<br>
        4. Prioritize high-sentiment products for Amazon Choice or Buy Box
        </p>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <p style='font-size: 25px;'>
        5. Don’t rely on heavy discounting without solving product quality issues<br>
        6. Invest in NLP tools to automate sentiment tracking and alerts<br>
        7. Drive internal visibility with live dashboards in category reviews<br>
        8. Focus marketing on category-specific strengths revealed by sentiment trends
        </p>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Conclusion ---
st.markdown("## 🧠 Conclusion", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px; text-align: justify;'>
This project tackled a key question: In a crowded e-commerce environment, how can Amazon maintain product quality visibility, enhance customer trust, and avoid unprofitable discount behavior?  
Through sentiment classification, rating-based segmentation, and performance visuals, I built a solution that exposes underperformers, validates category strength, and encourages smart, not desperate, discounting.  
What began as a dataset of 27M reviews ended as a business-ready dashboard and strategy framework for quality-first growth.
</p>
""", unsafe_allow_html=True)

st.markdown("### 🔑 Key Takeaways", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 25px;'>
- Products with strong sentiment and 4.8★+ ratings are worth doubling down on across all channels<br>
- 2.5★ and below rated products require attention—fix, improve or remove<br>
- 87% overall sentiment positivity hides weak zones in categories like Electronics and Fashion<br>
- Discounts above 25% don't improve satisfaction—they only increase returns if quality is poor<br>
- Dashboards allow category heads to make calls with clarity, not assumptions<br>
- Quality and trust are more scalable than discount wars—this analysis proves that
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Tools & Contact ---
st.markdown("## 🛠 Tools & Contacts", unsafe_allow_html=True)

tool_col, contact_col = st.columns(2)

with tool_col:
    st.markdown("""
    <p style='font-size: 25px;'>
    - Python: pandas, text processing, sentiment tagging<br>  
    - Power BI: layered dashboards, DAX-based KPIs<br>  
    - Skills: customer sentiment analysis, product strategy, data storytelling
    </p>
    """, unsafe_allow_html=True)

with contact_col:
    st.markdown("""
    <p style='font-size: 25px;'>
    📧 Email: <b>rajbgi377@gmail.com</b><br>
    🔗 <a href="https://www.linkedin.com/in/rajsinghsendhav" target="_blank">LinkedIn Profile</a><br>
    📁 <a href="https://yourwebsite.com/resume.pdf" target="_blank">Download Resume</a>
    </p>
    """, unsafe_allow_html=True)
