# pylint: disable=E0611
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel
import datetime


class TimeLog(BaseModel):
    task_id: int
    user_id: str
    start_time: Optional[datetime.datetime]
    end_time: Optional[datetime.datetime]
    note: str


class Task(BaseModel):
    user_id: str
    task_id: int
    name: str
    importance: float
    completed: Optional[bool]
    due: Optional[datetime.datetime]
    tags: Optional[List[str]]
    urls: Optional[List[str]]
    users: Optional[List[str]]
    notes: Optional[List[str]]
    time_logs: Optional[List[TimeLog]]