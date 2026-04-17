# skills.md
 
 skills:
-  - name: load_dataset
-    description: Reads the budget CSV, validates columns, and identifies all rows with null actual_spend values.
-    input: Path to the CSV file (string).
-    output: A list of rows or a DataFrame; and a separate list of null-containing rows with their notes.
-    error_handling: Return an error if mandatory columns (period, ward, category) are missing.
-
-  - name: compute_growth
-    description: Calculates growth (MoM or YoY) for a filtered dataset (ward + category) and includes the formula for each step.
-    input: Filtered data, growth_type (string).
-    output: A table showing period, spend, growth %, formula, and flags.
-    error_handling: If growth_type is missing or if data is insufficient for MoM calculation, report the issue clearly.
