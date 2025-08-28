from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)


# normal loading (this is slow)
docs = loader.load()

for document in docs:
    print(document.metadata)




# Lazy Loading (happens 1 doc at at time and works much better with large number of documents)
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)