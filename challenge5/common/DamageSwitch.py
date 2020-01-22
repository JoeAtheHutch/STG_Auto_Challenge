import time
from collections import Counter


class damageSwitch:
    def switch(self, damage):

        def Rear():
            return "REAR END"
        
        def Front():
            return "FRONT END"
        
        def Dent():    
            return "MINOR DENT/SCRATCHES"
        
        def Under():
            return "UNDERCARRIAGE"
        
        def Default():
            return "MISC."

        damage = damage.replace(" ", "")
        damage = damage.replace("/", "")
        switcher = {
            "REAREND": Rear,
            "FRONTEND": Front,
            "MINORDENTSCRATCHES": Dent,
            "UNDERCARRIAGE": Under
        }

        return switcher.get(damage, Default)()