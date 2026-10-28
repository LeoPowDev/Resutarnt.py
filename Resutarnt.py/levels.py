class Levels:
    def __init__(self):
        self.xp = 0
        self.achievements = []
        self.vip = False

    def Achievement(self, name, xp):
        if name in self.achievements:
            return

        self.achievements.append(name)
        self.xp += xp

        print("\nACHIEVEMENT UNLOCKED!")
        print(name)
        print(f"+{xp} XP")
        print(f"Total XP: {self.xp}")

        if self.xp >= 250 and not self.vip:
            self.vip = True
            print("\nVIP UNLOCKED!")
            print("You have reached 250 XP.")
            print("You are now a VIP customer.")

    def ShowStatus(self):
        print("\n--- PLAYER STATUS ---")
        print(f"XP: {self.xp}")

        if self.vip:
            print("Status: VIP")
        else:
            print("Status: Customer")
            print(f"XP needed for VIP: {250 - self.xp}")

    def ShowAchievements(self):
        print("\n--- ACHIEVEMENTS ---")

        if not self.achievements:
            print("No achievements unlocked yet.")
            return

        for achievement in self.achievements:
            print(achievement)