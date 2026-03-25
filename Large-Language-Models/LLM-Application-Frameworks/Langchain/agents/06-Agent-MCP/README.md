# Agent works with MCP
Refer to [Model Context Protocol](../../../../Model-Context-Protocol/README.md) for more details about MCP server.

## Steps for set up MCP Server

### 1 Initializing project
We will use `uv` to manage Python package. Assume we have installed `uv` on our workstation. We use `uv` to initialize the <i>MCP_Demo</i> project.
```bash
$ uv init mcp_server

$ cd mcp_server
```


### 2. Install packages
Then we use `uv` to install required package for the project.
```bash
$ uv add "fastmcp"

$ uv add "aiohttp"
```

### 3. Up the MCP server
We implement the MCP server on `accuweather_mcp.py` file.
```bash
$ uv run accuweather_mcp.py
```

We could test MCP server with `test_accuweather_mcp.py` file. In other terminal execute:
```bash
$ uv run test_accuweather_mcp.py
```