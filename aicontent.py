# import os
# from urllib import response 
# import openai
# import config 
# openai.api_key = config.OPENAI_API_KEY

# def aicontent(query):
#     response = openai.chat.completions.create(
#         model='gpt-2',
#         prompt="Generate a detailed product description for:{}".format(query),
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0)
    
#     if 'choices' in response:
#         if len(response['choices']) >0:
#              answer = response['choices'][0]['text']
#         else:
#             answer = 'Ugh oh ! i accept i fail !'
#     return answer

import os
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

# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# def aicontent(query):
#     # Load the GPT-2 tokenizer and model from Hugging Face
#     tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
#     model = GPT2LMHeadModel.from_pretrained("gpt2")

#     # Encode the query and generate a response
#     input_text = "Generate a detailed product description for: " + query
#     input_ids = tokenizer.encode(input_text, return_tensors='pt')

#     # Generate text
#     output = model.generate(input_ids, max_length=256, temperature=0.7, top_p=1.0, do_sample=True)

#     # Decode the output and return the result
#     answer = tokenizer.decode(output[0], skip_special_tokens=True)
#     return answer
