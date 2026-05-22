# state.py

class WorkflowState:

    def __init__(self):

        self.memory = {
            "startup_idea": "",
            "industry": "",
            "target_audience": "",
            "web_research": "",
            "market_analysis": "",
            "competitor_analysis": "",
            "gtm_strategy": "",
            "investor_feedback": "",

            "retrieved_context": "",

            "final_report": ""
        }

    def update(self, key, value):
        self.memory[key] = value

    def get(self, key):
        return self.memory.get(key)