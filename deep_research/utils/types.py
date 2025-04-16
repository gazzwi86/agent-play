"""Common data schema and types for travel-concierge agents."""

from google.genai import types

json_response_config = types.GenerateContentConfig(
    response_mime_type="application/json",
    candidate_count=1,
    temperature=0.1,
    stop_sequences=["```"]
)
