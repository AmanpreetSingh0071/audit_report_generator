# app.py
import streamlit as st
from data_fetcher import fetch_company_data, generate_audit_report

# Streamlit UI
st.set_page_config(page_title="KYB Due Diligence Tool", layout="centered")

st.title("Know Your Business (KYB) Due Diligence Tool")

# Input for the company name
company_name = st.text_input("Enter Company Name")

if company_name:
    # Fetch company data from Groq
    st.write("Fetching data for:", company_name)
    try:
        company_details = fetch_company_data(company_name)
        st.subheader(f"Audit Report for {company_name}")
        
        # Generate the audit report using the fetched data
        audit_report = generate_audit_report(company_name, company_details)
        
        # Display the audit report in a readable format
        st.write(audit_report)
        
    except Exception as e:
        st.error(f"Error fetching data for {company_name}: {e}")

# Adding the signature
st.markdown(
    """
    <hr>
    <div style="text-align:center; font-size: 12px; color: gray;">
        Created by <strong>Amanpreet Singh</strong>
    </div>
    """,
    unsafe_allow_html=True
)