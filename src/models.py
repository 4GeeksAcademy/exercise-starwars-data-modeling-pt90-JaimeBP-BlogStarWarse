import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.sql import func   #Para que se asigne automaticamente la fecha de DateTime

Base = declarative_base()

# Tabla de Usuarios
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=func.now())

    favorites = relationship('Favorite', back_populates='user')

# Tabla de Personajes de Star Wars
class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    birth_year = Column(String(50))
    gender = Column(String(50))
    eye_color = Column(String(50))
    hair_color = Column(String(50))

    favorites = relationship('Favorite', back_populates='character')

# Tabla de Planetas de Star Wars
class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    terrain = Column(String(100))
    population = Column(Integer)

    favorites = relationship('Favorite', back_populates='planet')

# Tabla de Favoritos
class Favorite(Base):
    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)

    user = relationship('User', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')

# Generar el diagrama de la base de datos
try:
    result = render_er(Base, 'diagram.png')
    print("¡Éxito! Revisa el archivo diagram.png")
except Exception as e:
    print("Hubo un problema generando el diagrama")
    raise e
