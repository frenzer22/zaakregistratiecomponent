import factory

from ....rgbz.models import (
    AdelijkeTitel, AnderZaakObject, Contactpersoon, Naam, ZaakKenmerk
)


class NaamFactory(factory.django.DjangoModelFactory):
    voornamen = factory.sequence(lambda n: 'Willekeurige voornamen {0}'.format(n))
    geslachtsnaam = factory.sequence(lambda n: 'Willekeurige geslachtsnamen {0}'.format(n))
    voorvoegsel_geslachtsnaam = factory.SubFactory('zaakmagazijn.rgbz.tests.factory_models.VoorvoegselFactory')
    adelijke_titel = AdelijkeTitel.baron

    class Meta:
        model = Naam


class ContactpersoonFactory(factory.django.DjangoModelFactory):
    contactpersoonnaam = factory.sequence(lambda n: 'Contactpersoonnaam {0}'.format(n))

    class Meta:
        model = Contactpersoon


class AnderZaakObjectFactory(factory.django.DjangoModelFactory):
    ander_zaakobject_aanduiding = factory.sequence(lambda n: 'Identificerende beschrijving {0}'.format(n))
    ander_zaakobject_omschrijving = factory.sequence(lambda n: 'Korte omschrijving {0}'.format(n))

    class Meta:
        model = AnderZaakObject


class ZaakKenmerkFactory(factory.django.DjangoModelFactory):
    kenmerk = factory.sequence(lambda n: 'Identificatie {0}'.format(n))
    kenmerk_bron = factory.sequence(lambda n: 'Waar het kenmerk op slaat {0}'.format(n))

    class Meta:
        model = ZaakKenmerk
