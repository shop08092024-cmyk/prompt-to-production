"""
UC-0C app.py — Budget Data Auditor
Implementation based on RICE → agents.md → skills.md workflow.
"""
import argparse
import csv
import os

def load_dataset(input_path: str):
    """
    Reads the budget CSV and returns the data.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File {input_path} not found.")
    
    data = []
    with open(input_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def compute_growth(data, ward, category, growth_type):
    """
    Calculates growth for a specific ward and category.
    """
    filtered = [r for r in data if r['ward'] == ward and r['category'] == category]
    
    # Sort by period to ensure MoM is correct
    filtered.sort(key=lambda x: x['period'])
    
    results = []
    previous_spend = None
    
    for row in filtered:
        period = row['period']
        actual_spend_str = row['actual_spend'].strip()
        notes = row['notes']
        
        if not actual_spend_str:
            results.append({
                "period": period,
                "actual_spend": "NULL",
                "growth_value": "N/A",
                "formula": "N/A",
                "flag_reason": notes if notes else "Data missing"
            })
            previous_spend = None
            continue
            
        try:
            current_spend = float(actual_spend_str)
        except ValueError:
            results.append({
                "period": period,
                "actual_spend": actual_spend_str,
                "growth_value": "ERROR",
                "formula": "N/A",
                "flag_reason": "Invalid number format"
            })
            previous_spend = None
            continue

        if previous_spend is not None and growth_type == "MoM":
            growth = (current_spend - previous_spend) / previous_spend * 100
            formula = f"({current_spend} - {previous_spend}) / {previous_spend} * 100"
            growth_str = f"{growth:+.1f}%"
        else:
            growth_str = "n/a"
            formula = "n/a (first period or previous null)"
            
        results.append({
            "period": period,
            "actual_spend": current_spend,
            "growth_value": growth_str,
            "formula": formula,
            "flag_reason": ""
        })
        previous_spend = current_spend
        
    return results

def main():
    parser = argparse.ArgumentParser(description="UC-0C Budget Data Auditor")
    parser.add_argument("--input", required=True)
    parser.add_argument("--ward", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--growth-type", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    
    # Refusal logic
    if not args.ward or not args.category:
        print("Refusal: Ward and Category must be specified. Aggregation not allowed.")
        return
    if args.growth_type not in ["MoM", "YoY"]:
        print(f"Refusal: Growth type '{args.growth_type}' not supported. Use MoM or YoY.")
        return

    try:
        data = load_dataset(args.input)
        results = compute_growth(data, args.ward, args.category, args.growth_type)
        
        fieldnames = ["period", "actual_spend", "growth_value", "formula", "flag_reason"]
        with open(args.output, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"Results written to {args.output}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
