"""
UC-0A — Complaint Classifier
Implementation based on RICE → agents.md → skills.md workflow.
"""
import argparse
import csv
import os

def classify_complaint(row: dict) -> dict:
    """
    Classify a single complaint row into category, priority, reason, and flag.
    Follows enforcement rules from agents.md.
    """
    description = row.get("description", "").lower()
    complaint_id = row.get("complaint_id", "UNKNOWN")
    
    # Predefined Taxonomy
    categories = [
        "Pothole", "Flooding", "Streetlight", "Waste", "Noise", 
        "Road Damage", "Heritage Damage", "Heat Hazard", "Drain Blockage"
    ]
    
    # Severity keywords for Urgent priority
    severity_keywords = ["injury", "child", "school", "hospital", "ambulance", "fire", "hazard", "fell", "collapse"]
    
    category = "Other"
    reason_keyword = ""
    flag = ""
    
    # Mapping logic (Simple keyword matching for this implementation)
    mapping = {
        "pothole": "Pothole",
        "flooded": "Flooding",
        "flooding": "Flooding",
        "streetlight": "Streetlight",
        "lights out": "Streetlight",
        "flickering": "Streetlight",
        "garbage": "Waste",
        "waste": "Waste",
        "dumped": "Waste",
        "dead animal": "Waste",
        "noise": "Noise",
        "music": "Noise",
        "heritage": "Heritage Damage",
        "drain": "Drain Blockage",
        "heat": "Heat Hazard",
        "road surface": "Road Damage",
        "footpath": "Road Damage",
        "cracked": "Road Damage"
    }
    
    for kw, cat in mapping.items():
        if kw in description:
            category = cat
            reason_keyword = kw
            break
            
    # Priority Logic
    priority = "Standard"
    priority_keyword = ""
    for skw in severity_keywords:
        if skw in description:
            priority = "Urgent"
            priority_keyword = skw
            break
            
    # Refusal/Ambiguity Logic
    if category == "Other" or not description:
        category = "Other"
        flag = "NEEDS_REVIEW"
        reason = "Category could not be determined from the description."
    else:
        reason = f"Classified as {category} because description mentions '{reason_keyword}'."
        if priority == "Urgent":
            reason += f" Priority set to Urgent due to keyword '{priority_keyword}'."
        else:
            reason += " Priority set to Standard as no immediate hazards were identified."

    return {
        "complaint_id": complaint_id,
        "category": category,
        "priority": priority,
        "reason": reason,
        "flag": flag
    }


def batch_classify(input_path: str, output_path: str):
    """
    Read input CSV, classify each row, write results CSV.
    Must: flag nulls, not crash on bad rows, produce output even if some rows fail.
    """
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} not found.")
        return

    results = []
    try:
        with open(input_path, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                try:
                    classified = classify_complaint(row)
                    results.append(classified)
                except Exception as e:
                    # Log error and continue with a placeholder
                    results.append({
                        "complaint_id": row.get("complaint_id", "ERROR"),
                        "category": "Other",
                        "priority": "Standard",
                        "reason": f"Processing error: {str(e)}",
                        "flag": "NEEDS_REVIEW"
                    })
                    
        # Write results
        fieldnames = ["complaint_id", "category", "priority", "reason", "flag"]
        with open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
            
    except Exception as e:
        print(f"Critical error processing batch: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UC-0A Complaint Classifier")
    parser.add_argument("--input",  required=True, help="Path to test_[city].csv")
    parser.add_argument("--output", required=True, help="Path to write results CSV")
    args = parser.parse_args()
    batch_classify(args.input, args.output)
    print(f"Done. Results written to {args.output}")
