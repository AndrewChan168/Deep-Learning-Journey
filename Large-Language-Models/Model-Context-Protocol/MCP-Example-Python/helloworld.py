from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP Demo")

if __name__=="__main__":
    mcp.run(transport='stdio')