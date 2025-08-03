from langchain_core.prompts import ChatPromptTemplate


def get_medical_prompt() -> ChatPromptTemplate:
    """Create the medical expert prompt template."""
    system_prompt = (
        "You are a medical expert. Use only the information from the retrieved documents from the Gale Encyclopedia of Medicine (3rd Edition) "
        "to answer the user's question. Provide clear, accurate, and concise responses, including definitions, causes, symptoms, diagnosis, treatment, "
        "or prevention as relevant. Avoid speculation and do not introduce external knowledge. Maintain a professional, neutral, and informative tone "
        "suitable for a general audience."
        "If you do not have enough information to answer the question, say 'I don't know'. "
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    return prompt
