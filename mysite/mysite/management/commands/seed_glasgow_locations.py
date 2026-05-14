from django.core.management.base import BaseCommand
from django.utils.text import slugify

from mysite.models import Location


GLASGOW_AREAS = [
    "Airdrie",
    "Anderston",
    "Anniesland",
    "Balornock",
    "Barrhead",
    "Battlefield",
    "Bearsden",
    "Bellahouston",
    "Bellshill",
    "Bishopbriggs",
    "Bishopton",
    "Blantyre",
    "Blythswood Hill",
    "Bothwell",
    "Bridge of Weir",
    "Bridgeton",
    "Calton",
    "Cambuslang",
    "Camlachie",
    "Cardonald",
    "Carluke",
    "Carntyne",
    "Cathcart",
    "Cessnock",
    "Charing Cross",
    "City Centre",
    "Clarkston",
    "Clydebank",
    "Coatbridge",
    "Cowcaddens",
    "Crookston",
    "Crosshill",
    "Dalmarnock",
    "Dennistoun",
    "Dowanhill",
    "East End",
    "East Kilbride",
    "Erskine",
    "Finnieston",
    "Garnethill",
    "Giffnock",
    "Gilshochill",
    "Govan",
    "Govanhill",
    "Haghill",
    "Hamilton",
    "Hillhead",
    "Hillington",
    "Houston",
    "Hyndland",
    "Ibrox",
    "Johnstone",
    "Jordanhill",
    "Kelvinbridge",
    "Kelvingrove",
    "Kelvinside",
    "Kilmacolm",
    "King's Park",
    "Kinning Park",
    "Kirkintilloch",
    "Knightswood",
    "Lambhill",
    "Lanark",
    "Lanarkshire",
    "Langside",
    "Larkhall",
    "Lenzie",
    "Maryhill",
    "Merchant City",
    "Milngavie",
    "Milton",
    "Mosspark",
    "Motherwell",
    "Mount Florida",
    "Muirend",
    "Newlands",
    "Newton Mearns",
    "Paisley",
    "Parkhead",
    "Partick",
    "Partickhill",
    "Penilee",
    "Plantation",
    "Pollokshaws",
    "Pollokshields",
    "Possilpark",
    "Renfrew",
    "Riddrie",
    "Ruchill",
    "Rutherglen",
    "Scotstoun",
    "Scotstounhill",
    "Shawlands",
    "Shettleston",
    "Simshill",
    "Southside",
    "Springburn",
    "Stepps",
    "Stonehouse",
    "Strathbungo",
    "Summerston",
    "Tollcross",
    "Townhead",
    "Uddingston",
    "West End",
    "Whiteinch",
    "Wishaw",
    "Yoker",
]

FEATURED_AREAS = {
    "City Centre",
    "Dennistoun",
    "Finnieston",
    "Paisley",
    "Partick",
    "Rutherglen",
    "Shawlands",
    "West End",
}


class Command(BaseCommand):
    help = "Seeds Glasgow and its service areas."

    def handle(self, *args, **options):
        glasgow, created = Location.objects.get_or_create(
            slug="glasgow",
            parent=None,
            defaults={
                "name": "Glasgow",
                "location_type": Location.CITY,
                "is_active": True,
                "meta_title": "Glasgow Vehicle Recovery | M&M Recovery",
                "meta_description": "Vehicle recovery, roadside assistance, and towing across Glasgow.",
            },
        )

        if not created:
            changed = False
            if glasgow.name != "Glasgow":
                glasgow.name = "Glasgow"
                changed = True
            if glasgow.location_type != Location.CITY:
                glasgow.location_type = Location.CITY
                changed = True
            if not glasgow.is_active:
                glasgow.is_active = True
                changed = True
            if changed:
                glasgow.save()

        created_count = 0
        updated_count = 0
        for area_name in GLASGOW_AREAS:
            area_slug = slugify(area_name)
            area, area_created = Location.objects.get_or_create(
                slug=area_slug,
                parent=glasgow,
                defaults={
                    "name": area_name,
                    "location_type": Location.AREA,
                    "is_active": True,
                    "is_featured": area_name in FEATURED_AREAS,
                    "meta_title": f"{area_name} Vehicle Recovery Glasgow | M&M Recovery",
                    "meta_description": f"Fast vehicle recovery, towing, and roadside assistance in {area_name}, Glasgow.",
                },
            )
            if area_created:
                created_count += 1
                continue

            changed = False
            if area.name != area_name:
                area.name = area_name
                changed = True
            if area.location_type != Location.AREA:
                area.location_type = Location.AREA
                changed = True
            if not area.is_active:
                area.is_active = True
                changed = True
            if area.is_featured != (area_name in FEATURED_AREAS):
                area.is_featured = area_name in FEATURED_AREAS
                changed = True
            if changed:
                area.save()
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Glasgow seeded. Created {created_count} areas and updated {updated_count} existing areas."
            )
        )
