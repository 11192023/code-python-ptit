class Hogiadinh:
    def __init__(self,Hoten,Loaiho,Sodau,Socuoi,So):
        self.Ma=f"KH{So:02}"
        self.Hoten = " ".join(Hoten.split()).title()
        self.Loaiho= Loaiho.strip().upper()
        self.Sodau = Sodau
        self.Socuoi = Socuoi
    def tinhtiendien(self):
        if self.Loaiho == 'A':
            dinhmuc = 100
        elif self.Loaiho == 'B':
            dinhmuc = 500
        elif self.Loaiho == 'C':
            dinhmuc = 200
        sodien = self.Socuoi-self.Sodau
        if dinhmuc > sodien :
            tientrongdinhmuc = sodien*450
        else:
            tientrongdinhmuc = dinhmuc*450
        if dinhmuc<sodien:
            tienvuotdinhmuc = (sodien-dinhmuc)*1000
            thuevat = int(tienvuotdinhmuc/20)
        else:
            tienvuotdinhmuc = 0
            thuevat = 0
        sotienphainop = tientrongdinhmuc+tienvuotdinhmuc+thuevat
        return tientrongdinhmuc,tienvuotdinhmuc,thuevat,sotienphainop
def main():
    N = int(input())
    khachhang = []
    for i in range(N):
        Hoten = input()
        loaiho,sodau,socuoi = input().split()
        sodau,socuoi = map(int,[sodau,socuoi])
        khachhang.append(Hogiadinh(Hoten,loaiho,sodau,socuoi,len(khachhang)+1))
    for i in khachhang:
        tientrongdinhmuc,tienvuotdinhmuc,thuevat,sotienphainop = i.tinhtiendien()
        i.tientrongdinhmuc = tientrongdinhmuc
        i.tienvuotdinhmuc = tienvuotdinhmuc
        i.thuevat = thuevat
        i.sotienphainop = sotienphainop
    khachhang.sort(key=lambda x:x.sotienphainop,reverse=True)
    for j,i in enumerate(khachhang,start=1):
        print(f"{i.Ma} {i.Hoten} {i.tientrongdinhmuc} {i.tienvuotdinhmuc} {i.thuevat} {i.sotienphainop}")
main()