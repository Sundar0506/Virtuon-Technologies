from email_assistant import analyze_email, draft_reply

# Read the sample email
with open("sample_email.txt", "r", encoding="utf-8") as f:
    email_text = f.read()

# Run analysis
analysis = analyze_email(email_text)
print("=== ANALYSIS JSON ===")
print(analysis)
print()

# Generate drafted reply
reply = draft_reply(analysis)
print("=== DRAFTED REPLY ===")
print(reply)
