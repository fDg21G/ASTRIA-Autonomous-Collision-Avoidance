from setuptools import setup, find_packages

setup(
    name="astria",
    version="1.0.0",
    author="Houssam Rharbi",
    description="Autonomous collision avoidance for CubeSats.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "sgp4>=2.21",
        "scikit-learn>=1.0.0",
        "xgboost>=1.6.0",
    ],
    python_requires=">=3.9",
)
