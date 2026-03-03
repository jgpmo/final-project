
class Quiz:
    def __init__(self):
        self.cats = {
            'tabby': 0,
            'ragdoll': 0,
            'black cat': 0, 
            'siamese': 0,
            'maine coon': 0,

        }


    def add_point(self, category: str) -> None:
        if category == 'tabby':
            self.cats['tabby'] = self.cats.get('tabby') + 1
        if category == 'ragdoll':
            self.cats['ragdoll'] = self.cats.get('ragdoll') + 1

    def score(self) -> str:
        greatest = 0
        result = ''
        for cat, points in self.cats.items():
            if points > greatest:
                result = cat
                greatest = points
                
        return result