from djongo import models
from .utils import ctoi
# Create your models here.

class Color(models.TextChoices):
    RED = 'RED'
    GREEN = 'GREEN'
    BLUE = 'BLUE'
    PURPLE = 'PURPLE'
    YELLOW = 'YELLOW'
    ORANGE = 'ORANGE'

class Peg(models.TextChoices):
    BLACK = 'BLACK',
    WHITE = 'WHITE',
    NONE = 'NONE'

class Game(models.Model):
    name = models.CharField(max_length=32, default="{}".format(id))
    c1 = models.CharField(max_length=6,choices = Color.choices)
    c2 = models.CharField(max_length=6,choices = Color.choices)
    c3 = models.CharField(max_length=6,choices = Color.choices)
    c4 = models.CharField(max_length=6,choices = Color.choices)
    
    def __str__(self):
        return '{}'.format(self.name)

    # Return color serie matching
    def color_serie(self):
        result = [0,0,0,0,0,0]
        result[ctoi(self.c1)] += 1
        result[ctoi(self.c2)] += 1
        result[ctoi(self.c3)] += 1
        result[ctoi(self.c4)] += 1
        return result

class Play(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    c1 = models.CharField(max_length=6,choices = Color.choices)
    c2 = models.CharField(max_length=6,choices = Color.choices)
    c3 = models.CharField(max_length=6,choices = Color.choices)
    c4 = models.CharField(max_length=6,choices = Color.choices)

    def __str__(self):
        return 'Try in game {}'.format( self.game.name)

    

    # Looking for the answer matching, black if color and position match, white if we have just the same color
    # the vector returns 1 if black peg, 0 if white peg, -1 by default
    def keys(self):
        answer = self.game.color_serie()
        black = 0
        white = 0
        n1 = ctoi(self.c1)
        n2 = ctoi(self.c2)
        n3 = ctoi(self.c3)
        n4 = ctoi(self.c4)
        result = [-1,-1,-1,-1]
        if self.c1 == self.game.c1:
            black += 1
            answer[n1] -= 1
        if self.c2 == self.game.c2:
            black += 1
            answer[n2] -= 1
        if self.c3 == self.game.c3:
            black += 1
            answer[n3] -= 1
        if self.c4 == self.game.c4:
            black += 1
            answer[n4] -= 1
        
        if answer[n1] > 0:
            white += 1
            answer[n1] -= 1

        if answer[n2] > 0:
            white += 1
            answer[n2]-= 1

        if answer[n3]> 0:
            white += 1
            answer[n3]-= 1

        if answer[n4]> 0:
            white += 1
            answer[n4]-= 1
        

        result = ['','','','']
        last = 0
        for i in range(0,black):
            result[i] = 'BLACK'
            last += 1
        for j in range(0,white):
            result[j+last] = 'WHITE'

        return result