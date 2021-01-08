import dataclasses
import pygame

from pygame.math import Vector2

import src.const as const
from src.field.areaClass import Area


@dataclasses.dataclass
class Field:

    surface: pygame.Surface
    polygons : list[Area] = dataclasses.field(default_factory=list)

    def draw(self):
        pygame.draw.rect(
            surface=self.surface, color=const.Color.Border,
            rect=pygame.Rect(const.Game.Field.Pos, const.Game.Field.Size),
            width=1
        )

        for polygon in self.polygons:
            pygame.draw.polygon(
                surface=self.surface, color=const.Color.FillArea,
                points=polygon.vertexes,
                width=1,
            )
