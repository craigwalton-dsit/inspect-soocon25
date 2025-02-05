# This is a variant of task.py which has the suggested changes applied.
from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import includes
from inspect_ai.solver import generate, system_message


@task
def hello_world_completed():
    return Task(
        dataset=[
            Sample(
                input="Just reply with Hello World",
                target=["Hello World", "Hello, World"],
            ),
        ],
        solver=[
            system_message("Be succinct"),
            generate(),
        ],
        scorer=includes(),
    )
