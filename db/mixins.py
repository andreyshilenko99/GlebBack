import datetime

from sqlalchemy import Column, TIMESTAMP


class TimeStampMixin(object):
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        onupdate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))