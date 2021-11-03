from enum import Enum


class Genre:
    def __init__(self, genreId: int, genreName: str) -> None:
        self.genreId = genreId
        self.genreName = genreName


class Profession:
    def __init__(self, professionId: int, professionName: str) -> None:
        self.professionId = professionId
        self.professionName = professionName


class Artist:
    def __init__(self, artistId: int, artistName: str, foundationYear: int, description: str) -> None:
        self.description = description
        self.foundationYear = foundationYear
        self.artistName = artistName
        self.artistId = artistId


class Festival:
    def __init__(self, fesitvalId: int, festivalName: str, festivalStartingDate, festivalEndingDate):
        self.festivalEndingDate = festivalEndingDate
        self.festivalStartingDate = festivalStartingDate
        self.festivalName = festivalName
        self.fesitvalId = fesitvalId


class TicketVendor:
    def __init__(self, ticketVendorId: int, ticketVendorName: str, ticketVendorPage: str):
        self.ticketVendorPage = ticketVendorPage
        self.ticketVendorName = ticketVendorName
        self.ticketVendorId = ticketVendorId


class Organizer:
    def __init__(self, organizerId: int, organizerName: str, organizerPage: str):
        self.organizerPage = organizerPage
        self.organizerName = organizerName
        self.organizerId = organizerId


class Country:
    def __init__(self, countryId: int, countryName: str):
        self.countryName = countryName
        self.countryId = countryId


class City:
    def __init__(self, cityId: int, cityName: str, countryName: Country):
        self.countryName = countryName
        self.cityName = cityName
        self.cityId = cityId


class Localization:
    def __init__(self, localizationId: int, localizationName: str, postCode: str, address: str, city: City):
        self.city = city
        self.address = address
        self.postCode = postCode
        self.localizationName = localizationName
        self.localizationId = localizationId


class Event:
    def __init__(self, eventId: int, eventName: str, eventDate, eventTime, localization: Localization,
                 organizer: Organizer, festival: Festival):
        self.festival = festival
        self.organizer = organizer
        self.localization = localization
        self.eventTime = eventTime
        self.eventDate = eventDate
        self.eventName = eventName
        self.eventId = eventId


class Ticket:
    def __init__(self, ticketId: int, price: float, place: str, sellingPage: str, event: Event,
                 ticketVendor: TicketVendor):
        self.ticketVendor = ticketVendor
        self.event = event
        self.sellingPage = sellingPage
        self.place = place
        self.price = price
        self.ticketId = ticketId


# TRZEBA DODAĆ TYTUŁ BO TEŻ BRAKOWAŁO
class Piece:
    def __init__(self, pieceId: str, pieceTitle: str, pieceLength: int, genre: Genre, artist: Artist):
        self.artist = artist
        self.genre = genre
        self.pieceLength = pieceLength
        self.pieceTitle = pieceTitle
        self.pieceId = pieceId


class Role(Enum):
    USER: "user"
    MODERATOR: "moderator"
    ADMIN: "admin"


class User:
    def __init__(self, userId: int, username: str, password: str, email: str, role: Role, city: City):
        self.city = city
        self.role = role
        self.email = email
        self.password = password
        self.username = username
        self.userId = userId


class ArtistsProfessions:
    def __init__(self, artistProfessionsProfessions: Profession, artistProfessionsArtists: Artist):
        self.artistProfessionsArtists = artistProfessionsArtists
        self.artistProfessionsProfessions = artistProfessionsProfessions


class ArtistsEvents:
    def __init__(self, artistsEventsArtists: Artist, artistsEventsEvents: Event):
        self.artistsEventsArtists = artistsEventsArtists
        self.artistsEventsEvents = artistsEventsEvents
