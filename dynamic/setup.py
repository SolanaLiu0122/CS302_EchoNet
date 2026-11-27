import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="echonet",
    version="1.0.0",
    author="Stanford ML Group",
    description="Echocardiography video analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "click",
        "numpy",
        "pandas",
        "torch",
        "torchvision",
        "opencv-python",
        "scikit-image",
        "tqdm",
        "scikit-learn"
    ],
    entry_points={
        "console_scripts": [
            "echonet=echonet.__main__:main",
        ],
    },
)