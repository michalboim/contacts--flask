class Contact:
    def __init__(self, name: str, email:str, phone:str,  tid:int=1 ) -> None:
        self.tid=tid
        self.name=name
        self.email=email
        self.phone=phone