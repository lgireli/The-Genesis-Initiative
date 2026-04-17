def execute(context):
    """Simple test skill execution"""
    user_name = context.get("user_name", "Stranger")
    return f"Hello, {user_name}! The Genesis MK2 Skill Engine is operational."
