import zipfile


def extract_archive(archive_path, destination):
    # read mode to read the archive file
    """
    A function which takes the path to an archive file and extracts the content to the destination path
    """
    with zipfile.ZipFile(archive_path, "r") as archive:
        archive.extractall(destination)


if __name__ == "__main__":
    extract_archive("test/1.zip", "test/")
