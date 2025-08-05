def theme_summarization_prompt(theme: str, comments: list[str]) -> str:
    prompt = f"Summarize guest feedback related to '{theme}':\n"
    prompt += "\n".join(f"- {comment}" for comment in comments)
    prompt += "\n\nProvide a concise and objective summary."
    return prompt
