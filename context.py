from agents import RunContextWrapper

ctx = RunContextWrapper(
    context={
        "user_id": "user_123",
        "session_id": "session_456"
    }
)
