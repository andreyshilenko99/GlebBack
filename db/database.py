from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import MetaData

SQLALCHEMY_DATABASE_URL = 'sqlite:///./database.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
Session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, expire_on_commit=False
)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),

    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s'
}
metadata = MetaData(naming_convention=convention)
db_session = scoped_session(Session)


@as_declarative(metadata=metadata)
class Base:
    query = db_session.query_property()
    session = db_session

    def save(self, commit=True):
        Base.session.add(self)
        if commit:
            Base.session.commit()

    def delete(self, commit=True):
        Base.session.delete(self)
        if commit:
            Base.session.commit()

    def update(self):
        Base.session.commit()

    def merge(self, commit=True):
        Base.session.merge(self)
        if commit:
            Base.session.commit()
