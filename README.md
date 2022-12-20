# Betterprompt ReadME

Welcome to the Betterprompt ReadME. Betterprompt is a python library that provides a powerful way to measure the perplexity of text using the OpenAI GPT-3 API. With this library you can easily measure the complexity of natural language text!


## Getting Started 

To get started with Betterprompt, you will need to first install the library by running the following command:

`pip install betterprompt`

Once installed, you can import it into your python project by running the following:

`import betterprompt`

## Using Betterprompt

Betterprompt currently provides 1 main functions - `calculate_perplexity`. 

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
