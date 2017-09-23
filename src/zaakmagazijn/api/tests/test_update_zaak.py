from unittest import skip

from lxml import etree
from mock import patch

from ...rgbz.choices import Rolomschrijving, RolomschrijvingGeneriek
from ...rgbz.models import (
    Medewerker, OrganisatorischeEenheid, Rol, WaterdeelObject, Zaak
)
from ...rgbz.tests.factory_models import (
    BesluitFactory, BesluitTypeFactory, BetrokkeneFactory,
    BetrokkeneMetRolFactory, BetrokkeneMetVerzendingFactory,
    KlantcontactFactory, KlantcontactMetVestigingFactory, MedewerkerFactory,
    NatuurlijkPersoonFactory, NietNatuurlijkPersoonFactory,
    OrganisatorischeEenheidFactory, RolFactory, StatusFactory, Verzending,
    VestigingFactory, VestigingVanZaakBehandelendeOrganisatieFactory,
    ZaakFactory, ZaakKenmerk, ZaakTypeFactory
)
from ..stuf.choices import (
    BerichtcodeChoices, ClientFoutChoices, ServerFoutChoices
)
from .base import BaseSoapTests, BaseTestPlatformTests


class MaykinupdateZaak_ZakLk01ZakObjectTests(BaseTestPlatformTests):
    test_files_subfolder = 'maykin_updateZaak'
    porttype = 'OntvangAsynchroon'

    def setUp(self):
        super().setUp()

        self.context = {
            'gemeentecode': '1234',
            'datumVandaag': self.genereerdatum(),
            'datumGisteren': self.genereerdatum(-1),
            'datumEergisteren': self.genereerdatum(-2),
            'tijdstipRegistratie': self.genereerdatumtijd(),

            'zds_zaaktype_code': '12345678',
            'zds_zaaktype_omschrijving': 'Aanvraag burgerservicenummer behandelen',
            'referentienummer': self.genereerID(10),
            'creerzaak_identificatie_7': self.genereerID(10),
            'creerzaak_identificatie_11': self.genereerID(10)
        }
        self.zaak = ZaakFactory.create(
            zaakidentificatie="{}{}".format(self.context['gemeentecode'], self.context['creerzaak_identificatie_7']),
            omschrijving="omschrijving",
        )

    def test_zakobj_buurt(self):
        # TODO: Implement
        pass

    def test_zakobj_enkelvoudig_document(self):
        pass

    def test_zaakobject_gemeente(self):
        pass

    def test_zaakobject_gemeentelijkeOpenbareRuimte(self):
        # TODO: Implement
        pass

    def test_zaakobject_huishouden(self):
        # TODO: Implement
        pass

    def test_zaakobject_inrichtingselement(self):
        # TODO: Implement
        pass

    def test_zaakobject_kadastraleOnroerendeZaak(self):
        # TODO: Implement
        pass

    def test_zaakobject_kunstwerkdeel(self):
        # TODO: Implement
        pass

    def test_zaakobject_maatschappelijkeActiviteit(self):
        # TODO: Implement
        pass

    def test_zaakobject_medewerker(self):
        # TODO: Implement
        pass

    def test_zaakobject_natuurlijkPersoon(self):
        # TODO: Implement
        pass

    def test_zaakobject_nietNatuurlijkPersoon(self):
        # TODO: Implement
        pass

    def test_zaakobject_openbareRuimte(self):
        # TODO: Implement
        pass

    def test_zaakobject_organisatorischeEenheid(self):
        # TODO: Implement
        pass

    def test_zaakobject_pand(self):
        # TODO: Implement
        pass

    def test_zaakobject_samengesteldDocument(self):
        # TODO: Implement
        pass

    def test_zaakobject_spoorbaandeel(self):
        # TODO: Implement
        pass

    def test_zaakobject_status(self):
        # TODO: Implement
        pass

    def test_zaakobject_terreindeel(self):
        # TODO: Implement
        pass

    def test_zaakobject_vestiging(self):
        # TODO: Implement
        pass

    def test_zaakobject_waterdeel(self):
        vraag = 'updateZaak_ZakLk01_waterdeel.xml'
        self.context.update({
            'waterdeel_type': 'Zee',
            'waterdeel_naam': 'naam',
            'waterdeel_identificatie': 'BE.IMGEO.1234567890123456',
            'waterdeel_ingangsdatum': '20170902',
            'waterdeel_einddatum': '20170903',
        })
        response = self._do_request(self.porttype, vraag, self.context)
        self.assertEquals(response.status_code, 200, response.content)
        response_root = etree.fromstring(response.content)

        waterdeel = self.zaak.zaakobject_set.get().object.is_type()
        self.assertIs(type(waterdeel), WaterdeelObject)
        self.assertEquals(waterdeel.identificatie, self.context['waterdeel_identificatie'])
        self.assertEquals(waterdeel.naam, self.context['waterdeel_naam'])
        self.assertEquals(waterdeel.type_waterdeel, self.context['waterdeel_type'])
        self.assertEquals(waterdeel.datum_begin_geldigheid_waterdeel, self.context['waterdeel_ingangsdatum'])
        self.assertEquals(waterdeel.datum_einde_geldigheid_waterdeel, self.context['waterdeel_einddatum'])

    def test_zaakobject_wegdeel(self):
        # TODO: Implement
        pass

    def test_zaakobject_wijk(self):
        # TODO: Implement
        pass

    def test_zaakobject_woonplaats(self):
        # TODO: Implement
        pass

    def test_zaakobject_wozDeelobject(self):
        # TODO: Implement
        pass

    def test_zaakobject_wozObject(self):
        # TODO: Implement
        pass

    def test_zaakobject_wozWaarde(self):
        # TODO: Implement
        pass

    def test_zaakobject_zakelijkRecht(self):
        # TODO: Implement
        pass


