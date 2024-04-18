import pygame as pg

class Display:
  def __init__(self) -> None:
    self.windowSize: tuple[int] = (960, 720)
    self.window: pg.Surface = pg.display.set_mode(self.windowSize)
    self.ui: list[UIElement] = []
    self.font = pg.font.SysFont("arial", 24)
  
  def addElement(self, pos, size, color, text=None) -> object:
    self.ui.append(UIElement(pos, size, color, self, text))
    return self.ui[-1] #returns the newly created UI element
  
  def clickEvent(self, ctx) -> None:
    #ctx = [mouse down/up, clickpos, mouse button]
    for ui in self.ui:
      if (ui.pos[0] <= ctx[1][0] <= ui.pos[0] + ui.size[0]) and (ui.pos[1] <= ctx[1][1] <= ui.pos[1] + ui.size[1]):
        if ctx[0] and ctx[2] == 1:
          ui.clicked = True
        elif not(ctx[0]) and ctx[2] == 1:
          if ui.clicked and ui.clickable:
            ui.onClick()
          ui.clicked = False
      elif not(ctx[0]):
        ui.clicked = False

  def render(self) -> None:
    for ui in self.ui:
      self.window.blit(ui.surface, ui.pos)
    pg.display.flip()
          

class UIElement:
  def __init__(self, pos, size, color, parent, text) -> None:
    self.size: list[int] = size
    self.pos: list[int] = pos
    self.color = color
    self.parent: Display = parent
    self.clickable = False
    self.clicked = False
    self.surface = pg.surface.Surface(size)
    self.surface.fill(color)
    self.message = text

    if text != None:
      self.text: pg.Surface = self.parent.font.render(text, True, "#000000")
      self.textRect = self.text.get_rect(center = (size[0]//2, size[1]//2))
      self.surface.blit(self.text, self.textRect)
  
  def bindOnClick(self, func) -> None:
    self.onClick = func
    self.clickable = True
  
  def onClick(self):
    print("Undefined")

