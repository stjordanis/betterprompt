__version__ = '0.4.0'
import openai
import math
import os


model_name: str = "text-davinci-003"

def get_from_dict_or_env(env_key: str) -> str:
  """Get a value from a dictionary or an environment variable."""
  if env_key in os.environ and os.environ[env_key]:
      return os.environ[env_key]
  else:
      raise ValueError(
          f"Did not find {env_key}, please add an environment variable"
          f" `{env_key}` which contains it, or pass"
          f"  `{env_key}` as a named parameter."
      )
    

def call_openai(prompt: str):
  openai_api_key = get_from_dict_or_env("OPENAI_API_KEY")
  openai.api_key = openai_api_key
  #GET THE LOGPROB OF THE PROMPT
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=0,
    echo=True,
    logprobs=0
  )
  return response["choices"][0]["logprobs"]["token_logprobs"]

def calculate_perplexity(prompt: str):
  nlls = []

  token_logprobs = call_openai(prompt)
  for neg_log_likelihood in token_logprobs:
    if neg_log_likelihood == None: #default to -100, handles the initial token case
      neg_log_likelihood = -100
    nlls.append(neg_log_likelihood)

  perplexity = math.exp(sum(nlls)/len(token_logprobs))
  return perplexity