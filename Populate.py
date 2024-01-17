from SmartBlockchain import *


class Populate:
    def __init__(self):
        bc = SmartBlockchain()
        bc.new_block()
        bc.new_transaction("a", 10, "b")
        bc.new_transaction("b", 30, "c")
        print(bc.last_block_json())
        bc.new_block()
        print(bc.last_block_json())
