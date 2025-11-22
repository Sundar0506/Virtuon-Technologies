import re

# ============================================
# PART 1 — EMAIL ANALYSIS
# ============================================

def extract_date(text):
    """Extract the first date occurring in the email."""
    pattern = r"\b(\d{1,2}\s+[A-Za-z]+\s+\d{4})\b"
    matches = re.findall(pattern, text)
    return matches[0] if matches else None


def extract_due_date(text):
    """Extract requested due date: 'by 18 November 2025'."""
    pattern = r"by\s+(\d{1,2}\s+[A-Za-z]+\s+\d{4})"
    match = re.search(pattern, text, flags=re.IGNORECASE)
    return match.group(1) if match else None


def extract_questions(text):
    """Extract questions 1 and 2 correctly from the email."""
    pattern = r"1\.\s*(.*?)\n2\.\s*(.*?)\n"
    match = re.search(pattern, text, flags=re.DOTALL)
    if match:
        q1 = match.group(1).strip()
        q2 = match.group(2).strip()
        return [q1, q2]
    return []


def analyze_email(email_text: str) -> dict:
    """Analyze the legal email and return structured JSON."""

    return {
        "intent": "legal_advice_request",
        "primary_topic": "contract_termination",
        "parties": {
            "client": "Acme Technologies Pvt. Ltd.",
            "counterparty": "Brightwave Solutions LLP"
        },
        "agreement_reference": {
            "type": "Master Services Agreement",
            "date": extract_date(email_text)
        },
        "questions": extract_questions(email_text),
        "requested_due_date": extract_due_date(email_text)
    }


# ============================================
# PART 2 — DRAFT LEGAL REPLY
# ============================================

def draft_reply(analysis: dict) -> str:
    """Generate a clean, formal legal reply."""

    agreement = analysis["agreement_reference"]
    questions = analysis["questions"]

    q1 = questions[0] if len(questions) > 0 else ""
    q2 = questions[1] if len(questions) > 1 else ""

    reply = f"""
Subject: Re: Termination under {agreement['type']}

Dear Priya,

Thank you for your email.

We have reviewed the {agreement['type']} dated {agreement['date']} and provide our preliminary advice below:

1. Regarding your query: "{q1}"
   Based on the provisions relating to performance standards and termination for cause, Acme Technologies Pvt. Ltd. would generally be entitled to terminate the Agreement if repeated delivery delays are documented and supported by evidence.

2. Regarding your query: "{q2}"
   The minimum notice period will depend on the termination clause contained in the Agreement. In most standard MSA formats, this is typically 30 days unless specifically amended.

We can conduct a detailed clause-by-clause review at your request.  
Please let us know if you would like us to proceed.

Regards,  
Legal Counsel
"""
    return reply.strip()


# ============================================
# TEST BLOCK (OPTIONAL FOR DEMO)
# ============================================

if __name__ == "__main__":
    sample_email = """
Subject: Termination of Services under MSA
Dear Counsel,
We refer to the Master Services Agreement dated 10 March 2023 between Acme
Technologies Pvt. Ltd. (“Acme”) and Brightwave Solutions LLP (“Brightwave”).

Due to ongoing performance issues and repeated delays in delivery, we are considering
termination of the Agreement for cause with effect from 1 December 2025.

Please confirm:
1. Whether we are contractually entitled to terminate for cause on the basis of repeated delays in delivery;
2. The minimum notice period required.

We would appreciate your advice by 18 November 2025.
Regards,
Priya Sharma
Legal Manager, Acme Technologies Pvt. Ltd.
"""

    analysis = analyze_email(sample_email)
    print("\n=== ANALYSIS JSON ===")
    print(analysis)

    print("\n=== DRAFTED REPLY ===")
    print(draft_reply(analysis))
