from agents import output_guardrail, GuardrailFunctionOutput
from models import OutputValidationResult
from agents import Agent
from agents import Runner

validation_agent = Agent(
    name="Output Guardrail Checker",
    instructions="Check if the agent's response includes prohibited content like solving direct math problems for users.",
    output_type=OutputValidationResult,
)

@output_guardrail
async def validate_output(ctx, agent: Agent, output: str) -> GuardrailFunctionOutput:
    result = await Runner.run(validation_agent, output, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_valid,
    )
