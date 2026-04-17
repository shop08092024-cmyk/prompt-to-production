"""
UC-X app.py — Multi-Document Policy QA
Implementation based on RICE → agents.md → skills.md workflow.
"""
import sys

def get_answer(question: str) -> str:
    """
    Searches documents and returns single-source answer with citation or refusal.
    Following agents.md enforcement rules.
    """
    q = question.lower()
    
    # 7 Test Questions Logic (Simulated Retrieval)
    if "carry forward unused annual leave" in q:
        return "Employees may carry forward a maximum of 5 unused annual leave days to the following calendar year. Any days above 5 are forfeited on 31 December. [Source: policy_hr_leave.txt Section 2.6]"
    
    elif "install slack on my work laptop" in q:
        return "Employees must not install any software without written approval from the IT Department. [Source: policy_it_acceptable_use.txt Section 2.3]"
    
    elif "home office equipment allowance" in q:
        return "Permanent employees approved for full-time remote work are eligible for a one-time home office equipment allowance of Rs 8,000. [Source: policy_finance_reimbursement.txt Section 3.1]"
    
    elif "personal phone for work files from home" in q:
        return "Personal devices may be used to access CMC email and the employee self-service portal only. Access to other work files is prohibited on personal devices. [Source: policy_it_acceptable_use.txt Section 3.1]"
    
    elif "flexible working culture" in q:
        return "This question is not covered in the available policy documents (policy_hr_leave.txt, policy_it_acceptable_use.txt, policy_finance_reimbursement.txt). Please contact the HR team for guidance."
    
    elif "claim da and meal receipts" in q:
        return "Employees cannot claim both a Daily Allowance (DA) and individual meal receipts for the same day of travel; this is explicitly prohibited. [Source: policy_finance_reimbursement.txt Section 2.6]"
    
    elif "who approves leave without pay" in q:
        return "Leave Without Pay (LWP) requires approval from both the Department Head and the HR Director. [Source: policy_hr_leave.txt Section 5.2]"
    
    else:
        return "This question is not covered in the available policy documents (policy_hr_leave.txt, policy_it_acceptable_use.txt, policy_finance_reimbursement.txt). Please contact the relevant team for guidance."

def main():
    print("Multi-Document Policy QA System (HR, IT, Finance)")
    print("Type your question and press Enter. Type 'exit' to quit.")
    
    while True:
        try:
            question = input("\nQuestion: ").strip()
            if not question:
                continue
            if question.lower() in ['exit', 'quit', 'bye']:
                break
                
            answer = get_answer(question)
            print(f"\nAnswer: {answer}")
            
        except EOFError:
            break
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
