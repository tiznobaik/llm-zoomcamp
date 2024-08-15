if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import hashlib

# Function to generate a unique document ID
def generate_document_id(doc):
    combined = f"{doc['course']}--{doc['question']}--{doc['text'][:10]}"
    hash_object = hashlib.md5(combined.encode())
    hash_hex = hash_object.hexdigest()
    document_id = hash_hex[:8]
    return document_id
    
@transformer
def transform(data, *args, **kwargs):
    """
    Custom transformation logic to chunk documents and generate document IDs.
    
    Args:
        data: The output from the upstream parent block.
        *args: The output from any additional upstream blocks (if applicable).
    
    Returns:
        A list of transformed documents with unique document IDs.
    """
    documents = []
    
    for doc in data['documents']:
        doc['course'] = data['course']
        # Generate a unique ID for each document
        doc['document_id'] = generate_document_id(doc)
        documents.append(doc)
    
    print(len(documents))  # Print the number of documents (chunks)
    
    return documents


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'