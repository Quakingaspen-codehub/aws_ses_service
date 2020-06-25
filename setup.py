import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aws_ses_service",
    version="0.0.8",
    author="Quaking Aspen",
    author_email="info@quakingaspen.net",
    description="This library is to help send emails using AWS ses service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Quakingaspen-codehub/aws_ses_service",
    packages=["aws_ses_service"],
    install_requires=["aws-s3-resource==0.0.7", "boto3==1.13.15"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
