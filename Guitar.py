from enum import Enum

class Builder(Enum):
    FENDER = "Fender"
    MARTIN = "Martin"
    GIBSON = "Gibson"
    COLLINGS = "Collings"
    OLSON = "Olson"
    RYAN = "Ryan"
    PRS = "PRS"
    ANY = "Any"

class Type(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"
    ANY = "any"

class Wood(Enum):
    INDIAN_ROSEWOOD = "Indian Rosewood"
    BRAZILIAN_ROSEWOOD = "Brazilian Rosewood"
    MAHOGANY = "Mahogany"
    MAPLE = "Maple"
    COCOBOLO = "Cocobolo"
    CEDAR = "Cedar"
    ADIRONDACK = "Adirondack"
    ALDER = "Alder"
    SITKA = "Sitka"
    ANY = "Any"

class GuitarSpec:
    def __init__(self, builder, model, type, backwood, topwood):
        self.builder = builder
        self.model = model
        self.type = type
        self.backwood = backwood
        self.topwood = topwood

    def get_builder(self):
        return self.builder

    def get_model(self):
        return self.model

    def get_type(self):
        return self.type

    def get_backwood(self):
        return self.backwood

    def get_topwood(self):
        return self.topwood

    def matches(self, other_spec):
        if self.builder != other_spec.get_builder() and self.builder != Builder.ANY and other_spec.get_builder() != Builder.ANY:
            return False
        if self.model != other_spec.get_model() and self.model != "" and other_spec.get_model() != "":
            return False
        if self.type != other_spec.get_type() and self.type != Type.ANY and other_spec.get_type() != Type.ANY:
            return False
        if self.backwood != other_spec.get_backwood() and self.backwood != Wood.ANY and other_spec.get_backwood() != Wood.ANY:
            return False
        if self.topwood != other_spec.get_topwood() and self.topwood != Wood.ANY and other_spec.get_topwood() != Wood.ANY:
            return False
        return True

class Guitar:
    def __init__(self, serial_number, price, spec):
        self.serial_number = serial_number
        self.price = price
        self.spec = spec

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_spec(self):
        return self.spec


class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, builder, model, type, backwood, topwood):
        guitar_spec = GuitarSpec(builder, model, type, backwood, topwood)
        guitar = Guitar(serial_number, price, guitar_spec)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search(self, search_spec):
        matching_guitars = []
        for guitar in self.guitars:
            if guitar.get_spec().matches(search_spec):
                matching_guitars.append(guitar)
        return matching_guitars





if __name__ == '__main__':
    inventory = Inventory()

    inventory.add_guitar("11277", 3999.95, Builder.COLLINGS, "CJ",
                         Type.ACOUSTIC, Wood.INDIAN_ROSEWOOD, Wood.SITKA)
    inventory.add_guitar("V95693", 1499.95, Builder.FENDER, "Stratocaster",
                         Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
    inventory.add_guitar("V9512", 1549.95, Builder.FENDER, "Stratocaster",
                         Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
    inventory.add_guitar("122784", 5495.95, Builder.MARTIN, "D-18",
                         Type.ACOUSTIC, Wood.MAHOGANY, Wood.ADIRONDACK)
    inventory.add_guitar("76531", 6295.95, Builder.MARTIN, "OM-28",
                         Type.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD,
                         Wood.ADIRONDACK)
    inventory.add_guitar("70108276", 2295.95, Builder.GIBSON, "Les Paul",
                         Type.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE)
    inventory.add_guitar("82765501", 1890.95, Builder.GIBSON, "SG '61 Reissue",
                         Type.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY)
    inventory.add_guitar("77023", 6275.95, Builder.MARTIN, "D-28",
                         Type.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD,
                         Wood.ADIRONDACK)
    inventory.add_guitar("1092", 12995.95, Builder.OLSON, "SJ", Type.ACOUSTIC,
                         Wood.INDIAN_ROSEWOOD, Wood.CEDAR)
    inventory.add_guitar("566-62", 8999.95, Builder.RYAN, "Cathedral",
                         Type.ACOUSTIC, Wood.COCOBOLO, Wood.CEDAR)
    inventory.add_guitar("6 29584", 2100.95, Builder.PRS,
                         "Dave Navarro Signature", Type.ELECTRIC,
                         Wood.MAHOGANY, Wood.MAPLE)

    # Test guitar search
    what_bob_wants = GuitarSpec( Builder.PRS,
                         "Dave Navarro Signature", Type.ELECTRIC,
                         Wood.MAHOGANY, Wood.MAPLE)
    matching_guitars = inventory.search(what_bob_wants)

    if matching_guitars:
        for guitar in matching_guitars:
            spec = guitar.get_spec()
            print(
                f"We have a {spec.get_builder().value} {spec.get_model()} "
                f"{spec.get_type().value} guitar:\n   {spec.get_backwood().value} "
                f"back and sides,\n   {spec.get_topwood().value} top.\n"
                f"You can have it for only ${guitar.get_price()}!\n"
                f"  ----")
    else:
        print("Sorry, Bob, we have nothing for you.")
