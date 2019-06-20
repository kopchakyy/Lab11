import sys
sys.path.insert(0, '../models')
from ua.lviv.iot.part.models.Type import Type
from ua.lviv.iot.part.models.TransmissionType import TransmissionType
from ua.lviv.iot.part.models.Transmission import Transmission
from ua.lviv.iot.part.models.PartType import PartType
from ua.lviv.iot.part.models.BrandName import BrandName
from ua.lviv.iot.part.models.ProducingCountry import ProducingCountry
from ua.lviv.iot.part.models.Wheel import Wheel
from ua.lviv.iot.part.models.Motor import Motor
from ua.lviv.iot.part.models.Bloc import Bloc
from ua.lviv.iot.part.models.Part import Part


class PartManager:
    def __init__(self, *args):
        self.parts = args

    @staticmethod
    def sortBySerialNumber(parts, descending=False):
        return sorted(parts, key=lambda part: part.serial_number, reverse=descending)

    @staticmethod
    def sortBySerialNumberAcsending(parts):
        return PartManager.sortBySerialNumber(parts)

    @staticmethod
    def sortBySerialNumberDescending(parts):
        return PartManager.sortBySerialNumber(parts, True)

    @staticmethod
    def sortByProducingCountry(parts, descending=False):
        return sorted(parts, key=lambda part: part.producing_country, reverse=descending)

    @staticmethod
    def sortByProducingCountryAscending(parts):
        return PartManager.sortByProducingCountry(parts)

    @staticmethod
    def sortByProducingCountryDescending(parts):
        return PartManager.sortByProducingCountry(parts, True)


    def filterByBrandName(self, brand_name):
        return list(filter(lambda part: part.brand_name == brand_name, self.parts))


def main():
    parts = [
        Transmission(200, "AB9090LP", ProducingCountry.CHINA, PartType.BLOC, BrandName.HONDA, 2,
                     TransmissionType.AUTOMATIC),
        Part(250, "AB2222LP", ProducingCountry.USA, PartType.BLOC, BrandName.HONDA),
        Motor(100, "BC2209KO", ProducingCountry.JAPAN, PartType.MOTOR, BrandName.NISSAN, Type.DIESEL),
        Bloc(140, "LO26039PO", ProducingCountry.USA, PartType.BLOC, BrandName.HONDA, "L"),
        Wheel(170, "PC270918LO", ProducingCountry.JAPAN, PartType.WHEEL, BrandName.LEXSUS, 4)
    ]
    manager = PartManager(*parts)

    filteredList = manager.filterByBrandName(0)
    for s in filteredList:
        print(s)
    print()

    sortedList = PartManager.sortBySerialNumberAcsending(parts)
    for s in sortedList:
        print(s)
    print()

    sortedFilteredList = PartManager.sortByProducingCountryDescending(filteredList)
    for s in sortedFilteredList:
        print(s)


if __name__ == '__main__':
    main()
