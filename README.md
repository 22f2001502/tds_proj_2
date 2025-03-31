# tds_proj_2
# TDS LLM Answering API

Automatically answers questions from graded assignments using LLMs.

## Setup
1. Clone repo
2. `pip install -r requirements.txt`
3. Add OpenAI API key to `.env`

## Usage
POST to `/api/` with:
```json
{
  "question": "Your question here",
  "assignment_number": "ga1"
}
