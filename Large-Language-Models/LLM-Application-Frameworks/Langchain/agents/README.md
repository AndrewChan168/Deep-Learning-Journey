# Building Agents with Langchain
The fundamentl concept behind an agent in the context of generative AI application is the use of a language model as reasoning mechanism to select a seqence of actions to perform to achieve a goal. An agent has decision-making capabilities to handle complex tasks.
<br>
The `agent` module of **Langchain** is for us to build an agent. The `agent` module consists of 4 components:
- `Agent` component
- `AgentExecutor` component
- `Tool` component
- `Toolkit` component 

## Reference books:
1. AI Agents and Applications
2. Generative AI on Google Cloud with Langchain

## Use LangGraph to build Agent


## Use LangGraph to build Agentic Workflow
**LangGraph** provides a robust framework for building stateful, multi-step AI application. For each **LangGraph** application, it consists of components:
- **state** object with schema that serves as the input & output for all nodes and edges
- **node** function: a processing unit which can handles tasks such as generating search queries
- **edge**: between nodes determine the directed flow of data, defining how information moves through the graph
- **Entry Point** & **End Condition**: every graph needs a starting point & end conditions

### Simple workflow using LangGraph
This [notebook](by-LangGraph/01-BasicGraphWithoutLLM.ipynb) provides an example building workflow without LLM.

In next [notebook](by-LangGraph/02-BasicGraphWithLLM.ipynb), we added LLM to work. We modified the `state` object that the contents are stacked instead of overriding, because LLM needs reading old messages to response with accurate answer.

### State of LangGraph
In [notebook](by-LangGraph/03-MoreWaysToCreateState.ipynb), we are showing more ways to create a `state` object for overall nodes and edges in LangGraph that are:
- **TypeDict**
- **DataClass**
- **Pydantic.BaseModel**

### Foundation of Agent Architecture
**ReAct** is the most basic agent architecture. It consists of 3 steps:
1. **Act**: The step in which model calls specific tools
2. **Observe**: Passing output of tool back to model
3. **Reason**: Based on the output response from the tool, the model will decide what to do in the next step.

### Agent with Tools or Agent by ToolNode with LangGraph
Most of LLM is a chat model. To work with LLM, LangGraph needs to pass messages into LLM chat model.<br>

**Tools** can be integreted with LLM to interact with external systems which can be APIs or 3rd party tools. Whenever a query is asked the model can choose to call the tool and this query is based on natural language input, and this will return an output that matches tool's schema.<br>

<u>Agent, that is created by LangGraph</u>, can work with LLM by:
1. LLM binding with tool
2. Using pre-build ToolNode

This [notebook](by-LangGraph/04-WorkflowWithTools.ipynb) shows how to build an LLM agent that could use tool.

### Agent with Memory Saver
LangGraph cannot remember the conversation with users unless we compiled the graph with memory. This [notebook](by-LangGraph/05-WorkflowWithMemory.ipynb) shows difference between LangGraph workflow with Memory and without Memory saver.


## More Agent patterns with LangGraph
Apart from **ReAct** pattern, we still have 4 patterns.
1. **Reflection & Refine**
2. **Plan and Execution**
3. **Multi-agents: co-operation**
4. **Multi-agents: Supervisor**

### 1. Reflection Pattern
<u>Reflection</u> pattern is about having an agent review and critique its own work, then the agent revise the work based on that critique. 


### 2. Planning Pattern
When using <u>Planning</u> pattern, agent starts by analyzing the overall goal and understanding what success looks like. It then breaks down the goal into smaller subtasks. The agent execute the subtasks.


## Agentic RAG

### Basic agentic RAG

### Corrective RAG

### Adaptive RAG
