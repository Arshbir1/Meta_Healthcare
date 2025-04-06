# Cloud Function triggered when a report is uploaded
# Extracts text using Vision API
# Redacts PII using Google Cloud DLP API
# Passes cleaned text to Gemini for summarization
# Saves structured data to Firestore
