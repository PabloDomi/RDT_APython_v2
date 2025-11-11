"""
Strategy implementations for different frameworks
"""
from presto.strategies.base import BaseStrategy
from presto.strategies.flask_restx import FlaskRestxStrategy
from presto.strategies.fastapi import FastAPIStrategy
from presto.strategies.django_rest import DjangoRestStrategy

__all__ = [
    'BaseStrategy',
    'FlaskRestxStrategy',
    'FastAPIStrategy',
    'DjangoRestStrategy',
]
