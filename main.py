import pgzrun
from pgzero.actor import Actor

WIDTH, HEIGHT = 1280, 720

luigi = Actor("luigi")
mario = Actor("mario")
pgzrun.go()
