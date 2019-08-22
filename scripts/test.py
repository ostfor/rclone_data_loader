from rclone_data_loader.loader import download, upload


def test_upload():
    upload("data/upload/net_test")


def test_download():
    download("data/download/net_test")


if __name__ == '__main__':
    test_download()
