# google-form-capture
## Deployment Guide
### 1. Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Google Script Configuration
Open Google Form → Click "Extensions" → Select "Apps Script"

Paste contents of 'google_form.js'

Set up trigger:

Click "Triggers" → Add new trigger

Select onSubmit function

Choose event type "On form submit"

### 3. Environment Variables
Create '.env' file:

```
ADMIN_SLACK_TOKEN=your-token-here
ADMIN_OPENAI_API_KEY=your-key-here
```
