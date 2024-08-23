from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)

def generate_response(user_input):
    inputs = tokenizer(user_input, return_tensors="pt")
    reply_ids = model.generate(inputs['input_ids'])
    response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return response
