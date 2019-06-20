from ua.lviv.iot.part.models.BrandName import BrandName
from ua.lviv.iot.part.models.ProducingCountry import ProducingCountry
from ua.lviv.iot.part.models.PartType import PartType


class Part:

    def __init__(self,
                 price=0, serial_number="NoSerialNumber", producing_country=ProducingCountry.CHINA, part_type=PartType.TRANSMISSION, brand_name=BrandName.HONDA):

        self.price = price
        self.serial_number = serial_number
        self.producing_country = producing_country
        self.part_type = part_type
        self.brand_name = brand_name


    def __str__(self):

        return ', '.join((f"{name} = {value}" for name, value in self.__dict__.items()))