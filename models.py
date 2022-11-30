from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Task(Base):
    __tablename__ = 't_task'

    id = Column(Integer, primary_key=True, index=True)  # 设置主键和索引
    task_name = Column(String(32))
    email = Column(String(32))
    order_no = Column(String)
    pulished = Column(Boolean)
class File(Base):
    __tablename__ = 't_file'

    id = Column(Integer, primary_key=True, index=True)  # 设置主键和索引
    file_name = Column(String(32))
    task_id = Column(Integer)
    pulished = Column(Boolean)
