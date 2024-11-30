from django.db import models

class NFT(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()  # URL de la imagen del NFT
    metadata_uri = models.URLField()  # URI de la metadata (que será personalizada para cada NFT)
    claimed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ClaimedNFT(models.Model):
    wallet_address = models.CharField(max_length=42, unique=True)  # La dirección de la billetera
    nft_id = models.IntegerField()  # El ID del NFT que se ha reclamado
    claimed_at = models.DateTimeField(auto_now_add=True)  # Fecha en que se hizo la reclamación

    def __str__(self):
        return f"NFT {self.nft_id} reclamado por {self.wallet_address}"