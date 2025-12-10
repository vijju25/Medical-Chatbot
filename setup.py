setup(
    name="Generative AI Project",
    version="0.0.1",
    author="Vijay",
    author_email="jakkavijayreddy@gmail.com",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "pinecone-client",
        "python-dotenv",
        "PyMuPDF",
        "sentence-transformers"
    ],
)
