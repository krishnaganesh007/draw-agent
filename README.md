# Multi-Tool AI Agent: Math, AutoDraw & Gmail Automation

An intelligent AI agent that performs complex multi-step workflows involving mathematical calculations, browser automation with AutoDraw, and email reporting via Gmail API. Built using **Model Context Protocol (MCP)** with **FastMCP** and **Gemini 2.0 Flash**.

---

## 🎯 What It Does

The AI agent can autonomously:

* **Calculate:** Perform mathematical operations (ASCII values, exponentials, sums)
* **Draw:** Control AutoDraw in Chrome browser to create visual representations
* **Email:** Send detailed reports via Gmail API with results and summaries

### Example Workflow

**Query:**

```text
"Find ASCII values of INDIA, calculate sum of exponentials, draw rectangle in AutoDraw, write result inside, then email results"
```

**Agent Output:**

1. Calculates ASCII: I=73, N=78, D=68, I=73, A=65
2. Computes exponentials: e^73 + e^78 + e^68 + e^73 + e^65
3. Opens AutoDraw, draws rectangle, adds text with final result
4. Sends email with complete workflow summary

---

## 🛠️ Technical Stack

* **Python 3.8+** - Core language
* **FastMCP** - Model Context Protocol server
* **Gemini 2.0 Flash** - LLM for reasoning and orchestration
* **PyAutoGUI** - Browser and UI automation
* **Gmail API** - Email integration with OAuth2
* **AppleScript** - macOS Chrome tab control
* **Google Cloud Platform** - Gmail API credentials

---

## 📋 Prerequisites

### System Requirements

* macOS (for AppleScript Chrome control)
* Python 3.8 or higher
* Google Chrome browser
* Gmail account

### API Setup

**Google Cloud Console:**

1. Create new project
2. Enable Gmail API
3. Configure OAuth consent screen (External)
4. Add your Gmail as test user
5. Create Desktop OAuth Client ID
6. Download `client_secret.json`

For a detailed step-by-step guide, check this Medium tutorial: [Create a Gmail Agent with MCP](https://medium.com/@jason.summer/create-a-gmail-agent-with-model-context-protocol-mcp-061059c07777)

**Gemini API:**

* Get API key from Google AI Studio
* Add to `.env` file

---

## 🚀 Installation

Clone the repository:

```bash
git clone [YOUR_GITHUB_REPO_URL]
cd ai-agent-multitool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your API keys and paths
```

Configure credentials:

* Place `client_secret.json` in project root
* On first Gmail tool use, complete OAuth flow

---

## 📁 Project Structure

```
DRAW-AGENT/
├── YT/                  # (Your custom folder, contents not shown)
├── client_secret.json    # Google OAuth credentials (not in repo ideally)
├── mcp_server.py         # MCP server with all tools
├── open_autodraw.py      # Script for AutoDraw automation
├── pyproject.toml        # Project dependencies & metadata
├── README.md             # Project documentation
├── talk2mcp.py           # Client orchestrator
├── token.json            # Generated OAuth tokens (not in repo ideally)
└── uv.lock               # Lockfile for dependencies
```

---

## 🔧 Configuration

### Environment Variables (`.env`)

```text
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_CLIENT_SECRET_PATH=./client_secret.json
GMAIL_TOKEN_PATH=./token.json
GMAIL_SENDER=me
GMAIL_TO=recipient@gmail.com
LOG_LEVEL=INFO
```

### Display Coordinates

The AutoDraw tools use screen coordinates. Update these in `mcp_server.py` based on your display setup:

* `draw_button_x, draw_button_y` - AutoDraw Draw tool button
* `x_text_tool, y_text_tool` - AutoDraw Text tool button
* Canvas coordinates for drawing and text placement

---

## 🎮 Usage

Start the MCP server (in one terminal):

```bash
python mcp_server.py
```

Run the agent (in another terminal):

```bash
python talk2mcp.py
```

### Custom Queries

Edit the `query` variable in `talk2mcp.py`:

```python
query = """Your custom multi-step workflow here"""
```

### Available Tools

* `strings_to_chars_to_int(text)` - Convert string to ASCII values
* `add(a, b)` - Mathematical addition
* `exponential(x)` - Calculate e^x
* `draw_rectangle()` - Draw rectangle in AutoDraw
* `ensure_autodraw_and_write_text()` - Write text in AutoDraw
* `send_gmail_text()` - Send plain text email
* `send_gmail_html()` - Send HTML email

---

## 🔍 Troubleshooting

### OAuth Errors (403: access_denied)

* Ensure Gmail account is added as Test user in OAuth consent screen
* Check that Gmail API is enabled for your project
* Verify `client_secret.json` is from correct project

### AutoDraw Automation Fails

* Update screen coordinates for your display setup
* Ensure Chrome is running and AutoDraw tab is accessible
* Check macOS Accessibility permissions for Python

### Email Sending Fails

* Verify Gmail API is enabled and has send scope
* Check OAuth credentials and token validity
* Ensure recipient email is valid

### Debug Mode

Enable detailed logging:

```python
LOG_LEVEL=DEBUG
```

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 🎥 Demo

Watch the full tutorial: [\[YouTube Video Link\]](https://youtu.be/QP6lkwt1DQY)
