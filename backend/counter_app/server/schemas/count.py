from datetime import datetime

from counter_app.server.schemas import CounterAppModel


class CountBase(CounterAppModel):
    date: datetime

class CountCreate(CountBase):
    pass

class Count(CountBase):
    id: int
