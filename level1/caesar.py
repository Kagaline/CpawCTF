import argparse


def encrypt_caesar(plaintext, shift=3):
    """シーザー暗号での暗号化"""
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # アルファベットの場合のみ処理
            start = ord("a") if char.islower() else ord("A")
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            # アルファベットでない場合はそのまま追加
            encrypted_text += char
    return encrypted_text


def decrypt_caesar(ciphertext, shift=3):
    """シーザー暗号での復号"""
    return encrypt_caesar(ciphertext, -shift)


def main():
    """メイン"""

    parser = argparse.ArgumentParser(description="Argument Parser")
    parser.add_argument(
        "mode",
        help="mode: enc(encryption), dec(decryption) or both(encryption and decryption)",
    )
    parser.add_argument(
        "-i", "--input_file", help="Input file path", default="input.txt"
    )
    parser.add_argument(
        "-s", "--shift_size", help="Key of caesar crypt system", default=3
    )
    parser.add_argument(
        "-o", "--output_file", help="Output file path", default="output.txt"
    )

    args = parser.parse_args()

    match args.mode:
        case "enc":
            # 暗号化
            plaintext = args.input_file
            encrypted_text = encrypt_caesar(plaintext, shift=args.shift_size)
            print(f"Encrypted: {encrypted_text}")
        case "dec":
            # 復号
            encrypted_text = args.input_file
            decrypted_text = decrypt_caesar(encrypted_text, shift=args.shift_size)
            print(f"Decrypted: {decrypted_text}")
        case "both":
            # 暗号化と復号
            text = args.input_file
            encrypted_text = encrypt_caesar(text, shift=args.shift_size)
            decrypted_text = decrypt_caesar(text, shift=args.shift_size)
            print(f"Encrypted: {encrypted_text}")
            print(f"Decrypted: {decrypted_text}")
        case _:
            # 指定されたモード以外
            print("Something is wrong")


if __name__ == "__main__":
    main()
