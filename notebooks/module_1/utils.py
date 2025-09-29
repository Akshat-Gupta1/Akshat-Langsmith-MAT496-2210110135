"""Utility functions for LangSmith notebooks"""

def format_messages(messages: list) -> str:
    """Format conversation messages for display"""
    return "\n".join([f"{m['role']}: {m['content']}" for m in messages])

def extract_user_intent(message: str) -> str:
    """Extract user intent from message"""
    if "help" in message.lower():
        return "help_request"
    elif "?" in message:
        return "question"
    else:
        return "statement"

def create_metadata(thread_id: str, turn: int) -> dict:
    """Create metadata for tracing"""
    return {
        "thread_id": thread_id,
        "turn_number": turn,
        "timestamp": "auto"
    }
