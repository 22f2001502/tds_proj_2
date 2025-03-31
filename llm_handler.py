import openai
import os
from typing import Optional

class LLMHandler:
    def __init__(self):
        # Initialize with your preferred LLM (here using OpenAI as example)
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
    def get_answer(self, question: str, context: str) -> str:
        try:
            prompt = f"""
            You are an assistant that helps answer questions based on provided context from Google Colab notebooks.
            The user has asked: {question}
            
            Here is the relevant context from the notebook:
            {context}
            
            Please provide a concise answer that would be appropriate to enter in the assignment.
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that provides accurate answers based on the given context."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error generating answer: {str(e)}"
