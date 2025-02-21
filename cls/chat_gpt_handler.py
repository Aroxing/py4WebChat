import openai
import settings


class ChatGPTHandler:
    def __init__(self, op_log):
        self.op_log = op_log
        self.client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_API_MODEL

    def send_prompt(self, prompt: str) -> str:
        """
        Sends a prompt to ChatGPT and returns the response
        
        Args:
            prompt (str): The prompt to send to ChatGPT
            
        Returns:
            str: The response from ChatGPT
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                temperature=1,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            self.op_log.add2log('error', f"Error occurred while communicating with ChatGPT: {str(e)}")
