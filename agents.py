from agents import Agent
from models import MathHomeworkOutput

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeworkOutput,
)

support_agent = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
)
