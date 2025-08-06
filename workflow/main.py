# architecture.py

from adk.workflow import Workflow
from adk.agent import Agent

class TicketClassifier(Agent):
    def run(self, state):
        print("📥 Classifying ticket...")
        state["classification"] = "technical"
        return state

class KBRetriever(Agent):
    def run(self, state):
        print("🔍 Retrieving KB...")
        state["kb_article"] = "Try restarting your modem."
        return state

class TicketResponder(Agent):
    def run(self, state):
        print("✍️ Drafting response...")
        state["response"] = f"Hi, regarding your {state['classification']} issue: {state['kb_article']}"
        return state

def get_workflow():
    workflow = Workflow()
    workflow.add_agent("ticket_classifier", TicketClassifier())
    workflow.add_agent("kb_retriever", KBRetriever())
    workflow.add_agent("ticket_responder", TicketResponder())

    workflow.set_start("ticket_classifier")
    workflow.add_edge("ticket_classifier", "kb_retriever")
    workflow.add_edge("kb_retriever", "ticket_responder")
    workflow.set_end("ticket_responder")

    return workflow

# Optional entry point
if __name__ == "__main__":
    wf = get_workflow()
    result = wf.run({"ticket_text": "Internet is down"})
    print("✅ Final Result:\n", result)
