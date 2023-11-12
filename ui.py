import pygame as pg

class Display:
  def __init__(self) -> None:
    self.windowSize: tuple[int] = (800, 600)
    self.window: pg.Surface = pg.display.set_mode(self.windowSize)
    self.ui: list[UIElement] = []
  
  def addElement(self, element):
    self.ui.append(element)
    self.ui[-1].parent = self
  
  def clickEvent(self, ctx):
    #ctx = [clicktype, clickpos, button]
    for ui in self.ui:
      if (ui.pos[0] <= ctx[1][0] <= ui.pos[0] + ui.size[0]) and (ui.pos[1] <= ctx[1][1] <= ui.pos[1] + ui.size[1]):
        if ctx[0] and ctx[2] == 1:
          ui.clicked = True
          break
        elif not(ctx[0]) and ctx[2] == 1:
          if ui.clicked:
            ui.onClick()
          for j in self.ui:
            j.clicked = False
          

class UIElement:
  def __init__(self, pos, size, text="") -> None:
    self.size: list[int] = size
    self.pos: list[int] = pos
    self.text: str = text
    self.parent: Display = None
    self.clicked = False
    #self.surface = pg.surface.Surface(size, parent)
  
  def defOnClick(self, func):
    self.onClick = func
  
  def onClick(self):
    print("Undefined")

def test():
  display = Display()
  ui = UIElement([0, 0], [10, 10])
  display.addElement(ui)

  @ui.defOnClick
  def hi():
    print("hi")
  
  display.clickEvent([1, [2, 2], 1])
  display.clickEvent([0, [2, 2], 1])
