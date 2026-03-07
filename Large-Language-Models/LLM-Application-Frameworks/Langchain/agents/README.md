# Building Agents with Langchain
The fundamentl concept behind an agent in the context of generative AI application is the use of a language model as reasoning mechanism to select a seqence of actions to perform to achieve a goal. An agent has decision-making capabilities to handle complex tasks.
<br>
The `agent` module of **Langchain** is for us to build an agent. The `agent` module consists of 4 components:
- `Agent` component
- `AgentExecutor` component
- `Tool` component
- `Toolkit` component 

## Reference books:
1. Generative AI on Google Cloud with Langchain

## Use LangGraph to build Agent


## Use LangGraph to build Agentic Workflow
**LangGraph** provides a robust framework for building stateful, multi-step AI application. For each **LangGraph** application, it consists of components:
- **state** object: defines a clear and strongly typed state for the entire workflow
- **node** function: a processing unit which can handles tasks such as generating search queries
- **edge**: between nodes determine the directed flow of data, defining how information moves through the graph
- **Entry Point** & **End Condition**: every graph needs a starting point & end conditions