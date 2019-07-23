from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description="""
    Python S3 client.
    """)

    parser.add_argument("bucket",
                        help="s3 bucket to store data.",
                        require=True)
    parser.add_argument("filename",
                        help="name of file to upload.",
                        require=True)


    return parser

def main():
    import boto3
    from s3_client import s3

    args = create_parser().parse args()
    s3.bucket(args.bucket)
