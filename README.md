# MCP Sandbox  

A sandbox environment for experimenting with the **Model Context Protocol (MCP)** using **local LLMs** (e.g. Ollama, LM Studio) and custom tool integrations.  

This project demonstrates how to connect a **local language model** to the MCP ecosystem, enabling testing of client–server interactions, tool discovery, and execution workflows.  

---

## 🚀 Features  

- 🧩 **MCP Server & Client Setup** – Example code for running MCP servers and clients locally.  
- 🤖 **Local LLM Integration** – Tested with [Ollama](https://ollama.ai) (LLaMA, Mistral, Gemma, etc.).  
- 🔌 **Tooling Extensions** – Add and test custom MCP tools (e.g. file system access, API connectors).  
- 💻 **Developer Sandbox** – A safe space to explore MCP without relying on cloud APIs.  

---

## 🛠️ Getting Started  

### 1. Prerequisites  
- macOS (Apple Silicon M1/M2/M3 recommended)  
- [Python 3.10+](https://www.python.org/)  
- [Ollama](https://ollama.ai) or [LM Studio](https://lmstudio.ai) (for local LLMs)  
- [VS Code](https://code.visualstudio.com/) with MCP/Agent Mode enabled  

### 2. Clone the Repository  
```bash
git clone https://github.com/<your-username>/mcp-sandbox.git
cd mcp-sandbox
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Example MCP Server
```bash
python server.py
```

📂 Project Structure
```bash
mcp-sandbox/
│── server.py          # Example MCP server  
│── client.py          # Example MCP client  
│── requirements.txt   # Python dependencies  
│── README.md          # Project documentation  
│── examples/          # Sample configs and test scripts 
```
