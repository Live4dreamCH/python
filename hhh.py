class stu:
    stuID = 218546551
    name = ''
    grade = 82
    def cheat(self):
        self.grade = 0
    def tuixue(self):
        del self
    def wuxian(self, other):
        other.grade = 0


if __name__ == "__main__":
    a = stu()
    b = stu()
    a.cheat()
    a.grade = 60
    b.wuxian(a)
    print()