import asyncio
import os
from langchain_ollama.chat_models import ChatOllama
from mcp_use import MCPAgent, MCPClient

current_dir = os.path.dirname(os.path.abspath(__file__))
server_path = os.path.join(current_dir, "server.py")

CONFIG = {
    "mcpServers": {
        "fii-demo": {
            "command": "python3",
            "args": [server_path]
        }
    }
}

async def main():
    client = MCPClient.from_dict(CONFIG)
    llm = ChatOllama(model="qwen2.5:latest", base_url="http://localhost:11434")
    agent = MCPAgent(llm=llm, client=client, max_steps=20)
    #result = await agent.run("Compute md5 hash for following string: 'Hello, world!' then count number of characters in first half of hash and finally echo hello. also get the Add-ons & Devices amount")
    result = await agent.run("what is my rental amount?")
    print("\nResult:", result)
    await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(main())
