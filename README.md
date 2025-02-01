# Inspect workshop

## 0. Prerequisites

I'm assuming you have a basic understanding of Python and the command line and that you
have a laptop with Python 3.10 or higher installed.

If you don't, no worries, I hope you can still get some value from this workshop.

I suggest using [VS Code](https://code.visualstudio.com/), but any text editor and
terminal will do.

## 1. Clone this repo

```sh
git clone TODO
```

## 2. Setup a virtual environment

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

This will create a virtual environment for the depenencies of this project in the
`.venv` directory.

Some of the dependencies are for running a small LLM model locally, which you wouldn't
have to do if you had API access to a hosted model.

Optional: If you're using VS Code, consider installing the Inspect extension
https://marketplace.visualstudio.com/items?itemName=ukaisi.inspect-ai

## 3. Verify that `inspect` is installed

```sh
inspect
```

You should see output like

```raw
Usage: inspect [OPTIONS] COMMAND [ARGS]...
```

## 4. Run our first evaluation

Warning: This will download a 1.1B parameter model, which is about 2 GiB in size. 

```sh
inspect eval task.py --model hf/TinyLlama/TinyLlama-1.1B-Chat-v1.0 --limit 1 --max-tokens 20
```

This could take a while as it will download the TinyLlama model and perform inference on
your laptop. This is a relatively small and "cheap" model.

## 5. View the results

If you've got the Inspect [AI
extension](https://marketplace.visualstudio.com/items?itemName=ukaisi.inspect-ai)
for VS Code installed, the log viewer will open automatically inside the IDE.

If not, run

```sh
inspect view
```

This should launch a browser window with the results of the evaluation.

## References

* https://inspect.ai-safety-institute.org.uk/
* https://aisi.gov.uk/
* https://github.com/UKGovernmentBEIS/inspect_ai
* https://github.com/UKGovernmentBEIS/inspect_evals
