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



### Tools And ToolNode with LangGraph

### Agent with Memory Saver

## More Agent architectures with LangGraph
