from dataclasses import dataclass
from typing import Optional, Required

@dataclass
class Task:
    desc: str
    is_done: bool = False
    priority: Optional[str] = None
    project: Optional[str] = None
    context: Optional[str] = None
    due: Optional[str] = None
