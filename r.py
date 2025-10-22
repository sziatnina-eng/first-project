class Movable:
    def MoveUp(self) -> None:
        pass
    def MoveDown(self) -> None:
        pass
    def MoveLeft(self) -> None:
        pass
    def MoveRight(self) -> None:
        pass

class MovablePoint(Movable):
    x: int
    y: int
    xSpeed: int
    ySpeed: int
    def __init__(self, x:int, y:int, xSpeed:int, ySpeed:int):
        pass
    def toString(self) -> str:
        pass

class MovableCircle(Movable):
    center: MovablePoint
    radius: int
    def __init__(self, x:int, y:int, xSpeed:int, ySpeed:int, radius:int):
        pass
    def toString(self) -> str:
        pass
