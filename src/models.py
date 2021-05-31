import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

import enum

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id= Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String(50), nullable=False)
    name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    create_at = Column()
    comments: Column(Integer, ForeignKey('comment.id'))
    like: Column(Integer, ForeignKey('like.id'))
    media: Column(Integer, ForeignKey('media.id'))

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True, nullable=False)
    user_like_id = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, nullable=False)
    user_comment_id = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))


class MyEnum(enum.Enum):
    Image = 1
    Video = 2
    Reels = 3
    IGTV = 4
    Mixed = 5

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True, nullable=False)
    type_media = Column(Enum(MyEnum))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey("post.id"))


class Followers(Base):
    __tablename__ = "followers"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_follower = Column(Integer)




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e