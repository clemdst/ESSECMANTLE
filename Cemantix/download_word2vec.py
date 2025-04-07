import requests
from tqdm import tqdm
import os

url = "https://github.com/lovasoa/cemantriche/releases/download/v0/frWac_non_lem_no_postag_no_phrase_200_cbow_cut100.bin"
filename = "frWac_non_lem_no_postag_no_phrase_200_cbow_cut100.bin"

if not os.path.exists(filename):
    print("Téléchargement du modèle Word2Vec...")

    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024 * 1024  # 1 MB
    with open(filename, 'wb') as f, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024
    ) as bar:
        for chunk in response.iter_content(chunk_size=block_size):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))

    print("Téléchargement terminé.")
else:
    print("Le modèle existe déjà.")
