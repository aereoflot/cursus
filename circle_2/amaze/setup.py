from setuptools import setup  # type: ignore

setup(
    name="mazegen-ancrodri",
    version="1.0.0",
    author="ancrodri",
    description="A perfect maze generator using DFS algorithm with BFS pathfinding",
    py_modules=["mazegen"],
    python_requires=">=3.10",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
