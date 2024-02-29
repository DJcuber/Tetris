import pygame as pg
import pygame.locals as local
import json


class Keys:
  def __init__(self) -> None:
    with open("options.json", "r") as f:
      self.binds: dict = json.loads(f.read())["keybinds"]
    localsdict = local.__dict__
    for i in self.binds:
      self.binds[i] = localsdict[f"K_{self.binds[i]}"]
      #pg.constants, pg.locals
      
    self.keyEvents: dict = {i:False for i in ("left", "right", "hDrop", "sDrop", "hold", "rotClock", "rotAnti")}
    self.keyFunc: dict = dict()
    self.ctx = None

  def bindOnKey(self, *args, **kwargs):
    def inner(func) -> None:
      self.keyFunc[kwargs["action"]] = func
      if "ctx" in kwargs:
        self.ctx = kwargs["ctx"]
      
    return inner



if __name__ == "__main__":
  keys = Keys()
  
