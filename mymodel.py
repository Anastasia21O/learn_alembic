from sqlalchemy.orm import declarative_base
import sqlalchemy as sa

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    fullname = sa.Column(sa.String)
    nickname = sa.Column(sa.String)
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)