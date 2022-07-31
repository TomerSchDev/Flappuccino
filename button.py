import pygame


class Button:
    def __init__(self, price, pos):
        self.price = price
        self.background = pygame.image.load('data/gfx/retry_button.png')
        self.pos = (pos[0] - self.background.get_width() / 2, pos[1])

    def draw(self, DISPLAY, font_small):

        DISPLAY.blit(self.background, self.pos)
        priceDisplay = font_small.render(str(self.price), True, (0, 0, 0))
        x = self.pos[0] + self.background.get_width() / 2 - priceDisplay.get_width() / 2
        y = self.pos[1] + self.background.get_height() / 2 - priceDisplay.get_height() / 2
        DISPLAY.blit(priceDisplay, (x, y))

    def pressed(self, mouse_pos):
        pygame.mouse.get_pressed()
        width = self.background.get_width()
        height = self.background.get_height()
        return pygame.Rect(self.pos[0], self.pos[1], width, height).collidepoint(mouse_pos)


class UpgradeButton(Button):
    def __init__(self, price, sprite, pos):
        super().__init__(price, pos)
        self.background = pygame.image.load('data/gfx/button.png')
        self.level = 1
        self.sprite = pygame.image.load(sprite)
        self.typeIndicatorSprite = pygame.image.load('data/gfx/null_indicator.png')

    def draw(self, DISPLAY, font_small, font_20):
        """
        function to draw the buttons to the DISPLAY
        todo currently works only in upgrades
        :param DISPLAY: the window
        :param pos: the position of the button
        :param font_small: small font
        :param font_20: the big font
        :return:
        """
        super().draw(DISPLAY, font_small)
        x, y = self.pos
        levelDisplay = font_20.render('Lvl. ' + str(self.level), True, (200, 200, 200))
        DISPLAY.blit(levelDisplay, (x + 14, y + 48))
        DISPLAY.blit(self.typeIndicatorSprite, (x - 18, y - 15))
        DISPLAY.blit(self.sprite, (x - 18, y - 15))

    def buyUpgrade(self,beanCount):
        pass
