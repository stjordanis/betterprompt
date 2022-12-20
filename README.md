# betterprompt 🧪🔬

⚡ Test suite for LLM prompts before pushing them to PROD ⚡

Our work is inspired by this paper [**Demystifying Prompts in Language Models via Perplexity Estimation**](https://arxiv.org/pdf/2212.04037.pdf) which showed that 

>Over a wide range of tasks, we show that the lower the perplexity of the prompt (i.e. closer to zero) is, the better the prompt is able to perform the task.


## Getting Started 

To get started with betterprompt, you will need to first install the library by running the following command:

`pip install betterprompt`

Once installed, you can import it into your python project by running the following:

`import betterprompt`

## Using betterprompt

betterprompt currently provides 1 main functions - `calculate_perplexity`. 

The `calculate_perplexity` function takes in a prompt as a string and calculates the perplexity of the text using the OpenAI GPT-3 API. It returns the perplexity as a float. 

## Example

Here is an example of how to use Betterprompt to calculate the perplexity of a given prompt:

```
import betterprompt

prompt = "This is a sample prompt"

perplexity = betterprompt.calculate_perplexity(prompt)

print(perplexity) # Outputs the perplexity of the text
```

## Version

The current version of Betterprompt is `0.4.0`. 

## Contributing

We welcome contributions to Betterprompt! Please read our [contributing guidelines](https://github.com/betterprompt/readme/blob/master/CONTRIBUTING.md) for more information. 

## License

Betterprompt is released under the [MIT License](https://github.com/betterprompt/readme/blob/master/LICENSE).
