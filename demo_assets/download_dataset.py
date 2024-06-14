import os
import wget
import zipfile
import argparse

def main(target_path):
    target_path = os.path.abspath(target_path)
    wget.download('https://github.com/Louislin0128/AICUP-2024-competition/releases/tag/v0.0/small_image.zip', out=target_path)

    try:
        print("Start download the demo images...")
        if os.path.exists(os.path.join(target_path, "./small_image.zip")):
            with zipfile.ZipFile(os.path.join(target_path, "./small_image.zip")) as zip_ref:
                zip_ref.extractall(target_path)
    except Exception as error:
    #     print(f"Error Exception: {error}")
    # finally:
    #     if os.path.exists(os.path.join(target_path, "./small_image.zip")):
    #         os.remove(os.path.join(target_path, "./small_image.zip"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--target_path', type=str, default=".")
    args = parser.parse_args()
    main(args.target_path)
