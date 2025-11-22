Legal Email Assistant – Assignment Submission

This repository contains my official submission for the Virtuon Technologies – Internship Round 1 Assignment.
The goal of the assignment is to build an intelligent Legal Email Assistant capable of:

Analyzing an incoming legal email

Extracting structured information in JSON format

Drafting a formal legal reply based on the extracted details

The entire solution is implemented using clean, modular, and fully self-contained Python code.



📌 Features
1️⃣ Email Analysis — analyze_email()

This function reads a raw legal email and extracts structured details such as:

Intent of the email

Primary legal topic

Contract participants (client + counterparty)

Agreement type and agreement date

Numbered legal questions

Due date for response

Any additional requested actions

The extracted output strictly follows the schema provided in the assignment and is returned as a Python dictionary (JSON-serializable).



2️⃣ Drafting a Legal Reply — draft_reply()

This function uses the extracted information to generate a crisp and professional legal response. The reply:

Acknowledges the original request

References the correct agreement and date

Answers each question clearly and formally

Maintains an appropriate legal tone

Suggests next steps or timelines



📁 Repository Structure

legal-email-assistant/
│── email_assistant.py        # Main implementation (analysis + draft reply)
│── run.py                    # Optional runner script
│── sample_email.txt          # Optional sample email used for testing
│── README.md                 # Project documentation



▶️ How to Run the Project
🔧 Requirements

Python 3.8+

No external libraries required (standard library only)



▶️ Run the main program

python email_assistant.py

This will automatically print:

Extracted JSON output

Professional legal reply email



🧪 Example Output

The script generates:

Clean, properly structured extracted JSON

A formal reply referencing the Master Services Agreement

Clear answers to each question in the original email

(Exact outputs depend on the content of sample_email.txt.)



🏗️ Implementation Approach

Used Python’s built-in re (regex) module for robust pattern extraction

Followed modular programming for clarity and maintainability

Ensured the output strictly adheres to the assignment’s required schema

Maintained clear, professional formatting in the drafted email



✔️ Key Strengths of This Submission

Fully working, clean, production-style Python code

No unnecessary complexity — easy for evaluators to read and test

Professional email formatting that matches corporate legal standards

Works for any email with similar structure




📞 Contact

For queries or clarifications, feel free to reach out.
