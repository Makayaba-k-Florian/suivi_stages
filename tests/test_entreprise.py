from stages.models import Entreprise


def test_une_entreprise_s_affiche_avec_sa_ville(db):
    entreprise = Entreprise.objects.create(
        nom="Sokodé numerique",
        ville="Sokodé",
        secteur="informatique",
        contact="cts@gmail.com"
    )

    assert str(entreprise) == "Sokodé numerique (Sokodé)"