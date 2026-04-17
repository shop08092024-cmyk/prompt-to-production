# skills.md
 
 skills:
-  - name: retrieve_documents
-    description: Loads all 3 policy files (HR, IT, Finance) and indexes them by document name and section number for efficient retrieval.
-    input: None (loads from predefined data directory).
-    output: A structured index of policy sections.
-    error_handling: Return an error if any of the three required files are missing.
-
-  - name: answer_question
-    description: Searches the indexed policy documents for an answer to a user question and returns it with a single-source citation or the refusal template.
-    input: User question (string), indexed documents.
-    output: Formatted answer string with citation OR refusal template.
-    error_handling: If an answer is found across multiple documents but creates ambiguity, default to refusal or cite only the primary source.
