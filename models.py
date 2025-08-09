from pydantic import BaseModel

class MathHomeworkOutput(BaseModel):
    is_math_homework: bool
    reasoning: str

class OutputValidationResult(BaseModel):
    is_valid: bool
    message: str
