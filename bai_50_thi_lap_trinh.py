class Sinhvien:
    counter = 1
    def __init__(self, Tensinhvien, Mateam):
        self.Tensinhvien = Tensinhvien
        self.Mateam = Mateam
        self.Masinhvien = f"C{str(Sinhvien.counter).zfill(3)}"
        Sinhvien.counter += 1

    def __lt__(self, other):
        return self.Tensinhvien < other.Tensinhvien

class Team:
    counter = 1
    def __init__(self, Tenteam, Truong):
        self.Mateam = f"Team{str(Team.counter).zfill(2)}"
        self.Tenteam = Tenteam
        self.Truong = Truong
        Team.counter += 1
        self.Danhsachsinhvien = []

    def themsinhvien(self, Tensinhvien):
        self.Danhsachsinhvien.append(Tensinhvien)

def main():
    soluong = int(input())
    team = []
    for i in range(soluong):
        Tenteam = input().strip()
        Tentruong = input().strip()
        thanhvien = Team(Tenteam, Tentruong)
        team.append(thanhvien)

    sothanhvien = int(input())
    for i in range(sothanhvien):
        Tensinhvien = input().strip()
        Mateam = input().strip()
        for i in team:
            if i.Mateam == Mateam:
                sinhvien = Sinhvien(Tensinhvien, Mateam)
                i.themsinhvien(sinhvien)

    danhsachsinhvien = []
    for i in team:
        danhsachsinhvien.extend(i.Danhsachsinhvien)

    danhsachsinhvien.sort()
    for sv in danhsachsinhvien:
        ten_team = next((team.Tenteam for team in team if team.Mateam == sv.Mateam), '')
        print(f"{sv.Masinhvien} {sv.Tensinhvien} {ten_team} {next((team.Truong for team in team if team.Mateam == sv.Mateam), '')}")

if __name__ == "__main__":
    main()