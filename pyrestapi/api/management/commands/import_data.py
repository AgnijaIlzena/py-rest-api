import os
import json
from datetime import datetime
from dateutil import parser
from django.utils.timezone import make_aware  # ✅ Import Django timezone support
from django.core.management.base import BaseCommand
from api.models import Investment  # Replace with your actual app name

class Command(BaseCommand):
    help = 'Import investments from a JSON file'

    def handle(self, *args, **kwargs):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../data/dataset.json"))

        print(f"Attempting to open file: {file_path}")

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            print(f"Successfully loaded {len(data)} records from JSON file.")

            investments_to_create = []

            # function to convert date to one with timezone awareness
            def convert_date(value):
                if not value:
                    return None
                try:
                    value_str = str(value).strip()  # Ensure it's a string and remove spaces

                    # If the value is only a year (e.g., "2014"), convert to "2014-01-01 00:00:00"
                    if len(value_str) == 4 and value_str.isdigit():
                        date_obj = datetime.strptime(value_str, "%Y")
                        date_obj = date_obj.replace(month=1, day=1, hour=0, minute=0, second=0)
                    else:
                        date_obj = parser.parse(value_str)

                    return make_aware(date_obj)  # Convert to timezone-aware datetime

                except (ValueError, TypeError):
                    return None

            for entry in data:
                investment = Investment(
                    titreoperation=entry.get('titreoperation', ''),
                    entreprise=entry.get('entreprise', ''),
                    ville=entry.get('ville', ''),
                    mandataire=entry.get('mandataire', ''),
                    ppi=entry.get('ppi', ''),
                    lycee=entry.get('lycee', ''),

                    # Convert date fields to proper date types with timezone awareness
                    annee_de_livraison=convert_date(entry.get('annee_de_livraison')),
                    notification_du_marche=convert_date(entry.get('notification_du_marche')),
                    cao_attribution=convert_date(entry.get('cao_attribution')),

                    codeuai=entry.get('codeuai', ''),
                    longitude=entry.get('longitude', None),
                    etat_d_avancement=entry.get('etat_d_avancement', ''),
                    montant_des_ap_votes_en_meu=entry.get('montant_des_ap_votes_en_meu', None),
                    latitude=entry.get('latitude', None),
                    maitrise_d_oeuvre=entry.get('maitrise_d_oeuvre', ''),
                    mode_de_devolution=entry.get('mode_de_devolution', ''),
                    enveloppe_prev_en_meu=entry.get('enveloppe_prev_en_meu', None),

                    # Convert `annee_d_individualisation` to an integer
                    annee_d_individualisation=int(entry.get('annee_d_individualisation', 0))
                )

                investments_to_create.append(investment)

            Investment.objects.bulk_create(investments_to_create)
            print(f"Successfully imported {len(investments_to_create)} investments.")

        except FileNotFoundError:
            print(f"ERROR: File not found at {file_path}")
        except json.JSONDecodeError as e:
            print(f"ERROR: JSON Decode Error - {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