class MaykinupdateZaak_ZakLk01Tests(BaseTestPlatformTests):
    test_files_subfolder = 'maykin_updateZaak'
    porttype = 'OntvangAsynchroon'

    def setUp(self):
        super().setUp()

        self.context = {
            'gemeentecode': '1234',
            'datumVandaag': self.genereerdatum(),
            'datumGisteren': self.genereerdatum(-1),
            'datumEergisteren': self.genereerdatum(-2),
            'tijdstipRegistratie': self.genereerdatumtijd(),

            'zds_zaaktype_code': '12345678',
            'zds_zaaktype_omschrijving': 'Aanvraag burgerservicenummer behandelen',
            'referentienummer': self.genereerID(10),
            'creerzaak_identificatie_7': self.genereerID(10),
            'creerzaak_identificatie_11': self.genereerID(10)
        }
        self.zaak = ZaakFactory.create(
            zaakidentificatie="{}{}".format(self.context['gemeentecode'], self.context['creerzaak_identificatie_7']),
            omschrijving="omschrijving",
        )

    def _assert_error_response(self, response_root):
        ontvanger_organisatie = response_root.xpath('//stuf:stuurgegevens/stuf:ontvanger/stuf:organisatie', namespaces=self.nsmap)[0].text
        self.assertEquals(ontvanger_organisatie, 'KING')
        ontvanger_applicatie = response_root.xpath('//stuf:stuurgegevens/stuf:ontvanger/stuf:applicatie', namespaces=self.nsmap)[0].text
        self.assertEquals(ontvanger_applicatie, 'STP')
        ontvanger_gebruiker = response_root.xpath('//stuf:stuurgegevens/stuf:ontvanger/stuf:gebruiker', namespaces=self.nsmap)[0].text
        self.assertEquals(ontvanger_gebruiker, None)

        cross_refnummer = response_root.xpath('//stuf:stuurgegevens/stuf:crossRefnummer', namespaces=self.nsmap)[0].text
        self.assertEquals(cross_refnummer, self.context['referentienummer'])

    def test_eindig_relatie_entiteit(self):
        """
        Test a 'E' replace operation on a 'relatie-entiteit' and make sure
        only the Rol connected to the Zaak being updated is changed, but
        a Rol connected to a different Zaak is unmodified.
        """
        # TODO: Write test
        pass

    def test_identifiy_relatie_entiteit(self):
        """
        Test that a 'I' operation on a zaak only finds the object connected
        to the specified zaak, and not one connected to a different Zaak.
        """
        # TODO: Write test
        pass

    def test_replace_relatie_entiteit(self):
        """
        Test a 'R' replace operation on a 'relatie-entiteit' and make sure
        only the Rol connected to the Zaak being updated is changed, but
        a Rol connected to a different Zaak is unmodified.
        """
        identificatie = "12345678"
        oeh = OrganisatorischeEenheidFactory.create(
            identificatie=identificatie,
            organisatieidentificatie='1234',
            organisatieeenheididentificatie=identificatie,
            naam=identificatie
        )
        self.assertEqual(oeh.identificatie, identificatie)
        new_identificatie = "87654321"
        new_oeh = OrganisatorischeEenheidFactory.create(
            identificatie=new_identificatie,
            organisatieidentificatie='8765',
            organisatieeenheididentificatie=new_identificatie,
            naam=new_identificatie
        )
        self.assertEqual(new_oeh.identificatie, new_identificatie)

        rol1 = RolFactory.create(zaak=self.zaak, betrokkene=oeh, rolomschrijving=Rolomschrijving.initiator)
        rol2 = RolFactory.create(betrokkene=oeh, rolomschrijving=Rolomschrijving.initiator)

        besluittype = BesluitTypeFactory.create(besluittypeomschrijving='omschrijving5')
        vraag = 'updateZaak_ZakLk01_replace_relatie_entiteit.xml'
        response = self._do_request(self.porttype, vraag, self.context)
        self.assertEquals(response.status_code, 200, response.content)
        response_root = etree.fromstring(response.content)

        # Rol connected to the ZAK and to the OEH is changed.
        self.assertTrue(Rol.objects.filter(pk=rol1.pk, betrokkene=new_oeh.pk).exists())

        # The other Rol is not modified.
        self.assertTrue(Rol.objects.filter(pk=rol2.pk, betrokkene=oeh.pk).exists())

    def test_verwijder_relatie_entiteit(self):
        """
        Test a delete of a relatie-entiteit, and make sure only that relation is
        deleted, and not a relatie-entiteit with the same data, but connected
        to a different Zaak.
        """
        identificatie = "{gemeentecode}98765".format(gemeentecode=self.context['gemeentecode'])
        self.organisatorische_eenheid = OrganisatorischeEenheidFactory.create(
            identificatie=identificatie,
            organisatieeenheididentificatie=identificatie,
            organisatieidentificatie=self.context['gemeentecode'],
            naam=identificatie
        )
        self.assertEqual(self.organisatorische_eenheid.identificatie, identificatie)
        rol1 = RolFactory.create(zaak=self.zaak, betrokkene=self.organisatorische_eenheid, rolomschrijving=Rolomschrijving.initiator)
        rol2 = RolFactory.create(betrokkene=self.organisatorische_eenheid, rolomschrijving=Rolomschrijving.initiator)

        besluittype = BesluitTypeFactory.create(besluittypeomschrijving='omschrijving5')
        vraag = 'updateZaak_ZakLk01_delete_relatie_entiteit.xml'
        response = self._do_request(self.porttype, vraag, self.context)
        self.assertEquals(response.status_code, 200, response.content)
        response_root = etree.fromstring(response.content)

        # Rol connected to the ZAK and to the OEH is deleted.
        self.assertFalse(Rol.objects.filter(pk=rol1.pk).exists())

        # Any other role connected the OEH is kept.
        self.assertTrue(Rol.objects.filter(pk=rol2.pk).exists())

    def test_platgeslagen_velden(self):
        """
        Test that if a 'platgeslagen' entiteit is tried to be retrieved, but does
        not exist an error is thrown.
        """
        pass

    def test_leidtTot_identify(self):
        """
        """
        besluittype = BesluitTypeFactory.create(besluittypeomschrijving='omschrijving5')
        vraag = 'updateZaak_ZakLk01_leidtTot.xml'
        response = self._do_request(self.porttype, vraag, self.context)
        self.assertEquals(response.status_code, 200, response.content)
        response_root = etree.fromstring(response.content)

    @patch('zaakmagazijn.rgbz.models.zaken.Zaak.objects')
    def test_more_than_1_object_found(self, mock_zaak_objects):
        """
        Test that when more than 1 object is found, StUF067: "Dubbelen voor object gevonden"
        is returned.

        Note: It's not possible to test this case with real data, because there is a unique constraint
        on Zaakidentificatie.
        """
        mock_zaak_objects.get.side_effect = Zaak.MultipleObjectsReturned('some error message')

        vraag = 'updateZaak_ZakLk01_does_not_exist.xml'
        response = self._do_request(self.porttype, vraag, self.context)
        self.assertEquals(response.status_code, 500, response.content)
        response_root = etree.fromstring(response.content)

        response_berichtcode = response_root.xpath('//stuf:stuurgegevens/stuf:berichtcode', namespaces=self.nsmap)[0].text
        self.assertEqual(response_berichtcode, BerichtcodeChoices.fo03, response.content)

        code = response_root.xpath('//stuf:body/stuf:code', namespaces=self.nsmap)[0].text
        self.assertEqual(code, ServerFoutChoices.stuf067, response.content)

        omschrijving = response_root.xpath('//stuf:body/stuf:omschrijving', namespaces=self.nsmap)[0].text
        self.assertEqual(omschrijving, "Dubbelen voor object gevonden", response.content)

        details = response_root.xpath('//stuf:body/stuf:details', namespaces=self.nsmap)[0].text
        self.assertEqual(details, "some error message", response.content)

        self._assert_error_response(response_root)

    def test_object_doest_not_exist(self):
        """
        Make sure that: StUF064 "Object niet gevonden", is sent as a response
        when a Object is not found.
        """
        self.zaak.delete()

        vraag = 'updateZaak_ZakLk01_does_not_exist.xml'
        response = self._do_request(self.porttype, vraag, self.context)
        self.assertEquals(response.status_code, 500, response.content)
        response_root = etree.fromstring(response.content)

        response_berichtcode = response_root.xpath('//stuf:stuurgegevens/stuf:berichtcode', namespaces=self.nsmap)[0].text
        self.assertEqual(response_berichtcode, BerichtcodeChoices.fo03, response.content)

        code = response_root.xpath('//stuf:body/stuf:code', namespaces=self.nsmap)[0].text
        self.assertEqual(code, ServerFoutChoices.stuf064, response.content)

        omschrijving = response_root.xpath('//stuf:body/stuf:omschrijving', namespaces=self.nsmap)[0].text
        self.assertEqual(omschrijving, "Object niet gevonden", response.content)

        details = response_root.xpath('//stuf:body/stuf:details', namespaces=self.nsmap)[0].text
        self.assertEqual(details, "Zaak matching query does not exist.", response.content)

        self._assert_error_response(response_root)

    def test_updateZaak_zakLK01_different_mnmemonic(self):
        """
        Test that when an incorrect mnemonic is used, the service throws
        an error.
        """
        vraag = 'updateZaak_ZakLk01_mnemonic.xml'
        response = self._do_request(self.porttype, vraag, self.context)
        self.assertEquals(response.status_code, 500, response.content)
        response_root = etree.fromstring(response.content)

        response_berichtcode = response_root.xpath('//stuf:stuurgegevens/stuf:berichtcode', namespaces=self.nsmap)[0].text
        self.assertEqual(response_berichtcode, BerichtcodeChoices.fo03, response.content)

        details = response_root.xpath('//stuf:body/stuf:details', namespaces=self.nsmap)[0].text
        self.assertEqual(details, "Het entiteittype \'BSL\' komt niet overeen met het verwachtte entiteittype \'ZAK\'", response.content)

        self._assert_error_response(response_root)

    def test_updateZaak_zakLk01_verwerkingssoort_w_topfundamenteel(self):
        """
        Make sure something other than 'verwerkingssoort' 'W' is not allowed in the topfundamenteel.

        See StUF 3.01 - Tabel 5.3
        """
        vraag = 'updateZaak_ZakLk01_verwerkingssoort.xml'
        response = self._do_request(self.porttype, vraag, self.context)
        self.assertEquals(response.status_code, 500, response.content)
        response_root = etree.fromstring(response.content)

        response_berichtcode = response_root.xpath('//stuf:stuurgegevens/stuf:berichtcode', namespaces=self.nsmap)[0].text
        self.assertEqual(response_berichtcode, BerichtcodeChoices.fo03, response.content)

        details = response_root.xpath('//stuf:body/stuf:details', namespaces=self.nsmap)[0].text
        self.assertEqual(details, "Alleen de verwerkingssoort 'W' is toegestaan in het topfundamenteel.", response.content)

        self._assert_error_response(response_root)

    def test_updateZaak_zakLk01_mutatiesoort_w(self):
        """
        Make sure something other than 'mutatiesoort' 'W' is not allowed and returns
        a proper error.

        See StUF 3.01 - Tabel 5.3 and ZDS 1.2
        """
        vraag = 'updateZaak_ZakLk01_mutatiesoort.xml'
        response = self._do_request(self.porttype, vraag, self.context)
        self.assertEquals(response.status_code, 500, response.content)
        response_root = etree.fromstring(response.content)

        response_berichtcode = response_root.xpath('//stuf:stuurgegevens/stuf:berichtcode', namespaces=self.nsmap)[0].text
        self.assertEqual(response_berichtcode, BerichtcodeChoices.fo03, response.content)

        stuf_code = response_root.xpath('//stuf:body/stuf:code', namespaces=self.nsmap)[0].text
        self.assertEqual(stuf_code, ClientFoutChoices.stuf055, response.content)

        # Note: This is a schema validation error, and won't have a fully filled error response set.

    def test_updateZaak_zakLk01_ZAK_matching_fields(self):
        """
        Make sure that a 'Zaak' gets looked up by its matching field, i.e.:
        identificatie, bronorganisatie, omschrijving.

        See taiga issue #204: This is a bit weird, because 'identificatie' has a unique constraint
        in our database, so it's not possible to create two Zaak objects with
        the same 'identificatie' field value. Which means it's not possible to test this
        properly (other than checking if a certain database query is done)

        """
        # TODO: Write test.
        pass

    def test_updateZaak_zakLk01_stuurgegevens(self):
        """
        Make sure the 'stuurgegevens' are returned correctly.
        """
        # TODO: Write test.
        pass

    def test_updateZaak_zakLk01_unbalanced_old_and_new(self):
        """
        Make sure that if the first and second object don't hold an even
        amount of elements, an error is thrown.
        """
        # TODO: Write test.
        pass

    def test_updateZaak_zakLk01_unmatched_old_and_new(self):
        """
        Make sure that if the first and second object don't hold the same
        types of elements, an error is thrown.
        """
        # TODO: Write test.
        pass

    def test_updateZaak_zakLk01_transaction_rollback(self):
        """
        Make sure that if part of the request does not succeeded, the entire
        transaction is rolled back.
        """
        # TODO: Write test.
        pass

    def test_updateZaak_zakLk01_groups(self):
        """
        It's a bit unclear what the following would mean, make sure that it's either
        not allowed by the XSD, or that it is a error by the sender.

        <object StUF:entiteittype="ZAK" StUF:verwerkingssoort="W">
            <kenmerk xsi:nil=True>
            <kenmerk xsi:nil=True>
        </object>
        """
        # TODO: Write test.
        pass


