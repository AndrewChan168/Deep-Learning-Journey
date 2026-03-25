from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
import asyncio

stream_http_transport = StreamableHttpTransport(url="http://localhost:8020/accu-mcp-server")

client = Client(stream_http_transport)

async def main():
    async with client:
        print(f"Client connected: {client.is_connected()}")
        tools = await client.list_tools()
        print(f"Available tools: {tools}")
        if any(tool.name == "get_weather_conditions" for tool in tools):
            result = await client.call_tool("get_weather_conditions", {"location": "Penzance, UK"})
            print(f"Call result: {result}")
        
    # Connection is closed automatically here
    print(f"Client connected: {client.is_connected()}")

if __name__ == "__main__":
    asyncio.run(main())