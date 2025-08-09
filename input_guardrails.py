from agents import (
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    TResponseInputItem,
    input_guardrail,
    Runner,
    RunContextWrapper,
)
from typing import Union
from agents import guardrail_agent

@input_guardrail
async def math_guardrail(
    run_ctx: RunContextWrapper[None],
    agent,
    input: Union[str, list[TResponseInputItem]]
) -> GuardrailFunctionOutput:
    
    result = await Runner.run(guardrail_agent, input, context=run_ctx.context)

   
    if getattr(result.final_output, "is_math_homework", False):
       
        raise InputGuardrailTripwireTriggered("Math homework input detected!")
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=False,
    )
