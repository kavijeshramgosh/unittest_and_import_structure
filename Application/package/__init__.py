#Turns "package" into a package for main.py

from .Fourth import Four #This lets us call the function directly instead of adding Fourth.Four

__all__ = ["Third","Four"]#Third in the table lets us call Third.Three directly

