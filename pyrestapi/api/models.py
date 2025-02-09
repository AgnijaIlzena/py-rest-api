from django.db import models

class Investment(models.Model):
    titreoperation = models.TextField(default="-", db_column="titreoperation")
    entreprise = models.TextField(default="-", db_column="entreprise")
    ville = models.CharField(max_length=255, default="-", db_column="ville")
    annee = models.DateTimeField(blank=True, null=True, db_column="annee_de_livraison")
    mandataire = models.CharField(max_length=255, default="-", db_column="mandataire")
    ppi = models.CharField(max_length=255, default="-", db_column="ppi")
    lycee = models.CharField(max_length=255, default="-", db_column="lycee")
    notification = models.DateTimeField(blank=True, null=True, db_column="notification_du_marche")
    codeuai = models.CharField(max_length=255, default="-", db_column="codeuai")
    longitude = models.FloatField(blank=True, null=True, db_column="longitude")
    etatAvancement = models.CharField(max_length=255, default="-", db_column="etat_d_avancement")
    montantVotes = models.FloatField(blank=True, null=True, db_column="montant_des_ap_votes_en_meu")
    cao = models.DateTimeField(blank=True, null=True, db_column="cao_attribution")
    latitude = models.FloatField(blank=True, null=True, db_column="latitude")
    maitrise = models.CharField(max_length=255, default="-", db_column="maitrise_d_oeuvre")
    modeDevolution = models.CharField(max_length=255, default="-", db_column="mode_de_devolution")
    aneeIndividualisation = models.IntegerField(blank=True, null=True, db_column="annee_d_individualisation")
    enveloppePrev = models.FloatField(blank=True, null=True, db_column="enveloppe_prev_en_meu")

    def __str__(self):
        return self.titreoperation

