class C32:
    def __init__(self):
        self.state = AState(self)

    def add(self):
        return self.state.add()

    def hike(self):
        return self.state.hike()

    def mute(self):
        return self.state.mute()

    def stand(self):
        return self.state.stand()


# Главный класс конечного автомата Мили
class MileMachineState:
    def __init__(self, root):
        self.root = root

    def add(self):
        # print('RuntimeError')
        raise RuntimeError

    def hike(self):
        # print('RuntimeError')
        raise RuntimeError

    def mute(self):
        # print('RuntimeError')
        raise RuntimeError
    
    def stand(self):
        # print('RuntimeError')
        raise RuntimeError


# Состояние A
class AState(MileMachineState):
    def add(self):
        self.root.state = BState(self.root)
        return 0

# Состояние B
class BState(MileMachineState):
    def hike(self):
        self.root.state = BState(self.root)
        return 2

    def add(self):
        self.root.state = CState(self.root)
        return 1

# Состояние C
class CState(MileMachineState):
    def add(self):
        self.root.state = DState(self.root)
        return 3

# Состояние D
class DState(MileMachineState):
    def add(self):
        self.root.state = EState(self.root)
        return 4

# Состояние E
class EState(MileMachineState):
    def add(self):
        self.root.state = CState(self.root)
        return 7
      
    def mute(self):
        self.root.state = BState(self.root)
        return 6

    def stand(self):
        self.root.state = FState(self.root)
        return 5

    def hike(self):
        self.root.state = GState(self.root)
        return 8

# Состояние F
class FState(MileMachineState):
    def mute(self):
        self.root.state = GState(self.root)
        return 9

# Состояние G
class GState(MileMachineState):
    def stand(self):
        self.root.state = HState(self.root)
        return 10

    def hike(self):
        self.root.state = CState(self.root)
        return 11
        
class HState(MileMachineState):
    def stand(self):
        raise RuntimeError
        
    
    
    
    
        
    
    
