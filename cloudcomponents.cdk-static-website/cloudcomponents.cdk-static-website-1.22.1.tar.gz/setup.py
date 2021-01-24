import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cloudcomponents.cdk-static-website",
    "version": "1.22.1",
    "description": "Cdk component that creates a static website using S3, configures CloudFront (CDN) and maps a custom domain via Route53 (DNS)",
    "license": "MIT",
    "url": "https://github.com/cloudcomponents/cdk-constructs",
    "long_description_content_type": "text/markdown",
    "author": "hupe1980",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cloudcomponents/cdk-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cloudcomponents.cdk_static_website",
        "cloudcomponents.cdk_static_website._jsii"
    ],
    "package_data": {
        "cloudcomponents.cdk_static_website._jsii": [
            "cdk-static-website@1.22.1.jsii.tgz"
        ],
        "cloudcomponents.cdk_static_website": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-cloudfront>=1.86.0, <2.0.0",
        "aws-cdk.aws-iam>=1.86.0, <2.0.0",
        "aws-cdk.aws-route53-targets>=1.86.0, <2.0.0",
        "aws-cdk.aws-route53>=1.86.0, <2.0.0",
        "aws-cdk.aws-s3-deployment>=1.86.0, <2.0.0",
        "aws-cdk.aws-s3>=1.86.0, <2.0.0",
        "aws-cdk.core>=1.86.0, <2.0.0",
        "cloudcomponents.cdk-deletable-bucket>=1.21.1, <2.0.0",
        "constructs>=3.2.0, <4.0.0",
        "jsii>=1.17.1, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
