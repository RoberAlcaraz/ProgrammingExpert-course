class Animal:
    def sleep(self):
        print('ZzzZzz')

    def animal_sound(self):
        raise NotImplementedError

    def wake_up(self):
        self.animal_sound()
        print('I am awake!')


class Lion(Animal):
    def __init__(self):
        pass

    def animal_sound(self):
        print('Roar!')


leo = Lion()
leo.sleep()
leo.animal_sound()
leo.wake_up()
