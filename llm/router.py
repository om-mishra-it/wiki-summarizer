from langgraph.graph import StateGraph, END
from agent.summarizer_agent import summarize_text


def summarize_node(state):
    article_text = state["article"]
    summary = summarize_text(article_text)
    return {"summary": summary}


def build_graph():
    graph = StateGraph()
    graph.add_node("summarize", summarize_node)
    graph.set_entry_point("summarize")
    graph.add_edge("summarize", END)
    return graph.compile()
