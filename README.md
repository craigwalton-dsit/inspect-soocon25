# Inspect workshop

An workshop which introduces the Inspect LLM evaluation framework at
[SOOCon25](https://stateofopencon.com/).

What you'll have done by the end of this workshop:

* Installed Inspect
* Run an evaluation of a (small) language model locally
* Viewed the results of the evaluation
* Made changes to the evaluation and adjusted settings on the model

## 0. Prerequisites

I'm assuming that you:
* have a basic understanding of Python and the command line
* have a laptop with Python 3.10 or higher installed
* have internet access and are able to downlaod ~2 GiB of data

If you don't, no worries, I hope you can still get some value from this workshop by
getting a feel for the Inspect evaluation framework. Likewise, if you get stuck on one
step, feel free to skip ahead or ask for help. You're also welcome to complete this in
your own time - the repo will stay public.

I suggest using [VS Code](https://code.visualstudio.com/), but any text editor and
terminal will do.

If you don't have Python 3.10 or higher installed, you can download the latest stable
version from [python.org](https://www.python.org/downloads/).

## 1. Clone this repo

```sh
git clone https://github.com/craigwalton-dsit/inspect-soocon25.git
```

## 2. Setup a virtual environment

```sh
python -m venv .venv
source .venv/bin/activate  # For Linux and macOS
pip install -r requirements.txt
```

If `python` isn't recognised, try `python3` instead.

If you're on Windows, you'll need to replace the `source` command with

```sh
.venv\Scripts\activate.bat
```

or

```sh
.venv\Scripts\Activate.ps1
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

> [!WARNING]  
> This will download a 1.1B parameter model, which is about 2 GiB in size. 

```sh
inspect eval task.py --model hf/TinyLlama/TinyLlama-1.1B-Chat-v1.0 --max-tokens 20
```

This could take a while as it will download the TinyLlama model and perform inference on
your laptop. This is a relatively small and "cheap" model.

If you happen to have access to any model APIs (e.g. Anthropic, OpenAI), see the
[instructions here](https://inspect.ai-safety-institute.org.uk/models.html) for using a
hosted model.

The `--max-tokens 20` argument limits the number of tokens of the model's output to 20.
This will speed things up in case this unintelligent model is very talkative.

## 5. View the results

If you've got the Inspect [AI
extension](https://marketplace.visualstudio.com/items?itemName=ukaisi.inspect-ai) for VS
Code installed, the log viewer will open automatically inside the IDE.

If not, open a new terminal (this will allow you to keep Inspect view running in the
background) and run

```sh
inspect view
```

This should launch a browser window with the results of the evaluation. Take a look at
the score and the messages.

## 6. Adapt the scorer, re-run 10 parallel evaluations

Perhaps we don't mind if the model includes additional text in its response, so long as
it has written "hello world" somewhere in the output.

In `task.py`, let's replace the `exact()` scorer with a `includes()` scorer.

We can re-run the eval, but this time let's run 10 parallel evaluations to cover more of
the model's output space with the `epochs` argument.

```sh
inspect eval task.py --model hf/TinyLlama/TinyLlama-1.1B-Chat-v1.0 --max-tokens 20 --epochs 10
```

## 7. Re-run with a lower temperature

Temperature controls the "creativity" of the model. Lower temperatures like 0.1 will
make the model more deterministic, while higher temperatures like 2.0 will make the
model more creative.

With a low temperature of 0.1 you'll likely see all 10 responses being very similar.

```sh
inspect eval task.py --model hf/TinyLlama/TinyLlama-1.1B-Chat-v1.0 --max-tokens 20 --epochs 10 --temperature 0.1
```

## Optional extra

* Accept an answer of "hello, world" (note the comma) in addition to "hello world" by
  passing a list of strings as the `target` parameter.
* Try providing a system message as a solver before the `generate()`. See the
  [docs](https://inspect.ai-safety-institute.org.uk/solvers.html#built-in-solvers)
* Have a look at the other options you can pass to `inspect eval` by running `inspect
  eval --help`

## Stuck or can't download the model?

I've included some example logs in the `sample-logs` directory if you can't get the eval
running. View them with

```sh
inspect view --log-dir sample-logs
```

## Cleanup

You can delete the model which we downloaded to reclaim some space. It should be stored
at one of

```raw
~/.cache/huggingface/hub
C:\Users\<username>\.cache\huggingface\hub
```

## References

* https://inspect.ai-safety-institute.org.uk/
* https://aisi.gov.uk/
* https://github.com/UKGovernmentBEIS/inspect_ai
* https://github.com/UKGovernmentBEIS/inspect_evals
