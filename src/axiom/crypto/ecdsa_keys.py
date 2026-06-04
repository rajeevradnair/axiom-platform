from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec


def generate_private_key() -> ec.EllipticCurvePrivateKey:
    return ec.generate_private_key(ec.SECP256R1())


def private_key_to_pem(private_key: ec.EllipticCurvePrivateKey) -> bytes:
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )


def public_key_to_pem(private_key: ec.EllipticCurvePrivateKey) -> bytes:
    public_key = private_key.public_key()

    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )


def load_private_key_from_pem(
    private_key_pem: bytes,
) -> ec.EllipticCurvePrivateKey:
    private_key = serialization.load_pem_private_key(
        private_key_pem,
        password=None,
    )

    if not isinstance(private_key, ec.EllipticCurvePrivateKey):
        raise TypeError("Expected an ECDSA private key.")

    return private_key


def load_public_key_from_pem(
    public_key_pem: bytes,
) -> ec.EllipticCurvePublicKey:
    public_key = serialization.load_pem_public_key(public_key_pem)

    if not isinstance(public_key, ec.EllipticCurvePublicKey):
        raise TypeError("Expected an ECDSA public key.")

    return public_key