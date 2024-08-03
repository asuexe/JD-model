import openai
import config

# Set your API key from the config file
openai.api_key = config.OPENAI_API_KEY

def aicontent(query):
    try:
        response = openai.chat.completions.create(
             model="gpt-3.5-turbo",  # Specify the chat-based model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Generate a detailed product description for: {query}"}
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        if response and 'choices' in response:
            if len(response['choices']) > 0:
                answer = response['choices'][0]['text'].strip()
            else:
                answer = 'Ugh oh! I accept, I failed!'
        else:
            answer = 'Ugh oh! I accept, I failed!'
    except Exception as e:
        answer = f"Error: {str(e)}"
    
    return answer