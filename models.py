from dataclasses import dataclass


@dataclass
class Task:
    desc: str
    is_done: bool = False
    priority: str | None = None
    project: str | None = None
    context: str | None = None
    due: str | None = None
