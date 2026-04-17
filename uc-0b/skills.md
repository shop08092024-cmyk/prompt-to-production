# skills.md
 
 skills:
-  - name: retrieve_policy
-    description: Loads a policy text file and parses it into structured numbered sections for processing.
-    input: Path to the .txt file (string).
-    output: A dictionary or list of structured sections (e.g., { "2.3": "text", ... }).
-    error_handling: Return an error if the file is missing or contains no numbered clauses.
-
-  - name: summarize_policy
-    description: Produces a concise summary of policy sections while preserving all mandatory conditions and multi-approver requirements.
-    input: Structured sections from retrieve_policy.
-    output: A formatted string containing the bulleted summary.
-    error_handling: If a section is ambiguous or high-risk, flag it for verbatim inclusion.
