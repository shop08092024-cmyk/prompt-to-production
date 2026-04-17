# skills.md

skills:
  - name: classify_complaint
    description: Classifies a single civic complaint row into category, priority, reason, and flag using a strict taxonomy.
    input: A dictionary representing a single complaint row (e.g., from a CSV reader).
    output: A dictionary with keys: complaint_id, category, priority, reason, flag.
    error_handling: If input is null or ambiguous, set category to 'Other' and flag to 'NEEDS_REVIEW'. Never crash on missing fields.

  - name: batch_classify
    description: Processes a CSV file of complaints, applying classification to each row and writing the results to a new CSV.
    input: input_path (string) and output_path (string).
    output: None (writes results to output_path).
    error_handling: Must handle empty files, missing columns, and individual row failures without stopping the entire batch process. Flag invalid rows in the output.