class STPupdateZaak_ZakLk01Tests(BaseTestPlatformTests):
    """
    Precondities:
    Scenario creeerZaak (P) is succesvol uitgevoerd.
    Dit scenario voert wijzigingen door op zaken die in creeerZaak (P) zijn toegevoegd.
    """

    test_files_subfolder = 'stp_updateZaak'
    porttype = 'OntvangAsynchroon'

    def setUp(self):
        super().setUp()

        self.context = {
            # probably better set gemeentecode to '' or leave it out
            'gemeentecode': '1234',
            'datumVandaag': self.genereerdatum(),
            'datumGisteren': self.genereerdatum(-1),
            'datumEergisteren': self.genereerdatum(-2),
            'tijdstipRegistratie': self.genereerdatumtijd(),

            'zds_zaaktype_code': '12345678',
            'zds_zaaktype_omschrijving': 'Aanvraag burgerservicenummer behandelen',
            'referentienummer': self.genereerID(10),
            'creerzaak_identificatie_7': self.genereerID(10),
            'creerzaak_identificatie_11': self.genereerID(10)
        }

    def _test_response(self, response):
        self.assertEquals(response.status_code, 200, response.content)

        response_root = etree.fromstring(response.content)
        response_berichtcode = response_root.xpath('//stuf:stuurgegevens/stuf:berichtcode', namespaces=self.nsmap)[0].text
        self.assertEqual(response_berichtcode, BerichtcodeChoices.bv03, response.content)

    def test_updateZaak_ZakLk01_01(self):
        self.zaak = ZaakFactory.create(
            zaakidentificatie="{}{}".format(self.context['gemeentecode'], self.context['creerzaak_identificatie_7']),
            omschrijving="omschrijving",
        )
        identificatie = "{gemeentecode}98765".format(gemeentecode=self.context['gemeentecode'])
        self.organisatorische_eenheid = OrganisatorischeEenheidFactory.create(
            identificatie=identificatie,
            organisatieeenheididentificatie=identificatie,
            organisatieidentificatie=identificatie[:4],
            naam=identificatie
        )
        self.assertEqual(self.organisatorische_eenheid.identificatie, identificatie)

        rol = RolFactory.create(
            zaak=self.zaak, betrokkene=self.organisatorische_eenheid,
            rolomschrijving=Rolomschrijving.initiator, )

        # In the test it says 'T', but a lot of required fields are missing. My assumption
        # is that the test expected the medewerker to exist.
        medewerker = MedewerkerFactory.create(
            medewerkeridentificatie='12345')

        vraag = 'updateZaak_ZakLk01_01.xml'
        response = self._do_request(self.porttype, vraag, self.context)

        self._test_response(response)

        rol.refresh_from_db()

        self.assertEquals(rol.zaak, self.zaak)
        self.assertEquals(rol.betrokkene.is_type(), medewerker)

        # OEH should still exist.
        self.assertTrue(OrganisatorischeEenheid.objects.filter(pk=self.organisatorische_eenheid).exists())

    def test_updateZaak_ZakLk01_03(self):
        self.context['creerzaak_identificatie_9'] = self.genereerID(10)
        self.context['zds_zaaktype_omschrijving'] = 'Aanvraag burgerservicenummer behandelen'
        self.context['zds_zaaktype_code'] = '12345678'
        self.context['datumVandaag'] = self.genereerdatumtijd(0)
        self.context['datumEergisteren'] = self.genereerdatumtijd(-2)
        self.context['datumGisteren'] = self.genereerdatumtijd(-1)

        zaak = ZaakFactory.create(
            zaakidentificatie="{}{}".format(self.context['gemeentecode'], self.context['creerzaak_identificatie_9']),
            omschrijving="omschrijving",
            kenmerken=None,
        )
        identificatie = "0123456785"
        organisatorische_eenheid = OrganisatorischeEenheidFactory.create(
            identificatie=identificatie,
            organisatieeenheididentificatie=identificatie,
            organisatieidentificatie=identificatie[:4],
            naam='naam2',
            gevestigd_in__identificatie='012345678910'
        )

        medewerker1 = Medewerker.objects.create(**{
            'medewerkeridentificatie': "56781",
            'achternaam': 'achternaam2',
            'voorletters': 'voorletters2',
            'voorvoegsel_achternaam': 'voorvoeg2',
        })
        medewerker2 = Medewerker.objects.create(**{
            'medewerkeridentificatie': "56782",
            'achternaam': 'achternaam22',
            'voorletters': 'voorletters22',
            'voorvoegsel_achternaam': 'voorvoeg22',
        })
        medewerker3 = Medewerker.objects.create(**{
            'medewerkeridentificatie': "56783",
            'achternaam': 'achternaam2',
            'voorletters': 'voorletters2',
            'voorvoegsel_achternaam': 'voorvoeg2',
        })
        medewerker4 = Medewerker.objects.create(**{
            'medewerkeridentificatie': "56784",
            'achternaam': 'achternaam22',
            'voorletters': 'voorletters22',
            'voorvoegsel_achternaam': 'voorvoeg22',
        })
        medewerker5 = Medewerker.objects.create(**{
            'medewerkeridentificatie': "56786",
            'achternaam': 'achternaam6',
            'voorletters': 'voorletters6',
            'voorvoegsel_achternaam': 'voorvoeg6',
        })
        medewerker6 = Medewerker.objects.create(**{
            'medewerkeridentificatie': "56788",
            'achternaam': 'achternaam2',
            'voorletters': 'voorletters2',
            'voorvoegsel_achternaam': 'voorvoeg2',
        })
        medewerker7 = Medewerker.objects.create(**{
            'medewerkeridentificatie': "56790",
            'achternaam': 'achternaam20',
            'voorletters': 'voorletters20',
            'voorvoegsel_achternaam': 'voorvoeg20',
        })
        medewerker8 = Medewerker.objects.create(**{
            'medewerkeridentificatie': "56791",
            'achternaam': 'achternaam22',
            'voorletters': 'voorletters22',
            'voorvoegsel_achternaam': 'voorvoeg22',
        })

        vestiging = VestigingFactory.create(identificatie='010203040506')
        rol = RolFactory.create(zaak=zaak, betrokkene=vestiging, rolomschrijving=Rolomschrijving.initiator)

        # Make sure none of the test requirements are met before doing the update.
        self.assertEquals(Rol.objects.filter(zaak=zaak, betrokkene=medewerker1).count(), 0)
        self.assertEquals(Rol.objects.filter(zaak=zaak, betrokkene=medewerker2).count(), 0)
        self.assertEquals(Rol.objects.filter(zaak=zaak, betrokkene=organisatorische_eenheid).count(), 0)

        self.assertFalse(ZaakKenmerk.objects.exists())

        vraag = 'updateZaak_ZakLk01_03.xml'
        response = self._do_request(self.porttype, vraag, self.context)

        self._test_response(response)

        self.assertTrue(ZaakKenmerk.objects.exists())

        # Oud:
        # <ZKN:heeftAlsBelanghebbende StUF:entiteittype="ZAKBTRBLH" StUF:verwerkingssoort="T" xsi:nil="true"/>
        # Huidig:
        # <ZKN:heeftAlsBelanghebbende StUF:entiteittype="ZAKBTRBLH" StUF:verwerkingssoort="T">
        #     <ZKN:gerelateerde>
        #         <ZKN:medewerker StUF:entiteittype="MDW" StUF:verwerkingssoort="I">
        #             <ZKN:identificatie>{{ gemeentecode }}56781</ZKN:identificatie>
        #             <ZKN:achternaam>achternaam2</ZKN:achternaam>
        #             <ZKN:voorletters>voorletters2</ZKN:voorletters>
        #             <ZKN:voorvoegselAchternaam>voorvoeg2</ZKN:voorvoegselAchternaam>
        #         </ZKN:medewerker>
        #     </ZKN:gerelateerde>
        # </ZKN:heeftAlsBelanghebbende>

        self.assertEquals(Rol.objects.filter(zaak=zaak, betrokkene=medewerker1, rolomschrijving=Rolomschrijving.belanghebbende).count(), 1)

        # Oud:
        # <ZKN:heeftAlsBelanghebbende StUF:entiteittype="ZAKBTRBLH" StUF:verwerkingssoort="T" xsi:nil="true"/>
        # Huidig:
        # <ZKN:heeftAlsBelanghebbende StUF:entiteittype="ZAKBTRBLH" StUF:verwerkingssoort="T">
        #     <ZKN:gerelateerde>
        #         <ZKN:medewerker StUF:entiteittype="MDW" StUF:verwerkingssoort="I">
        #             <ZKN:identificatie>{{ gemeentecode }}56782</ZKN:identificatie>
        #             <ZKN:achternaam>achternaam22</ZKN:achternaam>
        #             <ZKN:voorletters>voorletters22</ZKN:voorletters>
        #             <ZKN:voorvoegselAchternaam>voorvoeg22</ZKN:voorvoegselAchternaam>
        #         </ZKN:medewerker>
        #     </ZKN:gerelateerde>
        # </ZKN:heeftAlsBelanghebbende>

        self.assertEquals(Rol.objects.filter(zaak=zaak, betrokkene=medewerker2, rolomschrijving=Rolomschrijving.belanghebbende).count(), 1)

        # Oud:
        # <ZKN:heeftAlsInitiator StUF:entiteittype="ZAKBTRINI" StUF:verwerkingssoort="R">
        #     <ZKN:gerelateerde>
        #         <ZKN:vestiging StUF:verwerkingssoort="I" StUF:entiteittype="VES">
        #             <BG:vestigingsNummer>010203040506</BG:vestigingsNummer>
        #         </ZKN:vestiging>
        #     </ZKN:gerelateerde>
        # </ZKN:heeftAlsInitiator>
        # Huidig:
        # <ZKN:heeftAlsInitiator StUF:entiteittype="ZAKBTRINI" StUF:verwerkingssoort="R">
        #     <ZKN:gerelateerde>
        #         <ZKN:organisatorischeEenheid StUF:entiteittype="OEH" StUF:verwerkingssoort="I">
        #             <ZKN:identificatie>0123456785</ZKN:identificatie>
        #             <ZKN:naam>naam2</ZKN:naam>
        #             <ZKN:isGehuisvestIn StUF:entiteittype="OEHVZO" StUF:verwerkingssoort="I">
        #                 <ZKN:gerelateerde StUF:entiteittype="VZO" StUF:verwerkingssoort="I">
        #                     <ZKN:isEen StUF:entiteittype="VZOVES" StUF:verwerkingssoort="I">
        #                         <ZKN:gerelateerde StUF:entiteittype="VES" StUF:verwerkingssoort="I">
        #                             <BG:vestigingsNummer>012345678910</BG:vestigingsNummer>
        #                             <!-- <BG:authentiek StUF:metagegeven="true" xsi:nil="true"/> -->
        #                             <!-- <BG:handelsnaam>handelsnaam</BG:handelsnaam> -->
        #                             <!-- <BG:verblijfsadres/> -->
        #                         </ZKN:gerelateerde>
        #                     </ZKN:isEen>
        #                 </ZKN:gerelateerde>
        #             </ZKN:isGehuisvestIn>
        #         </ZKN:organisatorischeEenheid>
        #     </ZKN:gerelateerde>
        # </ZKN:heeftAlsInitiator>
        self.assertEquals(Rol.objects.filter(zaak=zaak, betrokkene=organisatorische_eenheid, rolomschrijving=Rolomschrijving.initiator).count(), 1)

    def test_updateZaak_ZakLk01_05(self):
        self.context['zds_zaaktype_omschrijving'] = 'Aanvraag burgerservicenummer behandelen'
        self.context['zds_zaaktype_code'] = '12345678'

        besluittype = BesluitTypeFactory.create(
            besluittypeomschrijving='omschrijving5')
        besluit = BesluitFactory.create(
            identificatie='0123456789',
            besluitdatum=self.context['datumVandaag'],
            besluittype=besluittype)

        zaak_type = ZaakTypeFactory.create(
            zaaktypeidentificatie=self.context['zds_zaaktype_code'],
            zaaktypeomschrijving=self.context['zds_zaaktype_omschrijving'])

        vraag = 'updateZaak_ZakLk01_05.xml'
        zaak = ZaakFactory.create(
            zaakidentificatie="{}{}".format(self.context['gemeentecode'], self.context['creerzaak_identificatie_11']),
            omschrijving="omschrijving",
            kenmerken=None,
            zaaktype=zaak_type,
        )
        natuurlijk_persoon = NatuurlijkPersoonFactory.create(
            burgerservicenummer='012345678',
            naam__geslachtsnaam='geslachtsnaam5',
            naam__voornamen='voornamen5',
            geslachtsaanduiding='M',
            geboortedatum_ingeschreven_persoon=self.context['datumVandaag'],
        )
        deelzaak = ZaakFactory.create(
            zaakidentificatie='0123456789',
            omschrijving='omschrijving5',
            zaaktype=zaak_type,
        )

        # Initially, no deelzaken should exist.
        self.assertFalse(zaak.deelzaken.exists())
        # No besluiten should exist either.
        self.assertFalse(zaak.besluit_set.exists())

        response = self._do_request(self.porttype, vraag, self.context)

        self._test_response(response)

        # After the update the deelzaak should be added as a deelzaak of zaak.
        self.assertEquals(zaak.deelzaken.count(), 1)
        self.assertEquals(zaak.deelzaken.filter(pk=deelzaak.pk).count(), 1)

        # And a besluit should be added as well.
        self.assertEquals(zaak.besluit_set.count(), 1)
        self.assertEquals(zaak.besluit_set.filter(pk=besluit.pk).count(), 1)

    @skip('Test nog niet geimplementeerd')
    def test_updateZaak_zakLk01_07(self):
        self.zaak_13 = ZaakFactory.create()

        vraag = 'updateZaak_zakLk01_07_real.xml'
        self.context.update(
            creerzaak_identificatie_13=self.zaak_13.zaakidentificatie,
        )
        response = self._do_request(self.porttype, vraag, self.context)

        self._test_response(response)
