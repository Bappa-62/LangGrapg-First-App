from typing import TypedDict,Literal
from random import random
class State(TypedDict):
    graph_state:str

def start_play(state:State):
    print("Start Play node has been called.")
    return {"graph_state":state["graph_state"] + " I am playing"}

def cricket(state:State):
    print("Cricket node has been called.")
    return {"graph_state":state["graph_state"] + " Cricket."}

def football(state:State):
    print("Football node has been called.")
    return {"graph_state":state["graph_state"] + " Football."}


def random_play(state:State) -> Literal["cricket","football"]:
    graph_state = state["graph_state"]

    if random()>0.5:
        return "football"
    else:
        return "cricket"


from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END

## Build the graph
graph = StateGraph(State)

## Adding the nodes
graph.add_node("start_play",start_play) ## (Node name, Corresponding Function)
graph.add_node("cricket",cricket)
graph.add_node("football",football)

## Schedule the flow of the graph
graph.add_edge(START,"start_play")
graph.add_conditional_edges("start_play",random_play) ## random_play is not a node(it's a routing function) , so no node name(string)
graph.add_edge("cricket",END)
graph.add_edge("football",END)

## Compile the graph

graph_builder = graph.compile()

## View 
display(Image(graph_builder.get_graph().draw_mermaid_png()))


## Graph Invocation
graph_builder.invoke({"graph_state":"Hi! I am Bappa,"})