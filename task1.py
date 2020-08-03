import time


class TrafficLight:
    modes = (('Red', 7), ('Yellow', 2), ('Green', 9))
    __color = 'Red'

    def running(self):

        change_mode_time = time.time() // 1
        while True:
            i = 0
            while i < len(self.modes):
                if time.time() // 1 == change_mode_time:
                    change_mode_time = time.time() // 1 + self.modes[i][1]
                    self.__color = self.modes[i][0]
                    print(self.__color)
                    i += 1
                else:
                    continue
            else:
                i = i - 2
                while i > 0:
                    if time.time() // 1 == change_mode_time:
                        change_mode_time = time.time() // 1 + self.modes[i][1]
                        self.__color = self.modes[i][0]
                        print(self.__color)
                        i -= 1
                    else:
                        continue


lighter1 = TrafficLight()
lighter1.running()
