from agents import (
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    TResponseInputItem,
    input_guardrail,
    Runner,
)
from typing import Union
from models import MathHomeworkOutput
from agents import guardrail_agent
from context import ctx

@input_guardrail
async def math_guardrail(
    run_ctx: RunContextWrapper[None], agent, input: Union[str, list[TResponseInputItem]]
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input, context=run_ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math_homework,
    )
