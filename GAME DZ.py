class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        turn = True  # True - ход игрока, False - ход компьютера
        while self.player.is_alive() and self.computer.is_alive():
            if turn:
                self.player.attack(self.computer)
                turn = False
            else:
                self.computer.attack(self.player)
                turn = True
            self.status()
        self.declare_winner()

    def status(self):
        print(f"{self.player.name}: Здоровье = {self.player.health}")
        print(f"{self.computer.name}: Здоровье = {self.computer.health}")
        print()

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

def main():
    player_name = input("Введите имя игрока: ")
    game = Game(player_name)
    game.start()

if __name__ == "__main__":
    main()