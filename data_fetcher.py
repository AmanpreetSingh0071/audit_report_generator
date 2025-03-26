# data_fetcher.py
from groq import Groq

# Initialize the Groq client with your API key (replace with your actual key)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def fetch_company_data(company_name):
    # Prepare the prompt for Groq to fetch data
    prompt = f"""
    Fetch details for the company: {company_name}

    Provide company overview, financial summary, employee information, market share, etc.
    """

    # Create the chat completion request with Groq
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt,
        }],
        model="llama-3.3-70b-versatile",
    )
    
    # Get the company details from the response
    company_details = chat_completion.choices[0].message.content
    return company_details

def generate_audit_report(company_name, company_details):
    # Generate the audit report with the fetched company details
    prompt = f"""
    Here is the company data:

    {company_details}

    Generate a structured audit report for the company: {company_name}

    Organize findings under these headings:
    1. **General Business Profile**
    2. **Financial Health**
    3. **Market Position & Competitive Analysis**
    4. **ESG & Governance**
    5. **Operational & HR Risks**
    6. **Technology & Blockchain Verification**

    Deliverables:
    - A 1-paragraph executive summary synthesizing critical risks/strengths.
    - Bullet-point technical findings under each header.
    - Data-driven recommendations.
    - Flag metrics requiring external validation.
    """
    
    # Send the prompt to Groq for audit report generation
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt,
        }],
        model="llama-3.3-70b-versatile",
    )

    # Get the audit report
    audit_report = chat_completion.choices[0].message.content
    return audit_report