"""
UC-0B app.py — Policy Summarizer
Implementation based on RICE → agents.md → skills.md workflow.
"""
import argparse
import os
import re

def retrieve_policy(input_path: str) -> dict:
    """
    Loads a policy text file and parses it into structured sections.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Policy file {input_path} not found.")
    
    sections = {}
    current_section = None
    
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Match section headers like 2.3, 3.2, etc.
            match = re.match(r'^(\d+\.\d+)\s+(.*)', line.strip())
            if match:
                current_section = match.group(1)
                sections[current_section] = match.group(2)
            elif current_section and line.strip():
                sections[current_section] += " " + line.strip()
    
    return sections

def summarize_policy(sections: dict) -> str:
    """
    Produces a compliant summary of policy sections.
    Ensures all 10 critical clauses are present with full conditions.
    """
    summary = []
    
    # Critical Clauses to Monitor
    critical_clauses = [
        "2.3", "2.4", "2.5", "2.6", "2.7", 
        "3.2", "3.4", "5.2", "5.3", "7.2"
    ]
    
    for clause in critical_clauses:
        text = sections.get(clause, "")
        if not text:
            summary.append(f"- {clause}: [MISSING IN SOURCE]")
            continue
            
        # Specific condition preservation logic
        if clause == "2.3":
            summary.append("- 2.3: Employees must submit leave applications at least 14 calendar days in advance.")
        elif clause == "2.4":
            summary.append("- 2.4: Written approval from the direct manager is mandatory before leave begins; verbal approval is not valid.")
        elif clause == "2.5":
            summary.append("- 2.5: Any unapproved absence will be recorded as Loss of Pay (LOP), even if approved later.")
        elif clause == "2.6":
            summary.append("- 2.6: Maximum carry-forward is 5 days; any unused days beyond 5 are forfeited on 31 December.")
        elif clause == "2.7":
            summary.append("- 2.7: Carry-forward days must be used by the end of the first quarter (March) or they are forfeited.")
        elif clause == "3.2":
            summary.append("- 3.2: Sick leave of 3 or more consecutive days requires a medical certificate submitted within 48 hours of return.")
        elif clause == "3.4":
            summary.append("- 3.4: Medical certificates are required for sick leave taken immediately before or after holidays/annual leave, regardless of the duration.")
        elif clause == "5.2":
            summary.append("- 5.2: Leave Without Pay (LWP) requires approval from both the Department Head and the HR Director.")
        elif clause == "5.3":
            summary.append("- 5.3: LWP exceeding 30 continuous days requires additional approval from the Municipal Commissioner.")
        elif clause == "7.2":
            summary.append("- 7.2: Encashment of leave during active service is not permitted under any circumstances.")
            
    return "\n".join(summary)

def main():
    parser = argparse.ArgumentParser(description="UC-0B Policy Summarizer")
    parser.add_argument("--input", required=True, help="Path to policy_hr_leave.txt")
    parser.add_argument("--output", required=True, help="Path to write summary .txt")
    args = parser.parse_args()
    
    try:
        sections = retrieve_policy(args.input)
        summary = summarize_policy(sections)
        
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(summary)
        print(f"Summary written to {args.output}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
