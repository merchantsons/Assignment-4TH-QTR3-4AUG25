import asyncio
import os
from dotenv import load_dotenv

from agents import support_agent, Runner, InputGuardrailTripwireTriggered
from input_guardrails import math_guardrail
from output_guardrails import validate_output
from context import ctx

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables!")

os.environ["OPENAI_API_KEY"] = openai_api_key

# Set input guardrails to the math_guardrail function you defined
support_agent.input_guardrails = [math_guardrail]
support_agent.output_guardrails = [validate_output]

async def main():
    try:
        await Runner.run(
            support_agent,
            "Hello, can you help me solve for x: 2x + 3 = 11?",
            context=ctx["context"]  # note: ctx is a dict, so access context key here
        )
        print("Guardrail didn't trip - this is unexpected")
    except InputGuardrailTripwireTriggered:
        print("Math homework input guardrail tripped!")

if __name__ == "__main__":
    asyncio.run(main())
