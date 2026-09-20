from app.cleaning.cleaner import clean_text_values
from app.cleaning.validator import find_missing_values
from app.cleaning.deduplicator import remove_duplicates


def clean_data(data):

    # 1. Nettoyer les espaces inutiles
    data = clean_text_values(data)

    # 2. Supprimer les doublons
    data = remove_duplicates(data)

    # 3. Vérifier les valeurs manquantes
    missing_values = find_missing_values(data)

    return data, missing_values